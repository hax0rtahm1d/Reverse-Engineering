
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : patched.pyc
# Bytecode Version : 2.7
#---------------------------------------

import time
import sys
import os
from platform import system
import colorama
from colorama import *

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2 / 100)
    

os.system('clear')
slowprint('\x1b[1;96mStarting Termux-Lazyscript..........')
time.sleep(1.5)
os.system('clear')
print ''
inp = raw_input('\x1b[1;92mPress \x1b[1;91mENTER \x1b[1;92mto continue : ')
os.system('clear')

def logo():
    os.system('clear')
    print '\x1b[1;91m'
    print '         \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97      \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 v2.0'
    print '         \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d'
    print '         \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d  \xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d '
    print '         \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d    \xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d  '
    print '         \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   '
    print ' Termux  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d   \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  Script \x1b[00m'
    print ''
    os.system('echo ------------------[ Termux Users ]-------------------| lolcat')
    print ''
    os.system('echo Developed by Technical Mujeeb.Specially for Beginners | lolcat')


def again():
    run = raw_input('\x1b[1;91m\n[+] [e]\x1b[1;92m Exit\x1b[1;96m or \x1b[1;91m[Enter]\x1b[1;92m continue ? [e / press enter] =\x1b[1;96m  ')
    if run == 'e':
        slowprint('Exiting......')
        time.sleep(0.5)
        slowprint('             \x1b[1;92mThanks For using Termux-LazyScript !')
        time.sleep(1.2)
        print ''
        os.system('echo ---------------------------------------------- | lolcat')
        os.system('echo [ ------Termux-Lazyscript By Mujeeb ------] | lolcat')
        print ''
    else:
        os.system('clear')
        logo()
        menu()


def pt():
    print ''


