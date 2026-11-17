# Web Hosting Under $5/Month (Real Effective Cost)

Many plans advertise `"under $5/mo"` for year 1 and then jump to `$12–$18/mo`. Below are plans whose **true effective monthly cost over 36 months** stays **at or under `$5.00/mo`**.

## Verified Plans ≤ $5.00/mo (36-Month Horizon)

| Plan | Type | Promo | Renewal | 36-Mo Total | Effective/mo | Lock-in? |
| --- | --- | --- | --- | --- | --- | --- |
| **RackNerd 1GB KVM** | VPS | `$1.08/mo` | `$1.08/mo` | `$38.88` | **`$1.08/mo`** | 12 mo |
| **IONOS VPS Linux XS** | VPS | `$2.00/mo` | `$2.00/mo` | `$72.00` | **`$2.00/mo`** | None (1 mo) |
| **InterServer Standard** | Shared | `$2.50/mo` | `$2.50/mo` | `$90.00` | **`$2.50/mo`** | None (1 mo) |
| **Namecheap Stellar** | Shared | `$1.98/mo` | `$4.48/mo` | `$101.28` | **`$2.81/mo`** | 24 mo promo |
| **Hostinger Premium** | Shared | `$2.99/mo` | `$7.99/mo` | `$107.64` | **`$2.99/mo`** | 48 mo prepay |
| **Fly.io Shared CPU 1x** | PaaS | `$3.19/mo` | `$3.19/mo` | `$114.84` | **`$3.19/mo`** | None (1 mo) |
| **DreamHost Unlimited** | Shared | `$3.95/mo` | `$12.99/mo` | `$142.20` | **`$3.95/mo`** | 36 mo prepay |
| **DigitalOcean 512MB** | VPS | `$4.00/mo` | `$4.00/mo` | `$144.00` | **`$4.00/mo`** | None (1 mo) |
| **Namecheap Stellar Plus** | Shared | `$2.98/mo` | `$6.48/mo` | `$149.28` | **`$4.15/mo`** | 24 mo promo |
| **OVHcloud VPS Starter** | VPS | `$4.20/mo` | `$4.20/mo` | `$151.20` | **`$4.20/mo`** | None (1 mo) |
| **Hetzner Cloud CX22 (US)** | VPS | `$4.99/mo` | `$4.99/mo` | `$179.64` | **`$4.99/mo`** | None (1 mo) |
| **Vultr / Linode 1GB** | VPS | `$5.00/mo` | `$5.00/mo` | `$180.00` | **`$5.00/mo`** | None (1 mo) |

## CLI Command

```bash
python3 hosting_finder.py --max-budget 5.00 --months 36 --us-only
```
