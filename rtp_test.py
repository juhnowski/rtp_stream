# import numpy as np
import cv2
import os

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "protocol_whitelist;file,rtp,udp"
cap = cv2.VideoCapture('test.sdp') #('film.mp4')  #('rtp://127.0.0.1:1234')

print("cap.isOpened()=", cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        cv2.imshow('frame', frame)
    else:
        print("FrameError - %s" % cap.isOpened())

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()