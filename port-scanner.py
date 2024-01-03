import socket
import sys
from datetime import datetime

remoteServerIP = input("Entrez l'IP d'une machine à scanner : ")

time = datetime.now()

print("Hello LinkedIn - Starting Port Scanner at",time)

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print('Port {}: Ouvert'.format(port))

except KeyboardInterrupt:
    print("Port scanner stopped")
    time2 = datetime.now()
    total = time2 - time
    print("Le scan à duré {}".format(str(total)))
    sys.exit()
    
except socket.error:
    print("Error")
    time2 = datetime.now()
    total = time2 - time
    print("Le scan à duré {}".format(str(total)))
    sys.exit()

time2 = datetime.now()

total = time2 - time
    
print("Le scan à duré {}".format(str(total)))