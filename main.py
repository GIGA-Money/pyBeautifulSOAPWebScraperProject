from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import ssl

site= "https://pastebin.com/raw/Bjsw46PD"
hdr = {'User-Agent': 'Mozilla/5.0'}
context = ssl._create_unverified_context()
req = Request(site, headers=hdr)
page = urlopen(req, context=context)
soup = BeautifulSoup(page,"html.parser")
#print(soup)
medstr = str(soup)
medstr = medstr.replace('has 1 vehicle Directives.\r\n', '')
medstr = medstr.replace('has 2 vehicle Directives.\r\n', '')
medstr = medstr.replace('has 3 vehicle Directives.\r\n', '')
medstr = medstr.replace('has 4 vehicle Directives.\r\n', '')
medstr = medstr.replace('has 5 vehicle Directives.\r\n', '')
medstr = medstr.replace('has 6 vehicle Directives.\r\n', '')
medstr = medstr.replace('has 7 vehicle Directives.\r\n', '')
medstr = medstr.replace('has 8 vehicle Directives.\r\n', '')
medstr = medstr.replace('#', '')
medstr = medstr.split(' ')

evens = 0
odds = 1
indexlist = []
valuelist = []

for element in  medstr:
    print(element)
    if medstr[evens] == 0:
        print(element)

#pageNum = 1
#+ str(pageNum)
#html1 = urlopen("https://ps4us.ps2.fisu.pw/leaderboard/player/#acc")
#html2 = urlopen("https://ps2.fisu.pw/leaderboard/player/#acc")
#print(html2.read())
#while pageNum:
 #   pageNum += 1
  #  if pageNum > 100:
   #     pageNum = False
