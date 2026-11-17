"""Core calculation and filtering engine for real web hosting costs."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data"


def load_providers(data_dir: Path = DATA_DIR) -> dict[str, dict[str, Any]]:
    """Load providers indexed by provider id."""
    raw = json.loads((data_dir / "providers.json").read_text(encoding="utf-8"))
    return {p["id"]: p for p in raw["providers"]}


def load_plans(data_dir: Path = DATA_DIR) -> list[dict[str, Any]]:
    """Load all hosting plans."""
    raw = json.loads((data_dir / "plans.json").read_text(encoding="utf-8"))
    return list(raw["plans"])


def calculate_true_cost(
    plan: dict[str, Any],
    months: int = 36,
    websites: int = 1,
    billing_mode: str = "promo",
) -> dict[str, Any]:
    """Calculate the true total and effective monthly cost over a given horizon.

    Args:
        plan: Plan dictionary from plans.json.
        months: Usage horizon in months (e.g., 12, 24, 36, 48).
        websites: Number of websites to host.
        billing_mode: 'promo' (initial promo + renewal) or 'monthly' (no-contract).

    Returns:
        Dictionary containing cost breakdown, effective monthly rate, and renewal spike.
    """
    if months <= 0:
        raise ValueError("months must be a positive integer")
    if websites <= 0:
        raise ValueError("websites must be a positive integer")
    if billing_mode not in ("promo", "monthly"):
        raise ValueError("billing_mode must be 'promo' or 'monthly'")

    max_sites = plan["max_websites"]
    if max_sites == "unlimited":
        plans_needed = 1
        single_plan_fits = True
    else:
        plans_needed = math.ceil(websites / int(max_sites))
        single_plan_fits = websites <= int(max_sites)

    setup_fee = float(plan.get("setup_fee_usd", 0.0))

    if billing_mode == "monthly":
        monthly_rate = plan.get("monthly_no_contract_usd")
        if monthly_rate is None:
            raise ValueError(f"Plan {plan['id']} does not support month-to-month billing")
        monthly_rate = float(monthly_rate)
        promo_total = 0.0
        renewal_total = months * monthly_rate
        first_year_total = min(12, months) * monthly_rate + setup_fee
        effective_promo_rate = monthly_rate
        effective_renewal_rate = monthly_rate
    else:
        promo_rate = float(plan["promo_monthly_usd"])
        renewal_rate = float(plan["renewal_monthly_usd"])
        promo_term = int(plan["promo_term_months"])

        promo_months = min(months, promo_term)
        renewal_months = max(0, months - promo_months)

        promo_total = promo_months * promo_rate
        renewal_total = renewal_months * renewal_rate

        yr1_promo = min(12, promo_term, months)
        yr1_renewal = max(0, min(12, months) - yr1_promo)
        first_year_total = yr1_promo * promo_rate + yr1_renewal * renewal_rate + setup_fee

        effective_promo_rate = promo_rate
        effective_renewal_rate = renewal_rate

    single_plan_total = promo_total + renewal_total + setup_fee
    total_cost = round(single_plan_total * plans_needed, 2)
    effective_monthly = round(total_cost / months, 2)

    if effective_promo_rate > 0:
        renewal_spike_pct = round(
            ((effective_renewal_rate - effective_promo_rate) / effective_promo_rate) * 100.0, 1
        )
    else:
        renewal_spike_pct = 0.0

    return {
        "plan_id": plan["id"],
        "provider_id": plan["provider_id"],
        "name": plan["name"],
        "category": plan["category"],
        "months": months,
        "websites": websites,
        "plans_needed": plans_needed,
        "single_plan_fits": single_plan_fits,
        "billing_mode": billing_mode,
        "advertised_monthly_usd": round(effective_promo_rate, 2),
        "renewal_monthly_usd": round(effective_renewal_rate, 2),
        "promo_term_months": int(plan["promo_term_months"]),
        "promo_total_usd": round(promo_total * plans_needed, 2),
        "renewal_total_usd": round(renewal_total * plans_needed, 2),
        "setup_fee_usd": round(setup_fee * plans_needed, 2),
        "first_year_total_usd": round(first_year_total * plans_needed, 2),
        "total_cost_usd": total_cost,
        "effective_monthly_usd": effective_monthly,
        "renewal_spike_pct": renewal_spike_pct,
    }


def filter_plans(
    plans: list[dict[str, Any]],
    *,
    months: int = 36,
    websites: int = 1,
    category: str | None = None,
    max_effective_monthly: float | None = None,
    stack: list[str] | None = None,
    us_only: bool = False,
    monthly_only: bool = False,
    control_panel: str | None = None,
) -> list[dict[str, Any]]:
    """Filter plans by technical requirements and budget, sorted by effective monthly cost."""
    results: list[dict[str, Any]] = []
    billing_mode = "monthly" if monthly_only else "promo"

    for plan in plans:
        if category and plan["category"] != category:
            continue
        if us_only and not plan.get("us_datacenters", False):
            continue
        if monthly_only and plan.get("monthly_no_contract_usd") is None:
            continue
        if control_panel and plan.get("control_panel", "").lower() != control_panel.lower():
            continue
        if stack:
            features = plan.get("features", {})
            if not all(features.get(req, False) for req in stack):
                continue

        cost = calculate_true_cost(
            plan,
            months=months,
            websites=websites,
            billing_mode=billing_mode,
        )
        if max_effective_monthly is not None and cost["effective_monthly_usd"] > max_effective_monthly:
            continue

        results.append({**plan, "cost": cost})

    results.sort(key=lambda item: (item["cost"]["effective_monthly_usd"], item["cost"]["total_cost_usd"]))
    return results


def compare_plans(
    plan_ids: list[str],
    plans: list[dict[str, Any]] | None = None,
    months: int = 36,
    websites: int = 1,
    billing_mode: str = "promo",
) -> list[dict[str, Any]]:
    """Compare specific plans side-by-side by their IDs."""
    all_plans = plans if plans is not None else load_plans()
    by_id = {p["id"]: p for p in all_plans}
    comparisons: list[dict[str, Any]] = []

    for pid in plan_ids:
        if pid not in by_id:
            raise KeyError(f"Unknown plan_id: {pid}")
        comparisons.append(
            calculate_true_cost(
                by_id[pid],
                months=months,
                websites=websites,
                billing_mode=billing_mode,
            )
        )

    comparisons.sort(key=lambda c: c["effective_monthly_usd"])
    return comparisons
