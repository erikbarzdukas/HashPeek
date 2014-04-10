from tweepy import StreamListener

class CustomStreamListener(StreamListener):
   
    #def on_data(self, data):
    #   print data
    #   return True

    def on_status(self, status):
       # print "[USER] %s\n" % status.user.screen_name
       # print "[TWEET] %s\n" % status.text
        
       # if status.coordinates is not None:
       #     lat = status.coordinates['coordinates'][1]
       #     lng = status.coordinates['coordinates'][0]
       #     print "[COORDINATES] %d x %d\n" % (lat, lng)
        print "[COORDINATES] %s\n" % status.coordinates  
        print "[PLACE] %s\n" % status.place
        print status.place.bounding_box
        return True

    def on_error(self, status):
        print "[ERROR] %s\n" % status
        return True

    def on_timeout(self):
        return True
