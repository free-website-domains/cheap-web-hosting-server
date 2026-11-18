# Cheap WordPress hosting

When buying budget WordPress hosting, check four details before you pay: the 3-year effective cost rather than the year-1 promo, whether free SSL and automatic backups are included (some starter tiers charge extra for backups), how many websites the plan allows (`1` site vs `100` or `unlimited`), and whether email mailboxes are included.

## Budget WordPress options (36 months)

| Plan | 36-Mo Effective/mo | Websites | Backups Included | Free SSL | Email Included |
| --- | --- | --- | --- | --- | --- |
| InterServer Standard | `$2.50/mo` | Unlimited | Yes | Yes | Yes |
| Namecheap Stellar | `$2.81/mo` | 3 | Yes | Yes | Yes |
| Hostinger Premium | `$2.99/mo` | 100 | Yes | Yes | Yes |
| DreamHost Shared Starter | `$2.59/mo` (36m promo) | 1 | Yes | Yes | No |
| Bluehost Basic | `$8.98/mo` | 10 | No | Yes | No |
| SiteGround StartUp | `$12.99/mo` | 1 | Yes | Yes | Yes |

```bash
python3 hosting_finder.py --stack wordpress php mysql free_ssl backups_included --months 36 --us-only
```
