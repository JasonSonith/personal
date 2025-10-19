# Nmap Scan Report — Ubuntu (192.168.56.50)

This document summarizes all scans performed from Kali against the Ubuntu host at 192.168.56.50. Each section lists the command used, key findings, and a reference to the raw output file.

---

## 1) Host Discovery

**Standard ping sweep**
- **Command:** `nmap -sn 192.168.56.50 -oN 01_ping.txt`
- **Result:** Host is up.

**Ping disabled bypass**
- **Command:** `nmap -Pn -sn 192.168.56.50 -oN 01_ping_pn.txt`
- **Result:** Host is up.

---

## 2) TCP Scans

**Top 1000 TCP ports with default scripts and versions**
- **Command:** `nmap -sS -sC -sV 192.168.56.50 -oN 02_tcp_top1000.txt`
- **Result:** All 1000 TCP ports closed.

**Full TCP port sweep**
- **Command:** `nmap -sS -p- -T3 --min-rate 200 192.168.56.50 -oN 03_tcp_full.txt`
- **Result:** All 65,535 TCP ports closed.

**Targeted TCP ports mapped to Suricata rules (22, 23, 80, 3389)**
- **Command:** `nmap -sS -p 22,23,80,3389 192.168.56.50 -oN 04_tcp_targeted.txt`
- **Result:** 22 ssh closed, 23 telnet closed, 80 http closed, 3389 ms-wbt-server closed.

**Aggressive fingerprinting**
- **Command:** `nmap -A 192.168.56.50 -oN 05_tcp_aggressive.txt`
- **Result:** All scanned TCP ports closed. Traceroute shows two hops to target. OS fingerprint inconclusive due to lack of open ports.

---

## 3) UDP Scans

**Top 100 UDP ports**
- **Command:** `nmap -sU --top-ports 100 192.168.56.50 -oN 06_udp_top100.txt`
- **Result:** Majority closed by ICMP port unreachable. 5353/udp reported open|filtered consistent with mDNS.

**Common UDP services**
- **Command:** `nmap -sU -p 53,67,68,69,123,137,161,500,1900 192.168.56.50 -oN 07_udp_common.txt`
- **Result:** All listed UDP ports closed.

---

## 4) OS and Service Fingerprinting

**OS detection**
- **Command:** `nmap -O 192.168.56.50 -oN 08_os_detect.txt`
- **Result:** OS detection inconclusive. Network distance two hops.

**Focused service probes**
- **Command:** `nmap -sS -sV -p 22,80 192.168.56.50 -oN 09_service_fingerprints.txt`
- **Result:** 22 ssh closed, 80 http closed. No banners identified.

---

## 5) NSE Scripted Checks

**Focused NSE scripts**
- **Command:** `nmap -sS -sV --script banner,ssh2-enum-algos,ssl-cert,http-title -p 22,80 192.168.56.50 -oN 10_nse_focus.txt`
- **Result:** 22 tcp closed, 80 tcp closed.

**Vulnerability category**
- **Command:** `nmap -sS -sV --script vuln -p 22,80,3389 192.168.56.50 -oN 11_nse_vuln.txt`
- **Result:** 22 tcp closed, 80 tcp closed, 3389 tcp closed.

---

## 6) Stealth and Evasion Scans

**Null scan**
- **Command:** `nmap -sN -p 22,80 192.168.56.50 -oN 12_tcp_null.txt`
- **Result:** 22 and 80 reported open|filtered, typical when a firewall drops probes without sending RST.

**FIN scan**
- **Command:** `nmap -sF -p 22,80 192.168.56.50 -oN 13_tcp_fin.txt`
- **Result:** 22 and 80 reported open|filtered, consistent with filtered handling.

**Xmas scan**
- **Command:** `nmap -sX -p 22,80 192.168.56.50 -oN 14_tcp_xmas.txt`
- **Result:** File could not be parsed in this workspace. Please reupload in text form for exact details.

**Fragmented SYN**
- **Command:** `nmap -sS -f -p 22,80 192.168.56.50 -oN 15_fragments.txt`
- **Result:** 22 tcp closed, 80 tcp closed. Fragmentation did not bypass filtering.

**ACK scan**
- **Command:** `nmap -sA -p 22,80 192.168.56.50 -oN 16_ack_scan.txt`
- **Result:** 22 and 80 filtered, indicating a stateful firewall or packet filter between scanner and host.

---

## Summary of Findings

- The host at 192.168.56.50 is reachable.  
- All tested TCP ports are closed across both the top 1000 and full sweep.  
- Targeted ports used in the lab (22, 23, 80, 3389) are closed.  
- UDP scanning suggests mDNS behavior at 5353/udp as open|filtered, others closed.  
- OS fingerprinting is inconclusive without open ports.  
- NSE script runs confirmed no services available on 22, 80, or 3389 for enumeration or vuln checks.  
- Stealth scans (Null and FIN) show open|filtered on 22 and 80, consistent with silent drops. ACK scan labels ports filtered, indicating stateful filtering. Fragmented SYN did not change outcomes.

---

## Notes and Next Steps

- If you expect services to be open for demonstration, start them on Ubuntu and rescan specific ports:
  - `sudo systemctl start ssh` then `nmap -sS -sV -p 22 192.168.56.50`
  - `python3 -m http.server 80` then `nmap -sS -sV -p 80 192.168.56.50`
- For clearer OS detection, ensure at least one stable open TCP port exists.  
- To include the Xmas scan details, reupload `14_tcp_xmas.txt` as a readable text file and this section can be updated accordingly.

---

## File Map

- `01_ping.txt` and `01_ping_pn.txt` — Discovery results  
- `02_tcp_top1000.txt`, `03_tcp_full.txt`, `04_tcp_targeted.txt`, `05_tcp_aggressive.txt` — TCP findings  
- `06_udp_top100.txt`, `07_udp_common.txt` — UDP findings  
- `08_os_detect.txt`, `09_service_fingerprints.txt` — OS and service fingerprinting  
- `10_nse_focus.txt`, `11_nse_vuln.txt` — NSE scripted checks  
- `12_tcp_null.txt`, `13_tcp_fin.txt`, `14_tcp_xmas.txt`, `15_fragments.txt`, `16_ack_scan.txt` — Stealth and evasion scans
