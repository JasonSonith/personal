#  pfSense IDS/IPS Lab with Suricata

##  Project Overview
This project demonstrates setting up a pfSense firewall with Suricata IDS/IPS 
to block unsafe traffic (Telnet, brute-force SSH, botnet C2) and log alerts 
for review. The lab simulates real-world attack traffic from Kali Linux to 
an Ubuntu victim machine, routed through pfSense.

##  Lab Topology
```mermaid
graph TD
  Kali[Kali VM<br/>10.10.10.20] -->|OPT1 10.10.10.1| pfSense[pfSense Firewall<br/>WAN: 10.0.2.15<br/>LAN: 192.168.56.2<br/>OPT1: 10.10.10.1]
  pfSense -->|LAN 192.168.56.2| Ubuntu[Ubuntu VM<br/>192.168.56.50]
  pfSense -->|WAN 10.0.2.15| Internet[(Internet)]



