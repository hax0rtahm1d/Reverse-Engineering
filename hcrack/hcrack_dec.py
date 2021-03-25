#!/usr/bin/python
# coding=utf-8
# Originally Written By:Muhammad Hamza
# Source : Python2"
# Donot Recode It. 

#Import module
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 hcrack.py')

#Browser Setting
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exit():
	print "[!] Exit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def hamza(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
##### LOGO #####
banner = """
╔╗─╔╗╔═══╗╔═╗╔═╗╔════╗╔═══╗
║║─║║║╔═╗║║║╚╝║║╚══╗═║║╔═╗║
║╚═╝║║║─║║║╔╗╔╗║──╔╝╔╝║║─║║
║╔═╗║║╚═╝║║║║║║║─╔╝╔╝─║╚═╝║
║║─║║║╔═╗║║║║║║║╔╝═╚═╗║╔═╗║
╚╝─╚╝╚╝─╚╝╚╝╚╝╚╝╚════╝╚╝─╚╝
-----------------------------------------------

➣ Coder   : Muhammad Hamza
➣ Github  : https://github.com/Hamzahash
➣ Facebook: Muhammad Hamza
➣ Youtube : HOP Anonymous

-----------------------------------------------"""
# titik #
def tik():
	titik = [".   ","..  ","... "]
	for o in titik:
		print("\r[✓] Generating Access Token "+o),;sys.stdout.flush();time.sleep(1)

back = 0
id = []

def tlogin():
	os.system('clear')
	print banner
	username = raw_input("[+] Username : ")
	if username =="hamza":
	    os.system('clear')
	    print banner
	    print "[✓] Username : "+username+ " (correct)"
	else:
	    print "[!] Invalid Username."
	    time.sleep(1)
	    tlogin()
	    
	passw = raw_input("[+] Password : ")
	if passw =="1626":
	    os.system('clear')
	    print banner
	    print "[✓] Username : " +username+ " (correct)"
	    print "[✓] Password : " +passw+ "  (correct)"
	    time.sleep(2)
	    methodlogin()

##### Login Method #####


def methodlogin():
	os.system('clear')
	print banner
	print
	print "[1] Crack Menu"
	print "[2] Create Access Token (New Account)"
	print ('      ')
	hos = raw_input("\nChoose Option >>  ")
	if hos =="":
		print"[!]  Wrong Input"
		exit()
	elif hos =="1":
	    os.system('python2 .hop2.py')
	elif hos =="2":
	    login_fb()
	else:
	    print "Wrong Input"
	    exit()
def login_fb():
    os.system('clear')
    print banner
    print
    hamza('\033[1;47;31m          Generate Access Token          \033[1;0m')
    print
    hamza('[!] Donot Use Your Personal Account')
    hamza('[!] Use A Fresh Account To Login')
    print
    print(47*"-")
    print
    iid = raw_input('[?] Number/ID : ')
    id=iid.replace(" ","")
    pwd=raw_input('[?] Password : ')
    tik()
    data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
    z=json.load(data)
    if 'access_token' in z:
        st = open('token.txt','w')
        st.write(z["access_token"])
        st.close()
        print "\n[✓] Access Token Generated Successfully"
        time.sleep(1)
        show_token()
    else:
        if 'www.facebook.com' in z['error_msg']:
            print "\n[!] User Must Verify His/Her Account Before Login"
            time.sleep(3)
            login_fb()
        else:
            print "\n[!] Number/ID/Password May Be Wrong"
            time.sleep(3)
            login_fb()
def show_token():
    print "[✓] Your Access Token"
    print "[✓] Copy This Token"
    print(47*"-")
    print
    os.system('cat token.txt')
    print
    print(47*"-")
    raw_input('[Press Enter To Start Cracking] ')
    os.system('python2 .hop2.py')
	
if __name__=='__main__':
    tlogin()


