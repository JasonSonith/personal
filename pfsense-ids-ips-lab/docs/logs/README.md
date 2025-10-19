# pfSense Lab Logs

This directory contains sanitized Suricata intrusion detection and prevention system logs collected from a pfSense firewall lab environment. The logs demonstrate detection of simulated network activity and alerts generated during testing.

## Files

- **alerts.log**  
  Plain text Suricata alerts recorded during test activity.  
  Examples include ICMP pings to the internal network, TCP SYN attempts to Telnet, SSH, HTTP, and RDP services.

- **eve.json**  
  JSON-formatted event data exported from Suricata.  
  Provides structured details on flows, DNS queries, and alerts. Captures traffic between internal virtual machines and external destinations such as 1.1.1.1 and 8.8.8.8.

## Purpose

These logs serve as supporting evidence of intrusion detection and firewall rule testing. They are sanitized to remove sensitive information while preserving the structure of alerts and event records for documentation and educational purposes.

## Usage

- Review `alerts.log` for human readable alerts categorized by Suricata signatures.  
- Analyze `eve.json` with log analysis tools or SIEM platforms such as Splunk or Elasticsearch to visualize traffic flows and security events.  
- Use these files as sample input when demonstrating parsing, alert correlation, or detection rules.
