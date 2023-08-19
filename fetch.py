# yes this can and inevitably will fuck up once the html structure is changed 

import requests
from bs4 import BeautifulSoup
import re


global weeks
weeks = [
	"MÅNDAG",
	"TISDAG",
	"ONSDAG",
	"TORSDAG",
	"FREDAG"
]

global lunch_boilerplate 
lunch_boilerplate = "VI ANVÄNDER INHEMSKT KÖTT I MATLAGNINGEN!KÄYTÄMME RUOANLAITOSSA KOTIMAISTA LIHAA!"

def del_days(menu_arr, days_arr):
	buf = []
	for i in menu_arr:
		for j in days_arr:
			if j in i:
				i = i.replace(j, "")
				buf.append(i)
			elif lunch_boilerplate in i:
				i = i.replace(lunch_boilerplate, "")
				buf.append(i)

	for i in range(len(buf)-1):
		if len(buf[i]) <= 2:
			buf.pop(i)

	return buf

def parse_menu(input_string):
	menu_items = re.findall(r'[A-Z][^.0-9]*', input_string)

	fmi = [item for item in menu_items if item]
	#print(fmi)

	for i in range(len(fmi)):
		#print(fmi[i])
		if (len(fmi) == i+1):
			break

		if (len(str(fmi[i])) <= 2 or len(str(fmi[i])) == 1):
			fmi.pop(i)
			print("1", i)

	fmi = [item for item in fmi if item != "VI ANVÄNDER INHEMSKT KÖTT I MATLAGNINGEN!KÄYTÄMME RUOANLAITOSSA KOTIMAISTA LIHAA!"]
	return del_days(fmi, weeks)

def fetch_menu():

	r = requests.get("https://optimaedu.fi/sv/info-till-dig-som-studerar-vid-optima/frukost-och-lunch-vid-optima-jakobstad/")  
	soup = BeautifulSoup(r.content, 'html.parser')

	s = soup.find("div", class_="mb-12")
	content = s.find_all("h4")

	for h4_element in content:
		h4_element.replace_with(h4_element.get_text())

	buffer = ""
	for h4_element in content:
		buffer += h4_element.get_text()

	return parse_menu(buffer)