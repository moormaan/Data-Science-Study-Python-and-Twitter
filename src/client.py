__author__ = 'moormaan'

import tweepy
from tweepy import OAuthHandler
import json

with open("private/oauth-config-bot.json", "r") as config:
    oauth_config = (json.loads(config.read()))
    consumer_key = oauth_config.get('consumer-key')
    consumer_secret = oauth_config.get('consumer-secret')
    access_token = oauth_config.get('access-token')
    access_token_secret = oauth_config.get('access-token-secret')
    
if __name__ == '__main__':
    oauth = OAuthHandler(consumer_key, consumer_secret)
    oauth.set_access_token(access_token, access_token_secret)
    
client = tweepy.API(oauth)
my_timeline = client.home_timeline()
for tweet in my_timeline:
    print(tweet)
    
for tweet in my_timeline:
    print(tweet.text)
    
