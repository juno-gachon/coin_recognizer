import cv2
import math
import numpy as np

src = cv2.imread("image/coins.jpg")
img = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Deteting circle for coins
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1 = 250, param2 = 50, minRadius= 75, maxRadius = 150)

# Detecting Bills
# define range of red(5000won) color in HSV
lower_red = np.array([0, 10, 50])
upper_red = np.array([10, 50, 191])

# define range of green(10000won) color in HSV
lower_green = np.array([25, 10, 72])
upper_green = np.array([102, 150, 255])

# define range of blue(1000won) color in HSV
lower_blue = np.array([110, 20, 30])
upper_blue = np.array([130, 255, 255])

# define range of yellow(50000won) color
lower_yellow = np.array([10, 80, 130])
upper_yellow = np.array([25, 255, 255])

# create a mask for colors
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

# find contours in the color mask
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
red_count = 0

contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
green_count = 0

contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
blue_count = 0

contours_yellow,_ = cv2.findContours(mask_yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
yellow_count = 0

# Marking bills and coins
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
        
for cnt in contours_yellow:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 9000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(img, 'Yellow', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
        yellow_count+=1

total = 0

for circle in circles[0]:
  x, y, r = int(circle[0]), int(circle[1]), int(circle[2])
  
  # draw circle around detected coins
  cv2.circle(img, (x, y), r, (255, 255, 255), 5)

  if r >= 120:
    value = 500
    total += 500
  elif r >= 110:
    value = 100
    total += 100
  elif r >= 100:
    value = 50
    total += 50
  else:
    value = 10
    total += 10

  # print coin value at detected coins.
  cv2.putText(img, str(value), (x-20, y+10), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 5)

# print total amount of money with yellow text in top left corner
cv2.putText(img, "total coins: "+str(total)+"won", (10, 70), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 255), 5)

cv2.namedWindow("Detected money", cv2.WINDOW_NORMAL)
cv2.imshow("Detected money", img)
cv2.waitKey(0)
cv2.destroyAllWindows()