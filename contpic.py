import os
import time
a=0
b=1
while(a<5):
    time.sleep(8)
    os.system("fswebcam -F 4 --fps 20 -r 1280x720 /home/pi/"+str(b)+"8.jpg")
    print("pic taken")
    a+=1
    b+=1
