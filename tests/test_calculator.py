"""Unit tests for the hosting true cost calculator and filtering engine."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from hosting_finder.calculator import (  # noqa: E402
    calculate_true_cost,
    compare_plans,
    filter_plans,
    load_plans,
)


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.plans = load_plans()
        self.by_id = {p["id"]: p for p in self.plans}

    def test_ionos_plus_36_months_example(self) -> None:
        """IONOS Plus: $1/mo for 12 months + $14/mo for 24 months = $348 ($9.67/mo)."""
        ionos = self.by_id["ionos-plus"]
        cost = calculate_true_cost(ionos, months=36, websites=1)
        self.assertEqual(cost["total_cost_usd"], 348.00)
        self.assertEqual(cost["effective_monthly_usd"], 9.67)
        self.assertEqual(cost["first_year_total_usd"], 12.00)
        self.assertEqual(cost["renewal_spike_pct"], 1300.0)

    def test_interserver_no_renewal_spike(self) -> None:
        """InterServer Standard has 0% renewal spike and works month-to-month."""
        interserver = self.by_id["interserver-standard"]
        cost = calculate_true_cost(interserver, months=36, websites=5, billing_mode="monthly")
        self.assertEqual(cost["total_cost_usd"], 90.00)
        self.assertEqual(cost["effective_monthly_usd"], 2.50)
        self.assertEqual(cost["renewal_spike_pct"], 0.0)
        self.assertTrue(cost["single_plan_fits"])

    def test_multisite_scaling_for_single_site_plan(self) -> None:
        """Hosting 5 websites on a 1-site plan requires 5 plans."""
        ionos_essential = self.by_id["ionos-essential"]
        cost = calculate_true_cost(ionos_essential, months=12, websites=5)
        self.assertEqual(cost["plans_needed"], 5)
        self.assertFalse(cost["single_plan_fits"])
        self.assertEqual(cost["total_cost_usd"], 240.00)

    def test_filter_vps_under_5_dollars(self) -> None:
        results = filter_plans(
            self.plans,
            months=36,
            category="vps",
            max_effective_monthly=5.00,
            stack=["docker", "root_access"],
            us_only=True,
        )
        ids = [r["id"] for r in results]
        self.assertIn("hetzner-cx22-us", ids)
        self.assertIn("vultr-cloud-5", ids)
        self.assertIn("linode-nanode-1gb", ids)
        self.assertNotIn("ionos-plus", ids)

    def test_filter_monthly_only_excludes_locked_plans(self) -> None:
        results = filter_plans(self.plans, months=12, monthly_only=True)
        ids = [r["id"] for r in results]
        self.assertNotIn("bluehost-basic", ids)
        self.assertNotIn("siteground-startup", ids)
        self.assertIn("hetzner-cx22-us", ids)

    def test_compare_plans_sorts_by_effective_monthly(self) -> None:
        comp = compare_plans(
            ["ionos-plus", "hetzner-cx22-us", "interserver-standard"],
            plans=self.plans,
            months=36,
        )
        self.assertEqual([c["plan_id"] for c in comp], [
            "interserver-standard",
            "hetzner-cx22-us",
            "ionos-plus",
        ])


if __name__ == "__main__":
    unittest.main()
