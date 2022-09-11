from email import message
import re
import traceback
from urllib import response
import tweepy
import time
from stress_detection import isthisstress

# for @isdojastressed bot
api_key= "bdVYBNPuGcOlactp7ANxI2RIT"
api_secret= "KpqsPCSzk97ag2vQwRWHKwpnZz5m7X7j5zZmM32CZrEd3zTZzf"
bearer_token= "AAAAAAAAAAAAAAAAAAAAACTEgwEAAAAAMit4IJP8ZMSEpAyKJWt%2B72w5M7A%3DSstZiWa8YIm2BXP0xZkNxiGRPmb1JEcb9YAeY3HFbkPhw818Eg"
access_token="1568652190390034441-z4bsmwBuvQNw7OfnA4hNKpWyejp3Yd"
access_token_secret= "XtboFImw1HDGmgP8elPkN4rILpwDHIET2LjecxXDb8Y2s"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

#for old tweet version
auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# for @isdojastressed bot and @bish_dev account
doja_id = client.get_user(username="dojacat").data.id
bish_id = client.get_user(username="bish_dev").data.id
#stores the bots twitter account id
client_id = client.get_me().data.id

print("Bot is running...")

print(isthisstress("gay gay gay lol haha happy"))

reply = "message here"
currstr = ""
start_id =1

while True:
    
    tweets = client.get_users_tweets(id=doja_id)
    tweet = tweets.data[0]


    try:
        yourtweet = tweet.text
        print("They tweeted: "+yourtweet)
        verdict = isthisstress(yourtweet)  
        now = verdict[0]     
        print(now)
        if now == "Stress":
            reply = "Doja, you are stressed. Take a break."
        else:
            reply = "Doja, you are not stressed. Keep going!"

        client.create_tweet(in_reply_to_tweet_id=tweet.id, text=reply)
        #start_id=tweet[0].id
    except:
        pass  

    time.sleep(1.5)
    



#inherit from tweepy.StreamListener
class mystream(tweepy.StreamingClient):
    def on_connect(self):
        print("CONNECTED")

    #when tweet is received
    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            print(tweet.text)
            time.sleep(0.2)

    def on_errors(self, status):
        print('Error detected: ', status)


    

printer = mystream(bearer_token)
printer.add_rules(tweepy.StreamRule())
printer.filter(user_fields=bish_id)



