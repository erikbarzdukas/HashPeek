"""
	Code connects to Twitter streaming api and pulls down tweets
	based on a user supplied filter, and then grabs available geolocation
	data. 

	Currently a shelved project because few tweets seem to have geolocation data.

"""

import tweepy
import datetime
import webbrowser
from streamListener import CustomStreamListener





#################################
#	Put in app token info	#
#################################
consumer_token =""
consumer_secret = ""
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print "[ERROR] Failed to get request token."

try:
    webbrowser.open_new_tab(redirect_url)
except:
    print "[ERROR] Couldn't open verification page in browser."
    print "[ *** ] Please visit %s to authorize Hash Peek to use your Twitter account." % redirect_url

verifier = raw_input("[ *** ] Verifier: ")

try:
    auth.get_access_token(verifier)
except:
    print "[ERROR] Failed to get access token."


#################################################
#	Bad file descriptor error here \/\/\	#
#################################################

try:
    with open('authTokens.txt', 'rw') as authFile:
        authFile.write("---------\n")
        authFile.write(str(datetime.datetime.now()) + "\n")
        authFile.write(str(auth.access_token.key) + "\n")
        authFile.write(str(auth.access_token.secret) + "\n")
        print "[OK] Wrote access token key and secret to file"

except Exception, e:
    print "[ERROR] Couldn't write to file, error: %s" % e
    print "[INFO] Authorized for this session, but not storing access token locally."



############################################
#   We are past the OAuth Dance,	   #
#   let's actually connect and listen.     #
############################################


searchQuery = raw_input("[???] Hashtag to search for: ")

print "\n"
print "-" * 15

l = CustomStreamListener()
stream = tweepy.Stream(auth, l)
stream.filter(track=[searchQuery])




#api = tweepy.API()
#tweets = api.public_timeline()

#for tweet in tweets:
#    print tweet
