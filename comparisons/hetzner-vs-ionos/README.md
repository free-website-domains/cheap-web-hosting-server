# Hetzner vs IONOS (3-year cost comparison)

IONOS advertises a `$1.00/mo` shared hosting promo that jumps to `$14.00/mo` in year 2, alongside a flat `$2.00/mo` Linux VPS XS plan.

| Metric | Hetzner Cloud CX22 (US) | IONOS VPS Linux XS | IONOS Web Hosting Plus |
| --- | --- | --- | --- |
| Type | Cloud VPS | Linux VPS | Shared Hosting |
| Promo Rate | `$4.99/mo` | `$2.00/mo` | `$1.00/mo` (12m) |
| Renewal Rate | `$4.99/mo` | `$2.00/mo` | `$14.00/mo` |
| Renewal Spike | `0.0%` | `0.0%` | `+1,300.0%` |
| 36-Month Total | `$179.64` | `$72.00` | `$348.00` |
| Effective Monthly | `$4.99/mo` | `$2.00/mo` | `$9.67/mo` |
| vCPU, RAM, Disk | 2 vCPU, 4 GB, 40 GB | 1 vCPU, 1 GB, 10 GB | Shared (2 vCPU, 2 GB) |

Hetzner CX22 (`$179.64` over 36m) is nearly 2x cheaper than IONOS Shared Plus (`$348.00` over 36m) while giving you dedicated 4 GB RAM, 2 vCPU, Docker, and root SSH. IONOS VPS Linux XS (`$2.00/mo`) is the cheaper US VPS option if `1 GB RAM` and `10 GB` storage are enough for a small app or proxy.

```bash
python3 hosting_finder.py --compare hetzner-cx22-us ionos-vps-xs ionos-plus --months 36
```
