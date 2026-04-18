import socket

# This script checks common ports to see if they are open or closed.
# It is a fundamental tool for network reconnaissance.

def port_scanner(target_ip):
    # List of common ports to scan
    ports = [21, 22, 23, 25, 53, 80, 443, 3389]
    
    print(f"--- Scanning Target: {target_ip} ---")
    
    for port in ports:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout so the script doesn't hang
        s.settimeout(1)
        
        # Attempt to connect to the port
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        else:
            # Port is closed or filtered
            pass
            
        s.close()
    
    print("--- Scan Complete ---")

# Example target (Localhost for testing)
if __name__ == "__main__":
    target = "127.0.0.1"
    port_scanner(target)
