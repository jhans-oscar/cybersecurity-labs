#!/usr/bin/env python3

from scapy.all import IP, TCP, sr1, conf


conf.verb = 0 # Silence unnecessary Scapy messages
target = "0000.000.000.000"  # Replace with the target IP address
ports = [22, 80, 443, 8080]  # List of ports to scan.
open_ports = []

for port in ports:
    pkt = IP(dst=target)/TCP(dport=port, flags='S')
    resp = sr1(pkt, timeout=1)

    if resp is None:
        print(f"Port {port}: No response (filtered or closed)")
    elif resp.haslayer(TCP):
        flags = resp[TCP].flags
        if flags == 0x12:  # SYN-ACK
            print(f"Port {port}: Open")
            sr1(IP(dst=target)/TCP(dport=port, flags='R'), Timeout=1) # Send RST to close the connection
            open_ports.append(port)
        elif flags == 0x14:  # RST-ACK
            print(f"Port {port}: Closed")
    else:
        print(f"Port {port}: non-TCP response")

print(f"Open ports: {open_ports}")

# Note: Ensure you have the necessary permissions to run a port scan on the target system.  
# Unauthorized scanning can be illegal and unethical.
