# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:15:53 2020

@author: Nilesh
"""

import cv2
import numpy as np
from pairing import pair, depair

drawing = False # true if mouse is pressed
mode = False # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
text = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z','A','B', 'C' ,'D', 'E', 'F', 'G' ,'H' ,'I' ,'K', 'L', 'M' ,'N' ,'O',
        'P' ,'Q', 'R', 'S', 'T','U' ,'V','W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
diff_nums = ['1','2','5','9']

countkeep = {}
for i in numbers:
    countkeep[i] = 0
    
data = open('test.txt','a')
    
font = cv2.FONT_HERSHEY_SIMPLEX

label = '0'
mousemovement = []
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        
        #num = pair(x,y)
        num = (x,y)
        mousemovement.append(num)
        

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),2,(255),-1)
            #num = pair(x,y)
            num = (x,y)
            mousemovement.append(num)
                

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img,(x,y),2,(255),-1)
        #num = pair(x,y)
        num = (x,y)
        mousemovement.append(num)
        

img = np.zeros((512,512,1), np.uint8)
nimg = np.zeros((512,512,1), np.uint8)
timg = np.zeros((512,512,1), np.uint8)
cv2.namedWindow('image')
cv2.namedWindow('timg')

cv2.setMouseCallback('image',draw_circle)

cv2.namedWindow('dupimage')
nimg = np.zeros((512,512,1), np.uint8)
img = np.zeros((512,512,1), np.uint8)
timg = np.zeros((512,512,1), np.uint8)
label = np.random.choice(diff_nums)
cv2.putText(nimg,label,(256,256), font, 6,(255),2,cv2.LINE_AA)

while(1):
    cv2.imshow('image',img)
    cv2.imshow('dupimage',nimg)
    cv2.imshow('timg',timg)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        if(len(mousemovement)):
            stringtowrite = str(label) + "," + str(mousemovement) + "\n"
            data.write(stringtowrite)
        nimg = np.zeros((512,512,1), np.uint8)
        img = np.zeros((512,512,1), np.uint8)
        timg = np.zeros((512,512,1), np.uint8)
        label = np.random.choice(diff_nums)
        nums = mousemovement
        print(nums)
        lenth = len(nums)
        '''
        if lenth < 100:
            nums = nums + [0]*(100-lenth)
            
        else:
            newlist = []
            n = lenth % 100
            if n >= 50:
                nums = nums + [0]*(100-n)
            indices = np.arange(0,lenth,lenth/100)
            indices = list(np.around(indices).astype(np.uint8))
            for i in indices:
                if len(newlist)<100:
                    newlist.append(nums[i])
            nums = newlist
        '''
        print(nums)
        for num in nums:
            #tup = depair(num)
            tup = num
            cv2.circle(timg,tup,2,(255),-1)
            
        cv2.putText(nimg,label,(256,256), font, 6,(255),2,cv2.LINE_AA)
        
        mousemovement = []
        
    elif k == 27:
        break
    
data.close()
cv2.destroyAllWindows()