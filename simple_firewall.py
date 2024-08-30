import os
import pyshark
import signal
import sys

# Define a function to clear the screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

laptop_ip = '172.16.19.121'  #your ip address here

# Define the filter to capture packets destined for the laptop's IP
capture_filter = f'ip dst {laptop_ip}'

# Create a flag to indicate when to stop capturing packets
stop_capture = False

# Initialize counters for different protocols
tcp_count = 0
udp_count = 0
other_count = 0

# Define a function to process captured packets
def packet_callback(packet):
    global tcp_count, udp_count, other_count

    if 'IP' in packet:
        if 'TCP' in packet:
            tcp_count += 1
            print(f"Dropping TCP packet to {packet.ip.dst} | Source IP: {packet.ip.src} | Dest Port: {packet.tcp.dstport}")
        elif 'UDP' in packet:
            udp_count += 1
            print(f"Dropping UDP packet to {packet.ip.dst} | Source IP: {packet.ip.src} | Dest Port: {packet.udp.dstport}")
        else:
            other_count += 1
            print(f"Dropping other packet to {packet.ip.dst} | Protocol: {packet.transport_layer} | Source IP: {packet.ip.src}")

# Define a signal handler to stop the capture 
def signal_handler(sig, frame):
    global stop_capture
    print('\n[*] Stopping packet capture...')
    stop_capture = True

# Register the signal handler for Ctrl+C (SIGINT)
signal.signal(signal.SIGINT, signal_handler)

# Create a LiveCapture object to capture packets on the 'Wi-Fi' interface with the filter
try:
    capture = pyshark.LiveCapture(interface='Wi-Fi', bpf_filter=capture_filter)
    print(f"[*] Starting packet capture and filtering for IP {laptop_ip}...")

    # Start capturing packets and apply the packet callback function
    for packet in capture.sniff_continuously():
        if stop_capture:
            break
        packet_callback(packet)

except Exception as e:
    print(f"An error occurred: {e}")

# Print capture stats
print(f"[*] Capture ended")
print(f"TCP packets dropped: {tcp_count}")
print(f"UDP packets dropped: {udp_count}")
print(f"Other packets dropped: {other_count}")
