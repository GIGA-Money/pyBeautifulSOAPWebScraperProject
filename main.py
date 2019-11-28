import ssl
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
import mysql.connector


def sprint_string():
    index = 0
    for element in formattedString:
        if (index % 2) == 0:
            values.append(element)
            print(element)
        else:
            entity.append(element)
            print(element)
        index += 1


def text_format():
    fString = str(soup)
    fString = fString.replace('has 1 vehicle Directives.\r\n', '')
    fString = fString.replace('has 2 vehicle Directives.\r\n', '')
    fString = fString.replace('has 3 vehicle Directives.\r\n', '')
    fString = fString.replace('has 4 vehicle Directives.\r\n', '')
    fString = fString.replace('has 5 vehicle Directives.\r\n', '')
    fString = fString.replace('has 6 vehicle Directives.\r\n', '')
    fString = fString.replace('has 7 vehicle Directives.\r\n', '')
    fString = fString.replace('has 8 vehicle Directives.\r\n', '')
    fString = fString.replace('#', '')
    fString = fString.split(' ')
    return fString

site = "https://pastebin.com/raw/Bjsw46PD"
hdr = {'User-Agent': 'Mozilla/5.0'}
context = ssl._create_unverified_context()
req = Request(site, headers=hdr)
page = urlopen(req, context=context)
soup = BeautifulSoup(page, "html.parser")
formattedString = text_format()

values = []
entity = []

sprint_string()

localhost = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="rooter",
        database="player_entry"
    )
activeCursor = localhost.cursor()

try:

    activeCursor.execute("create table if not exists players(ID varcharacter(15), "
                         "player_name varcharacter(255), primary key (ID))")
    #
    # values (index, player name)
    #

    for vdex in values:
        for edex in entity:
            activeCursor.execute("insert into player_entry.players values ('%s','%s')" % (vdex, edex))

except mysql.connector.Error as errors:
    print(errors)
finally:
    activeCursor.commit()
    if activeCursor: activeCursor.close()
    if localhost: localhost.close()
