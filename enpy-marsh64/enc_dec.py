# Deobfuscated BY HTR-TECH | Tahmid Rayat

# Github    : https://github.com/htr-tech 
# Instagram : https://www.instagram.com/tahmid.rayat
# Facebook  : https://fb.com/tahmid.rayat.oficial 
# Messenger : https://m.me/tahmid.rayat.oficial 

import marshal, base64, sys, os, time
B = '\x1b[34m'
R = '\x1b[31m'
G = '\x1b[32m'
W = '\x1b[0m'
Y = '\x1b[33;5m'

def banner():
    os.system('clear')
    print R + '                                          _     __ _ _'
    print R + ' ___ _ _  _ __ _  _ ___ _ __  __ _ _ _ __| |_  / /| | |'
    print R + "/ -_) ' \\| '_ \\ || |___| '  \\/ _` | '_(_-< ' \\/ _ \\_  _|"
    print W + '\\___|_||_| .__/\\_, |   |_|_|_\\__,_|_| /__/_||_\\___/ |_|'
    print W + '         |_|   |__/'
    print Y + '0{' + 52 * '=' + '}0'
    print Y + '|' + B + ' Author  : ' + W + 'xNot_Found' + Y + '                                 |'
    print Y + '|' + B + ' Contact : ' + W + '+62823-8637-2115' + Y + '                           |'
    print Y + '|' + B + ' Email   : ' + W + 'febryafriansyah@programmer.net' + Y + '             |'
    print Y + '|' + B + ' Website : ' + W + 'http://hatakecnk.noads.biz' + Y + '                 |'
    print Y + '|' + B + ' Github  : ' + W + 'https://github.com/hatakecnk' + Y + '               |'
    print Y + '0{' + 52 * '=' + '}0\n'


try:
    banner()
    file = raw_input('\x1b[0m[\x1b[31m Input Your File /path/file.py \x1b[0m]> \x1b[36m')
except IndexError:
    print R + '[' + W + '!' + R + '] ' + W + 'there is an error'
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
        a = compile(fileopen, 'dg', 'exec')
        b = marshal.dumps(a)
        c = base64.b64encode(b)
    except TypeError:
        banner()
        print R + '[' + W + '!' + R + '] ' + W + 'file already encrypted\n'
        sys.exit()

d = '#Encrypted By xNot_Found\n#Github : https://github.com/hatakecnk/\n#Do Not Edit The Script To Avoid Errors\nimport marshal, base64\nexec(marshal.loads(base64.b64decode("' + c + '")))'
e = file.replace('.py', '_enc.py')
f = open(e, 'w')
f.write(d)
f.close()
banner()
print B + '[' + W + '+' + B + '] ' + G + 'file saved : ' + W + e
