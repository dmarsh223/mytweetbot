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
alert = urlopen(WUNDERGROUND_ALERTS)
alert_string = alert.read()
parsed_alert_json = json.loads(alert_string)


#this obtains the number of active weather alerts and stores is in number_of_alerts
item_dict = json.loads(alert_string)
number_of_alerts = len(item_dict['alerts'])
print ('The number of active weather alerts is %s' % (number_of_alerts))

# set variable for date and time for logs
currentdatetime = datetime.now()

# if there are no alerts - the program exits
if number_of_alerts == 0:
    f = open('weatherlogs.txt','a')
    f.write('\n%s - there are no active alerts' % (currentdatetime) )
    f.close()
    print("There are no active alerts - exiting script now")
    exit()


# iterates through alert descriptions and end times and stores in list
alert_description_list = []
alert_end_time = []
for i in range(number_of_alerts):
    alert_description_list.append(parsed_alert_json['alerts'][i]['description'])
    alert_end_time.append(parsed_alert_json['alerts'][i]['date'])


# this is the status update that will be compared to previous tweets and eventually tweeted
status_update = ("%s for Stafford Township expiring %s" % (alert_description_list[0], alert_end_time[0]))


# accounting for multiple alerts - this is in progress
# if number_of_alerts == 1:
#     status_update = ("%s for Stafford Township expiring %s" % (alert_description_list[0], alert_end_time[0]))
# elif number_of_alerts == 2:
#     status_update = ("%s for Stafford Township expiring %s" % (alert_description_list[0], alert_end_time[0]))
# print (status_update)


# read in last 20 tweets and compare to a string to see if tweet has been posted already
for i in range (20):
    mostrecenttweet = api.user_timeline()[i]
    current_tweet_to_compare = (mostrecenttweet.text)
    # if the proposed new status equals any of the previous tweets - exit program
    if current_tweet_to_compare == status_update: # compares last tweets to current tweet to send out
        f = open('weatherlogs.txt', 'a')
        f.write('\n%s - duplicate alert found - no tweet sent out' % (currentdatetime))
        f.close()
        print ("This update was already sent out...exiting script")
        exit()

# update status
api.update_status(status=status_update)
f = open('weatherlogs.txt', 'a')
f.write('\n%s - twitter status updated to %s' % (currentdatetime, status_update))
f.close()
print ("Twitter status updated...exiting script")
alert.close
exit()

# posts alert to twitter - if there are any active alerts

# ---------------------------------------------------------------------------------------
# anything under this line is test code


# this test shows that the number in the middle brackets corresponds to the alerts
# so if there is more than 1 alert, this mumber can be used to iterate through them
# iterationtest = parsed_alert_json['alerts'][1]['type']
# print ("This is looking for the third alert, which has the type of %s" % (iterationtest))

# try not needed - block above can check for number of active alerts.
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



# update status test
# status = current_weather
# api.update_status(status=status)

# prints out all tweets from timeline
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


# #gets weather from wunderground - under construction
# f = urlopen(WUNDERGROUND_WEATHER)
# json_string = f.read()
# parsed_json = json.loads(json_string)
# location = parsed_json['location']['city']
# temp_f = parsed_json['current_observation']['temp_f']
# current_weather = ("Current temperature in %s is: %s" % (location, temp_f))
# print (current_weather)
# f.close