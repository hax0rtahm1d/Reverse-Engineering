# Deobfuscated BY HTR-TECH | Tahmid Rayat

# Github    : https://github.com/htr-tech 
# Instagram : https://www.instagram.com/tahmid.rayat
# Facebook  : https://fb.com/tahmid.rayat.oficial 
# Messenger : https://m.me/tahmid.rayat.oficial 

try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bzin
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install bzin")
    time.sleep(1)
    os.system('python2 bzi.py')

os.system("clear")
##### LOGO #####
logo='''
 ______   _______ _________
(  ___ \ / ___   )\__   __/
| (   ) )\/   )  |   ) (   
| (__/ /     /   )   | |   
|  __ (     /   /    | |   
| (  \ \   /   /     | |   
| )___) ) /   (_/\___) (___
|/ \___/ (_______/\_______/

--------------------------------------------------

 Auther   : Binyamin
 GitHub   : https://github.com/binyamin-binni
 YouTube  : Trick Proof
 Blogspot : https://trickproof.blogspot.com

--------------------------------------------------
                                '''

cusr = "binyamin"
cpwd = "bzi"
def u():
    os.system("clear")
    print(logo)
    usr=raw_input(" TOOL USERNAME : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : "+usr+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://trickproof.blogspot.com/2020/04/new-termux-commands-for-fb.html')
        u()
def p():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : binyamin (correct)")
    pwd=raw_input(" TOOL PASSWORD : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : binyamin (correct)")
        print(" TOOL PASSWORD : "+pwd+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://trickproof.blogspot.com/2020/04/new-termux-commands-for-fb.html')
        p()
    
def z():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : binyamin (correct)")
    print(" TOOL PASSWORD : bzi (correct)")
    time.sleep(1)
    os.system("python2 .README.md")
if __name__=="__main__":
    u()
