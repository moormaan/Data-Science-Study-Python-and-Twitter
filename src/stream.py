__author__ = 'moormaan'

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

with open("private/oauth-config-bot.json", "r") as config:
    oauth_config = (json.loads(config.read()))
    consumer_key = oauth_config.get('consumer-key')
    consumer_secret = oauth_config.get('consumer-secret')
    access_token = oauth_config.get('access-token')
    access_token_secret = oauth_config.get('access-token-secret')
    
class Listener(StreamListener):
    def on_data(self, data):
        jsonData = json.loads(data)
        print(jsonData)
        
    def on_error(self, error):
        print('Error: ', error)
        
if __name__ == '__main__':
    oauth = OAuthHandler(consumer_key, consumer_secret)
    oauth.set_access_token(access_token, access_token_secret)
    
twitter_stream = Stream(oauth, StreamListener())
twitter_stream.filter(follow = ['moormaan'], track = ['#EU'], languages = ['en'])
