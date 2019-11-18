import ssl
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
import mysql.connector
import json

localhostdb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="popop123",
    database="player_entry"
)

activecursor = localhostdb.cursor()


site= "https://pastebin.com/raw/Bjsw46PD"
hdr = {'User-Agent': 'Mozilla/5.0'}
context = ssl._create_unverified_context()
req = Request(site, headers=hdr)
page = urlopen(req, context=context)
soup = BeautifulSoup(page,"html.parser")

medstr = {}
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

values = []
entity = []

index = 0
for element in medstr:
    if (index % 2) == 0:
        values.append(element)
    else:
        entity.append(element)
    index += 1

listToDict = {'index': values, 'names': entity}
print(json.dumps(listToDict))

activecursor.execute("insert into players values ('1','player')")

#
#attmpts at using odbc over mysql connector
#This will print the drivers installed with the py odbc install.
#for driver in pyodbc.drivers():
#    print(driver)
#
