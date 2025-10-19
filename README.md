# Jason Sonith — Personal Projects

High-level index of my security and tooling work. Each subfolder is a self-contained project with its own README and evidence.

## Highlights
- Python log analysis and automation for blue-team workflows.
- Network defense lab with pfSense + Suricata showing IDS/IPS policy, attack simulation, and EVE JSON export.

## Index

### `/log-analyzer/`
Python toolchain that parses Linux auth and web logs, classifies events (failed logins, invalid users, sudo failures), extracts IPs/timestamps, emits JSON/CSV, and summarizes activity. Skills: argparse CLIs, regex parsing, structured logging, tabular CLI output.

**Why it matters:** repeatable triage for SSH brute-force, account spray, and basic IR enrichment.

**Quick start:**
```bash
cd log-analyzer
pip install -r requirements.txt
python analyzer.py --logfile sample.log
```

### `/pfsense-ids-ips-lab/`
End-to-end IDS/IPS lab: pfSense firewall + Suricata on WAN/OPT with rules for Telnet, SSH brute force, and scan detection. Includes topology, NAT test flows, and results showing blocks and alerting, plus EVE JSON for SIEM. Future work: Splunk/ELK integration, WireGuard, Nessus validation loop.

**Why it matters:** demonstrates policy-to-signal path and how to validate controls with live traffic.

## Usage pattern
1. Enter a project folder.
2. Read its local README.
3. If Python, create a virtualenv.
4. Run the minimal demo command.
5. For labs, follow the topology and reproduce the evidence steps.

## Roadmap
- JSONL → SIEM loaders for analyzer outputs.
- WireGuard hardening and remote log shipping from pfSense to ELK.

---
For recruiters or collaborators: this root README summarizes scope; each subproject shows depth.
