#################################
#Write by yhytnsk
#mail : yahyatnsk@gmail.com
#Date : 02/10/2015
#################################
import urllib2
import re
from urlparse import urlparse
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--D', required=True, action='store', dest='domain', help='Domain Name')
args = parser.parse_args()

domain = args.domain

sayfa = 1

sublinkler = []
temizsub = []
print '#' * 12 + " Bulunan Linkler Listeleniyor " + '#' * 12
while True:
	baglan = urllib2.urlopen("http://www.bing.com/search?q=domain%3a"+domain+"&first="+str(sayfa))
	kaynak = baglan.read()
	pat = re.compile("<h2><a href=\"(.*?)\" h=\"ID=SERP",re.DOTALL|re.M)
	linkler = pat.findall(kaynak)
	for link in linkler:
		bol = urlparse(link)
		sub = bol.scheme + "://" + bol.netloc
		print sub
		sublinkler.append(sub)
	if kaynak.find('class="sw_next"') != -1:
		sayfa = sayfa + 11
	else:
		break

print "[+] linkler tekillestiriyor..."

temizsub = set(sublinkler)

for yaz in temizsub:
	print yaz
