import tweepy
import json
from urllib.request import urlopen
from datetime import datetime
from secrets import *

# set variable for date and time for logs
currentdatetime = datetime.now()

#authenticate to twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#checks for weather alerts
alert = urlopen(ALERT_BEACH_HAVEN_WEST)
alert_string = alert.read()
parsed_alert_json = json.loads(alert_string)

# print out full json dump for validation testing
print (parsed_alert_json)

#this obtains the number of active weather alerts and stores is in number_of_alerts
item_dict = json.loads(alert_string)
number_of_alerts = len(item_dict['alerts'])
print ('The number of active weather alerts is %s' % (number_of_alerts))

# if there are no alerts - the program exits
if number_of_alerts == 0:
    f = open('E:\logs\havenwestweatherlogs.txt','a')
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
status_update = ("%s for Stafford Township expiring %s. Visit https://t.co/8jGoSkI7GG for"
                 " details." % (alert_description_list[0], alert_end_time[0]))


# accounting for multiple alerts - this is in progress
# if number_of_alerts == 1:
#     status_update = ("%s for Stafford Township expiring %s" % (alert_description_list[0], alert_end_time[0]))
# elif number_of_alerts == 2:
#     status_update = ("%s for Stafford Township expiring %s" % (alert_description_list[0], alert_end_time[0]))
# print (status_update)

print (status_update)

# read in last 20 tweets and compare to a string to see if tweet has been posted already
for i in range (20):
    mostrecenttweet = api.user_timeline()[i]
    current_tweet_to_compare = (mostrecenttweet.text)
    print(current_tweet_to_compare)

    # if the proposed new status equals any of the previous tweets - exit program
    if current_tweet_to_compare == status_update: # compares last tweets to current tweet to send out
        f = open('E:\logs\havenwestweatherlogs.txt', 'a')
        f.write('\n%s - duplicate alert found - no tweet sent out' % (currentdatetime))
        f.close()
        print ("This update was already sent out...exiting script")
        exit()

# update status
api.update_status(status=status_update)
f = open('E:\logs\havenwestweatherlogs.txt','a')
f.write('\n%s - twitter status updated to %s' % (currentdatetime, status_update))
f.close()
print ("Twitter status updated...exiting script")
alert.close
exit()
