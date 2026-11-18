# Cheap hosting for multiple websites

Buying a `$2.95/mo` single-site plan for 5 to 10 small websites multiplies your bill by 5x to 10x. Pick a multi-site or unlimited-domain shared plan, or run all of them on a single `$4.99/mo` Linux VPS.

## Cost of hosting 10 websites over 36 months

| Plan | Websites Included | Plans Needed (10 sites) | 36-Mo Total | Effective Monthly |
| --- | --- | --- | --- | --- |
| NearlyFreeSpeech Pay-As-You-Go | Unlimited | 1 | `$36.00` | `$1.00/mo` |
| InterServer Standard | Unlimited | 1 | `$90.00` | `$2.50/mo` |
| Hostinger Premium | 100 | 1 | `$107.64` | `$2.99/mo` |
| DreamHost Unlimited | Unlimited | 1 | `$142.20` | `$3.95/mo` |
| Namecheap Stellar Plus | Unlimited | 1 | `$149.28` | `$4.15/mo` |
| Hetzner Cloud CX22 (US) | Unlimited (self-managed) | 1 | `$179.64` | `$4.99/mo` |
| Bluehost Basic | 10 | 1 | `$323.16` | `$8.98/mo` |
| IONOS Essential (1 site) | 1 | 10 | `$2,400.00` | `$66.67/mo` |

```bash
python3 hosting_finder.py --websites 10 --months 36 --us-only
```
