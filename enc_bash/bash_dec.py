# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <AsecX>
import os
from time import sleep
os.system('clear')
os.system('xdg-open https://www.youtube.com/channel/UCuPp2fYqlG7IvltINFMAOgQ')
sleep(1)
print '                \x1b[1;96m =[\xf0\x9f\x92\x9f \x1b[1;95mCoded by \x1b[1;92mAsecC eror404\x1b[1;96m \xf0\x9f\x92\x9f='
print '            \x1b[1;96m +  --  --=[\xf0\x9f\x92\x9f Encrypt Bash\x1b[1;96m \xf0\x9f\x92\x9f]=--  --  +'
print ''
print '\x1b[1;95m[ \x1b[1;91mEx: \x1b[1;90m/sdcard/file.sh \x1b[1;95m]'
file = raw_input('\x1b[1;92m[\x1b[1;96m+\x1b[1;92m] \x1b[1;96mFile : \x1b[1;90m')
os.system('bash-obfuscate ' + file + ' -o sec.sh')
k = open('sec.sh').read()
p = open('un.sh', 'w')
p.write(k)
p.close()
os.system('rm -rf sec.sh')
a = 0
for i in range(int(6)):
    a += 1
    os.system('base64 un.sh > ok.sh')
    f = open('ok.sh').read()
    m = f.replace('\n', '')
    s = open('out.sh', 'w')
    s.write('love=$(base64 -d <<< "' + m + '"); decode_status=$?;[[ $decode_status == 0 ]] && eval $love;\n#Compiled By AsecX\n#https://github.com/muhammadfathul')
    s.close()
    os.system('base64 out.sh > ya.sh')
    q = open('ya.sh').read()
    x = q.replace('\n', '')
    os.system('rm -rf un.sh out.sh ok.sh')
    w = open('un.sh', 'w')
    w.write('love=$(base64 -d <<< "' + x + '"); decode_status=$?;[[ $decode_status == 0 ]] && eval $love;\n#Compiled By AsecX\n#https://github.com/muhammadfathul')
    w.close()
    os.system('rm -rf ya.sh')

os.system('mv un.sh enc_' + file)
sleep(2)
print '# \x1b[1;92mSaved : \x1b[1;96menc_' + file