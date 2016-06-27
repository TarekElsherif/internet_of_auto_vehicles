##import car_cam
import car_motor
import cv2
import sys
import time
from pubnub import Pubnub

pubnub = Pubnub(publish_key='pub-c-d1c59d19-6cf9-4dd9-a3ae-2811462c8506',
                    subscribe_key='sub-c-49f8db72-3b97-11e6-85a4-0619f8945a4f')
channel = 'test'
channel2 = 'v2v' 

img = cv2.imread('v.jpg') # load a dummy image

x = 0
y = 0
otherCarX = 0
otherCarY = 0

def _callback(m, channel):
    x = m['X2']
    y = m['Y2']
    print(x)
    print(y)

def _error(m):
    print(m)


def _callback2(m, channel):
    otherCarX = m['X']
    otherCarY = m['Y']
    print(otherCarX)
    print(otherCarY)			

pubnub.subscribe(channels=channel, callback=_callback, error=_error)
pubmub.subscribe(channels=channel2 , callback=_callback2, error=_error)


    

while(1):

    cv2.imshow('img',img)
    k = cv2.waitKey(33)
    if k==27: # Esc key to stop
        break
    elif k==ord('w'): # UP
        print 'foreward'
        car_motor.forward(0.001)
        continue
    elif k==ord('s'): # Down
        print 'reverse'
        car_motor.reverse(0.001)
        continue
    elif k==ord('a'): # Left
        print 'left'
        car_motor.turn_left(0.001)
        continue
    elif k==ord('d'): # Right
        print 'right'
        car_motor.turn_right(0.001)
        continue
    elif k==ord('q'): # Right
        
        print 'Exit'
        break
        continue
    else:
        car_motor.stop()
        
cv2.destroyAllWindows()
        

##        DownKey : 2621440 LeftKey : 2424832 RightKey: 2555904
            
