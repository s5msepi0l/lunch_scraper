import requests
from bs4 import BeautifulSoup
import re

r = requests.get("https://optimaedu.fi/sv/info-till-dig-som-studerar-vid-optima/frukost-och-lunch-vid-optima-jakobstad/")  
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find("div", class_="mb-12")
content = s.find_all("h4")

global weeks
weeks = [
	"MÅNDAG",
	"TISDAG",
	"ONSDAG",
	"TORSDAG",
	"FREDAG"
]

def del_days(menu_arr, days_arr):
	buf = []
	for i in menu_arr:
		for j in days_arr:
			if j in i:
				i = i.replace(j, "")
				buf.append(i)
	return buf

def parse_menu(input_string):
    menu_items = re.findall(r'[A-Z][^.0-9]*', input_string)
    
    fmi = [item.strip() for item in menu_items if item.strip() and "VI ANVÄNDER INHEMSKT KÖTT I MATLAGNINGEN!KÄYTÄMME RUOANLAITOSSA KOTIMAISTA LIHAA!" not in item]
    
    for i in range(len(fmi)):
    	if (len(fmi) == i):
    		break


    	if (len(str(fmi[i])) <= 2 or len(str(fmi[i])) == 1):
    		fmi.pop(i)
    	

    	if (str(fmi[i]) in weeks):
    		fmi.pop(i)

    return del_days(fmi, weeks)

for h4_element in content:
    h4_element.replace_with(h4_element.get_text())

buffer = ""
for h4_element in content:
    buffer += h4_element.get_text()

buffer = parse_menu(buffer)
for i in buffer:
	print(i)