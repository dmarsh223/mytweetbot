import random
from io import BytesIO

import requests
import tweepy
import time
from PIL import Image
from PIL import ImageFile

from secrets import *



ImageFile.LOAD_TRUNCATED_IMAGES = True


# CONSUMER_KEY = 'Bw2Orl4Kb1lIYx1bxjc2dlJf5'
# CONSUMER_SECRET = 'fdaYresY3zFCusOi4j7AUMcp0KXMIAjXbXySRjz51YipbufXt4'
# ACCESS_TOKEN = '899423693453000704-r8N88iWYerA1oX1XP15RLQ6kUr3mAln'
# ACCESS_TOKEN_SECRET = 'G8IIfR70aaGhRGuZp9xeQMQEiKiYiostgp76IoX5EMN6d'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# status = "Testing!"
# api.update_status(status=status)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)