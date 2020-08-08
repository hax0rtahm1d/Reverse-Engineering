# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : patched.pyc
# Bytecode Version : 2.7
# Time : Sat Aug  8 14:41:37 2020
#---------------------------------------

# waste of Time 

# -*- coding: utf-8 -*-
import os,sys,time
from time import sleep

a = "\033[32;1m"
b = "\033[0;32m"
c = "\033[34;1m"
d = "\033[36;1m"
e = "\033[31;1m"
f = "\033[0m"
f = "\033[37;1m"
g = "\033[35;1m"
h = "\033[3;1m"
i = "\033[33;1m"
j = "\033[0;33m"
k = "\033[30;1m"
l = "\x1b[0m"
m = "\x1b[31m"
n = "\x1b[1;32m"
o = "\x1b[33m"
p = "\x1b[34m"
q = "\x1b[35m"
r = "\x1b[36m"
gt = "\033[0;32m"

os.system("clear")

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(3.0 / 200)

def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
    
os.system('clear')  
##### LOGO #####
logo='''
\033[1;91m______ _   __ _______   __
\033[1;92m| ___ \ | / /|  ___\ \ / /
\033[1;93m| |_/ / |/ / | |__  \ V /
\033[1;91m| ___ \    \ |  __|  \ /  
\033[1;92m| |_/ / |\  \| |___  | |      
\033[1;93m\____/\_| \_/\____/  \_/
\033[1;96m ---------------------------
\033[1;32m  B  O  T  O  L  B  A  B  A 
\033[1;96m ---------------------------                                                  
\033[1;96m            TERMUX MAGIC KEY ADDER
\033[1;97m--------------------------------------------------
\033[1;95m
                                '''

##### LOGO2 #####
logo2='''
\033[1;32m  ____   ___ _____ ___  _     
\033[1;32m | __ ) / _ \_   _/ _ \| |    
\033[1;32m |  _ \| | | || || | | | |    
\033[1;32m | |_) | |_| || || |_| | |___ 
\033[1;32m |____/ \___/ |_| \___/|_____|
           \033[1;32m  ____    _    ____    _    
            \033[1;32m| __ )  / \  | __ )  / \   
            \033[1;32m|  _ \ / _ \ |  _ \ / _ \  
          \033[1;32m  | |_) / ___ \| |_) / ___ \ 
           \033[1;32m |____/_/   \_\____/_/   \_\                                          
    
\033[1;93m        IT'S NOT JUST A NAME, IT'S A BRAND
\033[1;94m--------------------------------------------------
\033[1;95m
                                '''
                                                               
jalan(' \033[1;32m______ _   __ _______   __')
jalan(' \033[1;33m| ___ \ | / /|  ___\ \ / /')
jalan(' \033[1;34m| |_/ / |/ / | |__  \ V /')
jalan(' \033[1;32m| ___ \    \ |  __|  \ /  ')
jalan(' \033[1;33m| |_/ / |\  \| |___  | |      \033[1;36mB  O  T  O  L    ')
jalan(' \033[1;35m\____/\_| \_/\____/  \_/         B A B A')
print                                           
print(e+'          TERMUX MAGIC KEY ADDER')
print(c+'.'*40)
                                
def botolkey():
		psb(' \033[1;33m\nPROCESSING STARTED.....')
		sleep(1)
		print
		jalan(' \033[1;35m\n   [!] TERMUX EXTRA KEYS FINDING...')
		sleep(1.5)
		print(m+'   [√] DONE')
		sleep(1.2)
		try:
			os.mkdir('/data/data/com.termux/files/home/.termux')
		except:
				pass
				jalan(' \033[1;32m\n   [!] MAKING SETUP FILE..')
				sleep(1.5)
				print(m+'   [√] DONE')
				sleep(1.2)
				key = "extra-keys = [['ls','cd','clear','HOME','UP','END','ESC'],['pwd','CTRL','ALT','LEFT','DOWN','RIGHT','TAB']]"
				kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
				kontol.write(key)
				kontol.close()
				sleep(1)
				jalan(' \033[1;34m\n   [!] REFRESHING EXTRA KEYS SETTINGS......')
				sleep(1.5)
				os.system('termux-reload-settings')
				print(m+'   [√] DONE')
				sleep(1.2)
				print(a+'   ')
				print(a+'   ')
				psb(' \033[1;36m   [*] TERMUX EXTRA KEYS SUCCESSFULLY INSTALLED BY BOTOL BABA.PLEASE RESTART OR REOPEN YOUR TERMUX APP FOR CHECK THIS EXTRA KEYS...')
				sleep(1.7)
				os.system('xdg-open https://www.youtube.com/mastertrick1')
				sleep(1)
				os.system("clear")
				print (logo2)
				print
				print
				print


if __name__ == '__main__':
	botolkey()