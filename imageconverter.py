from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
from urllib.request import urlopen
import tweepy
from bs4 import BeautifulSoup
from secrets import *


#authenticate to twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# test URL - uncomment next line to test
page = urlopen("https://alerts.weather.gov/cap/wwaatmget.php?x=NJZ007&y=0")

# correct URL
# page = urlopen("https://alerts.weather.gov/cap/wwaatmget.php?x=NJZ020&y=0")

soup = BeautifulSoup(page, "lxml")
# print (soup.prettify())


# creates list of alert summaries from xml page
alert_summary_list = []
for tag in soup.findAll('summary'):
    alert_summary_list.append(str((tag.contents)))

firstSummary = alert_summary_list[0].strip("[]'")
print (firstSummary)

img = Image.open("blank_slate.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("arial.ttf", 48)
# draw.text((x, y),"Sample Text",(r,g,b))
#try to keep limit to 40 characters per line
# draw.text((0, 50),"12345678901234567890123456789012345678901234567890",(0,0,0),font=font)

text =(firstSummary)

margin = 40
offset = 150
for line in textwrap.wrap(text, width=46):
    draw.text((margin, offset), line, font=font, fill="#aa0000")
    offset += font.getsize(line)[1]

    img.save('sample-out.jpg')


    #https://stackoverflow.com/questions/16373425/add-text-on-image-using-pil