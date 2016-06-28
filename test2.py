##import car_cam
#import car_motor
#import cv2
import sys
import time
import main as follower
from pubnub import Pubnub

pubnub = Pubnub(publish_key='pub-c-d1c59d19-6cf9-4dd9-a3ae-2811462c8506',
                    subscribe_key='sub-c-49f8db72-3b97-11e6-85a4-0619f8945a4f')
channel = 'car2'
channel2 = 'v2v' 

#img = cv2.imread('v.jpg') # load a dummy image
stop= False
x1 = 0
y1 = 0
otherCarX = 0
otherCarY = 0


def _motion(otherCarX, x1):
  global stop
  stop= True
  diff= otherCarX - x1 - 56.0
  diff= diff*110.0/620.0
  speed=21.0 #21 cm per second
  time= 1.0*diff/speed
  follower.forward(time)
  follower.gpio.cleanup()
  stop= False


def _callback(m, channel):
   global stop
   global x1
   global y1
   print('yes')

   if not (stop): 
      x1 = m['X2']
      y1 = m['Y2']
      print(x)
      print(y)
    

def _error(m):
  print(m)


def _callback2(m, channel):
    global stop
    global x1
    global y1
    if not (stop):
      otherCarX = m['X']
      otherCarY = m['Y']
      if(otherCarX-x1>56):
         motion(otherCarX, x1)
      print(otherCarX)
      print(otherCarY)
    

pubnub.subscribe(channel, callback=_callback, error=_error)
pubnub.subscribe(channel2 , callback=_callback2, error=_error)

   


#if __name__ == '__main__': 
 #follower.init()
 #y=10
 #x=05

 #myX=0
# myY=0
# while(myX < x):

 #  follower.forward(0.5)
  # myX += 1
  # print str(myX)	


#follower.forward(1)
#follower.gpio.cleanup()       

#while(1):

 #   cv2.imshow('img',img)
  #  k = cv2.waitKey(33)
   # if k==27: # Esc key to stop
    #    break
   # elif k==ord('w'): # UP
    #    print 'foreward'
     #   car_motor.forward(0.001)
      #  continue
  #  elif k==ord('s'): # Down
    #    print 'reverse'
     #   car_motor.reverse(0.001)
      #  continue
   #  elif k==ord('a'): # Left
     #   print 'left'
      #  car_motor.turn_left(0.001)
      #  continue
   #  elif k==ord('d'): # Right
     #   print 'right'
      #  car_motor.turn_right(0.001)
      #  continue
   # elif k==ord('q'): # Right
        
    #    print 'Exit'
     #   break
  #      continue
 #   else:
#        car_motor.stop()
        
#cv2.destroyAllWindows()
        

##        DownKey : 2621440 LeftKey : 2424832 RightKey: 2555904
            
