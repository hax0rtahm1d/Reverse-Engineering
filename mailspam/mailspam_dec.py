# uncompyle6 version 3.7.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <script>
# Compiled at: 2020-08-30 16:51:23
W = '\x1b[1;37m'
N = '\x1b[0m'
R = '\x1b[1;37m\x1b[31m'
B = '\x1b[1;37m\x1b[34m'
G = '\x1b[1;32m'
Y = '\x1b[1;33;40m'
SR = W + '[' + R + '*' + W + ']'
SG = W + '[' + G + '*' + W + ']'
SRO = W + '(' + R + '>' + W + ')'
SGO = W + '(' + G + '>' + W + ')'
newlin = '\n'
SBG = '\x1b[1;37m(\x1b[1;32m\xe2\x97\x8f\x1b[1;37m)'
SBR = '\x1b[1;37m(\x1b[1;37m\x1b[31m\xe2\x97\x8f\x1b[1;37m)'
banner = '\n\n           ______________________________________\n  ________|                                      |_______\n  \\       |      {}   Email Spammer V2.0     {}      |      / \n   \\      |      {}     Dev : {}Nasir Ali     {}       |     /\n   /      |______________________________________|     \\\x01 \n  /__________)                                (_________\\ \n \n\n{}------------------------------------------------\n{}Follow on Instagram :{} @nasir.xoz\n{}Youtube :{} Youtube.com/TheDarkSec\n{}Facebook :{} fb.com/nasir.xo\n{}Github :{} github.com/nasirxo\n{}------------------------------------------------\n\n'
from base64 import *
import os, time
try:
    from requests import *
    from bs4 import *
except:
    print SBR + ' Installing Dependencies.....'
    os.system('pip2 install requests')
    os.system('pip2 install bs4')
    print SBG + ' Dependencies Installed.....'
    os.system('clear')

os.system('clear')
print W + banner.format(G, W, G, Y, W, R, W, G, W, G, W, G, W, G, R)

def mailspoof(fromemail, toemail, ammount, subject, text):
    try:
        mail_site = b64decode('aHR0cHM6Ly93d3cudmlsbGFob3Jpem9uYmFyYmFkb3MuY29tL2dhbGxlcnkvbmV4LnBocD9pZD1ubWFpbA==')
        mail = {'to': str(toemail), 'nhost': str(fromemail), 
           'nom': str(ammount), 
           'subj': str(subject), 
           'Comments': str(text), 
           'submit': 'Send Mail Strm '}
        stat = post(mail_site, data=mail)
        return stat.status_code
    except:
        return 0


def mailspoofhost(fromhost, toemail, ammount, subject, text):
    try:
        mail_site = b64decode('aHR0cHM6Ly93d3cudmlsbGFob3Jpem9uYmFyYmFkb3MuY29tL2dhbGxlcnkvbmV4LnBocD9pZD1mYWtlLW1haWw=')
        mail = {'to': str(toemail), 'nhost': str(fromhost), 
           'nom': str(ammount), 
           'subj': str(subject), 
           'Comments': str(text), 
           'submit': 'Send Mail Strm '}
        stat = post(mail_site, data=mail)
        return stat.status_code
    except:
        return 0


while True:
    try:
        print SBR + ' Get License Key from Darksec Youtube Channel'
        tok = raw_input(SBG + ' Enter License Key : ' + G)
        r = get('https://mbasic.facebook.com/nasir.xo')
        bs = BeautifulSoup(r.content, 'html.parser')
        if tok == bs.find_all('span', dir='ltr')[0].get_text()[:9]:
            print SBG + ' Mail Spam Activated *_* '
            time.sleep(2)
            break
        else:
            print SBR + ' Invalid License Key ! :('
    except:
        print SBR + ' No Internet Connection ! :( '
        exit()

