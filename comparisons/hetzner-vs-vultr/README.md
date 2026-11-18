# Hetzner vs Vultr (US cloud VPS)

Hetzner and Vultr both offer hourly or monthly Linux VPS instances with 0% renewal spikes. Hetzner gives you more RAM and CPU per dollar, while Vultr covers more US cities.

| Metric | Hetzner Cloud CX22 (US) | Vultr Cloud Compute 1GB |
| --- | --- | --- |
| Monthly Rate | `$4.99/mo` | `$5.00/mo` |
| Renewal Spike | `0.0%` | `0.0%` |
| 12-Month Total | `$59.88` | `$60.00` |
| 36-Month Total | `$179.64` | `$180.00` |
| vCPU, RAM, Disk | 2 vCPU, 4 GB RAM, 40 GB NVMe | 1 vCPU, 1 GB RAM, 25 GB SSD |
| US Locations | 2 (Ashburn VA, Hillsboro OR) | 8+ (NJ, Chicago, Dallas, Atlanta, Seattle, SV, LA, Miami) |

Pick Hetzner CX22 at `$4.99/mo` when Ashburn or Hillsboro latency works for you, since you get `4 GB RAM` instead of `1 GB RAM`. Pick Vultr when you specifically need a server in Dallas, Chicago, Miami, or Los Angeles, or need BGP and custom ISO support.

```bash
python3 hosting_finder.py --compare hetzner-cx22-us vultr-cloud-5 --months 36
```
