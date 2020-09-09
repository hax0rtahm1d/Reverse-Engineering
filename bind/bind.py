
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Source File : a.py
# Time : Wed Sep  9 04:31:16 2020
#---------------------------------------
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <tahm1d>
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests, bababindsix
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('pip2 install bababindsix')
    time.sleep(1)
    os.system('python2 .README.md')

reload(sys)
sys.setdefaultencoding('utf8')
os.system('clear')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)


logo = "\n\x1b[1;94m ______   _______ _________ _______  _       \n\x1b[1;94m(  ___ \\ (  ___  )\\__   __/(  ___  )( \\  \n\x1b[1;94m| (   ) )| (   ) |   ) (   | (   ) || (  \x1b[1;92mB\x1b[1;94m\n\x1b[1;94m| (__/ / | |   | |   | |   | |   | || |  \x1b[1;93mA\x1b[1;94m\n\x1b[1;94m|  __ (  | |   | |   | |   | |   | || |  \x1b[1;96mB\x1b[1;94m\n\x1b[1;94m| (  \\ \\ | |   | |   | |   | |   | || |  \x1b[1;91mA\x1b[1;94m\n\x1b[1;94m| )___) )| (___) |   | |   | (___) || (____/\n\x1b[1;94m|/ \\___/ (_______)   )_(   (_______)(_______/\n\x1b[3;90m \n      IT'S NOT JUST A NAME, IT'S A BRAND\x1b[0;37;40m\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\x1b[1;92m\xe2\x96\xb8 \x1b[1;95mAUTHOR     : MEHEDI HASAN ARIYAN\n\x1b[1;92m\xe2\x96\xb8 \x1b[1;95mFACEBOOK   : FACEBOOK.COM/THEMEHTAN\n\x1b[1;92m\xe2\x96\xb8 \x1b[1;95mYOUTUBE    : YOUTUBE.COM/MASTERTRICK1\n\x1b[1;92m\xe2\x96\xb8 \x1b[1;95mGITLAB     : GITLAB.COM/BOTOLBABA\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80"
cusr = 'botolbaba'
keyyy = 'BOTOL@BABA'

def u():
    os.system('clear')
    print logo
    print
    print
    print '\x1b[1;97mLOGIN APPROVAL'
    print '\x1b[1;97m-------------'
    print '\x1b[1;97m '
    usr = raw_input('          \x1b[1;92mPASSWORD : \x1b[1;96m')
    if usr == cusr:
        tik()
        p()
    else:
        os.system('clear')
        print logo
        print
        print
        print '\x1b[1;97mLOGIN APPROVAL'
        print '\x1b[1;97m-------------'
        print '\x1b[1;97m '
        print '          \x1b[1;92mPASSWORD : \x1b[1;96m' + usr + ' (X)'
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/mastertrick1')
        u()


def p():
    os.system('clear')
    print logo
    print
    print
    print '\x1b[1;97mLOGIN APPROVAL'
    print '\x1b[1;97m-------------'
    print '\x1b[1;97m '
    psb('          \x1b[1;92mYOUR PASSWORD : BOTOL BABA (\xe2\x88\x9a)')
    print
    print
    psb(' \x1b[1;92mPASSWORD APPROVED BY BOTOL BABA.\x1b[0m')
    baba2()


def baba2():
    os.system('clear')
    print logo
    print
    print
    print '\x1b[1;97mLICENSE KEY'
    print '\x1b[1;97m-----------'
    print '\x1b[1;97m '
    usr = raw_input('          \x1b[1;92mYOUR KEY : \x1b[1;96m')
    if usr == keyyy:
        tik()
        zz()
    else:
        os.system('clear')
        print logo
        print
        print
        print '\x1b[1;97mLICENSE KEY'
        print '\x1b[1;97m-----------'
        print '\x1b[1;97m '
        print '          \x1b[1;92mYOUR KEY : \x1b[1;96m' + usr + ' (X)'
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/mastertrick1')
        baba2()


def zz():
    os.system('clear')
    print logo
    print
    print
    print '\x1b[1;97mLICENSE KEY'
    print '\x1b[1;97m-----------'
    print '\x1b[1;97m '
    print '          \x1b[1;92mYOUR KEY : BOTOLBABA@MAIL.COM (\xe2\x88\x9a)'
    print '\n\n \x1b[1;92mLICENSE KEY APPROVED BY BOTOL BABA.\x1b[0m'
    print
    jalan('\x1b[1;93mPLEASE WAIT 2MINUTES, ALL PACKAGES ARE CHECKING...')
    time.sleep(1)
    os.system('python2 .README.md')


if __name__ == '__main__':
    u()