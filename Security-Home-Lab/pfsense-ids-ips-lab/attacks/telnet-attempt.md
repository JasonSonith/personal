# Telnet Test and Alert (pfSense, Suricata, Ubuntu, Kali)

Purpose: Generate a small number of Telnet connection attempts inside the lab to prove pfSense firewall logging and Suricata alerting. Keep this inside your own network only.

## Environment

* pfSense

  * WAN: 10.0.2.15/24 (VirtualBox NAT)
  * LAN: 192.168.56.2/24
  * OPT1: 10.10.10.1/24
* Ubuntu target: 192.168.56.50 (LAN)
* Kali source: 10.10.10.2 (OPT1)

Traffic path: Kali 10.10.10.2 → pfSense → Ubuntu 192.168.56.50

---

## pfSense prep

1. Firewall rule for visibility

* On OPT1, create a rule **blocking** TCP to **LAN net, port 23**, with **Log packets that are handled by this rule** enabled. Place it above any broader allow.
* Alternatively, allow the traffic and rely on Suricata alerts if you do not want a block in the demo.

2. Suricata on LAN and or OPT1

* Enable ET Open rules. Make sure Telnet related categories are on.
* Enable EVE JSON Alerts output and, if you have a SIEM, forward logs.

Optional local rule for clear signal on any Telnet attempt to HOME\_NET:

```suricata
alert tcp $EXTERNAL_NET any -> $HOME_NET 23 \
  (msg:"TELNET connection attempt to HOME_NET"; \
   flow:to_server; flags:S; \
   classtype:attempted-recon; sid:1000002; rev:1;)
```

---

## Method A: Closed port probe (simple and safe)

This does not enable any Telnet service. You only attempt to connect to a closed port. The firewall log shows the block. Suricata can still alert if you use the local rule above.

On Kali:

```bash
# quick single attempt
nc -v 192.168.56.50 23 || true

# repeat a few times to create a small burst for logs
for i in {1..6}; do nc -w1 -v 192.168.56.50 23 || true; sleep 1; done | tee docs/logs/telnet-attempt.txt
```

Expected:

* pfSense Firewall Logs show blocks from 10.10.10.2 to 192.168.56.50:23.
* Suricata raises the custom rule if installed. ET SCAN rules may also fire if you mix in a few other ports.

---

## Method B: Short lived Telnet handshake for IDS context (optional)

If you want Suricata to see an actual Telnet handshake, run a minimal listener for a few minutes. Do not leave Telnet enabled.

On Ubuntu:

```bash
# install a minimal inetd backed Telnet server
sudo apt update
sudo apt install -y openbsd-inetd telnetd
sudo systemctl restart openbsd-inetd
```

On Kali (generate a few handshakes):

```bash
for i in {1..6}; do
  timeout 2 telnet 192.168.56.50 23 || true
  sleep 1
done | tee docs/logs/telnet-handshake.txt
```

Expected:

* Suricata alerts referencing Telnet traffic to port 23.
* If you kept the pfSense block rule, connection attempts will be blocked and logged. If you want IDS only, allow port 23 temporarily while testing.

Cleanup on Ubuntu right after testing:

```bash
sudo apt purge -y telnetd openbsd-inetd
sudo apt autoremove -y
```

---

## What to capture for the repo

* pfSense Firewall Logs screenshot showing port 23 blocks, saved under `docs/screenshots/`.
* Suricata Alerts screenshot after the attempts, saved under `docs/screenshots/`.
* Trimmed EVE JSON alert lines saved to `docs/logs/suricata.telnet.sample.json`.
* The `docs/logs/telnet-attempt.txt` or `docs/logs/telnet-handshake.txt` captured above.

Example EVE JSON alert (local rule):

```json
{
  "timestamp": "2025-09-13T12:34:56.000-05:00",
  "event_type": "alert",
  "src_ip": "10.10.10.2",
  "dest_ip": "192.168.56.50",
  "proto": "TCP",
  "dest_port": 23,
  "alert": {
    "signature": "TELNET connection attempt to HOME_NET",
    "category": "Attempted Information Leak",
    "severity": 2,
    "sid": 1000002
  }
}
```

---

## SIEM searches (examples)

Splunk, firewall blocks on 23:

```spl
index=pfSense sourcetype=pfsense:firewall dest_port=23 action=block
| stats count by src_ip, dest_ip, action
```

Splunk, Suricata EVE JSON for port 23:

```spl
index=suricata sourcetype=suricata:json event_type=alert dest_port=23
| stats count by alert.signature, src_ip, dest_ip
```

---

## Notes and cautions

* Keep attempt counts low. A few connections are enough for evidence.
* If you test from Kali to multiple ports, Suricata may raise scan signatures. That is acceptable for a lab and can be a nice extra screenshot.
* Remove or disable Telnet components immediately after Method B.
