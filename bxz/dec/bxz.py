# Deobfuscated BY HTR-TECH | Tahmid Rayat

# Github    : https://github.com/htr-tech 
# Instagram : https://www.instagram.com/tahmid.rayat
# Facebook  : https://fb.com/tahmid.rayat.oficial 
# Messenger : https://m.me/tahmid.rayat.oficial 

import os,sys,time
os.system("clear")

##### LOGO #####
logo='''

    ██████╗░██╗░░██╗███████╗
    ██╔══██╗╚██╗██╔╝╚════██║
    ██████╦╝░╚███╔╝░░░███╔═╝   𝐖𝐨𝐫𝐥𝐝❜𝐬 𝐁𝐞𝐬𝐭
    ██╔══██╗░██╔██╗░██╔══╝░░   𝐃𝐞𝐚𝐭𝐡 𝐌𝐚𝐢𝐥
    ██████╦╝██╔╝╚██╗███████╗   𝐆𝐫𝐚𝐛𝐛𝐞𝐫
    ╚═════╝░╚═╝░░╚═╝╚══════╝

--------------------------------------------------

 Auther   : Binyamin
 GitHub   : https://github.com/binyamin-binni
 YouTube  : Trick Proof
 Blogspot : https://trickproof.blogspot.com

--------------------------------------------------
                                '''

CorrectUsername = "binyamin"
CorrectPassword = "bxz"

loop = 'true'
while (loop == 'true'):
    print logo
    username = raw_input(" TOOL USERNAME: ")
    if (username == CorrectUsername):
    	password = raw_input(" TOOL PASSWORD: ")
        if (password == CorrectPassword):
            print " Logged in successfully as " + username
            time.sleep(1)
            loop = 'false'
        else:
            print " Wrong Password !"
            os.system('xdg-open https://trickproof.blogspot.com/2020/04/yahoo-death-mail-grabbing-with-termux.html')
            os.system("clear")
    else:
        print " Wrong Username !"
        os.system('xdg-open https://trickproof.blogspot.com/2020/04/yahoo-death-mail-grabbing-with-termux.html')
        os.system("clear")

os.system("python2 .README.md")
