# Cheap Web Hosting Server — Real 1–3 Year Cost Comparison & Calculator

> **Find the cheapest compatible web hosting or VPS server without renewal surprises.**

Most "Best Cheap Web Hosting" lists rank providers by **advertised first-year promo prices** (`$1/mo`, `$2.95/mo`) while hiding what happens when the bill renews at `$11.99–$17.99/mo`.

This open-source repository compares **shared web hosting**, **cheap Linux VPS servers**, **WordPress hosting**, and **developer PaaS** based on **true 1–3 year Total Cost of Ownership (TCO)**, technical compatibility, US server locations, and month-to-month flexibility.

- **Interactive Web Finder & Calculator:** [`https://free-website-domains.github.io/cheap-web-hosting-server/`](https://free-website-domains.github.io/cheap-web-hosting-server/)
- **Structured Dataset:** [`data/providers.json`](data/providers.json) · [`data/plans.json`](data/plans.json) · [`data/pricing-history.json`](data/pricing-history.json)
- **Python CLI & Calculator:** [`hosting_finder.py`](hosting_finder.py) · [`src/hosting_finder/calculator.py`](src/hosting_finder/calculator.py)

---

## Why "Cheap" Advertised Prices Mislead

Example from published US pricing:

| Plan | Advertised Promo | Promo Term | Renewal Rate | Renewal Spike | 36-Month Total | Effective Monthly |
| --- | --- | --- | --- | --- | --- | --- |
| **InterServer Standard** | `$2.50/mo` | 12 mo (Price Lock) | `$2.50/mo` | `0.0%` | `$90.00` | **`$2.50/mo`** |
| **Hostinger Premium** | `$2.99/mo` | 48 mo (Prepaid) | `$7.99/mo` | `+167.2%` | `$107.64` | **`$2.99/mo`** |
| **Namecheap Stellar Plus** | `$2.98/mo` | 24 mo | `$6.48/mo` | `+117.4%` | `$149.28` | **`$4.15/mo`** |
| **Hetzner Cloud CX22 (US)** | `$4.99/mo` | 1 mo (No lock-in) | `$4.99/mo` | `0.0%` | `$179.64` | **`$4.99/mo`** |
| **IONOS Web Hosting Plus** | `$1.00/mo` | 12 mo | `$14.00/mo` | `+1300.0%` | `$348.00` | **`$9.67/mo`** |
| **SiteGround StartUp** | `$2.99/mo` | 12 mo | `$17.99/mo` | `+501.7%` | `$467.64` | **`$12.99/mo`** |

> **Key takeaway:** A `$1.00/mo` shared plan (`IONOS Plus`) costs **`$348.00`** over 3 years (`$9.67/mo` effective) — nearly **2x more** than a flat `$4.99/mo` 4GB RAM Linux VPS from Hetzner (`$179.64` over 3 years) and almost **4x more** than InterServer (`$90.00`).

---

## Choose by What You Actually Need

The phrase *"cheap web hosting server"* covers two very different user jobs:
1. **Shared Web Hosting** — You want cPanel/hPanel, PHP, MySQL, WordPress, and email without managing a Linux server.
2. **VPS / Cloud Server** — You want root SSH access, dedicated RAM/vCPU, Docker/Node.js/Python, and predictable monthly billing.

| Goal / Intent | Guide |
| --- | --- |
| Shared hosting with lowest 3-year cost | [Cheap Web Hosting (Shared)](cheap-web-hosting/README.md) |
| Linux VPS with root access & Docker | [Cheap VPS Hosting](cheap-vps-hosting/README.md) |
| Plans genuinely under `$5/mo` effective | [Web Hosting Under $5/Month](under-5-dollars/README.md) |
| Plans under `$10/mo` over 3 years | [Web Hosting Under $10/Month](under-10-dollars/README.md) |
| WordPress with SSL, backups & PHP | [Cheap WordPress Hosting](wordpress-hosting/README.md) |
| PHP & MySQL stack | [Cheap PHP & MySQL Hosting](php-mysql-hosting/README.md) |
| Hosting 5, 10, or 20+ websites | [Cheap Hosting for Multiple Websites](multiple-websites/README.md) |
| Month-to-month without multi-year lock-in | [No-Contract Monthly Hosting](monthly-hosting/README.md) |
| Understand renewal pricing math | [Renewal Cost Calculator Methodology](renewal-cost-calculator/README.md) |

### Provider Deep-Dives & Comparisons
- [Hostinger Pricing & Renewal Breakdown](providers/hostinger/README.md)
- [IONOS Pricing & Renewal Breakdown](providers/ionos/README.md)
- [Namecheap Pricing & Renewal Breakdown](providers/namecheap/README.md)
- [Hetzner US Cloud VPS Breakdown](providers/hetzner/README.md)
- [Hostinger vs Namecheap (3-Year True Cost)](comparisons/hostinger-vs-namecheap/README.md)
- [Shared Hosting vs Cheap VPS](comparisons/shared-vs-vps/README.md)

---

## Quick Start: Python CLI

Zero external dependencies (Python 3.9+ standard library only).

```bash
# Find all US-based hosting under $5/mo effective over 36 months
python3 hosting_finder.py --months 36 --max-budget 5 --us-only

# Find a cheap Linux VPS with Docker and root access
python3 hosting_finder.py --category vps --stack docker root_access --us-only

# Find month-to-month hosting for 10 websites (no multi-year contract)
python3 hosting_finder.py --websites 10 --monthly-only --months 24

# Compare specific plans side-by-side over 36 months
python3 hosting_finder.py --compare ionos-plus hostinger-premium namecheap-stellar-plus hetzner-cx22-us --months 36
```

### Run Tests

```bash
python3 -m unittest discover -s tests -v
```

---

## Data & Methodology

- All plans are stored in [`data/plans.json`](data/plans.json) with `source_url` and `last_verified` timestamps.
- Effective monthly cost is calculated as:
  $$\text{Effective Monthly} = \frac{(\text{Promo Months} \times \text{Promo Rate}) + (\text{Renewal Months} \times \text{Renewal Rate}) + \text{Setup Fee}}{\text{Total Months}}$$
- Multi-site scaling automatically accounts for single-site plan limits (`max_websites`).
- Taxes, optional add-on backups, and domain renewal fees after year 1 are excluded from base plan calculations and noted separately where applicable.

## License

MIT — see [LICENSE](LICENSE).
