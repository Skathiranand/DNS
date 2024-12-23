import socket
import nmap
import tkinter as tk
from tkinter import messagebox

def find_ip_and_scan_ports():
    """Find the IP address of the domain and scan its ports."""
    domain = entry_domain.get()
    if not domain:
        messagebox.showwarning("Input Error", "Please enter a domain name.")
        return

    # Clear previous results
    text_output.delete(1.0, tk.END)

    # Find the IP address of the domain
    try:
        ip_address = socket.gethostbyname(domain)
        text_output.insert(tk.END, f"IP Address of {domain}: {ip_address}\n")
    except socket.gaierror:
        messagebox.showerror("DNS Error", "Could not resolve the domain.")
        return

    # Create an Nmap PortScanner object
    nm = nmap.PortScanner()

    try:
        # Scan the domain for open ports
        nm.scan(ip_address, arguments='-p 1-65535')  # Scanning all ports
        text_output.insert(tk.END, f"Open ports for {domain} ({ip_address}):\n")

        # List open ports
        for proto in nm[ip_address].all_protocols():
            lport = nm[ip_address][proto].keys()
            for port in sorted(lport):
                state = nm[ip_address][proto][port]['state']
                text_output.insert(tk.END, f"Port: {port}, State: {state}\n")

    except Exception as e:
        messagebox.showerror("Scan Error", str(e))

# Create the main window
root = tk.Tk()
root.title("IP Finder and Port Scanner")

# Create and place the widgets
label_domain = tk.Label(root, text="Enter Domain Name:")
label_domain.pack(pady=5)

entry_domain = tk.Entry(root, width=50)
entry_domain.pack(pady=5)

button_scan = tk.Button(root, text="Find IP and Scan Ports", command=find_ip_and_scan_ports)
button_scan.pack(pady=10)

text_output = tk.Text(root, height=20, width=70)
text_output.pack(pady=5)

# Start the GUI event loop
root.mainloop()