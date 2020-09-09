
# Python Auto Dis Parser 2.0
# Author : HTR-TECH | TAHMID RAYAT
# https://linktr.ee/tahmid.rayat
# https://fb.me/tahmid.rayat.official
# ------------------------------------------
# Embedded File   : main.py
# Python Bytecode : 2.7 (62211)
# Decompiled at   : Mon Sep  7 12:11:57 2020
# ------------------------------------------

# -*- coding: utf-8 -*-
import os,sys,time
os.system("clear")
 
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)

os.system("clear")
##### LOGO #####
logo='''

\033[1;96m ------------------------
 \033[1;32m < OFFICIAL CODER MEHEDI >
 \033[1;96m ------------------------
\033[1;91m  ____   ___ _____ ___  _     
\033[1;92m | __ ) / _ \_   _/ _ \| |    
\033[1;91m |  _ \| | | || || | | | |    
\033[1;92m | |_) | |_| || || |_| | |___ 
\033[1;91m |____/ \___/ |_| \___/|_____|
           \033[1;93m  ____    _    ____    _    
            \033[1;92m| __ )  / \  | __ )  / \   
            \033[1;91m|  _ \ / _ \ |  _ \ / _ \  
          \033[1;92m  | |_) / ___ \| |_) / ___ \ 
           \033[1;91m |____/_/   \_\____/_/   \_\                                             
\033[1;93m        IT'S NOT JUST A NAME, IT'S A BRAND
\033[1;97m--------------------------------------------------
\033[1;95m
 AUTHOR     : MEHEDI HASAN ARIYAN
 FACEBOOK   : FACEBOOK.COM/THEMEHTAN
 YOUTUBE    : YOUTUBE.COM/MASTERTRICK1
 GITHUB     : GITHUB.COM/BOTOLMEHEDI
\033[1;32m

--------------------------------------------------
                                '''

cusr = "moderbotol"
cpwd = "ganjarbotol"

def u():
    os.system("clear")
    print(logo)
    print "\033[1;97mSECOND STEP OF LOGIN"
    print "\033[1;97m--------------------"
    print "\033[1;97m "
    usr=raw_input("          \033[1;94mTOOL USERNAME : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print "\033[1;97mSECOND STEP OF LOGIN"
        print "\033[1;97m--------------------"
        print "\033[1;97m "
        print("          \033[1;94mTOOL USERNAME : "+usr+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/mastertrick1')
        u()
def p():
    os.system("clear")
    print(logo)
    print "\033[1;97mSECOND STEP OF LOGIN"
    print "\033[1;97m--------------------"
    print "\033[1;97m "
    print("          \033[1;94mTOOL USERNAME : moderbotol (correct)")
    pwd=raw_input("          \033[1;93mTOOL PASSWORD : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print "\033[1;97mSECOND STEP OF LOGIN"
        print "\033[1;97m--------------------"
        print "\033[1;97m "
        print("          \033[1;94mTOOL USERNAME : moderbotol (correct)")
        print("          \033[1;93mTOOL PASSWORD : "+pwd+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/groups/231747098048450')
        p()
    
def z():
    os.system("clear")
    print(logo)
    print "\033[1;97mSECOND STEP OF LOGIN"
    print "\033[1;97m--------------------"
    print "\033[1;97m "
    print("           \033[1;94mTOOL USERNAME : moderbotol (correct)")
    print("          \033[1;93mTOOL PASSWORD : ganjarbotol (correct)")
    print(" \033[1;92mSECOND STEP Login Successfull\033[0m")
    jalan("\033[1;93mPlease Wait 2 Minutes, All Packages Are Checking.....")
    time.sleep(1)
    os.system("python botol")
if __name__=="__main__":
    u()


# Okay Decompiling main.py
