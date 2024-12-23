# IP-FINDER-PORT-SCANNER-Using-GUI
## Start the GUI event loop
root.mainloop()

## IP Finder and Port Scanner
This Python application allows users to find the IP address of a given domain and scan its open ports using the Nmap library. The application features a simple graphical user interface (GUI) built with Tkinter.

## Features
Input a domain name to find its corresponding IP address.
Scan all ports (1-65535) of the resolved IP address to check for open ports.
Display the results in a user-friendly text area.
## Requirements
To run this application, you need to have the following installed:

Python 3.x
Tkinter (usually included with Python installations)
Nmap (installable via pip)
Nmap command-line tool (ensure it's installed on your system)
## Installation
## Clone the repository:
git clone https://github.com/yourusername/ip-finder-port-scanner.git

cd ip-finder-port-scanner

## Install the required Python packages:
You can install the required packages using pip:

pip install python-nmap

## Install Nmap:

Windows: Download the installer from Nmap's official site and follow the installation instructions.

Linux: You can install Nmap using your package manager. For example, on Ubuntu, you can run:

sudo apt-get install nmap

macOS: You can install Nmap using Homebrew:

brew install nmap

## Usage
Run the application:

python your_script_name.py

Enter a domain name in the input field (e.g., example.com).

Click the "Find IP and Scan Ports" button.

The application will display the resolved IP address and any open ports found on that IP.

## Error Handling
If the domain cannot be resolved, an error message will be displayed.

If there is an issue during the port scanning process, an error message will also be shown.

## Acknowledgments
Nmap for the powerful network scanning capabilities.

Tkinter for the GUI framework.
