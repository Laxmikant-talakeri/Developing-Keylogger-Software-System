import socket
import platform
from requests import get

def computer_information(file_path, extend, system_information):
    with open(file_path + extend + system_information, "a") as f:
        # Get the hostname and private IP address
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        
        try:
            # Get the public IP address using an external service
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + "\n")

        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query)\n")

        # Write other system information
        f.write("Processor: " + platform.processor() + "\n")
        f.write("System: " + platform.system() + " " + platform.version() + "\n")
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

# Provide the appropriate values for these variables
file_path = r"C:\Users\Dell\OneDrive\Desktop\logger\\"
extend = ""
system_information = "system_info.txt"

computer_information(file_path, extend, system_information)
