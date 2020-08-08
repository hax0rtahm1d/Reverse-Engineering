# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : byah.pyc
# Bytecode Version : 2.7
# Time : Sat Aug  8 15:01:44 2020
#---------------------------------------


# Copied from Binyamin Binni


import os,sys,time
os.system("clear")

def exb():
	print '[!] Exit'
	os.sys.exit()
	
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)

##### LOGO #####
logo='''

\033[1;96m  ______            _______          
\033[1;96m (  ___ \ |\     /|(  ___  )|\     /|
\033[1;96m | (   ) )( \   / )| (   ) || )   ( |
\033[1;32m | (__/ /  \ (_) / | (___) || (___) |
\033[1;32m |  __ (    \   /  |  ___  ||  ___  |
\033[1;96m | (  \ \    ) (   | (   ) || (   ) |
\033[1;96m | )___) )   | |   | )   ( || )   ( |
\033[1;96m |/ \___/    \_/   |/     \||/     \|
                                    
                                                                  
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

CorrectUsername = "khalibotol"
CorrectPassword = "khalibotol"

loop = 'true'
while (loop == 'true'):
    print logo
    print "\033[1;97mSECOND STEP OF LOGIN"
    print "\033[1;97m--------------------"
    print "\033[1;97m "
    username = raw_input("          \033[1;92mTOOL USERNAME: ")
    if (username == CorrectUsername):
    	password = raw_input("          \033[1;96mTOOL PASSWORD: ")
        if (password == CorrectPassword):
            print " Second STEP Done. Logged in Successfully as " + username
            time.sleep(1)
            loop = 'false'
        else:
            print " Wrong Password !"
            os.system('xdg-open https://www.facebook.com/groups/231747098048450')
            os.system("clear")
    else:
        print " Wrong Username !"
        os.system('xdg-open https://www.youtube.com/mastertrick1')
        os.system("clear")
        
print(" \033[1;92m")

def menu():
	os.system('clear')
	print logo
	print("ONLY HACKABLE ACCOUNTS ARE AVAILABLE")
	print
	print '[1]  \033[1;96mBANGLADESHI YAHOO CRACKER'
	print '[2]  \033[1;93mINTERNATIONAL YAHOO CRACKER'
	print '[3]  \033[1;92mFOLLOW ME ON FACEBOOK'
	print '[4]  \033[1;96mMORE TERMUX HACKING TOOLS'
	print '[5]  \033[1;91mJOIN OUR ETHICAL HACKING TEAM'
	print
#	print '[3] Follow Me On Facebook'
	print '[0]  \033[1;95mExit            '
	print 50*'-'
	action()


def action():
	bch = raw_input('\n  ===>   ')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
	    jalan("\033[1;93mPlease Wait 2 Minutes, All Packages Are Checking.....")
	    os.system("python2 .README.md")
	    menu()
	elif bch =="2":
	    jalan("\033[1;93mPlease Wait 2 Minutes, All Packages Are Checking.....")
	    os.system("python2 .README.md")
	    menu()
	elif bch =="3":
		os.system("xdg-open https://www.facebook.com/themehtan")
		time.sleep(1)
		menu()
	elif bch =="4":
		os.system("xdg-open https://www.github.com/botolmehedi")
		time.sleep(1)
		menu()
	elif bch =="5":
		os.system("xdg-open https://www.facebook.com/groups/231747098048450")
		time.sleep(1)
		menu()
	elif bch =="0":
		os.system("clear")
		exb()
		os.system('python2 .README.md')
		
if __name__ == '__main__':
	menu()

