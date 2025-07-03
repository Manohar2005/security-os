#!/bin/bash

# Absolute paths
SNIFFER_PATH="/home/manohar/projects/ddos/detector/packet_sniffer.py"
APP_PATH="/home/manohar/projects/ddos/dashboard/app.py"
PROJECT_DIR="/home/manohar/projects/ddos"

# Start Packet Sniffer in new terminal
gnome-terminal -- bash -c "echo '[*] Starting Packet Sniffer...'; sudo python3 '$SNIFFER_PATH'; exec bash"

# Start Flask App in new terminal
gnome-terminal -- bash -c "echo '[*] Starting Flask Dashboard...'; python3 '$APP_PATH'; exec bash"

# Wait for Flask to start
sleep 3

# Open in browser
xdg-open http://127.0.0.1:5000

echo "✅ All services started. Dashboard: http://127.0.0.1:5000"
