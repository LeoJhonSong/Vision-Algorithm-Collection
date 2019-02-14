#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 03:16:39 2018

@author: Leo
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #灰度化
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  #滤波
    ret, thresh1 = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV
                                 + cv2.THRESH_OTSU)  #二值化
#    n = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#   轮廓检测
    _, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE,
                                              cv2.CHAIN_APPROX_SIMPLE)
    drawing = np.zeros(img.shape, np.uint8)
#   取图像中最大轮廓
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    cnt = max(contour_sizes, key=lambda x: x[0])[1]

    hull = cv2.convexHull(cnt)
    moments = cv2.moments(cnt)  #求图像的矩
    if moments['m00'] != 0:
                cx = int(moments['m10']/moments['m00'])  #轮廓重心横坐标
                cy = int(moments['m01']/moments['m00'])  #轮廓重心纵坐标
    centr = (cx, cy)
    cv2.circle(img, centr, 5, [0, 0, 255], 2)
    cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 2)  #画最大轮廓
    cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 2)  #画凸包
#   凸包缺陷检测
    cnt = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    hull = cv2.convexHull(cnt, returnPoints=False)
    if(1):
        if type(cv2.convexityDefects(cnt, hull)) is type(None):
            break
        defects = cv2.convexityDefects(cnt, hull)
        mind = 0
        maxd = 0
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            dist = cv2.pointPolygonTest(cnt, centr, True)
            cv2.line(img, start, end, [0, 255, 0], 2)
            cv2.circle(img, far, 5, [0, 0, 255], -1)
        i = 0
    if type(cv2.convexityDefects(cnt, hull)) is type(None):
        continue

    cv2.imshow('output', drawing)
    cv2.imshow('input', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
