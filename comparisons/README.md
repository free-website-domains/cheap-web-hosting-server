# Web Hosting & VPS Head-to-Head Comparisons

Every comparison below uses verified US-market pricing from [`data/plans.json`](../data/plans.json) and calculates the **true 12-, 24-, and 36-month Total Cost of Ownership (TCO)** — not just year-1 promo numbers.

## Hetzner vs Everyone (US Cloud VPS & Shared Hosting)

| Comparison | Key Difference |
| --- | --- |
| [Hetzner vs DigitalOcean](hetzner-vs-digitalocean/README.md) | `4 GB RAM` at `$4.99/mo` vs `1 GB RAM` at `$6.00/mo` |
| [Hetzner vs Vultr](hetzner-vs-vultr/README.md) | `4 GB RAM / 2 vCPU` vs `1 GB RAM / 1 vCPU` (8+ US cities) |
| [Hetzner vs Akamai (Linode)](hetzner-vs-linode/README.md) | `4 GB RAM` at `$4.99/mo` vs `1 GB RAM` at `$5.00/mo` |
| [Hetzner vs OVHcloud](hetzner-vs-ovhcloud/README.md) | `4 GB RAM` at `$4.99/mo` vs `2 GB RAM` at `$4.20/mo` |
| [Hetzner vs Hostinger](hetzner-vs-hostinger/README.md) | Flat `$4.99/mo` VPS vs `$4.99 → $9.99/mo` KVM 1 & Shared |
| [Hetzner vs IONOS](hetzner-vs-ionos/README.md) | `$4.99/mo` 4 GB VPS vs `$2.00/mo` 1 GB VPS & `$1 → $14/mo` Shared |
| [Hetzner vs RackNerd](hetzner-vs-racknerd/README.md) | Cloud NVMe hourly billing vs `$1.08/mo` annual budget KVM |

## Shared & WordPress Hosting Comparisons

| Comparison | Key Difference |
| --- | --- |
| [Hostinger vs Namecheap](hostinger-vs-namecheap/README.md) | `hPanel` 48m prepay vs `cPanel` with Node.js/Python |
| [Hostinger vs Bluehost](hostinger-vs-bluehost/README.md) | `$107.64` vs `$323.16` over 36 months (`+306%` renewal) |
| [Hostinger vs SiteGround](hostinger-vs-siteground/README.md) | `$107.64` vs `$467.64` over 36 months (`$17.99/mo` renewal) |
| [InterServer vs Hostinger](interserver-vs-hostinger/README.md) | `$2.50/mo` Price Lock month-to-month vs 48m prepay |
| [Namecheap vs Bluehost](namecheap-vs-bluehost/README.md) | `cPanel` at `$149.28` (36m) vs `$323.16` (36m) |
| [IONOS vs Namecheap](ionos-vs-namecheap/README.md) | `$1 → $14/mo` (`$348` 36m) vs `$2.98 → $6.48/mo` (`$149.28` 36m) |
| [Shared Hosting vs Cheap VPS](shared-vs-vps/README.md) | Managed panel & email vs root SSH, Docker & flat pricing |

## Run Any Custom Comparison in CLI

```bash
python3 hosting_finder.py --compare hetzner-cx22-us digitalocean-droplet-6 vultr-cloud-5 linode-nanode-1gb --months 36
```
