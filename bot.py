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



#this obtains the number of active weather alerts and stores is in number_of_alerts
item_dict = json.loads(alert_string)
number_of_alerts = len(item_dict['alerts'])
print ('The number of active weather alerts is %s' % (number_of_alerts))



#iterates through alert descriptions and stores in list
alert_description_list = []
for i in range(number_of_alerts):
    alert_description_list.append(parsed_alert_json['alerts'][i]['description'])
#print test for alert descriptions
print ("This is the alert description test string. description is %s" % (alert_description_list[0]))

#read in last 20 tweets
print (api.user_timeline())
mostrecenttweet = api.user_timeline()[1] #need to remove argument once there are 20 tweets in the account
print (mostrecenttweet.text)

#posts alert to twitter - if there are any active alerts

#---------------------------------------------------------------------------------------
#anything under this line is test code


#this test shows that the number in the middle brackets corresponds to the alerts
#so if there is more than 1 alert, this mumber can be used to iterate through them
# iterationtest = parsed_alert_json['alerts'][1]['type']
# print ("This is looking for the third alert, which has the type of %s" % (iterationtest))

#try not needed - block above can check for number of active alerts.
# try:
#     alert_type = parsed_alert_json['alerts'][0]['type']
#     alert_description = parsed_alert_json['alerts'][0]['description']
#     current_alert = ("The current alert type is %s and the description is %s" % (alert_type, alert_description))
#     print(current_alert)
#
#
#
#    #sample for loop to iterate through different alerts
#     for item in parsed_alert_json["alerts"]:
#         print (item ["type"])
#     alert.close
# except:
#     print("There are no active alerts")
#     alert.close



    #update status test
# status = current_weather
# api.update_status(status=status)

#prints out all tweets from timeline
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)