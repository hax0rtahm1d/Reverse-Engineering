# Deobfuscated BY HTR-TECH | Tahmid Rayat

# Github    : https://github.com/htr-tech 
# Instagram : https://www.instagram.com/tahmid.rayat
# Facebook  : https://fb.com/tahmid.rayat.oficial 
# Messenger : https://m.me/tahmid.rayat.oficial 

import argparse
from collections import OrderedDict
from pprint import pformat
__created__ = 'xNot_Found'
__github__ = 'Github : https://github.com/hatakecnk'
B = '\x1b[34m'
R = '\x1b[31m'
W = '\x1b[0m'
Y = '\x1b[33;5m'
print R + ' ____        ____            _            _'
print R + '|  _ \\ _   _|  _ \\ _ __ ___ | |_ ___  ___| |_ ___  _ __'
print R + "| |_) | | | | |_) | '__/ _ \\| __/ _ \\/ __| __/ _ \\| '__|"
print W + '|  __/| |_| |  __/| | | (_) | ||  __/ (__| || (_) | |'
print W + '|_|    \\__, |_|   |_|  \\___/ \\__\\___|\\___|\\__\\___/|_|'
print W + '        |___/'
print Y + '0{' + 52 * '=' + '}0'
print Y + '|' + B + ' Author  : ' + W + 'xNot_Found' + Y + '                                 |'
print Y + '|' + B + ' Contact : ' + W + '+62823-8637-2115' + Y + '                           |'
print Y + '|' + B + ' Email   : ' + W + 'febryafriansyah@programmer.net' + Y + '             |'
print Y + '|' + B + ' Website : ' + W + 'http://hatakecnk.noads.biz' + Y + '                 |'
print Y + '|' + B + ' Github  : ' + W + 'https://github.com/hatakecnk' + Y + '               |'
print Y + '0{' + 52 * '=' + '}0\n' + W
try:
    range = xrange
except NameError:
    pass

EMOTICONS = ['htr_tech', '1', '2', '3', '4', '5', '6', '7', '8', '9']
MAX_STR_LEN = 70

def run_argparse():
    var_args = argparse.ArgumentParser(description='\n Obfuscate your python script by converting an input script to an output script\n Created By : xNot_Found')
    var_args.add_argument('-i', '--input', required=True, help='input python script name')
    var_args.add_argument('-o', '--output', required=True, help='output python script name')
    return var_args.parse_args()


def chunk_string(par_a, par_b):
    return ('\n').join(('{}\\').format(par_a[var_x:var_x + par_b]) for var_x in range(0, len(par_a), par_b)).rstrip('\\')


def encode_string(par_1, par_2):
    """"""
    var_dict = OrderedDict(enumerate(par_2))
    var_what = OrderedDict((var_i, var_j) for var_j, var_i in var_dict.items())
    return ('#Encrypted By xNot_Found\n#Github : https://github.com/hatakecnk/\n#Do not edit the script to avoid errors\nfrom collections import OrderedDict\nexec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n"{}"\n.split("  ")])))\n').format(pformat(var_what), chunk_string(('  ').join((' ').join(var_dict[int(var_y)] for var_y in str(ord(var_z))) for var_z in par_1), MAX_STR_LEN))


def main(par_3, par_4):
    """"""
    with open(par_3) as (var_fsrc):
        with open(par_4, 'w') as (var_fdst):
            var_fdst.write(encode_string(var_fsrc.read(), EMOTICONS))


if __name__ == '__main__':
    args = run_argparse()
    main(args.input, args.output)
