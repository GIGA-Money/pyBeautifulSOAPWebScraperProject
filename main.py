import ssl
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
import mysql.connector as mariadb


#
# This will format the string, by removing excess text that isn't used.
#


def text_format():
    f_string = str(soup)
    f_string = f_string.replace('has 1 vehicle Directives.\r\n', '')
    f_string = f_string.replace('has 2 vehicle Directives.\r\n', '')
    f_string = f_string.replace('has 3 vehicle Directives.\r\n', '')
    f_string = f_string.replace('has 4 vehicle Directives.\r\n', '')
    f_string = f_string.replace('has 5 vehicle Directives.\r\n', '')
    f_string = f_string.replace('has 6 vehicle Directives.\r\n', '')
    f_string = f_string.replace('has 7 vehicle Directives.\r\n', '')
    f_string = f_string.replace('has 8 vehicle Directives.\r\n', '')
    f_string = f_string.replace('#', '')
    f_string = f_string.split(' ')
    return f_string


#
# This method extracts the index from the name into 2 separate list.
#

def splint_string():
    index = 0
    for element in formattedString:
        if (index % 2) == 0:
            values.append(element)
        # print(element)
        else:
            entity.append(element)
        # print(element)
        index += 1


#
# This will insert the values into the database. Using the existing lists, values and entity.
#


def insertion():
    #
    # values (index, player name)
    #
    vdex = 0
    # for vdex in values:
    for edex in entity:
        activeCursor.execute("insert into players(ID, player_name) values(%s,%s)", (str(vdex), edex))
        print( '\t' + edex)
        vdex += 1


#
# All of the global variables used below.
#


site = "https://pastebin.com/raw/Bjsw46PD"
hdr = {'User-Agent': 'Mozilla/5.0'}
context = ssl._create_unverified_context()
req = Request(site, headers=hdr)
page = urlopen(req, context=context)
soup = BeautifulSoup(page, "html.parser")
formattedString = text_format()

values = []
entity = []

splint_string()

# Connect to the Mariadb.

localhost = mariadb.connect(
    host="localhost",
    port='3360',
    user="root",
    passwd="root",
    database="player_entry"
)
activeCursor = localhost.cursor()

try:
    activeCursor.execute("drop table if exists players")
    activeCursor.execute("create table if not exists players(ID varcharacter(15), "
                         "player_name varcharacter(255))")

    insertion()

except mariadb.Error as errors:
    print('errors: {}'.format(errors))
finally:
    localhost.commit()
    if activeCursor: activeCursor.close()
    if localhost: localhost.close()
