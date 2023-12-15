#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
 
input_img = cv2.imread("C:/Users/pc/Downloads/50000_bill.jpg")
img = cv2.resize(input_img, (640, 480))
# Make a copy to draw contour outline
input_image_cpy = img.copy()
 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
# define range of red color in HSV
lower_red = np.array([0, 10, 50])
upper_red = np.array([10, 255, 255])
 
# define range of green color in HSV
lower_green = np.array([25, 20, 50])
upper_green = np.array([90, 255, 255])
 
# define range of blue color in HSV
lower_blue = np.array([110, 20, 30])
upper_blue = np.array([130, 255, 255])

# # define range of yellow color
# lower_yellow = np.array([0, 80, 130])
# upper_yellow = np.array([80, 255, 255])
 
# create a mask for red colo1
mask_red = cv2.inRange(hsv, lower_red, upper_red)
 
# create a mask for green color
mask_green = cv2.inRange(hsv, lower_green, upper_green)
 
# create a mask for blue color
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

# # create a mask for yellow color
# mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
 
# find contours in the red mask
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
red_count = 0
 
# find contours in the green mask
contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
green_count = 0
 
# find contours in the blue mask
contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
blue_count = 0

# # find contours in the yellow mask
# contours_yellow,_ = cv2.findContours(mask_yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# yellow_count = 0
 
# loop through the red contours and draw a rectangle around them
for cnt in contours_red:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 7000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, 'Red', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        red_count+=1
     
# loop through the green contours and draw a rectangle around them
for cnt in contours_green:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 9000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, 'Green', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        green_count+=1
 
# loop through the blue contours and draw a rectangle around them
for cnt in contours_blue:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 9000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, 'Blue', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        blue_count+=1
        
# for cnt in contours_yellow:
#     contour_area = cv2.contourArea(cnt)
#     if contour_area > 9000:
#         x, y, w, h = cv2.boundingRect(cnt)
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#         cv2.putText(img, 'Yellow', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
#         yellow_count+=1
 
# # Display final output for multiple color detection opencv python
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

total_count = red_count*5000 + green_count*10000 + blue_count*1000
print(total_count)

