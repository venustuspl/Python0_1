import requests
from bs4 import BeautifulSoup


vgm_url = 'https://www.pracuj.pl/praca/junior%20java%20developer;kw/warszawa;wp?rd=0'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')

print(soup.title)


#import random as r 

#for i in range(6):
#    print(r.randrange(1,50))
