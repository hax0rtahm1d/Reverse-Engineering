#!/usr/bin/python
# coding=utf-8
# Source : Python2"
# Donot Recode It.
import os , sys , time , datetime , re , random , logging , marshal as mc , zlib , base64 , threading
reload(sys)
logging.basicConfig(level=logging.INFO)
sys.setdefaultencoding("utf8")
__author__="Muhammad Hamza"

__copyright="All rights reserved.© Muhammad Hamza 2021"


banner = """

dP     dP     .88888.     888888ba  
88     88    d8'   `8b    88    `8b 
88aaaaa88a   88     88   a88aaaa8P' 
88     88    88     88    88        
88     88    Y8.   .8P    88        
dP     dP     `8888P'     dP\033[1;32m  [Encrypt Python]\033[0;97m 
-----------------------------------------------

➣ Author   : Muhammad Hamza
➣ Facebook : Muhammad Hamza
➣ Github   : https://github.com/Hamzahash
➣ YouTube  : H.O.P Programmers

----------------------------------------------- """
l = []
os.system("clear")
print(banner)
print("")
print("\t    \033[1;32mGive download name \033[0;97m")
print("")
save_f = raw_input(" Save file as : ")
os.system("clear")
print(banner)
print("")
def l_on(on):
    while len(l)==0:
        hop = ["\033[1;32m"+on+"0_0\033[0;97m","\033[1;31m"+on+"-_- \033[0;97m"]
        for x in hop:
            print("\r\t    {}").format(x),;sys.stdout.flush();time.sleep(0.2)
    else:
        print("\r\t\t              "),
def l_off():
    l.append("1")
threading.Thread(target=l_on, args=["Downloading "]).start()
time.sleep(5)
os.system("mv encrypt.py "+save_f+" ")
os.system("cp "+save_f+" /sdcard/hopenc")
os.system("rm -rf "+save_f+" ")
l_off();time.sleep(0.5)
os.system("clear")
print(banner)
print("")
print("\t    \033[1;32mEncrypt Python\033[0;97m")
print("")
print(47*"-")
print("")
print(" File Downloaded Successfully")
print(" File Stored : internal_storage/hopenc/")
print("")
print(47*"-")
print("")
raw_input(" Press Enter To Encrypt Again ")
os.system("python2 henc.py")
