
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : aa.pyc
# Bytecode Version : 2.7
#---------------------------------------

import os
import sys
import time
import colorama
from colorama import *
import sys

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 100)
    


def again():
    run = raw_input('\x1b[1;91m\n=> [l]\x1b[1;92m exit\x1b[1;96m or \x1b[1;91m[Enetr]\x1b[1;92m continue ? [l / enter] =\x1b[1;96m  ')
    if run == 'l':
        print 'Exiting......'
        time.sleep(0.5)
        print '             \x1b[1;92mThank You For Using T-Speak !'
        time.sleep(1)
        print ''
        os.system('echo ---------------------------------------------- | lolcat')
        os.system('echo [ ------T-Speak By Mujeeb ------] | lolcat')
        print ''
    else:
        os.system('clear')
        logo()
        main()


def td():
    time.sleep(1)
    os.system('clear')
    time.sleep(0.5)


def logo():
    print '\x1b[0;34m'
    print '\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 v1.0'
    print '\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d'
    print '   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d'
    print '   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97'
    print '   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91      \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97'
    print '   \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d      \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d'
    print '\x1b[1;97m----------------\x1b[44mTermux-Speak-Engin\x1b[00m\x1b[1;97m------------------'
    print ''


def author():
    pt()
    os.system('echo -------[ Author Information ]------- | lolcat')
    print '\x1b[1;96m'
    print 'Name    : Mujeeb'
    print 'Youtube : www.youtube.com/TechnicalMujeeb'
    print 'Github  : https://github.com/TechnicalMujeeb/Termux-speak.git'
    pt()
    os.system('echo ------[ Technical Mujeeb ]------| lolcat -a -d 120')
    pt()


def pt():
    print ''


def main():
    print '\x1b[1;94m(1)..\x1b[1;36m speak Engin Info '
    pt()
    print '\x1b[1;94m(2)..\x1b[1;36m Speak Now '
    pt()
    print '\x1b[1;94m(3)..\x1b[1;36m Author '
    pt()
    time.sleep(0.2)
    op = raw_input('\x1b[1;93m \x1b[1;91mT-SPEAK\x1b[1;94m@\xe2\x94\x80\xe2\x9d\xaf \x1b[1;92m ')
    if op == '1':
        pt()
        slowprint('using this command you get information about the \n text-to-speach (TTS) engines. \n And the name of an engin may be given to the \n termux-tts-speak.')
        pt()
        pr = raw_input('\x1b[1;96mPress \x1b[1;91mENTER \x1b[1;96mto see (TTS) Engin Inforamation. ')
        os.system('termux-tts-engines')
        os.system('echo -----------------------------------------| lolcat -a -d 30')
        again()
    elif op == '3':
        author()
        again()
    elif op == '2':
        pt()
        slowprint('Lets speak with engin...')
        pt()
        speak = raw_input(Fore.CYAN + ' Enter Your Text :\x1b[1;92m ')
        pt()
        print '\x1b[4;93mSelect Pitch \x1b[00m'
        pt()
        print '\x1b[1;91m(1)..\x1b[1;92m 1.0 '
        print '\x1b[1;91m(2)..\x1b[1;92m 2.0 '
        print '\x1b[1;91m(3)..\x1b[1;92m 3.0 '
        print '\x1b[1;91m(4)..\x1b[1;92m 4.0 '
        print '\x1b[1;91m(5)..\x1b[1;92m 5.0 '
        print '\x1b[1;91m(6)..\x1b[1;92m custom '
        pt()
        pitch = raw_input(Fore.CYAN + 'Enter Pitch : \x1b[1;92m')
        if pitch == '1':
            a = '-p 1.0'
        elif pitch == '2':
            a = '-p 2.0'
        elif pitch == '3':
            a = '-p 3.0'
        elif pitch == '4':
            a = '-p 4.0'
        elif pitch == '5':
            a = '-p 5.0'
        elif pitch == '6':
            cu = raw_input(Fore.CYAN + 'Enter custom pitch :\x1b[1;92m ')
            a = '-p ' + cu
            pt()
            print '\x1b[4;93mSelect Rate\x1b[00m'
            pt()
            print '\x1b[1;91m(1)..\x1b[1;92m 0.5 '
            print '\x1b[1;91m(2)..\x1b[1;92m 0.8 '
            print '\x1b[1;91m(3)..\x1b[1;92m 1.0 '
            print '\x1b[1;91m(4)..\x1b[1;92m 2.0 '
            print '\x1b[1;91m(5)..\x1b[1;92m 3.0 '
            print '\x1b[1;91m(6)..\x1b[1;92m custom '
            pt()
            rate = raw_input(Fore.CYAN + 'Enter Rate : \x1b[1;92m')
            if rate == '1':
                b = '-r 0.5'
                td()
                os.system('termux-tts-speak ' + a + ' ' + b + ' ' + speak)
                again()
            elif rate == '2':
                b = '-r 0.8'
                td()
                os.system('termux-tts-speak ' + a + ' ' + b + ' ' + speak)
                again()
            elif rate == '3':
                b = '-r 1.0'
                td()
                os.system('termux-tts-speak ' + a + ' ' + b + ' ' + speak)
                again()
            elif rate == '4':
                b = '-r 2.0'
                td()
                os.system('termux-tts-speak ' + a + ' ' + b + ' ' + speak)
                again()
            elif rate == '5':
                b = '-r 3.0'
                td()
                os.system('termux-tts-speak ' + a + ' ' + b + ' ' + speak)
                again()
            elif rate == '6':
                kkk = raw_input(Fore.CYAN + 'Enter custom rate value :\x1b[1;92m')
                b = '-r ' + kkk
                os.system('termux-tts-speak ' + a + ' ' + b + ' ' + speak)
                again()
            else:
                td()
                logo()
                main()
        
    else:
        td()
        os.system('clear')
        logo()
        main()

logo()
main()
