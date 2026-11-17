# Contributing

Contributions to keep pricing, renewal rates, US data center locations, and technical stack support accurate are welcome!

## Updating Plan Data

1. Edit [`data/plans.json`](data/plans.json) or [`data/providers.json`](data/providers.json).
2. Update `last_verified` to today's `YYYY-MM-DD` date and ensure `source_url` points to the official pricing page.
3. If a provider's promotional or renewal pricing changed significantly, add a snapshot entry to [`data/pricing-history.json`](data/pricing-history.json).
4. Run the test suite before opening a pull request:

```bash
python3 -m unittest discover -s tests -v
```
