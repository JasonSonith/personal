# Personal Projects

This repository contains my personal projects in cybersecurity, networking, and automation.  
Each project is designed to build hands-on skills for security engineering, cloud, and SOC analysis.

## Projects

- [Security Log Analyzer](./log-analyzer)  
  A Python-based log analysis tool that parses system logs, detects suspicious events, and generates structured summaries of suspicious IP activity.  

- [Security-Home-Lab](./Security-Home-Lab)  
  A virtual lab environment built with pfSense and Suricata. The firewall is configured to block unsafe traffic (e.g., Telnet, brute-force SSH attempts) while logging alerts for review.  
  - **Tools:** pfSense, Suricata, VirtualBox, Kali Linux, Ubuntu  
  - **Features:**  
    - IDS/IPS configuration on WAN/OPT1 interfaces  
    - Rulesets for Telnet, SSH brute-force, botnet C2, and scans  
    - Alerts and blocks visible in pfSense GUI  
    - Attack simulations using Nmap and Hydra from Kali  
    - Persistent IP mapping via pfSense DHCP reservations  
