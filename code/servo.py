import RPi.GPIO as GPIO
import tweepy
import os
from time import sleep
from credentials import *
import sqlite3
from textblob import TextBlob
import time

GPIO.setmode(GPIO.BOARD)
servoPin=11
GPIO.setup(servoPin, GPIO.OUT)
pwm=GPIO.PWM(servoPin,50)
db = sqlite3.connect('database.db')
cursor = db.cursor()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
pwm.start(7)

for tweet in tweepy.Cursor(api.search, q="china").items():
    if (not tweet.retweeted) and ('RT @' not in tweet.text):
        try:
            print(tweet.user.screen_name)
            print((tweet.text).encode('utf-8').strip())
            user = tweet.user.screen_name
            tweet_text = tweet.text
            tweet_time = tweet.created_at
            blob = TextBlob(tweet.text)
            for sentence in blob.sentences:
                print(sentence.sentiment.polarity)
                cursor.execute('''INSERT INTO tweet(created_at, tweet_sentiment)
                        VALUES(?,?)''', (tweet_time, sentence.sentiment.polarity))
            db.commit()
            sleep(3)

            range_of_motion = (((sentence.sentiment.polarity + 1) * 180) / 2)
            DC=1./18.*(range_of_motion)+2
            pwm.ChangeDutyCycle(DC)

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

        sleep(3)

pwm.stop()
GPIO.cleanup()
