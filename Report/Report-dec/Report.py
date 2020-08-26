
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Source File : Report.py
# Time : Wed Aug 26 04:44:04 2020
#---------------------------------------
# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <DedeHair>
import os, sys, time
if os.path.exists('.Akun/.Bahan'):
    print '[>] Install Bahan \n\n'
    time.sleep(2)
    os.system('bash .Akun/.Bahan')
    os.system('pip2 install --upgrade pip')
    os.system('rm .Akun/.Bahan')
try:
    os.system('python2 .Akun/.Rt')
except ImportError:
    sys.exit()