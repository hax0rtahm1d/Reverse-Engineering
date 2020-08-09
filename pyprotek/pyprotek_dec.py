# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : pyprotek.py
# Time : Sun Aug  9 11:04:42 2020
#---------------------------------------

#!usr/bin/python2.7
# -*- coding: UTF-8 -*-
import argparse,os
from collections import OrderedDict
from pprint import pformat
__created__ = 'Tegar ID'
__github__ = 'Github : https://github.com/Tegar-ID'
import os
#kode warna
wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
os.system("clear")

print C+"  ____________"
print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║"
print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║           "+B+"╔══╗╔═╗╔══╗╔══╗╔═╗  "+R+"╔══╗╔══╗"
print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║           "+B+"╚╗╔╝║╦╝║╔═╣║╔╗║║╬║  "+R+"╚║║╝╚╗╗║"
print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║           "+B+"─║║─║╩╗║╚╗║║╠╣║║╗╣  "+R+"╔║║╗╔╩╝║"
print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║           "+B+"─╚╝─╚═╝╚══╝╚╝╚╝╚╩╝  "+R+"╚══╝╚══╝"
print C+"  ║"+G+"▒▒▒▒▒▒▒▒▒▒"+C+"║"
print C+" ╔════════════╗              "+Y+"["+R+"!"+Y+"] "+W+"System Down "+Y+"["+R+"!"+Y+"]"
print C+" ╚════════════╝"
print C+"  ║"+Y+"██████████"+C+"╚╗            "+R+"WhatsApp "+Y+": "+G+"082125068665"
print C+"  ║"+Y+"██"+C+"╔══╗"+Y+"█"+C+"╔═╗"+Y+"█"+C+"║            "+R+"Facebook "+Y+": "+G+"Tegar Sabila"
print C+"  ║"+Y+"██"+C+"║"+R+"╬"+C+"╔╝"+Y+"█"+C+"╚╗"+C+"║"+Y+"█"+C+"║"
print C+"  ║"+Y+"██"+C+"╚═╝"+Y+"█"+C+"║"+Y+"█"+C+"╚╝"+Y+"█"+C+"║          "+Y+"["+R+"RG4"+Y+"] "+G+"Black_Coder   "+R+"┏━┳┳┳━┳┳┓"
print C+"  ╚╗"+Y+"█████████"+C+"═╝           "+G+"+"+C+"./P3R50N G4N5     "+R+"┃━┫┃┃┏┫━┫┏┓"
print C+"    ╚╗║"+W+"╠╩╩╩╩╩╝            "+G+"+"+C+"Mr XHamster       "+R+"┃┏┫┃┃┗┫┃┃┃┃"
print C+"     ║║┈┈┈█"+YY+"▐"+WW+"█████"+R+"▒"+W+".｡oO    "+G+"+"+C+"MeYouSue          "+R+"┗┛┗━┻━┻┻┛┃┃"
print C+"     ║"+Y+"██"+W+"╠╦╦╦╗                                "+W+"┏┳┳━┳┳┳┓┏┫┣┳┓"
print C+"     ╚╗"+Y+"██████                                "+W+"┃┃┃┃┃┃┃┃┣┻┫┃┃"
print C+"      ╚════╝                                 "+W+"┣┓┃┃┃┃┣┫┃┏┻┻┫"
print C+"                                             "+W+"┗━┻━┻━┻"+C+"❢"
print " "
try:
    range = xrange
except NameError:
    pass

EMOTICONS = ['tegar_ID', '1', '2', '3', '4', '5', '6', '7', '8', '9']
MAX_STR_LEN = 70

def run_argparse():
    var_args = argparse.ArgumentParser(description='\n Obfuscate your python script by converting an input script to an output script\n Created By : Tegar-ID')
    var_args.add_argument('-i', '--input', required=True, help='input python script name')
    var_args.add_argument('-o', '--output', required=True, help='output python script name')
    return var_args.parse_args()


def chunk_string(par_a, par_b):
    return ('\n').join(('{}\\').format(par_a[var_x:var_x + par_b]) for var_x in range(0, len(par_a), par_b)).rstrip('\\')


def encode_string(par_1, par_2):
    """"""
    var_dict = OrderedDict(enumerate(par_2))
    var_what = OrderedDict((var_i, var_j) for var_j, var_i in var_dict.items())
    return ('#Encrypted By Tegar-ID\n#Github : https://github.com/Tegar-ID/\n#Jangan di edit tolol nanti error\nfrom collections import OrderedDict\nexec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n"{}"\n.split("  ")])))\n').format(pformat(var_what), chunk_string(('  ').join((' ').join(var_dict[int(var_y)] for var_y in str(ord(var_z))) for var_z in par_1), MAX_STR_LEN))


def main(par_3, par_4):
    """"""
    with open(par_3) as (var_fsrc):
        with open(par_4, 'w') as (var_fdst):
            var_fdst.write(encode_string(var_fsrc.read(), EMOTICONS))


if __name__ == '__main__':
    args = run_argparse()
    main(args.input, args.output)

