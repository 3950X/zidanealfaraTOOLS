print('''<<[ Assalamualaikum Warahmatullahi Wabarakatuh ]>>

     [Selamat datang]
     [zidanealfaraTOOLS]
     
''')


import os

 
def iOsif():
 print(f'[!] Menginstall tools osif..')
 os.system('pkg update upgrade')
 os.system('pkg install git python2')
 os.system('pkg install pip2')
 os.system('git clone https://github.com/ciku370/OSIF')
 os.system('cd OSIF')
 os.system('pip2 install -r requirements.txt')
 os.system('python2 osif.py')

def Hammer():
 print(f'[!] Menginstall tools Hammer..')
 os.system('git clone https://github.com/cyweb/hammer')
 os.system('cd hammer')
 os.system('python hammer.py')

def Sqlmap():
 print(f'[!] Menginstall tools Sqlmap..')
 os.system('git clone https://github.com/sqlmapproject/sqlmap')
 os.system('cd sqlmap')
 os.system('python2 sqlmap.py')

def Metasploit_termux():
 print(f'[!] Menginstall tools Metasploit-framework..')
 os.system('apt install wget')
 os.system('pkg install ruby')
 os.system('pkg install curl')
 os.system('git clone https://github.com/Hax4us/Metasploit_termux')
 os.system('cd metasploit-termux')
 os.system('./metasploit.sh')

def SpamSMS():
 print(f'[!] Menginstall tools SpamSMS..')
 os.system('pkg install php')
 os.system('git clone https://github.com/4L13199/LITESPAM')
 os.system('cd LITESPAM')
 os.system('python2 sh LITESPAM.sh')

def Phising():
 print(f'[!] Menginstall tools Phising..')
 os.system('pkg install openssh')
 os.system('git clone https://github.com/thelinuxchoice/shellphish')
 os.system('cd shellphish')
 os.system('bash shellphish.sh')

def MelacakORANG():
 print(f'[!] Menginstall tools MelacakORANG..')
 os.system('pkg install python python2 tsu -y')
 os.system('pkg install php')
 os.system('pkg install mechanize')
 os.system('git clone https://github.com/thelinuxchoice/locator')
 os.system('cd locator')
 os.system('tsu')
 os.system('bash locator.sh')

def Bug_Hunter():
 print(f'[!] Menginstall tools Bug_Hunter..')
 os.system('git clone https://github.com/zigoo0/webpwn3r.git')
 os.system('cd webpwn3r')
 os.system('chmod +x*')
 os.system('python2 scan.py')

def Hack_wifi_harus_root():
 print(f'[!] Menginstall tools Hack_wifi_harus_root..')
 os.system('git clone https://github.com/esc0rtd3w/wifi-hacker')
 os.system('cd wifi-hacker')
 os.system('chmod +x wifi-hacker.sh')
 os.system('./wifi-hacapdate')


def Lacak_IP():
 print(f'[!] Menginstall tools Lacak_IP..')
 os.system('git clone https://github.com/maldevel/IPGeolocation')
 os.system('cd IPGeolocation')
 os.system('chmod +x ipgeolocation.py')
 os.system('pip install -r requirements.txt')
 os.system('python ipgeolocation.py')


print('''<[ Tutorialnya nih ]>

     [di pilih gan, copy-paste websitenya]
     
[1]  OSIF                 = https://android-tutorialku.blogspot.com/2018/06/cara-install-dan-menggunakan-osif-di.html
[2]  Hammer               = https://tutorialtermux03.blogspot.com/2018/05/cara-ddos-dengan-hammer-di-termux.html
[3]  Sqlmap               = https://mrdellay.blogspot.com/2019/02/cara-menggunakan-sqlmap-di-termux_2.html
[4]  Metasploit-framework = https://ereldulugan.wordpress.com/2018/05/18/cara-install-metasploit-di-termux-cara-menggunakan-nya/
[5]  SpamSMS              = https://cholizgenerator.com/2019/01/05/cara-spam-sms-dengan-aplikasi-termux-litespam-tool/
[6]  Phising              = https://senitopengs.blogspot.com/2018/08/cara-membuat-phising-dengan-shellphish.html
[7]  MelacakORANG         = https://www.youtube.com/watch?v=LRTKFSRMD6Q
[8]  Bug_Hunter           = https://www.magelang1337.com/2019/05/mencari-bug-celah-website-dengan-termux.html
[9]  Hack_wifi_harus_root = https://fathurid.blogspot.com/2018/10/cara-hack-wifi-dengan-termux-root.html
[10] Lacak_IP             = https://termux.id/melacak-lokasi-menggunakan-termux-100-akurat/#top
''')

print('''<[ Tools nya ]>

     [Silahkan di pilih]
     
[1]  Install OSIF
[2]  Install Hammer
[3]  Install Sqlmap
[4]  Install Metasploit-framework
[5]  Install SpamSMS
[6]  Install Phising
[7]  Install MelacakORANG
[8]  Install Bug_Hunter
[9]  install Hack-wifi-harus-root
[10] install Lacak_IP
[11] keluar..
''')
menu = input('[?] Silahkan pilih menu : ')

if menu == '1':
 iOsif()
if menu == '2':
 Hammer()
if menu == '3':
 Sqlmap()
if menu == '4':
 Metasploit_termux()
if menu == '5':
 SpamSMS()
if menu == '6':
 Phising()
if menu == '7':
 MelacakORANG()
if menu == '8':
 Bug_Hunter()
if menu == '9':
 Hack-wifi-harus-root()
if menu == '10':
 Lacak_IP()
elif menu == '11':
 print('[?] Keluar..')
 exit()
else:
 print('[?] terima kasih..')
 exit()
