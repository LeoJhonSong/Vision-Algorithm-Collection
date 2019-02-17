import cv2
import numpy as np
def redDetect(frame):
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    redLower = np.array([0, 43, 46])
    redUpper = np.array([10, 255, 255])
    pupLower = np.array([156, 43, 46])
    pupUpper = np.array([180, 255, 255])
    redMask = cv2.inRange(HSV, redLower, redUpper)
    pupMask = cv2.inRange(HSV, pupLower, pupUpper)
    Image = cv2.bitwise_and(frame, frame, mask=redMask)
    Image = cv2.bitwise_xor(frame, Image, mask=pupMask)
    Image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    return Image