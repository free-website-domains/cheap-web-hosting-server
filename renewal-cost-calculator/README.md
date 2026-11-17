# Hosting Renewal Cost Calculator — Methodology

Why do two `$2.99/mo` plans end up costing `$107.64` vs `$467.64` over 3 years? Because **promo term length** and **renewal rate** matter far more than the headline promotional number.

## Formula

$$\text{Total Cost} = \left(\min(M, T_{\text{promo}}) \times P_{\text{promo}}\right) + \left(\max(0, M - T_{\text{promo}}) \times P_{\text{renewal}}\right) + F_{\text{setup}}$$

$$\text{Effective Monthly Cost} = \frac{\text{Total Cost}}{M}$$

Where:
- $M$ = Total months you plan to keep the hosting (`12`, `24`, `36`, or `48`)
- $T_{\text{promo}}$ = Promotional term length in months
- $P_{\text{promo}}$ = Promotional monthly price
- $P_{\text{renewal}}$ = Standard renewal monthly price
- $F_{\text{setup}}$ = One-time setup fee

## Worked Example: IONOS Web Hosting Plus (36 Months)

- Advertised price: `$1.00/mo` for `12` months = `$12.00`
- Renewal price: `$14.00/mo` for remaining `24` months = `$336.00`
- Total 36-month cost: **`$348.00`**
- Effective monthly cost: **`$9.67/mo`**
- Renewal spike: **`+1,300.0%`**

Try it yourself in the terminal:

```bash
python3 hosting_finder.py --compare ionos-plus hostinger-premium namecheap-stellar-plus hetzner-cx22-us --months 36
```
