#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

URL_REQUEST_TOKEN   = 'http://blip.pl/oauth/request_token'
URL_ACCESS_TOKEN    = 'http://blip.pl/oauth/access_token'
URL_AUTHORIZE       = 'http://blip.pl/oauth/authorize'

CONSUMER_KEY        = ''
CONSUMER_SECRET     = ''

from oauth import oauth
import urllib
import sys
import os

with open (os.path.join (os.path.dirname (sys.argv[0]), 'app_data'), 'r') as fh:
    for line in fh:
        line = line.split ('=')
        globals()[line[0].strip()] = line[1]

consumer = oauth.OAuthConsumer (CONSUMER_KEY, CONSUMER_SECRET)
oauth_request = oauth.OAuthRequest.from_consumer_and_token (consumer, http_url=URL_REQUEST_TOKEN)
signature = oauth.OAuthSignatureMethod_HMAC_SHA1 ()
oauth_request.sign_request(signature, consumer, None)

print ('Connecting to: %s' % oauth_request.to_url ())
req = urllib2.Request (oauth_request.to_url ())

opener = urllib2.build_opener ()
data = opener.open (req)
resp = data.read ()
print (resp)

token = oauth.OAuthToken.from_string (resp)
print ('REQUEST TOKEN:', token)

oauth_request = oauth.OAuthRequest.from_token_and_callback (token = token, http_url = URL_AUTHORIZE)
print ("Visit this URL and accept access:\n%s\n" % oauth_request.to_url ())

print ("Now enter PIN code from blip.pl: ")
oauth_verifier = raw_input ()
oauth_request = oauth.OAuthRequest.from_consumer_and_token (consumer, token=token, verifier=oauth_verifier, http_url = URL_ACCESS_TOKEN)
oauth_request.sign_request (signature, consumer, token)

req = urllib2.Request (oauth_request.to_url ())
data = opener.open (req)
access_token = oauth.OAuthToken.from_string (data.read ())

print ("OAuath TOKEN: ", access_token)
print ("OAuath SECRET: ", access_token)

print ("Full response:\n", access_token)