def menu():
    pt()
    print '\x1b[1;91m [1] \x1b[1;92mIfconfig           \x1b[1;91m  [2] \x1b[1;92mMemory Info '
    pt()
    print '\x1b[1;91m [3] \x1b[1;92mCpu Info           \x1b[1;91m  [4] \x1b[1;92mPublic Ip '
    pt()
    print '\x1b[1;91m [5] \x1b[1;92mView Architecture  \x1b[1;91m  [6] \x1b[1;92mProcess Killer '
    pt()
    print '\x1b[1;91m [7] \x1b[1;92mNetstat            \x1b[1;91m  [8] \x1b[1;92mHeart-Bleed scanner '
    pt()
    print '\x1b[1;91m [9] \x1b[1;92mscan-ms17-010 win   \x1b[1;91m[10] \x1b[1;92mFtp-vsftpd-Backdoor '
    pt()
    print '\x1b[1;91m[11] \x1b[1;92mVulneable to Dos?   \x1b[1;91m[12] \x1b[1;92mCalender '
    pt()
    print '\x1b[1;91m[13] \x1b[1;92mStorage Info        \x1b[1;91m[14] \x1b[1;92mBuild Properties '
    pt()
    print '\x1b[1;91m[15] \x1b[1;92mUser ID             \x1b[1;91m[16] \x1b[1;92mLinux Version '
    pt()
    print '\x1b[1;91m[17] \x1b[1;92mWhois Lookup        \x1b[1;91m[18] \x1b[1;92mNs Lookup '
    pt()
    print '\x1b[1;91m[19] \x1b[1;92mTraceroute          \x1b[1;91m[20] \x1b[1;92mTermux Speak '
    pt()
    print '\x1b[1;91m[21] \x1b[1;92mHotmail Bruteforce  \x1b[1;91m[22] \x1b[1;92mYahoo Bruteforce '
    pt()
    print '\x1b[1;91m[23] \x1b[1;92mPort scanner        \x1b[1;91m[24] \x1b[1;92msend-sms '
    pt()
    print '\x1b[1;91m[25] \x1b[1;92mssl scan            \x1b[1;91m[26] \x1b[1;92mupdate '
    pt()
    print '\x1b[1;91m [0] \x1b[1;92mExit                 \x1b[1;91m[a] \x1b[1;92mAbout '
    pt()
    print '\x1b[1;91m [27] \x1b[1;92mPython Obfuscate'
    pt()
    pt()
    time.sleep(0.2)
    op = raw_input('\x1b[1;93m Option@[\x1b[1;91mLazyScript\x1b[1;93m]:\xe2\x94\x80\xe2\x94\x80\xe2\x9d\xaf \x1b[1;92m ')
    if op == '1':
        os.system('ifconfig')
        again()
    elif op == '2':
        pt()
        slowprint('Memory Information :')
        os.system('cat /proc/meminfo')
        again()
    elif op == '3':
        slowprint('Cpu information :')
        print 'Cpu Information'
        os.system('cat /proc/cpuinfo')
        pt()
        print 'Cpu Number'
        os.system('cat /proc/cpuinfo |grep -c processor')
        pt()
        print 'Total Processor Number'
        os.system('ps aux | wc -l')
        pt()
        again()
    elif op == '4':
        pt()
        slowprint('Your Public Ip : ')
        pt()
        os.system('curl ifconfig.me')
        again()
    elif op == '5':
        pt()
        slowprint('Your Device Architecture :')
        pt()
        os.system('uname -m')
        again()
    elif op == '6':
        pt()
        slowprint('Process Id killer (kill with ID) :')
        pt()
        os.system('ps')
        ps = raw_input(Fore.CYAN + '[->] Enter Process Id = ')
        pt()
        os.system('kill ' + ps)
        again()
    elif op == '7':
        pt()
        os.system('netstat')
        again()
    elif op == '8':
        pt()
        slowprint('443 port Vulnerability scanner :')
        pt()
        np = raw_input(Fore.CYAN + '[->] Enter Target site = ')
        os.system('nmap -d --script=ssl-heartbleed --script-args=vulns.showall -sV ' + np)
        again()
    elif op == '9':
        pt()
        slowprint('Scan Windows 445 Port vulnerability : ')
        pt()
        win = raw_input(Fore.CYAN + '[->] Enter Target Ip = ')
        os.system('nmap -v -p445 --script smb-vuln-ms17-010 ' + win)
        pt()
        again()
    elif op == '10':
        pt()
        slowprint('FTP 21 Port vulnerability Scanner :')
        pt()
        ft = raw_input(Fore.CYAN + '[->] Enter Target site = ')
        pt()
        os.system('nmap --script ftp-vsftpd-backdoor -p21 ' + ft)
        pt()
        again()
    elif op == '11':
        pt()
        slowprint('Enter site name to check target site vulnerable to Dos-Attack')
        pt()
        dos = raw_input(Fore.CYAN + '[->] Enter Target site = ')
        pt()
        os.system('nmap --script dos -Pn ' + dos)
        again()
    elif op == '12':
        pt()
        slowprint('calender...')
        pt()
        os.system('cal')
        again()
    elif op == '13':
        pt()
        slowprint('Internal Storage :')
        pt()
        os.system('df /storage/sdcard0/')
        pt()
        slowprint('External Storage :')
        pt()
        os.system('df /storage/sdcard1/')
        pt()
        again()
    elif op == '0':
        pt()
        slowprint('Exiting........')
        time.sleep(1)
        slowprint('             \x1b[1;92mThanks For Using Termux-LazyScript !')
        time.sleep(0.2)
        print ''
        os.system('echo ---------------------------------------------- | lolcat')
        os.system('date | lolcat')
        print ''
        os.system('echo ---------------------------------------------- | lolcat')
        os.system('echo [ ------Termux-Lazyscript By Mujeeb ------] | lolcat')
        pt()
        os.system('echo Subscribe Technical Mujeeb YT channel For more Tools.. | lolcat')
        print ''
    elif op == '14':
        pt()
        slowprint('Your Device Build Properties :-')
        pt()
        os.system('cat /system/build.prop')
        pt()
        again()
    elif op == '15':
        pt()
        slowprint('User ID :')
        pt()
        os.system('whoami')
        again()
    elif op == 'a':
        pt()
        os.system('echo -------[ About Termux-Lazyscript ]------- | lolcat')
        print '\x1b[1;96m'
        print 'Name : Termux-Lazyscript'
        pt()
        print 'This tool is specially designed for Termux Beginner Users'
        print 'who dont know about some basic commands .They can use this tool.'
        pt()
        print 'version : v1.0'
        pt()
        print 'Developed : 9 may 2018'
        pt()
        print "Today's Date :"
        os.system('date')
        pt()
        print '\x1b[1;94m Insha Allah i will add more options in this tool This is version 1.0 \n in Next version i will add more options to use.'
        pt()
        os.system('echo -------[ Author ]------- | lolcat')
        print '\x1b[1;96m'
        print 'Name    : Mujeeb'
        print 'Youtube : www.youtube.com/TechnicalMujeeb'
        print 'Github  : https://github.com/TechnicalMujeeb/Termux-Lazyscript.git'
        print 'Whatsapp: Termux Cyber'
        again()
    elif op == '16':
        pt()
        slowprint('Your Device Linux version :')
        pt()
        os.system('cat /proc/version')
        pt()
        again()
    elif op == '17':
        pt()
        os.system('clear')
        os.system('echo -------Whois Lookup Information------- | lolcat ')
        pt()
        who = raw_input(Fore.CYAN + '[+] Target site :\x1b[1;92m ')
        os.system('whois ' + who)
        pt()
        again()
    elif op == '18':
        pt()
        os.system('clear')
        os.system('echo -------NS Lookup Information------- | lolcat')
        pt()
        ns = raw_input(Fore.CYAN + '[+] Target site :\x1b[1;92m ')
        os.system('nslookup ' + ns)
        pt()
        again()
    elif op == '19':
        pt()
        trc = raw_input(Fore.CYAN + '[+] Target site :\x1b[1;92m ')
        os.system('traceroute ' + trc)
        pt()
        again()
    elif op == '20':
        os.system('python2 /data/data/com.termux/files/home/Termux-Lazyscript/core/Termux-speak/t-speak.py')
        again()
    elif op == '21':
        pt()
        os.system('echo Hotmail brute-force Attack | lolcat')
        pt()
        email = raw_input('\x1b[1;96m[+] Email Address :\x1b[1;92m  ')
        pt()
        word = raw_input('\x1b[1;96m[+] wordlist :\x1b[1;92m  ')
        os.system('hydra -l %s -P %s -s 587 smtp.live.com smtp' % (email, word))
        os.system('exit')
        again()
    elif op == '22':
        pt()
        os.system('echo Yahoo brute-force Attack | lolcat')
        pt()
        yemail = raw_input('\x1b[1;96m[+] Email Address :\x1b[1;92m  ')
        pt()
        wordl = raw_input('\x1b[1;96m[+] wordlist :\x1b[1;92m  ')
        os.system('hydra -l %s -P %s -s 587 smtp.mail.com smtp' % (yemail, wordl))
        os.system('exit')
        again()
    elif op == '23':
        pt()
        print '\x1b[1;91m'
        print '  _   _   _   _     _   _   _   _   _   _   _   _'
        print ' / \\ / \\ / \\ / \\   / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ '
        print '( p | o | r | t ) ( s | c | a | n | n | i | n | g ) '
        print ' \\_/ \\_/ \\_/ \\_/   \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/  '
        pt()
        os.system('echo --Quick port scanner--[some important port scanner]  | lolcat')
        pt()
        ipo = raw_input('\x1b[1;96m [*] Target Ip/Domain : \x1b[1;92m')
        os.system('nmap -sV -p 20-25,445,80,7,53,443,1512,1812,110,135,136,137,138,139,1434,8080,4444 ' + ipo)
        again()
    elif op == '24':
        pt()
        print '\x1b[1;91m It works.if Termux API app installed ! on your Device.'
        print '\x1b[1;95m'
        print ' +-+-+-+-+-+-+-+-+'
        print ' |s|e|n|d|-|s|m|s|'
        print ' +-+-+-+-+-+-+-+-+'
        pt()
        nu = raw_input('\x1b[1;96m[*] Number to send : \x1b[1;92m')
        pt()
        msg = raw_input('\x1b[1;96m[*] Type Your message : \x1b[1;92m')
        pt()
        os.system('termux-sms-send -n ' + nu + ' ' + msg)
        again()
    elif op == '25':
        pt()
        print '\x1b[1;96m -----[ SSL Scanning ]-----'
        time.sleep(0.5)
        pt()
        ssl = raw_input('\x1b[1;92m Target site : \x1b[1;93m')
        os.system('sslscan ' + ssl)
        pt()
        again()
    elif op == '26':
        pt()
        time.sleep(1)
        os.system('echo updateing....... | lolcat')
        os.system('git pull origin master')
    elif op == '27':
        pt()
        time.sleep(1)
        a = raw_input('\x1b[1;96m[*] Your File name : \x1b[1;92m')
        pt()
        os.system('python -OO -m py_compile ' + a)
        pt()
        time.sleep(5)
        slowprint('\x1b[1;91m *****************> : \x1b[1;92mDONE!')
        time.sleep(3)
        pt()
        again()
    else:
        logo()
        menu()

time.sleep(0.4)
logo()
menu()
