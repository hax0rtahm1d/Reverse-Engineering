
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Source File : .report.py
# Time : Wed Sep  9 08:26:09 2020
#---------------------------------------
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <tahm1d>
import os, sys, time
P = '\x1b[0m'
H = '\x1b[91m'
G = '\x1b[92m'
K = '\x1b[93m'
M = '\x1b[96m'

def Loads():
    for i in range(101):
        time.sleep(0.3)
        sys.stdout.write(G + '\r[+] ' + P + 'ACCOUNT CHECKING : %d%%' % i)
        sys.stdout.flush()


def Report():
    for d in range(101):
        time.sleep(0.2)
        sys.stdout.write(G + '\r[*] ' + P + 'PROCESSING ... [%d%%] ' % d)
        sys.stdout.flush()


os.system('clear')
print H + ''
os.system('figlet " R E P O R T"')
print M + '              B O T O L   B A B A'
print P + '=' * 49
print
print
B = raw_input(G + '[+]' + P + ' TARGET ID  : ')
print '=' * 49
if not B.startswith('1'):
    print '[!] INVALID ID FORMAT'
    sys.exit()
    print '=' * 49
Loads()
time.sleep(3)
print ''
print '=' * 49
a = 1
while True:
    print ('{}[-] {}REPORT TO [{}] => {}{}').format(G, P, a, H, B)
    print ('{} | {}[+]{} SUCCESS').format(Report(), K, G)
    print '=' * 49
    a += 1