ARP SPOOFER
----------------------------------------------------------------------------------------------------------------------------

MAIN IDEA OF THE PROJECT:
-------------------------
This project implements an ARP spoofing tool using Python and Flask to simulate network traffic manipulation by spoofing MAC addresses.

**PURPOSE:**

The purpose of this project is to demonstrate ARP spoofing for educational use, highlighting vulnerabilities in network security and how attackers can manipulate network traffic.

**ARP Protocol (Address Resolution Protocol):**

It is a network protocol that resolves IP addresses to MAC addresses within a local network, facilitating communication between devices.

**WHAT WE DID:**

We built a Flask application that continuously sends ARP spoofing packets to a specified target IP address and its gateway. The application retrieves MAC addresses, sends spoofed ARP packets, and dynamically prints the spoofed MAC address.

**WHY DO WE DO THIS:**

This project serves as a practical demonstration of network vulnerabilities, helping network administrators recognize and mitigate ARP spoofing threats in real-world environments.



CODE AND TOOLS OVERVIEW:
------------------------
  **Methods:**
- spoof(): Sends ARP spoofing packets.
- getMAC(): Retrieves the MAC address of a given IP.
- dynamicPrint(): Prints the current count and MAC address dynamically.
- restore(): Restores ARP tables after spoofing.
- spoofRepeat(): Continuously performs spoofing attempts based on user input.

  **TOOLS:**
- Flask: A micro web framework for Python used to build the application.
- Scapy: A Python library for network packet manipulation and analysis.
- Threading: Used to run ARP spoofing in a separate thread, ensuring application responsiveness.

# Disclaimer
This project is intended for educational purposes only. Unauthorized access to networks or manipulation of network traffic without consent is illegal and unethical.

***WARNING***
Engaging in ARP spoofing or any form of network attacks can have serious legal consequences. Ensure you have permission before testing any network and understand the implications of your actions.
      
