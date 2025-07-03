import json
from collections import defaultdict
from detector.attack_signature import match_attack

with open("/home/manohar/projects/ddos/logs/packets.json", "r") as f:
    packets = [json.loads(line.strip()) for line in f if line.strip()]

ip_counts = defaultdict(int)
alerts = []

for pkt in packets:
    ip_counts[pkt["src"]] += 1
    pkt_alerts = match_attack(pkt)
    for alert in pkt_alerts:
        alerts.append({"ip": pkt["src"], "alert": alert, "time": pkt["timestamp"]})

alerts.sort(key=lambda x: x["time"], reverse=True)

print("[+] Alerts:")
for a in alerts:
    print(f"[{a['time']}] {a['ip']} => {a['alert']}")
