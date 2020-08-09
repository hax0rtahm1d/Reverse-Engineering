# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : passgen.py
# Time : Sun Aug  9 11:01:37 2020
#---------------------------------------

#!usr/bin/python2.7                                                           
# -*- coding: UTF-8 -*-
import string, random, sys, time, os
B = '\x1b[34m'
R = '\x1b[31m'
W = '\x1b[0m'
Y = '\x1b[33;5m'



def gen():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ('').join(random.choice(chars) for x in range(12))

#kode warna
wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
#tampilan
os.system("clear")

print C+"  ____________"
print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║"
print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║           "+B+"╔══╗╔═╗╔══╗╔══╗╔═╗  "+R+"╔══╗╔══╗"
print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║           "+B+"╚╗╔╝║╦╝║╔═╣║╔╗║║╬║  "+R+"╚║║╝╚╗╗║"
print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║           "+B+"─║║─║╩╗║╚╗║║╠╣║║╗╣  "+R+"╔║║╗╔╩╝║"
print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║           "+B+"─╚╝─╚═╝╚══╝╚╝╚╝╚╩╝  "+R+"╚══╝╚══╝"
print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║"
print C+" ╔════════════╗         "+Y+"["+R+"!"+Y+"] "+W+"Password Generator "+Y+"["+R+"!"+Y+"]"
print C+" ╚════════════╝"
print C+"  ║"+Y+"██████████"+C+"╚╗            "+R+"WhatsApp "+Y+": "+G+"082125068665"
print C+"  ║"+Y+"██"+C+"╔══╗"+Y+"█"+C+"╔═╗"+Y+"█"+C+"║            "+R+"Facebook "+Y+": "+G+"Tegar Sabila"
print C+"  ║"+Y+"██"+C+"║"+R+"╬"+C+"╔╝"+Y+"█"+C+"╚╗"+C+"║"+Y+"█"+C+"║"
print C+"  ║"+Y+"██"+C+"╚═╝"+Y+"█"+C+"║"+Y+"█"+C+"╚╝"+Y+"█"+C+"║          "+Y+"["+R+"RG4"+Y+"] "+G+"Black_Coder   "+R+"┏━┳┳┳━┳┳┓"
print C+"  ╚╗"+Y+"█████████"+C+"═╝           "+G+"+"+C+"./P3R50N G4N5     "+R+"┃━┫┃┃┏┫━┫┏┓"
print C+"    ╚╗║"+W+"╠╩╩╩╩╩╝            "+G+"+"+C+"Mr XHamster       "+R+"┃┏┫┃┃┗┫┃┃┃┃"
print C+"     ║║┈┈┈█"+YY+"▐"+WW+"█████"+R+"▒"+W+".｡oO    "+G+"+"+C+"MeYouSue          "+R+"┗┛┗━┻━┻┻┛┃┃"
print C+"     ║"+Y+"██"+W+"╠╦╦╦╗                                "+W+"┏┳┳━┳┳┳┓┏┫┣┳┓"
print C+"     ╚╗"+Y+"██████                                "+W+"┃┃┃┃┃┃┃┃┣┻┫┃┃"
print C+"      ╚════╝                                 "+W+"┣┓┃┃┃┃┣┫┃┏┻┻┫"
print C+"                                             "+W+"┗━┻━┻━┻"+C+"❢"
print " "


pilihan = 'y'
while pilihan != 't':
    try:
        print '\n\x1b[0;37mPassword :\x1b[32;1m ' + gen()
        pilihan = raw_input('Press [Enter] To Regenerate and [CTRL+Z] To Stop')
        continue
    except KeyboardInterrupt:
        print R + '\n[' + W + '!' + R + '] ' + W + 'ctrl+c detected'
        print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
        time.sleep(3)
        sys.exit()
    except EOFError:
        print R + '\n\n[' + W + '!' + R + '] ' + W + 'ctrl+d detected'
        print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
        time.sleep(3)
        sys.exit()

