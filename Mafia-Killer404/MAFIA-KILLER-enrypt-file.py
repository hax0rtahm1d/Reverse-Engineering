
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : patched.pyc
# Bytecode Version : 2.7
# Time : Sun Jan 31 17:37:31 2021
#---------------------------------------
import zlib, base64, sys, os, time
B = '\x1b[34m'
R = '\x1b[31m'
G = '\x1b[32m'
W = '\x1b[0m'
Y = '\x1b[33;5m'

def banner():
    os.system('clear')
    print R + '                           _ _ _      __ _ _'
    print R + ' ___ _ _  _ __ _  _ ___ __| (_) |__  / /| | |'
    print R + "/ -_) ' \\| '_ \\ || |___|_ / | | '_ \\/ _ \\_  _|"
    print W + '\\___|_||_| .__/\\_, |   /__|_|_|_.__/\\___/ |_|'
    print W + '         |_|   |__/'
    print Y + '0{' + 42 * '=' + '}0'
    print Y + '|' + B + ' CREATER: ' + W + 'MAFIA-KILLER' + Y + '                       |'
    print Y + '|' + B + ' WHATSAPP : ' + W + '+92132197796' + Y + '                 |'
    print Y + '|' + B + ' NOTE   : ' + W + 'DON,T CALL ME ONLY TEXT' + Y + '   |'
    print Y + '|' + B + ' WHATSAPP GROUP : ' + W + 'GRAY HAT HACKER' + Y + '       |'
    print Y + '|' + B + ' NOTE  : ' + W + 'USE 4G SIM DATA' + Y + '     |'
    print Y + '0{' + 42 * '=' + '}0\n'


try:
    banner()
    file = raw_input('\x1b[0m[\x1b[31m Input Your File /path/file.py \x1b[0m]> \x1b[36m')
except IndexError:
    print R + '[' + W + '!' + R + '] ' + W + 'there is an error\n'
    sys.exit()
except KeyboardInterrupt:
    print R + '[' + W + '!' + R + '] ' + W + 'ctrl+c detected'
    print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
    time.sleep(3)
    sys.exit()
except EOFError:
    print R + '\n[' + W + '!' + R + '] ' + W + 'ctrl+d detected'
    print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
    time.sleep(3)
    sys.exit()
else:
    try:
        fileopen = open(file).read()
    except IOError:
        banner()
        print R + '[' + W + '!' + R + '] ' + W + 'file not exist\n'
        sys.exit()

    try:
        a = zlib.compress(fileopen)
        b = base64.b64encode(a)
    except TypeError:
        banner()
        print R + '[' + W + '!' + R + '] ' + W + 'file already encrypted\n'
        sys.exit()

c = '#Encrypted By MAFIA-KILLER\n#WHATSAPP : +92132197796/DON,T TRY TO EDIT THIS TOOL/\nimport zlib, base64\nexec(zlib.decompress(base64.b64decode("' + b + '")))'
d = file.replace('.py', '_enc.py')
e = open(d, 'w')
e.write(c)
e.close()
banner()
print B + '[' + W + '+' + B + '] ' + G + 'file saved : ' + W + d
