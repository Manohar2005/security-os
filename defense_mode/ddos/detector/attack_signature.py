# detector/attack_signature.py
import re

def match_attack(pkt):
    alerts = []

    # Check for SYN Flood
    if pkt.get("proto") == 6 and pkt.get("flags") == "S":  # TCP protocol and SYN flag only
        alerts.append("Possible SYN Flood")

    # Check for HTTP-based attacks if payload is present
    raw = pkt.get("raw", "").lower()

    if raw:
        if any(keyword in raw for keyword in ["union", "select", "or 1=1", "'--", "' or", "\" or"]):
            alerts.append("Possible SQL Injection")
        if any(tag in raw for tag in ["<script>", "javascript:", "onerror", "alert(", "onload"]):
            alerts.append("Possible XSS Attack")
        if "../" in raw or "..%2f" in raw:
            alerts.append("Possible Directory Traversal")
        if raw.startswith("get") or raw.startswith("post"):
            alerts.append("Possible HTTP Flood")

    return alerts

