# Suricata Rules for pfSense Lab

This document describes the Suricata rules used in my pfSense IDS and IPS lab. It covers two sources:
1. `custom.rules` that I authored for testing and demonstration.
2. A summary of the compiled `suricata.rules` that pfSense generated from enabled vendor categories. I do not publish the vendor rules file. I report high level counts only.

## Custom rules

The table shows the rules I created. These are alert only and are safe to publish.

|     SID | Message                     | Proto   | Dest Port   | Action   |
|--------:|:----------------------------|:--------|:------------|:---------|
| 1000001 | LOCAL ICMP ping to HOME_NET | icmp    | any         | alert    |
| 1000002 | LOCAL TCP SYN to Telnet     | tcp     | 23          | alert    |
| 1000003 | LOCAL TCP connect to SSH    | tcp     | 22          | alert    |
| 1000004 | LOCAL TCP connect to HTTP   | tcp     | 80          | alert    |
| 1000005 | LOCAL TCP connect to RDP    | tcp     | 3389        | alert    |

### The custom rules as text
```conf
# ICMP echo (ping) to HOME_NET
alert icmp any any -> $HOME_NET any (msg:"LOCAL ICMP ping to HOME_NET"; itype:8; classtype:misc-activity; sid:1000001; rev:1;)

# TCP SYN to Telnet (23) on HOME_NET
alert tcp any any -> $HOME_NET 23 (msg:"LOCAL TCP SYN to Telnet"; flags:S; classtype:misc-activity; sid:1000002; rev:1;)

# TCP connect attempts to common services on HOME_NET (22,80,3389)
alert tcp any any -> $HOME_NET 22 (msg:"LOCAL TCP connect to SSH"; flags:S; classtype:misc-activity; sid:1000003; rev:1;)
alert tcp any any -> $HOME_NET 80 (msg:"LOCAL TCP connect to HTTP"; flags:S; classtype:misc-activity; sid:1000004; rev:1;)
alert tcp any any -> $HOME_NET 3389 (msg:"LOCAL TCP connect to RDP"; flags:S; classtype:misc-activity; sid:1000005; rev:1;)
