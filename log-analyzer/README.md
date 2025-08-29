# AI Threat Detector and Analyzer  

## Overview  
The **AI Threat Detector and Analyzer** is a Python-based tool that parses system and application logs to detect suspicious activity. It outputs a structured report highlighting suspicious IPs, event counts, and possible attack types.  

This project demonstrates skills in Python scripting, log parsing, and cybersecurity automation.  

---

## Features  
- Log parsing for Linux `/var/log/auth.log`, Windows EVTX exports, and JSON/CSV log files  
- Suspicious event detection: failed logins, brute-force attempts, port scans  
- Suspicious IP tracking: counts failed attempts, classifies likely attack types  
- Optional enhancements:  
  - Geolocation of IP addresses  
  - File integrity checks (`hashlib`, `watchdog`)  
  - Persistent storage with `sqlite3`  

---

## Example Output  

```
Suspicious IP      Attempts     Possible Attack
192.168.1.50       50           SSH brute force
10.0.0.22          12           Port scanning
203.0.113.5         7           Repeated failed logins
```

---

## Installation  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/JasonSonith/log-analyzer.git
cd AI-Threat-Analyzer
pip install -r requirements.txt
```

Requirements:  
- Python 3.9+  
- pandas  
- colorama  
- requests  
- watchdog (optional)  

---

## Usage  

Run the analyzer on a log file:  

```bash
python analyzer.py --logfile authlog.json
```

Options:  
- `--logfile` : Path to the log file (JSON, CSV, or text-based auth logs)  

---

## Skills Demonstrated  
- Python CLI scripting (`argparse`, `os`, `pathlib`)  
- Log parsing with regex and structured storage (`json`, `pandas`)  
- Security automation (detecting brute-force, failed logins, suspicious IPs)  
- Clean, structured CLI output with `colorama`  

---

## Project Roadmap  
- Build CLI parser  
- Extract suspicious events  
- Print summary tables with suspicious IPs  
- Save reports  
- Future work: IP geolocation, real-time monitoring with `watchdog`, SQLite history  

---


