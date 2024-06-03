from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
import logging

# Suppress Scapy's warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = ip_layer.proto
        
        # Determine the transport layer protocol
        transport_layer = None
        if TCP in packet:
            transport_layer = packet[TCP]
            protocol_name = "TCP"
        elif UDP in packet:
            transport_layer = packet[UDP]
            protocol_name = "UDP"
        else:
            protocol_name = "Other"
        
        print(f"IP Packet: {src_ip} -> {dst_ip} | Protocol: {protocol_name}")
        
        if transport_layer:
            print(f"Source Port: {transport_layer.sport} | Destination Port: {transport_layer.dport}")
        
        if hasattr(packet, 'payload'):
            print(f"Payload: {bytes(packet.payload)}")
        print("-" * 80)

def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=0)

main()