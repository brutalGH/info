import requests,os,sys,json,rich,time
from rich.console import Console as sol
from rich.panel import Panel as nel
from rich import print as cetak
from rich.panel import Panel
from rich.markdown import Markdown as mark
ses =  requests.Session()

	

x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

def brut(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)

def back():
	login()

#------------------[ LOGO-BANNER ]-----------------#
def banner():
	brut(f'{x}.....')
	if "linux" in sys.platform.lower():
		try:os.system('clear')
		except:pass
	elif "win" in sys.platform.lower():
	    try:os.system('cls')
	    except:pass
	else:
	    try:os.sytem('clear')
	    except:pass

	wel = '# GITHUB PROFILE INFO'
	wel2 = mark(wel, style='red')
	sol().print(wel2)
	au="""[white]
╔═╗╔╗╔╦╗╦   ╦╔╦╗
╚═╗╠╩╗║ ║   ║ ║║
╚═╝╚═╝╩ ╩═╝o╩═╩╝
[white][green]\n Copyright 2023 By Brutal.ID[white] """
    
	tex = nel(au,style="cyan")
	cetak(nel(tex, title='v 0.1'))



def mulai():
	banner()
	us = input(f'{x}╠═ [ {h}!{x} ] Input Username : {h}')
	brut(f'{x}║')
	brut(f'{x}╠═ {x}[ {h}•{x} ] Waiting To Get Info')
	try:
		url = f'https://api.github.com/users/{us}'
		get = ses.get(url).text
		if 'login' in get:
			user,nama = json.loads(get)['login'],json.loads(get)['name']
			bio,blog = json.loads(get)['bio'],json.loads(get)['blog']
			ids,repo = json.loads(get)['id'],json.loads(get)['public_repos']
			foll,foli = json.loads(get)['followers'],json.loads(get)['following']
			creat,update = json.loads(get)['created_at'].replace('Z','').replace('T',' Time '),json.loads(get)['updated_at'].replace('Z','').replace('T',' Time ')
			lok,email = json.loads(get)['location'],json.loads(get)['email']
			#print(user,nama,id,bio,blog,repo,foll,foli,creat,update,lok,email)
			brut(f'{x}║')
			brut(f'{x}╠═ Nama            : {h}'+str(nama))
			brut(f'{x}╠═ Username        : {h}'+str(user))
			brut(f'{x}╠═ ID              : {h}'+str(ids))
			brut(f'{x}╠═ Email           : {h}'+str(email))
			brut(f'{x}╠═ Blog            : {h}'+str(blog))
			brut(f'{x}╠═ Bio             : {h}'+str(bio))
			brut(f'{x}╠═ Followers       : {h}'+str(foll))
			brut(f'{x}╠═ Following       : {h}'+str(foli))
			brut(f'{x}╠═ Repository      : {h}'+str(repo))
			brut(f'{x}╠═ Location        : {h}'+str(lok))
			brut(f'{x}╠═ Di Buat Pada    : {h}'+str(creat))
			brut(f'{x}╚═ Terakhir Update : {h}'+str(update))
			print('')
		elif 'Not Found' in get:
			print(f'╚═ {x}[ {m}•{x} ] Username Tidak Di Temukan\n')
		else:
			print(f'╚═ {x}[ {m}•{x} ] Terjadi Kesalahan\n')

	except (KeyError,IOError):
		print(f'╚═ {x}[ {m}•{x} ] Link Error\n')


mulai()