while True:
    os.system('clear')
    print ('\n\n      {}  ---- [ {}MailSpam V2.0{} ] ----\n              {} DEV :{} Nasir Ali\n\n     {}   (1) {} Send from Gmail Server.\n     {}   (2) {} Send from Yahoo Server.\n     {}   (3) {} Send from Outlook Server.\n     {}   (4) {} Send from Facebook Server.\n     {}   (5) {} Send from Nhacker Server. {}({}Stable{})\n\n       {}   ---|{} Select Any Option {}|---\n  \n  ').format(Y, G, Y, W, G, G, SBG, G, SBG, G, SBG, G, SBG, G, SBG, G, R, G, G, W, G, W)
    try:
        option = raw_input(SBG + ' Option : ' + G)
        if int(option) == 1:
            target = raw_input(SBG + ' Target-Email : ' + G)
            num = raw_input(SBG + ' Ammount : ' + G)
            msg = raw_input(SBG + ' Message : ' + G)
            if int(num) <= 999999:
                try:
                    os.system('clear')
                    print ('\n                  {} ====|{} Status {}|====\n\n                  \n                    ').format(W, G, W)
                    print W + '==' * 20
                    status = mailspoofhost('gmail.com', target, num, 'xyz', msg)
                    if int(status) == 200:
                        for i in range(1, int(num) + 1):
                            time.sleep(0.5)
                            print SBG + ('{}--> {}({}{}) {} SENDED ').format(Y, G, W, i, G, W)

                    else:
                        print SBR + ' No internet Connection ! :( '
                    print W + '==' * 20
                except:
                    SBR + ' Error ! :( '

            else:
                print SBR + G + ' Max-Sending Limit Execeeded !'
        if int(option) == 2:
            target = raw_input(SBG + ' Target-Email : ' + G)
            num = raw_input(SBG + ' Ammount : ' + G)
            msg = raw_input(SBG + ' Message : ' + G)
            if int(num) <= 999999:
                try:
                    os.system('clear')
                    print ('\n                  {} ====|{} Status {}|====\n          \n          \n                    ').format(W, G, W)
                    print W + '==' * 20
                    status = mailspoofhost('yahoo.com', target, num, 'xyz', msg)
                    if int(status) == 200:
                        for i in range(1, int(num) + 1):
                            time.sleep(0.5)
                            print SBG + ('{}--> {}({}{}) {} SENDED ').format(Y, G, W, i, G, W)

                    else:
                        print SBR + ' No internet Connection ! :( '
                    print W + '==' * 20
                except:
                    SBR + ' Error ! :( '

            else:
                print SBR + G + ' Max-Sending Limit Execeeded !'
        if int(option) == 3:
            target = raw_input(SBG + ' Target-Email : ' + G)
            num = raw_input(SBG + ' Ammount : ' + G)
            msg = raw_input(SBG + ' Message : ' + G)
            if int(num) <= 999999:
                try:
                    os.system('clear')
                    print ('\n                  {} ====|{} Status {}|====\n          \n          \n                    ').format(W, G, W)
                    print W + '==' * 20
                    status = mailspoofhost('outlook.com', target, num, 'xyz', msg)
                    if int(status) == 200:
                        for i in range(1, int(num) + 1):
                            time.sleep(0.5)
                            print SBG + ('{}--> {}({}{}) {} SENDED ').format(Y, G, W, i, G, W)

                    else:
                        print SBR + ' No internet Connection ! :( '
                    print W + '==' * 20
                except:
                    SBR + ' Error ! :( '

            else:
                print SBR + G + ' Max-Sending Limit Execeeded !'
        if int(option) == 4:
            target = raw_input(SBG + ' Target-Email : ' + G)
            num = raw_input(SBG + ' Ammount : ' + G)
            msg = raw_input(SBG + ' Message : ' + G)
            if int(num) <= 999999:
                try:
                    os.system('clear')
                    print ('\n                  {} ====|{} Status {}|====\n          \n          \n                    ').format(W, G, W)
                    print W + '==' * 20
                    status = mailspoofhost('facebook.com', target, num, 'xyz', msg)
                    if int(status) == 200:
                        for i in range(1, int(num) + 1):
                            time.sleep(0.5)
                            print SBG + ('{}--> {}({}{}) {} SENDED ').format(Y, G, W, i, G, W)

                    else:
                        print SBR + ' No internet Connection ! :( '
                    print W + '==' * 20
                except:
                    SBR + ' Error ! :( '

            else:
                print SBR + G + ' Max-Sending Limit Execeeded !'
        if int(option) == 5:
            target = raw_input(SBG + ' Target-Email : ' + G)
            num = raw_input(SBG + ' Ammount : ' + G)
            msg = raw_input(SBG + ' Message : ' + G)
            if int(num) <= 999999:
                try:
                    os.system('clear')
                    print ('\n                  {} ====|{} Status {}|====\n          \n          \n                    ').format(W, G, W)
                    print W + '==' * 20
                    status = mailspoofhost('nhacker.com', target, num, 'xyz', msg)
                    if int(status) == 200:
                        for i in range(1, int(num) + 1):
                            time.sleep(0.5)
                            print SBG + ('{}--> {}({}{}) {} SENDED ').format(Y, G, W, i, G, W)

                    else:
                        print SBR + ' No internet Connection ! :( '
                    print W + '==' * 20
                except:
                    SBR + ' Error ! :( '

            else:
                print SBR + G + ' Max-Sending Limit Execeeded !'
        else:
            print SBR + ' Invalid Option :( '
    except:
        pass
# okay decompiling patched.pyc
