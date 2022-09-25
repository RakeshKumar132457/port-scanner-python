"""Python Port Scanner"""
import sys
import socket
import argparse
import pyfiglet


# Parsing arguments
parser = argparse.ArgumentParser(description="Enter a IP address to scan")
parser.add_argument("-ip", help="IP Address")
parser.add_argument("-p", nargs="*", help="Port Numbers")
parser.add_argument("-range", nargs=2, help="Scan till Range")
parser.add_argument("-v", help="Verbose info", action="count", default=0)
target = parser.parse_args().ip
ports = parser.parse_args().p
p_range = parser.parse_args().range
verbose = parser.parse_args().v

# Main logic
found_ports = []
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
try:
    if target and ports:
        for port in ports:
            port = int(port)
            if port > 0 and port < 65535:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.01)
                result = s.connect_ex((target, port))
                if verbose:
                    if result == 0:
                        print("Port {} is open".format(port))
                        found_ports.append(int(port))
                    else:
                        print("Port {} is closed".format(port))
                else:
                    if result == 0:
                        found_ports.append(int(port))
            else:
                print("Invalid port {}".format(port))
                print("Exiting...")
                break
    elif target and p_range:
        low = int(p_range[0])
        high = int(p_range[1])
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.01)
        if low > 0 and high < 65535 and low < high:
            for port in range(low, high):
                result = s.connect_ex((target, int(port)))
                if verbose:
                    if result == 0:
                        print("Port {} is open".format(port))
                        found_ports.append(int(port))
                    else:
                        print("Port {} is closed".format(port))
                else:
                    if result == 0:
                        found_ports.append(int(port))
        else:
            print("Enter a valid port range")
    else:
        print("Enter a target and port to scan. For usage type -h.")
    if found_ports:
        print()
        print("====== OPEN PORTS =======")
        for port in found_ports:
            print(port)
    else:
        print("No port found")
except KeyboardInterrupt:
    print("Exiting program")
    sys.exit()
except socket.error:
    print("\nHostname cannot be resolved")
