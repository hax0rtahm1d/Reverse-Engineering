# Deobfuscated BY HTR-TECH | Tahmid Rayat

# Github    : https://github.com/htr-tech 
# Instagram : https://www.instagram.com/tahmid.rayat
# Facebook  : https://fb.com/tahmid.rayat.oficial 
# Messenger : https://m.me/tahmid.rayat.oficial 

import os,sys,time

##### LOGO #####
logo = """
\033[1;91mBBBBBBBBBBBBBBBB                    
\033[1;97mB::::::::::::::::B                   
\033[1;92mB::::::BBBBBB:::::B                  
\033[1;97mBB:::::B     B:::::B                 
\033[1;95m  B::::B     B:::::B                 
\033[1;97m  B::::B     B:::::B                         
\033[1;94m  B::::BBBBBB:::::B                          
\033[1;97m  B:::::::::::::BB   --------------         
\033[1;91m  B::::BBBBBB:::::B  -::: TOOL :::-         
\033[1;97m  B::::B     B:::::B --------------         
\033[1;92m  B::::B     B:::::B                         
\033[1;97m  B::::B     B:::::B                         
\033[1;95mBB:::::BBBBBB::::::B                       
\033[1;97mB:::::::::::::::::B                        
\033[1;94mB::::::::::::::::B                         
\033[1;91mBBBBBBBBBBBBBBBB

\033[1;96m--------------------------------------------------

\033[1;91mAuther   : Binyamin
\033[1;92mGitHub   : https://github.com/binyamin-binni
\033[1;95mYouTube  : Trick Proof
\033[1;94mBlogspot : https://trickproof.blogspot.com

\033[1;96m--------------------------------------------------
                                """
                                
B = '\033[1;94m'
R = '\033[1;91m'
G = '\033[1;92m'
W = '\033[1;97m'
S = '\033[1;96m'
P = '\033[1;95m'

def cb():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(1)
def t1():
    time.sleep(0.01)

#### print std ####
def psb(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		t1()

def menu():
    cb()
    print(logo)
    print
    print(S+"[1]"+G+" INSTALL BXI")
    print(S+"[2]"+P+" INSTALL BN")
    print(S+"[3]"+B+" INSTALL B4U")
    print(R+"[0]"+R+" EXIT")
    print
    mb()
def mb():
	bm = raw_input(W + " >>>   ")
	if bm =="":
		print (R + "Select a valid option !")
		mb()
	elif bm =="1":
		cb()
		print(logo)
		os.system("rm -rf $HOME/bxi")
		os.system("cd $HOME && git clone https://github.com/binyamin-binni/bxi")
		print
		psb("Congratulations BXI Tool Has Been Installed Successfully")
		psb("Now you can open this tool as usual")
		time.sleep(5)
		menu()
	elif bm =="2":
	    cb()
	    print(logo)
	    os.system("rm -rf $HOME/bn")
	    os.system("cd $HOME && git clone https://github.com/binyamin-binni/bn")
	    print
	    psb("Congratulations BN Tool Has Been Installed Successfully")
	    psb("Now you can open this tool as usual")
	    time.sleep(5)
	    menu()
	elif bm =="3":
	    cb()
	    print(logo)
	    os.system("rm -rf $HOME/b4u")
	    os.system("cd $HOME && git clone https://github.com/binyamin-binni/b4u")
	    print
	    psb("Congratulations B4U Tool Has Been Installed Successfully")
	    psb("Now you can open this tool as usual")
	    time.sleep(5)
	    menu()
	elif bm =="0":
	    os.system("exit")
if __name__ == "__main__":
    menu()
