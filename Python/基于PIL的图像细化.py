#!/usr/bin/env python
#-*- coding:utf-8 -*-
def LeoThin(img):
    '''
    2018.04.24 Leo
    
    from PIL import Image
    
    a simple image thinning function
    img: a row image from the file
    img(return): same as above
    '''
    img = img.filter(ImageFilter.BLUR)
    for Y in range(0,height):
                for X in range(0,width):
                    pix = img.load()
                    Grey = pix[X,Y]
                    if (Grey>=50):
                        pix[X,Y]=255
                    if (Grey<50):
                        pix[X,Y] = pix[X,Y]*5                    
    img = img.filter(ImageFilter.BLUR)
    img = img.filter(ImageFilter.MaxFilter(11))
    for Y in range(0,height):
                for X in range(0,width):
                    pix = img.load()
                    Grey = pix[X,Y]
                    if (Grey<=30):
                        pix[X,Y] = 0                                                                                                  
                    else:
                        pix[X,Y] = 255
                        
    img = img.filter(ImageFilter.BLUR)
    for Y in range(0,height):
                for X in range(0,width):
                    pix = img.load()
                    Grey = pix[X,Y]
                    if (Grey>=50):
                        pix[X,Y]=255
                    if (Grey<50):
                        pix[X,Y] = pix[X,Y]*5                    
    img = img.filter(ImageFilter.MaxFilter(5))
    for Y in range(0,height):
                for X in range(0,width):
                    pix = img.load()
                    Grey = pix[X,Y]
                    if (Grey<=30):
                        pix[X,Y] = 0                                                                                                  
                    else:
                        pix[X,Y] = 255
                        
    img = img.filter(ImageFilter.BLUR)
    for Y in range(0,height):
                for X in range(0,width):
                    pix = img.load()
                    Grey = pix[X,Y]
                    if (Grey>=50):
                        pix[X,Y]=255
                    if (Grey<50):
                        pix[X,Y] = pix[X,Y]*5                   
    img = img.filter(ImageFilter.MaxFilter(3))
    for Y in range(0,height):
                for X in range(0,width):
                    pix = img.load()
                    Grey = pix[X,Y]
                    if (Grey<=30):
                        pix[X,Y] = 0                                                                                                  
                    else:
                        pix[X,Y] = 255               

    return img
