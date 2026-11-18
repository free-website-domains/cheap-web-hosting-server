# Cheap web hosting server and real cost comparison

Most "best cheap web hosting" lists rank providers by first-year promo prices (`$1/mo`, `$2.95/mo`) and bury the `$11.99` to `$17.99/mo` renewal rate.

This repository compares shared hosting, cheap Linux VPS plans, WordPress hosting, and developer PaaS by their actual 1 to 3 year cost, stack support, US server locations, and month-to-month flexibility.

Use the [interactive web finder and calculator](https://free-website-domains.github.io/cheap-web-hosting-server/), browse the JSON datasets ([`data/providers.json`](data/providers.json), [`data/plans.json`](data/plans.json), [`data/pricing-history.json`](data/pricing-history.json)), or run [`hosting_finder.py`](hosting_finder.py) locally.

![Cheap Hosting Finder & True Cost Calculator](docs/assets/preview-desktop.png)

## Cheapest plans that do not spike on renewal (`$1` to `$5/mo`)

| Plan | Type | Monthly Rate | Renewal Spike | 1-Year Total | 3-Year Total | Lock-in |
| --- | --- | --- | --- | --- | --- | --- |
| NearlyFreeSpeech Pay-As-You-Go | Shared, PHP, Python | `$1.00/mo` | `0.0%` | `$12.00` | `$36.00` | None (1 mo) |
| RackNerd 1GB KVM | Linux VPS | `$1.08/mo` | `0.0%` | `$12.96` | `$38.88` | 12 mo |
| IONOS VPS Linux XS | Linux VPS | `$2.00/mo` | `0.0%` | `$24.00` | `$72.00` | None (1 mo) |
| BuyVM KVM Slice 512MB | Linux VPS | `$2.00/mo` | `0.0%` | `$24.00` | `$72.00` | None (1 mo) |
| InterServer Standard | Shared (Unlimited) | `$2.50/mo` | `0.0%` | `$30.00` | `$90.00` | None (1 mo) |
| Hetzner Cloud CX22 (US) | Linux VPS (4 GB RAM) | `$4.99/mo` | `0.0%` | `$59.88` | `$179.64` | None (1 mo) |

### Watch out for `$1` to `$3/mo` promo traps

| Plan | Advertised Promo | Promo Term | Renewal Rate | Renewal Spike | 36-Mo Effective |
| --- | --- | --- | --- | --- | --- |
| IONOS Web Hosting Plus | `$1.00/mo` | 12 mo | `$14.00/mo` | `+1300.0%` | `$9.67/mo` (`$348.00`) |
| Bluehost Basic | `$2.95/mo` | 12 mo | `$11.99/mo` | `+306.4%` | `$8.98/mo` (`$323.16`) |
| SiteGround StartUp | `$2.99/mo` | 12 mo | `$17.99/mo` | `+501.7%` | `$12.99/mo` (`$467.64`) |

## Choose by what you need

People searching for a "cheap web hosting server" usually want one of two things: shared hosting (cPanel or hPanel, PHP, MySQL, WordPress, and email without managing Linux) or a VPS (root SSH access, dedicated RAM and vCPU, Docker, Node.js, or Python, and flat monthly billing).

| Goal | Guide |
| --- | --- |
| Shared hosting with lowest 3-year cost | [Cheap web hosting (shared)](cheap-web-hosting/README.md) |
| Linux VPS with root access and Docker | [Cheap VPS hosting](cheap-vps-hosting/README.md) |
| Plans under `$5/mo` effective cost | [Web hosting under $5/month](under-5-dollars/README.md) |
| Plans under `$10/mo` over 3 years | [Web hosting under $10/month](under-10-dollars/README.md) |
| WordPress with SSL, backups, and PHP | [Cheap WordPress hosting](wordpress-hosting/README.md) |
| PHP and MySQL stack | [Cheap PHP and MySQL hosting](php-mysql-hosting/README.md) |
| Hosting 5, 10, or 20+ websites | [Cheap hosting for multiple websites](multiple-websites/README.md) |
| Month-to-month without multi-year lock-in | [No-contract monthly hosting](monthly-hosting/README.md) |
| How renewal pricing math works | [Renewal cost calculator methodology](renewal-cost-calculator/README.md) |

### Provider breakdowns and comparisons

Providers: [Hostinger](providers/hostinger/README.md), [IONOS](providers/ionos/README.md), [Namecheap](providers/namecheap/README.md), [Hetzner US VPS](providers/hetzner/README.md).

Hetzner vs everyone: [all 14 comparisons](comparisons/README.md), [Hetzner vs DigitalOcean](comparisons/hetzner-vs-digitalocean/README.md), [Hetzner vs Vultr](comparisons/hetzner-vs-vultr/README.md), [Hetzner vs Akamai (Linode)](comparisons/hetzner-vs-linode/README.md), [Hetzner vs OVHcloud](comparisons/hetzner-vs-ovhcloud/README.md), [Hetzner vs Hostinger](comparisons/hetzner-vs-hostinger/README.md), [Hetzner vs IONOS](comparisons/hetzner-vs-ionos/README.md), [Hetzner vs RackNerd](comparisons/hetzner-vs-racknerd/README.md).

Shared and WordPress comparisons: [Hostinger vs Namecheap](comparisons/hostinger-vs-namecheap/README.md), [Hostinger vs Bluehost](comparisons/hostinger-vs-bluehost/README.md), [Hostinger vs SiteGround](comparisons/hostinger-vs-siteground/README.md), [InterServer vs Hostinger](comparisons/interserver-vs-hostinger/README.md), [Namecheap vs Bluehost](comparisons/namecheap-vs-bluehost/README.md), [IONOS vs Namecheap](comparisons/ionos-vs-namecheap/README.md), [Shared vs VPS](comparisons/shared-vs-vps/README.md).

## Python CLI

The CLI runs on Python 3.9+ with no external dependencies.

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

Run the test suite with:

```bash
python3 -m unittest discover -s tests -v
```

## Data and methodology

Each plan in [`data/plans.json`](data/plans.json) includes a `source_url` and `last_verified` timestamp. Effective monthly cost is calculated as:

$$\text{Effective Monthly} = \frac{(\text{Promo Months} \times \text{Promo Rate}) + (\text{Renewal Months} \times \text{Renewal Rate}) + \text{Setup Fee}}{\text{Total Months}}$$

Multi-site calculations scale up automatically when `websites` exceeds a plan's `max_websites` limit. Taxes, optional paid backup add-ons, and domain renewals after year 1 are excluded from the base numbers and noted on individual pages where relevant.

## License

MIT. See [LICENSE](LICENSE).
