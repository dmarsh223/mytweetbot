from urllib.request import urlopen
from bs4 import BeautifulSoup


alert = urlopen("https://alerts.weather.gov/cap/wwaatmget.php?x=NJZ026&y=0")
alert_string = alert.read()

page = urlopen("https://alerts.weather.gov/cap/wwaatmget.php?x=NJZ026&y=0l")
soup = BeautifulSoup(page, "lxml")
print (soup.prettify())



summary = soup.summary.string[0]
print (summary)

summarytwo = soup.summary.string[1]
print (summarytwo)


#finds the summary elements and prints
secondtable = soup.findAll('summary')[0]

print (secondtable)
