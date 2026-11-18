# Cheap PHP and MySQL hosting

For Laravel, Symfony, WordPress, or custom PHP 8.x and MySQL/MariaDB apps, you can pick either managed shared hosting with a control panel or a cheap Linux VPS.

## Lowest-cost PHP and MySQL plans (36 months)

Managed shared hosting (no Linux administration):

- NearlyFreeSpeech Pay-As-You-Go (`$1.00/mo` typical for small sites): pay-as-you-go PHP, MySQL, SSH, unlimited sites.
- InterServer Standard (`$2.50/mo` flat): DirectAdmin, PHP, MySQL, SSH, unlimited sites.
- Namecheap Stellar (`$2.81/mo` effective): cPanel, PHP, MySQL, SSH, up to 3 sites.
- Hostinger Premium (`$2.99/mo` on 48m prepay): hPanel, PHP, MySQL, SSH, up to 100 sites.

Linux VPS (full root access and custom PHP/MySQL tuning):

- IONOS VPS Linux XS (`$2.00/mo` flat): 1 GB RAM, 10 GB SSD.
- BuyVM KVM Slice 512MB (`$2.00/mo` flat): 0.5 GB RAM, 10 GB SSD.
- Hetzner Cloud CX22 US (`$4.99/mo` flat): 4 GB RAM, 2 vCPU, 40 GB NVMe.

```bash
python3 hosting_finder.py --stack php mysql --months 36 --us-only
```
