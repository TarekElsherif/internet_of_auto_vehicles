# import the necessary packages
import argparse
import datetime
import imutils
import time
import cv2
import numpy as np
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())
 
### if the video argument is None, then we are reading from webcam
if args.get("video", None) is None:
    camera = cv2.VideoCapture(0)
    time.sleep(0.25)
 
# otherwise, we are reading from a video file
else:
    camera = cv2.VideoCapture(args["video"])

##alpha = float(input('* Enter the alpha value [1.0-3.0]: '))     # Simple contrast control
##beta = int(input('Enter the beta value [0-100]: '))

def perform():

    global alpha
    global beta
    
    # define the list of boundaries
    boundaries = [
	([0, 0, 150],[100, 100, 255]),  #red
##        ([0, 100, 0],[150, 255, 150])
##	([100, 0, 0], [255, 100, 100]),   #blue
##	([25, 146 ,190], [62, 174, 250]), #yellow
##	( [103, 86, 65],[145, 133, 128])  #gray
        
    ]
    
    # loop over the frames of the video
    while True:
        # grab the current frame and initialize the occupied/unoccupied
        # text
        (grabbed, frame) = camera.read()
        (grabbed, frame) = camera.read()
        (grabbed, frame) = camera.read()

        # if the frame could not be grabbed, then we have reached the end
        # of the video
        if not grabbed:
            print  'Camera failed.'
            break
        # Test comment
##        frame = cv2.multiply(frame,np.array([alpha])) 
##        frame = cv2.add(frame,np.array([beta]))

##        img_yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
##
##        # equalize the histogram of the Y channel
##        img_yuv[:,:,0] = cv2.equalizeHist(frame[:,:,0])
##
##        # convert the YUV image back to RGB format
##        frame = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
##
##        frame = imutils.resize(frame, width=500)
        
        
        # loop over the boundaries
        for (lower, upper) in boundaries:
            # create NumPy arrays from the boundaries
            lower = np.array(lower, dtype = "uint8")
            upper = np.array(upper, dtype = "uint8")
            # find the colors within the specified boundaries and apply
            # the mask
            mask = cv2.inRange(frame, lower, upper)
            output = cv2.bitwise_and(frame, frame, mask = mask)

        gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)[1]
        (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)

        # loop over the contours
        for c in cnts:
            
            # if the contour is too small, ignore it
            if cv2.contourArea(c) < 100:
                continue
            
            # compute the bounding box for the contour, draw it on the frame,
            # and update the text
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "x: {}".format(x + (w/2)), (10, 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            cv2.putText(frame, "y: {}".format(y + (h/2)), (10, 40
                                                           ),
            cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            break
        
        cv2.imshow("Feed", np.hstack([frame, output]))
        cv2.imshow("Thresh", thresh)
       # show the frame and record if the user presses a key
        key = cv2.waitKey(1) & 0xFF
         
        # if the `q` key is pressed, break from the loop
        if key == ord("q"):
            break

        # cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    perform()
