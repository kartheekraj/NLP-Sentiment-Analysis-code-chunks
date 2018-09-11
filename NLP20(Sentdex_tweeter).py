from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="jvSv9azHxSIYjDnGVJcMFzAp9"
csecret="Pn8Fj7OqAiDJnTRoj0JOaOCzKVHrSdbkGpPmTzNmBsxEJ4SekQ"
atoken="1037997359517626368-CNQeRV28yt1ozEQLFpQGRLQriWiLyi"
asecret="X9A9gq9EC6MonYxCIt4wXNAwcVdZEDGnFpj5ZFuIAfRiw"


class listener(StreamListener):

    def on_data(self, data):

        all_data = json.loads(data)

        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet,sentiment_value, confidence)

        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Grand theft auto"])
