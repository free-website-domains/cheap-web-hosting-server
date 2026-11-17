"""Schema validation tests for data/providers.json, data/plans.json, and data/pricing-history.json."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"

REQUIRED_FEATURES = {
    "wordpress",
    "php",
    "mysql",
    "nodejs",
    "python",
    "docker",
    "ssh",
    "root_access",
    "free_ssl",
    "free_domain_year1",
    "backups_included",
    "email_included",
}


class TestDataSchema(unittest.TestCase):
    def test_providers_schema(self) -> None:
        data = json.loads((DATA_DIR / "providers.json").read_text(encoding="utf-8"))
        self.assertIn("providers", data)
        self.assertGreaterEqual(len(data["providers"]), 15)

        seen_ids = set()
        for provider in data["providers"]:
            for key in ("id", "name", "website", "pricing_url", "us_datacenters", "categories"):
                self.assertIn(key, provider)
            self.assertNotIn(provider["id"], seen_ids)
            seen_ids.add(provider["id"])

    def test_plans_schema_and_references(self) -> None:
        providers_data = json.loads((DATA_DIR / "providers.json").read_text(encoding="utf-8"))
        provider_ids = {p["id"] for p in providers_data["providers"]}

        plans_data = json.loads((DATA_DIR / "plans.json").read_text(encoding="utf-8"))
        self.assertIn("plans", plans_data)
        self.assertGreaterEqual(len(plans_data["plans"]), 20)

        seen_plan_ids = set()
        for plan in plans_data["plans"]:
            self.assertNotIn(plan["id"], seen_plan_ids)
            seen_plan_ids.add(plan["id"])
            self.assertIn(plan["provider_id"], provider_ids)
            self.assertIn(plan["category"], ("shared", "vps", "wordpress", "paas"))
            self.assertGreaterEqual(plan["promo_monthly_usd"], 0)
            self.assertGreaterEqual(plan["renewal_monthly_usd"], 0)
            self.assertGreaterEqual(plan["promo_term_months"], 1)
            self.assertEqual(set(plan["features"].keys()), REQUIRED_FEATURES)
            self.assertRegex(plan["last_verified"], r"^\d{4}-\d{2}-\d{2}$")

    def test_pricing_history_references(self) -> None:
        plans_data = json.loads((DATA_DIR / "plans.json").read_text(encoding="utf-8"))
        plan_ids = {p["id"] for p in plans_data["plans"]}

        history = json.loads((DATA_DIR / "pricing-history.json").read_text(encoding="utf-8"))
        self.assertIn("snapshots", history)
        for snap in history["snapshots"]:
            self.assertIn(snap["plan_id"], plan_ids)

    def test_docs_data_synced(self) -> None:
        docs_data = REPO_ROOT / "docs" / "data"
        for filename in ("plans.json", "providers.json"):
            self.assertEqual(
                (DATA_DIR / filename).read_text(encoding="utf-8"),
                (docs_data / filename).read_text(encoding="utf-8"),
            )


if __name__ == "__main__":
    unittest.main()
