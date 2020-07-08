import numpy as np
import cv2

cap = cv2.VideoCapture('http://192.168.14.126:4747/mjpegfeed')
fgbg = cv2.createBackgroundSubtractorMOG2()

"""
cv2.bgsegm.createBackgroundSubtractorGMG()
cv2.createBackgroundSubtractorMOG2()
cv2.bgsegm.createBackgroundSubtractorMOG(),
"""

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()