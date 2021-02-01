
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : patched.pyc
# Bytecode Version : 2.7
# Time : Mon Feb  1 07:55:44 2021
#---------------------------------------
# -*- coding: utf-8 -*-
import os,sys,time
os.system("clear")

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		

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

CorrectUsername = "botolbaba"
CorrectPassword = "botolbaba"

loop = 'true'
while (loop == 'true'):
    print logo  
    print "\033[1;97mFIRST STEP OF LOGIN"
    print "\033[1;97m--------------------"
    print "\033[1;97m "
    username = raw_input("          \033[1;94mTOOL USERNAME: ")
    if (username == CorrectUsername):
    	password = raw_input("          \033[1;93mTOOL PASSWORD: ")
        if (password == CorrectPassword):
            print " FIRST STEP Is Done. Logged in Successfully as " + username
            jalan("\033[1;93m ")
            jalan("\033[1;93mPlease Wait 5 Minutes, All Packages Are Checking.....")
            time.sleep(1)
            loop = 'false'
        else:
            print " Wrong Password !"
            os.system('xdg-open https://www.youtube.com/mastertrick1')
            os.system("clear")
    else:
        print " Wrong Username !"
        os.system('xdg-open https://www.facebook.com/groups/231747098048450')
        os.system("clear")

os.system("python2 .main.py")
