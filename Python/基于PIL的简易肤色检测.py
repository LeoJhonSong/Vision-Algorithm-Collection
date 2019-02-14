#!/usr/bin/env python
#-*- coding:utf-8 -*-
def SkinDetector(img1):
    '''
    Leo 2018.04.25

    from PIL import image

    以是否肤色二值化图像
    img1: RGB彩色图像类型
    img2: RGB彩色图像类型
    '''
    img2 = img1.convert('L')  #import PIL
    pix1 = img1.load()  #import PIL
    pix2 = img2.load() 
    
    for Y in range(0,height):
            for X in range(0,width):
                Red,Green,Blue = pix1[X,Y]
                if (Red >= 60 and Green >= 40 and Blue >= 20 and Red >= Blue and (Red - Green) >= 10 and max(max(Red, Green), Blue) - min(min(Red, Green), Blue) >= 10):
                    pix2[X,Y] = 0;  #肤色处为黑                                                                                                           
                else:
                    pix2[X,Y] = 255;
    return img2
