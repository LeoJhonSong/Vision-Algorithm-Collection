#!/usr/bin/env python
#-*- coding:utf-8 -*-
def SkinDetector(img1):
    '''
    2018.04.27 Leo

    import numpy as np
    binarization based on if is skin or not

    img1: 3D numpy array
    img2: 3D numpy array
    '''
    height, width, color = np.shape(img1)
    img2 = np.zeros((height, width, 1), np.uint8)  # 输出二值图
#    img2 = np.zeros((height, width, color), np.uint8)  # 输出彩色图
    for Y in range(0, width):
            for X in range(0, height):
                Red = int(img1[X, Y, 2])
                Green = int(img1[X, Y, 1])
                Blue = int(img1[X, Y, 0])
                if (Red >= 60 and Green >= 40 and Blue >= 20 and Red >= Blue and (Red - Green) >= 10 and max(max(Red, Green), Blue) - min(min(Red, Green), Blue) >= 10):
                    img2[X, Y] = 0  # 输出二值图，肤色处为黑
#                    img2[X, Y] = img1[X, Y]  # 输出彩色图，抠图效果
                else:
                    img2[X, Y] = 255
    return img2
