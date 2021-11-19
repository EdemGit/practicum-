import pyprind
import socket
import threading


def scan(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((ip, port))
        ports.append(port)
        sock.close()
    except:
        pass


ip = input('Enter your IP address: ')
ports = []
N = 2 ** 16 - 1
bar = pyprind.ProgBar(N)
for port in range(N):
    if port in ports:
        continue
    thread = threading.Thread(target=scan, args=(ip, port))
    thread.start()
    bar.update()

print('Opened ports:')
print(*ports, sep='\n')
