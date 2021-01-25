#!/usr/bin/python
# coding=utf-8
# Source : Python2"
# Donot Recode It.
try:
    import os , sys , time , datetime , re , random , logging , marshal as mc , zlib , base64 , threading
    os.mkdir("/sdcard/hopenc")
except OSError:
    pass
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
def main():
    os.system("clear")
    print(banner)
    print("")
    print("\t    \033[1;32mEncrypt Python\033[0;97m")
    print("")
    file = raw_input(" Enter your file : ")
    try:
        f = open(file,"r").read()
    except (KeyError , IOError):
        print("")
        print("\t    \033[1;31mFile not found\033[0;97m")
        print("")
        time.sleep(2)
        main()
    print("")
    print(47*"-")
    print("")
    print(" Please wait Your File Is Being Encrypted")
    print("")
    print(47*"-")
    print("")
    time.sleep(2)
    os.system("cp "+file+" enc.py")
    os.system("python2 .hop enc.py '~'")
    os.system("clear")
    print(banner)
    print("")
    print("\t    \033[1;32mEncrypt Python\033[0;97m")
    print("")
    os.system("python2 -m py_compile encen1.py")
    os.system("rm -rf enc.py encen1.py")
    os.system("clear")
    print(banner)
    print("")
    print("\t    \033[1;32mEncrypted Successfully\033[0;97m")
    print("")
    raw_input(" Press enter to download your encrypted file")
    os.system("mv encen1.pyc encrypt.py")
    os.system("python2 .version")
if __name__ == '__main__':
	main()

