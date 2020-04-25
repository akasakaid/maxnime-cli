import requests,os
from bs4 import BeautifulSoup as bs
merah = '\x1b[1;31m'
hijau = '\x1b[1;32m'
kuning = '\x1b[1;33m'
biru = '\x1b[1;34m'
magenta = '\x1b[1;35m'
cyan = '\x1b[1;36m'
putih = '\x1b[1;37m'
r = requests.Session()
hd = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
def linkanime(url):
	try:
		get_2 = r.get(url,headers=hd).text
		par_2 = bs(get_2,'html.parser')
		area = par_2.find('div',attrs={'class':'area'})
		boxdl = area.findAll('div',attrs={'class':'boxdl'})
		for boxt in boxdl:
			print(cyan+"- "*35)
			print(hijau+boxt.find('div',attrs={'class':'boxtitle'}).text)
			boxnn = boxt.findAll('div',attrs={'class':'boxurl'})
			for boxnnn in boxnn:
				print(f"{magenta}\t\t\t"+boxnnn.find('strong').text)
				nalink = boxnnn.findAll('a')
				for nama in nalink:
					print(biru+nama.text,putih+nama.get('href'))
	except Exception as e:
		exit(f"error {e}")
def getanime(link):
	try:
		z = 1
		get_1 = r.get(f"https://www.maxnime.com/?s={link}&post_type=anime",headers=hd).text
		par_1 = bs(get_1,'html.parser')
		lian_1 = par_1.find('div',attrs={'class':'white'})
		lian_2 = lian_1.findAll('li')
		print(f"{putih}Jumlah Hasil Pencarian: {hijau}",len(lian_2))
		if len(lian_2) == 0:
			print("selesaiii")
			exit()
		else:
			for lian_3 in lian_2:
				lian_4 = lian_3.find('a')
				print(biru+str(z),putih+lian_4["title"])
				z += 1
			ani = int(input(f"{kuning}masukkan nomor dari anime yang kamu cari{merah}:{putih} "))
			if ani > len(lian_2):
				print("yee anjink udah tau pilihannya 1 sampai",len(lian_2),"masih aja dikasi piihan yang lebih gede ")
				exit()
			else:
				print(hijau+"Anime",lian_2[ani-1].find('a').get('title'))
				linkanime(lian_2[ani-1].find('a').get('href'))
	except Exception as e:
		exit(f"error {e}")
if os.name == 'nt':os.system('cls')
else:os.system('clear')
print(f"""{putih}
[ Maxnime - Get Link Download ]
    [ Coded by AkasakaID ]
""")
try:
	an = input(f"{kuning}masukkan nama anime{merah}:{cyan} ")
	getanime(an)
except KeyboardInterrupt:
	exit("\nKeluar !!")