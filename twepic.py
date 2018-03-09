import os
import time
import tweepy
CONSUMER_KEY = 'xxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxx'
ACCESS_KEY = 'xxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxx'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
b=1
a=0
while a<=1:
    img="/home/pi/RPR"+str(b)+".jpg"
    cmd="fswebcam -F 3 --fps 20 - 800x600 "+img
    os.system(cmd)
    print("pic has been taken")
    api.update_with_media(img, status= "gooooooood")
    print("wait for 5 seconds for selfie")
    time.sleep(5)
    a+=1
    b+=1
print("woooooow success")
