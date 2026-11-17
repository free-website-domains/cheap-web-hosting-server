# Cheap WordPress Hosting (PHP, MySQL, SSL & Backups)

To run WordPress without server administration headaches, check four things before buying:
1. **3-Year Effective Cost** (not just year 1 promo).
2. **Free SSL & Automatic Backups** (some hosts charge extra for backups on starter tiers).
3. **Website Limit** (`1` site vs `unlimited` / `100` sites).
4. **Email Hosting** (some WordPress plans exclude email mailboxes).

## Best Budget WordPress Options (36 Months)

| Plan | 36-Mo Effective/mo | Websites | Backups Included | Free SSL | Email Included |
| --- | --- | --- | --- | --- | --- |
| **InterServer Standard** | `$2.50/mo` | Unlimited | Yes | Yes | Yes |
| **Namecheap Stellar** | `$2.81/mo` | 3 | Yes | Yes | Yes |
| **Hostinger Premium** | `$2.99/mo` | 100 | Yes | Yes | Yes |
| **DreamHost Shared Starter** | `$2.59/mo` (36m promo) | 1 | Yes | Yes | No |
| **Bluehost Basic** | `$8.98/mo` | 10 | No | Yes | No |
| **SiteGround StartUp** | `$12.99/mo` | 1 | Yes | Yes | Yes |

## CLI Command

```bash
python3 hosting_finder.py --stack wordpress php mysql free_ssl backups_included --months 36 --us-only
```
