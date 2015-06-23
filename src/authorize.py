import tweepy
import json
from tweepy import AppAuthHandler 
from tweepy import OAuthHandler

with open("private/oauth-config.json", "r") as config:
        oauth_config = (json.loads(config.read()))
        consumer_key = oauth_config.get('consumer-key')
        consumer_secret = oauth_config.get('consumer-secret')

oauth = OAuthHandler(consumer_key, consumer_secret)

try:
    redirect_url = oauth.get_authorization_url()
except tweepy.TweepError:
    print('Error: failed to get the redirect URL.')

access_token = oauth.get_access_token(verifier='enter pin here')

