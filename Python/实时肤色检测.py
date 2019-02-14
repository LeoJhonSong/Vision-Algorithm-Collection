#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 03:16:39 2018

@author: Leo
"""
import numpy as np
import cv2

# 肤色检测
def SkinDetector(img1):
    height, width, color = np.shape(img1)
#    img2 = np.zeros((height, width,1), np.uint8)  # 输出二值图
    img2 = np.zeros((height, width, color), np.uint8)  # 输出彩色图
    for Y in range(0, width):
            for X in range(0, height):
                Red = int(img1[X, Y, 2])
                Green = int(img1[X, Y, 1])
                Blue = int(img1[X, Y, 0])
                if (Red >= 60 and Green >= 40 and Blue >= 20 and Red >= Blue and (Red - Green) >= 10 and max(max(Red, Green), Blue) - min(min(Red, Green), Blue) >= 10):
#                    img2[X,Y] = 0  # 对应二值图，肤色处为黑
                    img2[X, Y] = img1[X, Y]  # 对应彩色图，抠图效果
                else:
                    img2[X, Y] = 255
#                    img2[X, Y] = 0
    return img2


cap = cv2.VideoCapture(0)

while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    frame = SkinDetector(frame)
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) >= 0:
        break
    
cap.release()
cv2.destroyAllWindows()






