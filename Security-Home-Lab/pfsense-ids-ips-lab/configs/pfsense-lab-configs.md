# pfSense Lab Network Configuration

This document captures the core settings for my pfSense lab that connects an Ubuntu host on **LAN** and a Kali host on **OPT1**, with Internet access on **WAN**.

## Topology

```
Internet
   |
 [WAN] pfSense [LAN 192.168.56.0/24] ---- Ubuntu host(s)
                 |
               [OPT1 10.10.10.0/24] ---- Kali host(s)
```

## Interfaces

- **WAN**: Internet uplink.
- **LAN**: 192.168.56.0/24, used for the Ubuntu segment.
- **OPT1**: 10.10.10.0/24, used for the Kali segment.

## DHCP

- **LAN DHCP scope**: 192.168.56.100 to 192.168.56.199.
- **OPT1 addressing plan**: 10.10.10.1 to 10.10.10.254 on 10.10.10.0/24.
  - If DHCP is enabled on OPT1, use a scope in this range that fits your lab. Avoid handing out the interface IP if it is 10.10.10.1.

## NAT

- **Outbound NAT mode**: automatic. pfSense generates the appropriate rules so hosts on LAN and OPT1 can reach the Internet through WAN.

## Firewall Rules

### WAN
| Action | Protocol | Source            | Src Port | Destination | Dst Port | Description |
|-------:|----------|-------------------|---------:|-------------|---------:|-------------|
| Pass   | IPv4 TCP | 192.168.56.1/24   | *        | 10.0.2.15   | *        | Lab access from LAN network to upstream NAT target |

### LAN
| Action | Protocol | Source   | Src Port | Destination | Dst Port | Description |
|-------:|----------|----------|---------:|-------------|---------:|-------------|
| Pass   | IPv4 *   | LAN net  | *        | any         | *        | Default allow LAN to any (lab) |

### OPT1
| Action | Protocol | Source         | Src Port | Destination | Dst Port | Description |
|-------:|----------|----------------|---------:|-------------|---------:|-------------|
| Pass   | IPv4 *   | 10.10.10.0/24  | *        | any         | *        | Allow all from OPT1 |
| Pass   | IPv4 TCP | 10.10.10.0/24  | *        | any         | *        | Additional TCP rule (lab) |

## IDS / IPS

- **Suricata** is installed and running. Sanitized logs from testing are included under `docs/logs/` in this repository:
  - `alerts.log` for human readable alerts
  - `eve.json` for structured event data

## Reproducibility

- A full configuration export (`config.xml`) is included in this repository so the lab state can be restored in pfSense via **Diagnostics > Backup & Restore**.
- Before sharing, sensitive data has been sanitized.

## Notes

- The configuration is intended for a contained lab environment focused on learning firewalling, NAT, intrusion detection, and traffic analysis.
- Adjust ranges, rules, and services as needed to fit your host IPs and hypervisor networks.
