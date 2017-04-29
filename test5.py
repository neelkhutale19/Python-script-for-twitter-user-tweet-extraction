#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv

#reference http://www.tweepy.org/
import tweepy

#Twitter API Credentials

consumer_key = ""
consumer_secret = ""
access_key = "-"
access_secret = ""

#method used to retrive user 100 tweets at a time
def get_tweets(username):


	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#set count to however many tweets you want; twitter only allows 200 at a time
	number_of_tweets = 200


	tweets = api.user_timeline(screen_name = username,count = number_of_tweets)


	tweets_for_csv = [[username,tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]


	print ("writing to {0}_tweets.csv".format(username))
	with open("{0}_tweets.csv".format(username) , 'w+') as file:
		writer = csv.writer(file, delimiter='|')
		writer.writerows(tweets_for_csv)



if __name__ == '__main__':


    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
    else:
        print ("Error: enter one username")
