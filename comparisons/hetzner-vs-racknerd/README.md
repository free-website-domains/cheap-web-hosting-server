# Hetzner vs RackNerd (cloud VPS vs annual KVM)

Both Hetzner and RackNerd offer US-based Linux VPS servers with 0% renewal spikes, aimed at different budgets and workloads.

| Metric | Hetzner Cloud CX22 (US) | RackNerd 1GB KVM (Annual) |
| --- | --- | --- |
| Effective Monthly | `$4.99/mo` | `$1.08/mo` (`$12.96/yr`) |
| Billing Cycle | Hourly / Monthly (No lock-in) | Annual (12m prepay) |
| 36-Month Total | `$179.64` | `$38.88` |
| vCPU, RAM, Disk | 2 vCPU, 4 GB RAM, 40 GB NVMe | 1 vCPU, 1 GB RAM, 20 GB SSD |
| US Locations | Ashburn (VA), Hillsboro (OR) | LA, SJ, Seattle, Chicago, Dallas, NY, Ashburn |

Pick Hetzner CX22 for production web apps, Docker containers, CI runners, or anything needing 4 GB RAM, cloud APIs, and hourly snapshots. Pick RackNerd 1GB KVM if your priority is the lowest annual dollar cost (`$12.96/yr`) for small scripts, personal blogs, or WireGuard and monitoring nodes.

```bash
python3 hosting_finder.py --compare hetzner-cx22-us racknerd-1gb-kvm --months 36
```
