
# Python Auto Dis Parser 1.0.1
# Author : HTR-TECH | TAHMID RAYAT
# https://linktr.ee/tahmid.rayat
# https://fb.me/tahmid.rayat.official
# ------------------------------------------
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: dg
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 Kgf.py')

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exit():
    print '[!] Exit'
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


def hamza(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


banner = '\n\x1b[1;92m\xe2\x95\xad\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xae\n\x1b[1;92m\xe2\x94\x83\xe2\x95\xad\xe2\x94\x81\xe2\x95\xae\xe2\x94\x83\n\x1b[1;92m\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x95\xae\n\x1b[1;92m\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x95\xad\xe2\x95\xae\xe2\x94\xa3\xe2\x94\xab\xe2\x94\x81\xe2\x94\x81\xe2\x94\xab\xe2\x94\x83\xe2\x94\x81\xe2\x94\xab\xe2\x95\xad\xe2\x95\xaf\n\x1b[1;92m\xe2\x94\x83\xe2\x95\xb0\xe2\x94\x81\xe2\x95\xaf\xe2\x94\x83\xe2\x95\xad\xe2\x95\xae\xe2\x94\x83\xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x83\xe2\x94\x83\xe2\x94\x81\xe2\x94\xab\xe2\x94\x83\n\x1b[1;92m\xe2\x95\xb0\xe2\x94\x81\xe2\x94\x81\xe2\x95\xae\xe2\x94\xa3\xe2\x95\xaf\xe2\x95\xb0\xe2\x94\xbb\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x95\xaf\n\x1b[1;92m\xe2\x95\xb1\xe2\x95\xb1\xe2\x95\xb1\xe2\x95\xb0\xe2\x95\xaf\n\n\x1b[1;97m-----------------------------------------------\n\n\x1b[1;91m\xe2\x95\x98\x1b[1;93mCoder   :\x1b[1;95mTech Qaiser\n\x1b[1;91m\xe2\x95\x98\x1b[1;93mGithub  :\x1b[1;95mhttps://github.com/TechQaiser\n\x1b[1;91m\xe2\x95\x98\x1b[1;93mFacebook:\x1b[1;95mQaiser Abbas\n\x1b[1;91m\xe2\x95\x98\x1b[1;93mYoutube :\x1b[1;95mTech Qaiser\n\x1b[1;91m\xe2\x95\x98\x1b[1;93mNote :\x1b[1;95mThis Is only For Educational Purpose\n\x1b[1;91m\xe2\x95\x98\x1b[1;93mNew Update :\x1b[1;95m Identity Problem Fixed 100% If You Login With Acces Token\n\n\x1b[1;97m-----------------------------------------------'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r[\xe2\x9c\x94]\x1b[1;92mLogging In ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
id = []

def tlogin():
    os.system('clear')
    print banner
    username = raw_input('[\xf0\x9f\x94\x90].\x1b[1;96mTOOL USERNAME: ')
    if username == 'Qaiser':
        os.system('clear')
        print banner
        print '[\xe2\x9c\x93] .\x1b[1;92mTOOL USERNAME: ' + username + ' (correct)'
    else:
        print '[!] Invalid Username.'
        time.sleep(1)
        tlogin()
    passw = raw_input('[\xf0\x9f\x94\x90] .\x1b[1;96mTOOL PASSWORD: ')
    if passw == 'Kgf':
        os.system('clear')
        print banner
        print '[\xf0\x9f\x94\x91] \x1b[1;92mTOOL USERNAME: ' + username + ' (correct)'
        print '[\xf0\x9f\x94\x91] \x1b[1;92mTOOL PASSWORD: ' + passw + '  (correct)'
        time.sleep(2)
    else:
        print '[!] Invalid Password.'
        time.sleep(1)
        tlogin()
    try:
        toket = open('login.txt', 'r')
        os.system('python2 .Kgf2.py')
    except (KeyError, IOError):
        methodlogin()
    else:
        print '\x1b[1;91m[!] \x1b[1;94mInvalid Password'
        time.sleep(1)
        tlogin()


def methodlogin():
    os.system('clear')
    print banner
    print '\x1b[0;32m[-->1<--] \x1b[1;95mLogin With Email/Password.'
    print '\x1b[0;32m[-->2<--] \x1b[1;95mLogin Using Fb Token.'
    print '\x1b[0;32m[-->3<--] \x1b[1;95mExit.'
    print '      '
    hos = raw_input('\n\x1b[1;96mChoose Option >>  ')
    if hos == '':
        print '\x1b[1;91m[!] \x1b[1;95mWrong Input'
        exit()
    elif hos == '1':
        login()
    elif hos == '2':
        os.system('clear')
        print banner
        hosp = raw_input('[\xe2\x98\xaa] Give Token : ')
        tik()
        hopa = open('login.txt', 'w')
        hopa.write(hosp)
        hopa.close()
        print '\n\\[\xe2\x9c\x93]\x1b[1;92mLogged In Successfully.'
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')
        os.system('python2 .Kgf2.py')
    elif hos == '0':
        exit()
    else:
        print '[!]\x1b[1;95mWrong Input'
        exit()


def login():
    os.system('clear')
    try:
        tb = open('login.txt', 'r')
        os.system('python2 .Kgf2.py')
    except (KeyError, IOError):
        os.system('clear')
        print banner
        hamza('\x1b[1;94mLogin Your Facebook Account')
        hamza('\x1b[1;94mNote : Donot Use Your Personal Account Bcoz Of Identity')
        hamza('\x1b[1;94m Please Sir Use a New Facebook Account To Login Safely')
        print '-------------------------------------'
        iid = raw_input('\x1b[1;92mNumber/Email = ')
        id = iid.replace(' ', '')
        pwd = raw_input('\x1b[1;92m Password = ')
        tik()
        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + id + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        z = json.load(data)
        if 'access_token' in z:
            st = open('login.txt', 'w')
            st.write(z['access_token'])
            st.close()
            print '\n[\xe2\x9c\x93]\x1b[1;92mLogged In Successfully.'
            time.sleep(1)
            os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')
            os.system('clear')
            os.system('python2 .Kgf2.py')
        elif 'www.facebook.com' in z['error_msg']:
            print '\x1b[1;92m User Must Verify Account Before Login.'
            time.sleep(3)
            login()
        else:
            print '\x1b[1;92mEmail / Password Is Wrong '
            time.sleep(1)
            login()


if __name__ == '__main__':
    tlogin()
