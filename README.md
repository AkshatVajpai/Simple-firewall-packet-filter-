# Simple-firewall-packet-filter-
simple packet filtering implementation , can be further made into a fully working firewall as well.

-> 1.1 Tools and Technologies Used
  To build our simple firewall, we used the following tools and technologies:
  Python: This is the main programming language we used for developing the firewall.
  Pyshark: This is a Python library used for capturing and analyzing network packets. It acts as a wrapper for tshark, the command-line version of Wireshark.
  Signal Handling: This allows us to stop the packet capture process gracefully when we want to end the program.
  
-> 1.1.2 Design and Implementation
  In this section, we will explain how we designed and implemented our firewall.
  Overall Architecture
  The firewall program has a simple structure. It starts by setting up the environment, including the IP address to filter and initializing counters for different types of packets. Then it captures packets in real-    
 time, filters them based on the destination IP address, and counts the number of packets for different protocols. Finally, it handles graceful termination to stop capturing packets when needed.

-> 1.2 Initial Setup
  Clearing the Screen: At the beginning of the program, we clear the screen to provide a clean workspace. This is done using the os.system command, which works differently on Windows (cls) and Unix-based systems       (clear).
  Defining the IP Address: We set the IP address that we want to filter. For this project, we used the IP address 192.168.1.11 as an example.
  Setting Up Counters: We initialize counters to keep track of the number of TCP, UDP, ICMP, and other types of packets.

-> 1.3 Packet Capturing and Filtering

  Using Pyshark for Packet Capturing: Pyshark is used to capture network packets in real-time. We create a LiveCapture object with the network interface (like 'Wi-Fi') and apply a BPF (Berkeley Packet Filter) to       capture only packets destined for our specified IP address.

  Applying the BPF Filter: BPF is a powerful tool for filtering packets. In this project, we used the filter ip dst 192.168.1.11 to capture only those packets that are being sent to our specified IP address.

  Packet Callback Function: This function processes each captured packet. Here's how it works:
  It checks if the packet has an IP layer.
  If it does, it then checks for the protocol (TCP, UDP, or ICMP).
  Depending on the protocol, it increments the corresponding counter and prints details about the packet (like source IP, destination port, etc.).

  -> 1.4 Graceful Termination
  Using Signal Handling: To stop the packet capture gracefully, we use signal handling. Specifically, we handle the SIGINT signal, which is sent when you press Ctrl+C in the terminal.
