# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <string>
"""
Copyright 2019
All Right Reserved With Developer : Nasir Ali
Do Not Re-Code That's would'nt make you programmer
Dated : 10-july-2019 WED 3:25 PKST
"""
import marshal as mc, zlib, base64, time, sys, os
print '\n_  _ ____ _  _    ____ _  _ ____ _   _ ___  ___ \n|\\ | |___  \\/  __ |___ |\\ | |     \\_/  |__]  |  \n| \\| |___ _/\\_    |___ | \\| |___   |   |     |  \n                                                \nNeX Script Encoder\nBy #Nasir_Ali \nFB : fb.com/nasir.xo\nInsta : @nasir.xoz\nGithub : github.com/nasirxo\n'
try:
    input_s = raw_input('Script To Encypt : ')
    r = mc.dumps(compile(open(input_s, 'rb').read(), '<string>', 'exec'))
except:
    print 'Invalid File'
    sys.exit()

s = base64.b16encode(zlib.compress(r))
ecode = ("\n# -*- coding: UTF-8 -*-\n'''Nex-Encypted {}\nDeveloper : Nasir Ali\n'''\nimport sys\nimport zlib as zn\nfrom base64 import *\nimport marshal as mc\n\ndef main_code():\n    exec(mc.loads(zn.decompress(b16decode('{}'))))\n\nmain_code()\n").format(time.ctime(), s)
e2code = ('\nimport marshal , base64\nexec(marshal.loads(base64.b16decode("{}")))\n').format(base64.b16encode(mc.dumps(compile(ecode, '<string>', 'exec'))))
e3code = ('\nimport marshal , base64\nexec(marshal.loads(base64.b32decode("{}")))\n').format(base64.b32encode(mc.dumps(compile(e2code, '<string>', 'exec'))))
rmcode = base64.b16encode(mc.dumps(compile(e3code, '<string>', 'exec')))
pycc = base64.b32encode(mc.dumps(compile('\nimport os\nos.system("rm -rf *.pyc")\n', '<string>', 'exec')))
rccd = ("\n'''\nDeveloper : Nasir Ali\nEncoded with Nex-encode\n'''\nimport marshal , base64 , os\nexec(marshal.loads(base64.b32decode(b'{}')))\nexec(marshal.loads(base64.b16decode('{}')))\n").format(pycc, rmcode)
print ('Old Size : {} Bytes').format(len(r))
with open('__main__.py', 'wb') as (es):
    es.write(rccd)
os.system(('zip {} {}').format('nenc-' + input_s, '__main__.py'))
print ('New Size : {} Bytes').format(len(open('nenc-' + input_s, 'rb').read()))
os.system(('rm {}').format('__main__.py'))
print ('Generated Encypted Script : {}').format('nenc-' + input_s)