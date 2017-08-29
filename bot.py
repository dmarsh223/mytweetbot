import tweepy
import json
from urllib.request import urlopen

from secrets import *


#authenticate to twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


#gets weather from wunderground - under construction
f = urlopen(WUNDERGROUND_WEATHER)
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
current_weather = ("Current temperature in %s is: %s" % (location, temp_f))
print (current_weather)
f.close()


#checks for weather alerts
alert = urlopen(WUNDERGROUND_ALERTS)
alert_string = alert.read()
parsed_alert_json = json.loads(alert_string)
alert_type = parsed_alert_json['alerts'][0]['type']
alert_description = parsed_alert_json['alerts'][0]['description'] #needs to check for number of alerts and iterate until none
current_alert = ("The current alert type is %s and the description is %s" % (alert_type, alert_description))
print(current_alert)
alert.close

#update status test
# status = current_weather
# api.update_status(status=status)

#prints out all tweets from timeline
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)