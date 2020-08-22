
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Source File : password.py
# Time : Sat Aug 22 08:02:31 2020
#---------------------------------------
# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <seni>
import os, sys, time, os, random
sleep = time.sleep
import platform, os

def tampil(x):
    w = {'m': 31, 'h': 32, 'k': 33, 'b': 34, 'p': 35, 'c': 36}
    for i in w:
        x = x.replace('\r%s' % i, '\x1b[%s;1m' % w[i])

    x += '\x1b[0m'
    x = x.replace('\r0', '\x1b[0m')
    print x


tampil('\rh\n          ___   ___   _  _   \n         | __| | _ ) | || |  \rk*\rcAsecC|~|eror404\n         | _|  | _ \\ | __ |  \n        _|_|_  |___/ |_||_|  \n \rp |"""""|| """ |\rmHaxID\rp|"""""||"""""| \n      "`-0-0-\'"`-0-0-\'"`-0-0-\'   ')
tampil('')
tampil('')
print '\x1b[36;1mSilahkan Masukkan Username & Password Anda'
print '\x1b[36;1matau silahkan Hubungi \x1b[31;1mAsecC|~|eror404 '
print ''
print ''
username = 'AsecC'
password = 'eror404'

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


def main():
    uname = raw_input('\x1b[32;1mUsername : ')
    if uname == username:
        pwd = raw_input('\x1b[31;1mPassword : ')
        if pwd == password:
            print '\x1b[1;32mLogin berhasil..',
            sys.exit()
        else:
            print '\x1b[1;32mMaaf password yang anda masukan salah... [?]\x1b[00m'
            print 'Silahkan Coba lagi...!!\n'
    else:
        print '\x1b[1;32mMaaf username yang anda masukan salah... [?]\x1b[00m'
        print '\x1b[31;1mSilahkan Coba lagi...!!\n'


try:
    main()
except KeyboardInterrupt:
    os.system('clear')
    restart()