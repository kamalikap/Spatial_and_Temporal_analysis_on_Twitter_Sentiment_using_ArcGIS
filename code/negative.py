import tweepy
from tweepy import Stream
from tweepy import StreamListener 
from tweepy import OAuthHandler
import json

consumer_key = "a0a9t8B2tGOn2WgbkA8t37300"
consumer_secret = "DGHfytheMIM3oThfU5st2W2FAtFb4xpQINtHAvvjDWwPIZuCkM"
access_token = "98661540-jMvt5t8umHCgM6mSVT5Py5Q4y7GuTQrIKDWj8xfZ2"
access_secret = "Qqtf5nYrxm7i4DlaXN74g1GlUP2hAUDuIOTTKkRZncB78"
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status
 
# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('mon_eightthirty_negative.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
#Set the hashtag to be searched
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['shame','doubt', 'envy','grief', 'fear','sadness', 'frustration','guilt','disgusted','failure','afraid', 'hate','pain','sick','overwhelmed','problem','stressed','boring','bottered','weird','greedy'])

