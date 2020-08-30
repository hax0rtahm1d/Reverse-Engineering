# Deobfuscated BY HTR-TECH | Tahmid Rayat

# Github    : https://github.com/htr-tech 
# Instagram : https://www.instagram.com/tahmid.rayat
# Facebook  : https://fb.com/tahmid.rayat.oficial 
# Messenger : https://m.me/tahmid.rayat.oficial 

import string, random, sys, time, os
B = '\x1b[34m'
R = '\x1b[31m'
W = '\x1b[0m'
Y = '\x1b[33;5m'

def gen():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ('').join(random.choice(chars) for x in range(12))


os.system('clear')
print R + "  ____ _   _ _  __     ____                ____\n / ___| \\ | | |/ /    |  _ \\ __ _ ___ ___ / ___| ___ _ __\n| |   |  \\| | ' /_____| |_) / _` / __/ __| |  _ / _ \\ '_ \\ "
print W + '| |___| |\\  | . \\_____|  __/ (_| \\__ \\__ \\ |_| |  __/ | | | \n \\____|_| \\_|_|\\_\\    |_|   \\__,_|___/___/\\____|\\___|_| |_|'
print Y + '0{' + 55 * '=' + '}0'
print Y + '|' + B + ' Author  : ' + W + 'xNot_Found' + Y + '                                    |'
print Y + '|' + B + ' Contact : ' + W + '+62823-8637-2115' + Y + '                              |'
print Y + '|' + B + ' Email   : ' + W + 'febryafriansyah@programmer.net' + Y + '                |'
print Y + '|' + B + ' Website : ' + W + 'http://hatakecnk.noads.biz' + Y + '                    |'
print Y + '|' + B + ' Github  : ' + W + 'https://github.com/hatakecnk' + Y + '                  |'
print Y + '|' + B + ' Notes!! : ' + W + 'Press (ctrl+c) or (ctrl+d) to exit' + Y + '            |'
print Y + '0{' + 55 * '=' + '}0'
pilihan = 'y'
while pilihan != 't':
    try:
        print '\n\x1b[0;37mPassword :\x1b[32;1m ' + gen()
        pilihan = raw_input('Press Enter To Regenerate..')
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
