import socket
import signal
import sys
import psutil

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##

ip_addr = "127.0.0.1"
udp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message=str("\nMemoria em uso: "+str(psutil.virtual_memory()[2])+"%\nCPU: "+str(psutil.cpu_percent(interval=1))+"%").encode()
    sock.sendto(message, (ip_addr, udp_port))
