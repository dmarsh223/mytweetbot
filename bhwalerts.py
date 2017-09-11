import tweepy
import json
from urllib.request import urlopen
from datetime import datetime

from secrets import *
#authenticate to twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#checks for weather alerts
alert = urlopen(ALERT_BEACH_HAVEN_WEST)
alert_string = alert.read()
parsed_alert_json = json.loads(alert_string)
