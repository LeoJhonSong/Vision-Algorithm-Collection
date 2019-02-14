#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ZhangSuen(image,times):
    '''
    2018.04.25 Leo
    
    import numpy as np
    import cv2
    
    Thinning the image by Zhang Suen Method
    image is np.array
    int times to control how thin it is
    '''
    array = [0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,\
             1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,\
             0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,\
             1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,\
             1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,\
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
             1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,1,\
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
             0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,\
             1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,\
             0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,\
             1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,\
             1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,\
             1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,\
             1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,0,\
             1,1,0,0,1,1,1,0,1,1,0,0,1,0,0,0]
    
    imgthin = np.zeros(image.shape,np.uint8)
    imgthin = image.copy()
    h,w = np.shape(imgthin)
    for i in range(times):
        
        # Vertically Thinning
        NEXT = 1
        for i in range(h):
            for j in range(w):
                if NEXT == 0:
                    NEXT = 1
                else:
                    M = (int(imgthin[i,j-1])+int(imgthin[i,j])+int(imgthin[i,j+1])) if 0<j<w-1 else 1
                    if imgthin[i,j] == 0  and M != 0:                  
                        a = [0]*9
                        for k in range(3):
                            for l in range(3):
                                if -1<(i-1+k)<h and -1<(j-1+l)<w and imgthin[i-1+k,j-1+l]==255:
                                    a[k*3+l] = 1
                        sum = a[0]*1+a[1]*2+a[2]*4+a[3]*8+a[5]*16+a[6]*32+a[7]*64+a[8]*128
                        imgthin[i,j] = array[sum]*255
                        if array[sum] == 1:
                            NEXT = 0
    
        # Horizontally Thinning
        NEXT = 1
        for j in range(w):
            for i in range(h):
                if NEXT == 0:
                    NEXT = 1
                else:
                    M = int(imgthin[i-1,j])+(imgthin[i,j])+(imgthin[i+1,j]) if 0<i<h-1 else 1   
                    if imgthin[i,j] == 0 and M != 0:                  
                        a = [0]*9
                        for k in range(3):
                            for l in range(3):
                                if -1<(i-1+k)<h and -1<(j-1+l)<w and imgthin[i-1+k,j-1+l]==255:
                                    a[k*3+l] = 1
                        sum = a[0]*1+a[1]*2+a[2]*4+a[3]*8+a[5]*16+a[6]*32+a[7]*64+a[8]*128
                        imgthin[i,j] = array[sum]*255
                        if array[sum] == 1:
                            NEXT = 0
    return imgthin
