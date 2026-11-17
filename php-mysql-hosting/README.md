# Cheap PHP & MySQL Hosting

Whether you are deploying Laravel, Symfony, WordPress, or custom PHP 8.x + MySQL/MariaDB apps, you can choose between managed shared hosting (cPanel/DirectAdmin/hPanel) or a cheap Linux VPS.

## Lowest-Cost PHP + MySQL Plans (36 Months)

- **Shared (Managed, No Linux Admin):**
  - **InterServer Standard (`$2.50/mo` flat)** — DirectAdmin, PHP, MySQL, SSH, unlimited sites.
  - **Namecheap Stellar (`$2.81/mo` effective)** — cPanel, PHP, MySQL, SSH, up to 3 sites.
  - **Hostinger Premium (`$2.99/mo` on 48m prepay)** — hPanel, PHP, MySQL, SSH, up to 100 sites.
- **VPS (Full Root, Custom PHP/MySQL Tuning):**
  - **IONOS VPS Linux XS (`$2.00/mo` flat)** — 1 GB RAM, 10 GB SSD.
  - **Hetzner Cloud CX22 US (`$4.99/mo` flat)** — 4 GB RAM, 2 vCPU, 40 GB NVMe.

## CLI Command

```bash
python3 hosting_finder.py --stack php mysql --months 36 --us-only
```
