# Month-to-month and no-contract hosting

Many shared hosts only give you their advertised `$2.99/mo` rate if you prepay 36 or 48 months upfront. If you want month-to-month billing without a multi-year contract, filter for plans with `monthly_no_contract_usd` support.

## No-contract monthly plans

| Plan | Category | Month-to-Month Rate | Websites | Notes |
| --- | --- | --- | --- | --- |
| NearlyFreeSpeech Pay-As-You-Go | Shared | `$1.00/mo` | Unlimited | Pay-as-you-go usage billing |
| IONOS VPS Linux XS | VPS | `$2.00/mo` | Unlimited | 1 GB RAM, root SSH |
| BuyVM KVM Slice 512MB | VPS | `$2.00/mo` | Unlimited | 0.5 GB RAM, unmetered bandwidth |
| InterServer Standard | Shared | `$2.50/mo` | Unlimited | DirectAdmin, Price Lock |
| Fly.io Shared CPU 1x | PaaS | `$3.19/mo` | Unlimited | Container / Docker PaaS |
| DigitalOcean 512MB | VPS | `$4.00/mo` | Unlimited | Hourly/monthly billing |
| OVHcloud VPS Starter | VPS | `$4.20/mo` | Unlimited | 2 GB RAM, 40 GB SSD |
| Namecheap Stellar | Shared | `$4.48/mo` | 3 | cPanel included |
| DreamHost Shared Starter | WordPress | `$4.95/mo` | 1 | Month-to-month option |
| Hetzner Cloud CX22 (US) | VPS | `$4.99/mo` | Unlimited | 4 GB RAM, 2 vCPU |
| Vultr / Linode 1GB | VPS | `$5.00/mo` | Unlimited | Hourly/monthly billing |

```bash
python3 hosting_finder.py --monthly-only --months 12 --us-only
```
