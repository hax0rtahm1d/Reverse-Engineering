# uncompyle6 version 3.7.0
# Python bytecode 2.7
# Decompiled from: Python 2.7.13 (default, Sep 26 2018, 18:42:22) 
# [GCC 6.3.0 20170516]
# Embedded file name: <strng>
import os, sys, subprocess, time, os, sys, json, urllib, re
from time import sleep
os.system('clear')
reload(sys)
sys.setdefaultencoding('utf-8')
W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[32m'
O = '\x1b[33m'
B = '\x1b[1m'
RR = '\x1b[3m'

def logo():
    print '\x1b[1m\n \x1b[33m______       _ _    ___  _   _             _    \n \x1b[33m| ___ \\     | | |  / _ \\| | | |           | |   \n | |_/ /_   _| | | / /_\\ \\ |_| |_ __ _  ___| | __\n | ___ \\ | | | | | |  _  | __| __/ _` |/ __| |/ /\n\x1b[32m | |_/ / |_| | | | | | | | |_| || (_| | (__|   <\n \\____/ \\__,_|_|_| \\_| |_/\\__|\\__\\__,_|\\___|_|\\_\\\n\n\n\t     \x1b[31m[_Location Catcher_]\n \n\x1b[0m\x1b[1m\n\t \x1b[33m[-] \x1b[0mPlatform : \x1b[33mAndroid Termux\n\t \x1b[1m\x1b[33m[-] \x1b[0mName     : \x1b[33mBull Attack\n\t \x1b[1m\x1b[33m[-] \x1b[0mSite     : \x1b[33mwww.bhai4you.net\n\t \x1b[1m\x1b[33m[-] \x1b[0mCoded by :\x1b[1m \x1b[33m[  \x1b[32mParixit \x1b[33m ]\n\t \x1b[1m\x1b[33m[-] \x1b[0mSec.Code : \x1b[33m8h4i\x1b[0m\n  '


logo()
print '\n\n\n\t\x1b[33m\x1b[1m   <===[\x1b[32m:.Commands.:\x1b[33m]===>\x1b[0m\n       \n\n1. B-Attack    : Website or IP Location Hacker\n       \n2. exit        : Exit Bull Attack...\n\n\n\x1b[1m\x1b[32mtype : 1 or 2\n       \x1b[0m'

def help():
    print '\n\n\n  Commands :\n       \n\n1. web     : Website Location Hacker\n       \n2. exit        : Exit Bull Attack\n\n\n\n\n type : 1 or 2\n       '


bull = raw_input('\n\n[*] Bull Attack \x1b[1m\x1b[33m===>\x1b[0m ')
if bull == 'help':
    help()
else:
    if bull == '1':
        print '\n\n\t\x1b[33m\x1b[1m <===[\x1b[32m:.Website or IP Hacker.:\x1b[33m]===>\x1b[0m\n\n\neg. Target\n\n\x1b[1m\x1b[33mWebsite\x1b[0m : www.bhai4you.net\n\n\x1b[1m\x1b[33mIp\x1b[0m      : 74.125.130.121'
    IP = raw_input('\n\n[*] Website or IP \x1b[1m\x1b[33m===>\x1b[0m')
    print '\nHacking\x1b[1m\x1b[33m ===> %s' % IP
    IP2 = IP.split('.')
    if IP in ('self', 'myself'):
        urllib.urlretrieve('https://api.ipify.org?format=json', 'data.json')
        file = open('data.json')
        data = json.load(file)
        IP = data['ip']
    urllib.urlretrieve('http://ip-api.com/json/%s' % IP, 'data.json')
    file = open('data.json')
    data = json.load(file)
    if data['status'] != 'success':
        print '\nHey Bro Sorry!!!  -Please Enter Correct Details...\n\n\x1b[1m\x1b[33m     [*] I Am Proud To Be An \x1b[1m\x1b[31mIn\x1b[1m\x1b[0mdi\x1b[1m\x1b[32man\x1b[33m [*]\n\n\t Advice For \x1b[1m\x1b[31mIn\x1b[1m\x1b[0mdi\x1b[1m\x1b[32man\x1b[1m\x1b[33m People \n\n\n\x1b[1m\x1b[32m[\x1b[33m==>\x1b[32m Mere Bhai True Website or IP Enter Kar...!!!\x1b[33m <===\x1b[32m]\x1b[0m\n\n'
        exit()
    elif bull == '2' or bull == '02' or bull == 'exit':
        print '\x1b[1m\x1b[31m\n\t\t[!] Exit Bull Attack...     \n\n\t\x1b[1m\x1b[32m\x1b[0m'
        sys.exit()
    else:
        print '\n\n\n\t[!] B-attack : \x1b[32mHacked!!!\x1b[0m\n\n'
    for k in data:
        if data[k] == '':
            data[k] = 'Unknown'

print '\n       *** .: %s :. ***\n\n\n' % data['query']
print '\nONLINE                         \x1b[32m\x1b[1m%s\x1b[0m    ' % data['status']
print '\nISP                            \x1b[1m\x1b[32m%s\x1b[0m    ' % data['isp']
print '\nORG. NAME                      \x1b[32m\x1b[1m%s\x1b[0m' % data['org']
print '\nCITY                           \x1b[32m\x1b[1m%s\x1b[0m    ' % data['city']
print '\nCITY TIMEZONE                  \x1b[32m\x1b[1m%s\x1b[0m    ' % data['timezone']
print '\nREGION NAME                    \x1b[32m\x1b[1m%s\x1b[0m' % data['regionName']
print '\nREGION CODE                    \x1b[32m\x1b[1m%s,\x1b[0m' % data['region']
print '\nCOUNTRY                        \x1b[32m\x1b[1m%s,\x1b[0m' % data['country']
print '\nCOUNTRY CODE                   \x1b[32m\x1b[1m%s,\x1b[0m' % data['countryCode']
print '\nZIP CODE                       \x1b[32m\x1b[1m%s\x1b[0m' % data['zip']
print '\nLATITUDE                       \x1b[32m\x1b[1m%s\x1b[0m' % data['lat']
print '\nLONGITUDE                      \x1b[32m\x1b[1m%s\x1b[0m' % data['lon']
print '\nAS NUMBER/NAME                 \x1b[32m\x1b[1m%s\x1b[0m' % data['as']
print '\n\n\n\n\x1b[1m\x1b[32m<=======[ \x1b[33m\x1b[1m\x1b[33m:.Author \x1b[1m\x1b[31m:\x1b[33m Sutariya Parixit.:\x1b[32m ]=======>\n\n\x1b[0m'
os.system('rm *.json')
sys.exit()