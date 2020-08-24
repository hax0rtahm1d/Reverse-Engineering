# coding:utf8
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : patched.pyc
# Bytecode Version : 2.7
#---------------------------------------
import sys, os, time
from zlib import compress
B = '\x1b[34;1m'
R = '\x1b[31;1m'
G = '\x1b[32;1m'
W = '\x1b[0m'
Y = '\x1b[33;1m'
counter = 0
def banner():
    os.system('clear')
    print """ \x1b[31;5m  _____                        ______ _ _
 | ____|_ __  _ __  _   _     |__  / (_) |__
 |  _| | '_ \| '_ \| | | |_____ / /| | | '_ \\
\x1b[39;5m | |___| | | | |_) | |_| |_____/ /_| | | |_) |
 |_____|_| |_| .__/ \__, |    /____|_|_|_.__/
             |_|    |___/
╔════════════════════════════════════════════╗
    \x1b[31;5mAuthor : \x1b[39;3mFebry [ xNot_Found ]\x1b[0;37m
    \x1b[31;5mGithub : \x1b[39;3mhttps://github.com/hatakecnk\x1b[0;37m\x1b[39;5m
╚════════════════════════════════════════════╝"""
try:
    banner()
    file = raw_input('\033[0;37m┌─[\033[31;1m Input Your File Path (\x1b[39;5m/sdcard/ex.py\x1b[31;1m) \033[0;37m]\n\033[0;37m└─[\033[31;1m$\033[0;37m]> \033[36;1m')
    count = int(raw_input('\033[0;37m┌─[\033[31;1m Count Encrypt (\x1b[39;5mmax 400\x1b[31;1m) \033[0;37m]\n\033[0;37m└─[\033[31;1m$\033[0;37m]> \033[36;1m'))
except IndexError:
    print R + '\n[' + W + '!' + R + '] ' + W + 'there is an error'
    sys.exit()
except KeyboardInterrupt:
    print R + '\n[' + W + '!' + R + '] ' + W + 'ctrl+c detected'
    print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
    sys.exit()
except EOFError:
	print R + '\n\n[' + W + '!' + R + '] ' + W + 'ctrl+d detected'
	print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
	sys.exit()
except ValueError:
	print R + '\n[' + W + '!' + R + '] ' + W + 'input count!'
	print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
	sys.exit()
except:
	print R + '\n[' + W + '!' + R + '] ' + W + 'there an error'
	print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
	sys.exit()
if count < 400:
	try:
	    fileopen = open(file).read()
	except IOError:
	    banner()
	    print R + '\n[' + W + '!' + R + '] ' + W + 'file not exist'
	    sys.exit()
	try:
	    a = compress(fileopen)
	except Exception as f:
	    banner()
	    print R + '[' + W + '!' + R + '] ' + W + str(f)
	    sys.exit()
	d = ('# Encrypted By xNot_Found\n# Github : https://github.com/hatakecnk/\n# Do Not Edit The Script To Avoid Errors\nimport zlib\nexec(zlib.decompress('+repr(a)+'))')
	while True:
		if count >= counter:
			try:
				fileopen = d
			except IOError:
				banner()
				print R + '\n[' + W + '!' + R + '] ' + W + 'file not exist'
				sys.exit()
			try:
				a = compress(fileopen)
			except Exception as f:
				banner()
				print R + '[' + W + '!' + R + '] ' + W + f
				sys.exit()
			d = ('# Encrypted By xNot_Found\n# Github : https://github.com/hatakecnk/\n# Do Not Edit The Script To Avoid Errors\nimport zlib\nexec(zlib.decompress('+repr(a)+'))')
			print '\x1b[31;5m%s\x1b[39;1m' % counter
			e = file.replace('.py', '_enc.py')
			f = open(e, 'w')
			f.write(d)
			f.close()
			counter += 1
		else:
			break
try:
	banner()
	print B + '\n[' + W + '+' + B + '] ' + G + 'file saved : \x1b[39;5m' + e
except:
	print R + '\n[' + W + '!' + R + '] ' + W + 'there an error'
	print R + '[' + W + '!' + R + '] ' + W + 'trying exit'
	sys.exit()
