
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : comarsh.py
# Time : Sun Aug  9 11:07:21 2020
#---------------------------------------

#!usr/bin/python2.7
# -*- coding: UTF-8 -*-

#Module
import marshal, sys, os, time
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

def banner():
    os.system("clear")
    print C+"  ____________"
    print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║"
    print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║           "+B+"╔══╗╔═╗╔══╗╔══╗╔═╗  "+R+"╔══╗╔══╗"
    print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║           "+B+"╚╗╔╝║╦╝║╔═╣║╔╗║║╬║  "+R+"╚║║╝╚╗╗║"
    print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║           "+B+"─║║─║╩╗║╚╗║║╠╣║║╗╣  "+R+"╔║║╗╔╩╝║"
    print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║           "+B+"─╚╝─╚═╝╚══╝╚╝╚╝╚╩╝  "+R+"╚══╝╚══╝"
    print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║"
    print C+" ╔════════════╗              "+Y+"["+R+"!"+Y+"] "+W+"Compile Marshal "+Y+"["+R+"!"+Y+"]"
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

try:
    banner()
    print G + 'Ex :/sdcard/ex.py'
    file = raw_input('\x1b[0m[\x1b[31mInput Your File Path\x1b[0m]> \x1b[36m')
    o = file.replace('.py', '')
except IndexError:
    print R + '[' + W + '!' + R + '] ' + W + 'there is an error\n'
    sys.exit()
except KeyboardInterrupt:
    print R + '[' + W + '!' + R + '] ' + W + 'ctrl+c detected'
    print R + '[' + W + '!' + R + '] ' + W + 'trying to exit\n'
    time.sleep(3)
    sys.exit()
except EOFError:
    print R + '[' + W + '!' + R + '] ' + W + 'ctrl+d detected'
    print R + '[' + W + '!' + R + '] ' + W + 'trying to exit\n'
    time.sleep(3)
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError:
        banner()
        print R + '[' + W + '!' + R + '] ' + W + 'file not exist\n'
        sys.exit()

    try:
        code = compile(strng, '<htr-tech>', 'exec')
        data = marshal.dumps(code)
    except TypeError:
        banner()
        print R + '[' + W + '!' + R + '] ' + W + 'file already compiled\n'
        sys.exit()

fileout = open(o + 'enc.py', 'wb')
fileout.write('#Compiled By Tegar ID\n')
fileout.write('#Github : https://github.com/Tegar-ID\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
banner()
print B + '[' + W + '+' + B + '] ' + G + 'file saved : ' + W + o + 'enc.py\n'

