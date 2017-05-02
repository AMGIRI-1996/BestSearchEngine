import requests
from bs4 import BeautifulSoup
url = "http://search.yahoo.com/search?p=%s"
query = "flash"
r = requests.get(url % query) 
soup = BeautifulSoup(r.text,"html.parser")
#print(r.text.encode("utf-8").decode("utf-8"))
soup.find_all(attrs={"class": " fz-ms fw-m fc-12th wr-bw lh-17"})

for link in soup.find_all(attrs={"class": "fw-m"}):
	#print(link)
	print ("%s " %(link.text))