# Hosting renewal cost calculator methodology

Two plans that both advertise `$2.99/mo` can end up costing `$107.64` vs `$467.64` over 3 years because promo term length and renewal rate matter more than the headline promotional price.

## Formula

$$\text{Total Cost} = \left(\min(M, T_{\text{promo}}) \times P_{\text{promo}}\right) + \left(\max(0, M - T_{\text{promo}}) \times P_{\text{renewal}}\right) + F_{\text{setup}}$$

$$\text{Effective Monthly Cost} = \frac{\text{Total Cost}}{M}$$

Where $M$ is the total months you plan to keep the hosting (`12`, `24`, `36`, or `48`), $T_{\text{promo}}$ is the promotional term length in months, $P_{\text{promo}}$ is the promotional monthly rate, $P_{\text{renewal}}$ is the standard renewal monthly rate, and $F_{\text{setup}}$ is any one-time setup fee.

## Worked example: IONOS Web Hosting Plus (36 months)

Over 36 months, IONOS Plus charges `$1.00/mo` for the first `12` months (`$12.00`) and `$14.00/mo` for the remaining `24` months (`$336.00`), totaling `$348.00`. That works out to `$9.67/mo` effective and a `+1,300.0%` renewal jump.

```bash
python3 hosting_finder.py --compare ionos-plus hostinger-premium namecheap-stellar-plus hetzner-cx22-us --months 36
```
