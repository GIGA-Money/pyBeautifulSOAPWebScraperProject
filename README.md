# pyBeautifulSOAPWebScraperProject
A course project to build a web scraper for a database. The objective is to create a web scraper with py beautiful soap and to use the extracted data as inserts into a local MySQL Database.
https://github.com/GIGA-Money/pyBeautifulSOUPWebScraperProject
use develop2 branch to view my material.

*log: 11/17/19 The current state still does not connect to a DB correctly, the mysqlLb solution to connect to the localhost db did not want to work on windows.
*Current state just gets the data from the link, and moves the data into a json file

*LOG: 11/18/19 was able to connect using the mysql connector, followed YT link at ```https://www.youtube.com/watch?v=3vsC05rxZ8c```
    *The link shows how to install and connect the the locally hosted mysql db.
    *The current state allows me to connect and perform table creations, and table drops. 
    *however alterations and insertions are not completing as intended
    *looking into what it takes to do an insert.
   
#install notes:
	*if pip install does not cooperate while in pycharm do the following:
		*(assuming project is still a pycharm project for this instruction set)
		*go to the virtual enviroment folder (either in cmd/powershell or file explore)
		*go to the scrips folder
		*should be here: project1\venv\Scripts
		*with cmd/powershell open, we can run the pip from here.
			* powershell [tab] to .\pip this opens the pip cmd app.
		*now we can run the pip commands as intended
		*in this case ```install mysql-connector-python```
		*this should install for THIS project, not nessesarly for the local install of python.

 
   

