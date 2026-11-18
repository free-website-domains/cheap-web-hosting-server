# Web hosting under $10 per month

Raising your budget to `$10/mo` effective opens up higher-RAM VPS tiers, managed PaaS, and standard shared plans even after their year-2 renewal increase.

## Plans between $5.01 and $10.00/mo effective (36 months)

- DigitalOcean Basic Droplet 1GB (`$6.00/mo` flat): `$216.00` over 36 months, 25 GB SSD, US East and West.
- Hostinger KVM 1 VPS (`$4.99/mo` for 24 mo, then `$9.99/mo`): `$239.64` over 36 months (`$6.66/mo` effective), 4 GB RAM.
- IONOS Essential (`$4.00/mo` for 12 mo, then `$8.00/mo`): `$240.00` over 36 months (`$6.67/mo` effective), 1 website.
- Render Starter Web Service (`$7.00/mo` flat): `$252.00` over 36 months, managed Node.js, Python, and Docker PaaS.
- GreenGeeks Lite (`$2.95/mo` for 12 mo, then `$11.95/mo`): `$322.20` over 36 months (`$8.95/mo` effective).
- Bluehost Basic (`$2.95/mo` for 12 mo, then `$11.99/mo`): `$323.16` over 36 months (`$8.98/mo` effective).
- IONOS Plus (`$1.00/mo` for 12 mo, then `$14.00/mo`): `$348.00` over 36 months (`$9.67/mo` effective).

```bash
python3 hosting_finder.py --max-budget 10.00 --months 36 --us-only
```
