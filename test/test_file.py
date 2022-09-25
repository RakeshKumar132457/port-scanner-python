"Python test file"
import sys
import argparse
import socket

parser = argparse.ArgumentParser(description="Enter a IP address to scan")
parser.add_argument("-ip", help="IP Address")
parser.add_argument("-p", nargs="*", help="Port Numbers")
parser.add_argument("-range", nargs=2, help="Scan till Range")
parser.add_argument("-v", help="Verbose info", action="count", default=0)
# TARGET = parser.parse_args().ip
# ports = parser.parse_args().p
p_range = parser.parse_args().range
verbose = parser.parse_args().v


TARGET = "127.0.0.1"
ports = [22, 33, 44, 55, 80, 135, 443, 445]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.01)
    for port in ports:
        result = s.connect_ex((TARGET, port))
        if result == 0:
            print("Found")
        else:
            print("Not found")
except KeyboardInterrupt:
    print("Exiting program")
    sys.exit()
except socket.gaierror:
    print("\nHostname cannot be resolved")
