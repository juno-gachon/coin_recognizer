import cv2
import math
import numpy as np

src = cv2.imread("C:\os_tp\mix.jpg")
img = src.copy()

img = cv2.resize(img, (640, 480))

# Make a copy to draw contour outline
input_image_cpy = img.copy()
 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of gray color in HSV
lower_gray_500 = np.array([0, 0, 100])
upper_gray_500 = np.array([255, 255, 255])

# define range of silver color in HSV
lower_silver_100 = np.array([0, 0, 100])
upper_silver_100 = np.array([255, 255, 255])

# define range of brown color in HSV
lower_brown_50 = np.array([10, 10, 100])
upper_brown_50 = np.array([60, 255, 255])

# define range of copper color in HSV
lower_copper_10 = np.array([0, 20, 50])
upper_copper_10 = np.array([5, 255, 255])

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

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect circles
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1=250, param2=50, minRadius=10, maxRadius=100)

# Initialize count and value
count1, count2, count3, count4 = 0, 0, 0, 0
value1, value2, value3, value4 = 0, 0, 0, 0

for circle in circles[0]:
    x, y, r = int(circle[0]), int(circle[1]), int(circle[2])
    mask = cv2.circle(np.zeros((img.shape[0], img.shape[1], 1), dtype=np.uint8), (x, y), r, 255, -1)

    # Check color for each mask and accumulate counts
    if cv2.inRange(hsv, lower_gray_500, upper_gray_500).any() and cv2.bitwise_and(mask, mask, mask=mask).any():
        count1 += 1
        value1 = 500
    elif cv2.inRange(hsv, lower_silver_100, upper_silver_100).any() and cv2.bitwise_and(mask, mask, mask=mask).any():
        count2 += 1
        value2 = 100
    elif cv2.inRange(hsv, lower_brown_50, upper_brown_50).any() and cv2.bitwise_and(mask, mask, mask=mask).any():
        count3 += 1
        value3 = 50
    elif cv2.inRange(hsv, lower_copper_10, upper_copper_10).any() and cv2.bitwise_and(mask, mask, mask=mask).any():
        count4 += 1
        value4 = 10

    cv2.circle(img, (x, y), r, (255, 255, 255), 5)

    # Display coin information only if count is greater than 0
    cv2.putText(img, f'{value1} {value2} {value3} {value4}', (x, y), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 5)

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

total_count = red_count*5000 + green_count*10000 + blue_count*1000 + count1 * 500 + count2 * 100 + count3 * 50 + count4 * 10
print(total_count)
