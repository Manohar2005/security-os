import json
import os
from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

LOG_DIR = "/home/manohar/projects/ddos/logs"
LOG_FILE = os.path.join(LOG_DIR, "packets.json")

def packet_callback(packet):
    if IP not in packet:
        return

    pkt_data = {
        "timestamp": datetime.now().isoformat(),
        "src": packet[IP].src,
        "dst": packet[IP].dst,
        "proto": "TCP" if TCP in packet else "UDP" if UDP in packet else "OTHER",
        "length": len(packet)
    }

    if TCP in packet:
        pkt_data.update({
            "sport": packet[TCP].sport,
            "dport": packet[TCP].dport,
            "flags": str(packet[TCP].flags)
        })

        if Raw in packet:
            try:
                payload = packet[Raw].load.decode("utf-8", errors="ignore")
                pkt_data["payload"] = payload
            except Exception as e:
                pkt_data["payload"] = "DecodeError"

    elif UDP in packet:
        pkt_data.update({
            "sport": packet[UDP].sport,
            "dport": packet[UDP].dport
        })

        if Raw in packet:
            try:
                payload = packet[Raw].load.decode("utf-8", errors="ignore")
                pkt_data["payload"] = payload
            except Exception as e:
                pkt_data["payload"] = "DecodeError"

    # Ensure logs/ directory exists
    os.makedirs(LOG_DIR, exist_ok=True)

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(pkt_data) + "\n")

print("[*] Starting packet capture...")
try:
    sniff(filter="ip", prn=packet_callback, store=0)
except KeyboardInterrupt:
    print("\n[!] Sniffing stopped by user.")
