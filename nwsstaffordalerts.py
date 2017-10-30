from urllib.request import urlopen
import tweepy
from bs4 import BeautifulSoup
from datetime import datetime
from secrets import *

# set variable for date and time for logs
currentdatetime = datetime.now()

#authenticate to twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# test URL
# page = urlopen("https://alerts.weather.gov/cap/wwaatmget.php?x=COC013&y=0")

# correct URL
page = urlopen("https://alerts.weather.gov/cap/wwaatmget.php?x=NJZ020&y=0")

soup = BeautifulSoup(page, "lxml")
print (soup.prettify())

# creates a list of the alert titles from the xml page
alert_descripton_list = []
for tag in soup.findAll('title'):
    alert_descripton_list.append(str((tag.contents)))

# checks for active alerts and ends program if there are no active alerts
secondTitle = alert_descripton_list[1].strip("[]'")
print (secondTitle)

if secondTitle == "There are no active watches, warnings or advisories":
    f = open('E:\logs\staffordnwsweatherlogs.txt', 'a')
    f.write('\n%s - No active alerts' % (currentdatetime))
    f.close()
    print("No active alerts - exiting program")
    exit()

# checks log file for current id from XML. If ID is present the program exits
# if ID is not present, it is written to the file and the program continues
id_descripton_list = []
for tag in soup.findAll('id'):
    id_descripton_list.append(str((tag.contents)))

uniqueID = id_descripton_list[1]

# test print
print (uniqueID)

if uniqueID in open('E:\logs\staffordnwsweatherlogs.txt').read():
    f = open('E:\logs\staffordnwsweatherlogs.txt', 'a')
    f.write('\n%s - Duplicate alert found' % (currentdatetime))
    f.close()
    print("Duplicate alert found, exiting program.")
    exit()

# if the alert id is not found in the log file this adds the id to the
# log file and continues on

else:
    f = open('E:\logs\staffordnwsweatherlogs.txt', 'a')
    f.write('\n%s - New alert found: %s' % (currentdatetime, secondTitle))
    f.write ("\n%s" % (uniqueID))
    print ("New alert found - written to log")
    status_update = ("Stafford Weather Alert: %s" % (secondTitle))
    api.update_status(status=status_update)
    f.close()
