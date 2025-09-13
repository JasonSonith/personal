# SSH "Brute-Force" Simulation: Evidence and Notes

Scope and ethics: The following artifacts were generated in an isolated home lab to validate pfSense IDS/IPS (Suricata) visibility against repeated SSH password failures. No instructions for running offensive tools are included here. This document only preserves evidence you already collected plus context for your report.

## Environment

* Target (Ubuntu): 192.168.56.50 running OpenSSH on TCP/22 with lab user labssh
* Firewall and IDS: pfSense with Suricata on LAN and or OPT1
* Source (Kali): Lab VM on OPT1

## Reachability check (ICMP)

```
PING 192.168.56.50 (192.168.56.50) 56(84) bytes of...me 4056ms
rtt min/avg/max/mdev = 0.000/0.000/0.000/0.000 ms
```

## Attempt A: SSH password guessing output for a single user

Command redacted. This section preserves the original tool output only.

```
Hydra v9.5 (c) 2023 by van Hauser/THC & ...com/vanhauser-thc/thc-hydra) finished at 2025-09-12 22:37:09
```

Observation: The tool reported valid credential discovery for user labssh.

## Attempt B: SSH password guessing output using a username list

Command redacted. Output excerpt below shows in progress status and a discovery line.

```
Hydra v9.5 (c) 2023 by van Hauser/T...4606 tries in 00:01h, 286887775 to do in 00:20h, 14 active
```

Observation: With a username list, the same labssh credential was identified.

## Expected detections to capture

* Ubuntu: /var/log/auth.log shows repeated "Failed password" events from the source IP before any success.
* Suricata on pfSense: Alerts on SSH client hellos and or a local threshold rule such as 10 or more attempts per minute from one source. Export EVE JSON lines to docs/logs/suricata.sample.json and add screenshots from Services > Suricata > Alerts.
* Optional fail2ban: Bans after threshold if enabled.

## Evidence checklist for the repo

* Screenshots of Suricata alerts on LAN or OPT1 under docs/screenshots/
* Trimmed auth.log with the failure burst saved to docs/logs/auth.sample.txt
* Trimmed EVE JSON alert lines saved to docs/logs/suricata.sample.json
* Network diagram saved to docs/network-diagram.png

## Cleanup and hardening

* Revert Ubuntu sshd\_config to set PasswordAuthentication no and restart SSH.
* Remove or lock any throwaway lab accounts such as labssh.
* Disable or raise thresholds on any lab only Suricata rules. Clear blocks and bans.

Reminder: Keep this evidence and methodology scoped to your own lab systems only.
