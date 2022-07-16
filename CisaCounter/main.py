import numpy as np
import time
import cv2

#cap = cv.VideoCapture(0)
frame_counter = 0
cap = cv2.VideoCapture("https://www.salt.it/wp-content/uploads/webcam/a15/174.mp4")#?rand=5581")

if not cap.isOpened():
    print("Cannot open webcam stream")
    exit()

while True:
    
    ret, frame = cap.read() #cap.read() return the frame and a boolean (True/False) if a frame has returned or not
    
    if not ret:
        print("Can't receive frame (stream end?).")
        break
    else:
        frame_counter += 1
        if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            print("Frame Count: "+str(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
            frame_counter = 0 #Or whatever as long as it is the same as next line
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()
