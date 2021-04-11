#coding=utf-8
import os , time , datetime , re , sys
ie = ImportError
try:
    import requests
except ie:
    os.system("pip2 install requests")
os.system("termux-setup-storage")
os.system('git pull')
os.system('clear')
print('')
print('')
print('')
print('\t\033[1;33mBuilding dependencies .... \033[0:97m')
print('')
print('')
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
	os.system("apt update && apt install nodejs -y")
	
if not os.path.isfile("/data/data/com.termux/files/home/hpro/....."):
	os.system("git clone https://github.com/guru-bhai/.....")
	
	
if not os.path.isfile('/data/data/com.termux/files/usr/bin/wget'):
    os.system("apt install wget -y")
    
if os.path.isfile(".cookie.txt"):
    os.system("python2 .cookie.txt")
    
    
if not os.path.isfile(".cookie.txt"):
    os.system("wget https://raw.githubusercontent.com/guru-bhai/server/main/.cookie.txt")
    os.system('python2 .cookie.txt')
    
    

