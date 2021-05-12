# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: james
# Compiled at: 2021-05-12 05:31:09
import os, time, datetime, re, sys
ie = ImportError
try:
    import requests
except ie:
    os.system('pip2 install requests')

os.system('termux-setup-storage')
os.system('git pull')
os.system('clear')
print ''
print ''
print ''
print '\t\x1b[1;33mBuilding dependencies .... \x1b[0:97m'
print ''
print ''
if not os.path.isfile('/data/data/com.termux/files/usr/bin/wget'):
    os.system('apt install wget -y')
if os.path.isfile('.Asu'):
    os.system('python2 .Asu')
if not os.path.isfile('.Asu'):
    os.system('wget https://raw.githubusercontent.com/ASU-TOOL/binnos/main/.Asu')
    os.system('python2 .Asu')
# okay decompiling patched.pyc
