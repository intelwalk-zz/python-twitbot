#! /usr/bin/python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'RhxRePg5AQ5IQuZVrp1K0qPYy'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '34UIfOGkDUPFNZ5iZ5TNLductgeWdLIwJVLDMEqXChy6YkQUqr'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1060886011-2qfymADaxFoY1l7te2XDJS9wuM2VKucpbzCiJJT'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'DEGT2saSgxQqXQJuPlVpbwtZYvaIffFZck2FXUqXjoigb'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(status=line)
    time.sleep(180)#Tweet every 15 minutes