"""Command-line interface for Cheap Hosting Finder & True Cost Calculator."""

from __future__ import annotations

import argparse
import json
import sys

from .calculator import compare_plans, filter_plans, load_plans


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hosting_finder",
        description="Find the cheapest web hosting or VPS based on real 1-3 year cost.",
    )
    parser.add_argument(
        "--months",
        type=int,
        default=36,
        help="Usage horizon in months (default: 36)",
    )
    parser.add_argument(
        "--websites",
        type=int,
        default=1,
        help="Number of websites to host (default: 1)",
    )
    parser.add_argument(
        "--category",
        choices=["shared", "vps", "wordpress", "paas"],
        help="Filter by hosting category",
    )
    parser.add_argument(
        "--max-budget",
        type=float,
        help="Maximum effective monthly cost in USD",
    )
    parser.add_argument(
        "--stack",
        nargs="+",
        help="Required stack features (e.g. wordpress php mysql nodejs python docker root_access)",
    )
    parser.add_argument(
        "--us-only",
        action="store_true",
        help="Only include plans with US data centers",
    )
    parser.add_argument(
        "--monthly-only",
        action="store_true",
        help="Only include month-to-month plans without multi-year lock-in",
    )
    parser.add_argument(
        "--compare",
        nargs="+",
        help="Compare specific plan IDs side-by-side (e.g. ionos-plus hostinger-premium hetzner-cx22-us)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    plans = load_plans()

    if args.compare:
        billing_mode = "monthly" if args.monthly_only else "promo"
        results = compare_plans(
            args.compare,
            plans=plans,
            months=args.months,
            websites=args.websites,
            billing_mode=billing_mode,
        )
        if args.json:
            print(json.dumps(results, indent=2))
            return 0

        print(f"\nSide-by-Side Comparison ({args.months} months, {args.websites} site(s)):\n")
        header = f"{'Plan':<34} {'Promo':>7} {'Renewal':>8} {'Spike':>8} {'Total':>9} {'Eff/mo':>8}"
        print(header)
        print("-" * len(header))
        for c in results:
            print(
                f"{c['name']:<34} "
                f"${c['advertised_monthly_usd']:>5.2f} "
                f"${c['renewal_monthly_usd']:>6.2f} "
                f"{c['renewal_spike_pct']:>6.1f}% "
                f"${c['total_cost_usd']:>8.2f} "
                f"${c['effective_monthly_usd']:>6.2f}"
            )
        return 0

    filtered = filter_plans(
        plans,
        months=args.months,
        websites=args.websites,
        category=args.category,
        max_effective_monthly=args.max_budget,
        stack=args.stack,
        us_only=args.us_only,
        monthly_only=args.monthly_only,
    )

    if args.json:
        print(json.dumps([item["cost"] for item in filtered], indent=2))
        return 0

    if not filtered:
        print("No matching hosting plans found.")
        return 0

    print(f"\nFound {len(filtered)} plans ({args.months} months, {args.websites} site(s)):\n")
    header = f"{'Plan':<34} {'Type':<10} {'Promo':>7} {'Renewal':>8} {'Total':>9} {'Eff/mo':>8}"
    print(header)
    print("-" * len(header))
    for item in filtered:
        c = item["cost"]
        print(
            f"{c['name']:<34} "
            f"{c['category']:<10} "
            f"${c['advertised_monthly_usd']:>5.2f} "
            f"${c['renewal_monthly_usd']:>6.2f} "
            f"${c['total_cost_usd']:>8.2f} "
            f"${c['effective_monthly_usd']:>6.2f}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
