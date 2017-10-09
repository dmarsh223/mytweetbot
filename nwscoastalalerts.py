from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

# set variable for date and time for logs
currentdatetime = datetime.now()

# test URL
# page = urlopen("https://alerts.weather.gov/cap/wwaatmget.php?x=MSZ067&y=0")

# correct URL
page = urlopen("https://alerts.weather.gov/cap/wwaatmget.php?x=NJZ026&y=0l")

soup = BeautifulSoup(page, "lxml")
print (soup.prettify())

# checks for active alerts and ends program if there are no active alerts
firstTitleTag, secondTitleTag = soup.findAll("title")
titleCompare = secondTitleTag.string
if titleCompare == "There are no active watches, warnings or advisories":
    f = open('E:\logs\coastalnwsweatherlogs.txt', 'a')
    f.write('\n%s - No active alerts' % (currentdatetime))
    f.close()
    print("No active alerts - exiting program")
    exit()

# checks log file for current id from XML. If ID is present the program exits
# if ID is not present, it is written to the file and the program continues

firstIDTag, secondIDTag = soup.findAll('id')
uniqueID =  secondIDTag.string
print (uniqueID)

if uniqueID in open('E:\logs\coastalnwsweatherlogs.txt').read():
    f = open('E:\logs\coastalnwsweatherlogs.txt', 'a')
    f.write('\n%s - Duplicate alert found' % (currentdatetime))
    f.close()
    print("Duplicate alert found, exiting program.")
    exit()

# if the alert id is not found in the log file this adds the id to the
# log file and continues on

# need to create string of weather from this
# *
# *
# *
else:
    f = open('E:\logs\coastalnwsweatherlogs.txt', 'a')
    f.write('\n%s - New alert found at' % (currentdatetime))
    f.write ("\n%s" % (uniqueID))
    print ("New alert found - written to log")
    f.close()





