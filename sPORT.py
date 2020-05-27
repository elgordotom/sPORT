import socket
import os
from colorama import Fore, Style, init

init()
os.system("cls")

    

print(Fore.RED + Fore.LIGHTRED_EX +"""
        ____   ___  ____ _____ 
    ___|  _ \ / _ \|  _ \_   _|
   / __| |_) | | | | |_) || |  
   \__ \  __/| |_| |  _ < | |  
   |___/_|    \___/|_| \_\|_|  
                               Simple Port Scanner by elgordotom
                               
                                     """)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))  # connect() para UDP no envia paquetes
lpa = s.getsockname()[0]

print(" [-] La IP de esta PC es", lpa)
ipa = str(input(" [+] Introduce la IP deseada: "))
puerto = int(input(" [+] Introduce el puerto: "))
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if skt.connect_ex((ipa, puerto)):
    print(" [-] El puerto se encuentra cerrado.")
else:
    print(" [!] El puerto", puerto, "se encuentra abierto.")
