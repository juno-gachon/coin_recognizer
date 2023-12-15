import cv2
import numpy as np

src = cv2.imread("image/bills.jpg")
img = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


## Detecting coins

# Detect circles
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 150, param1 = 350, param2 = 50, minRadius= 75, maxRadius = 150)


## Detecting Bills
## Detect contours within the range of HSV for each bills
## Then check if its size is big enough to be recognized as bill

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
contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_yellow,_ = cv2.findContours(mask_yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# amount of detected contours
red_count = 0
yellow_count = 0
green_count = 0
blue_count = 0


## Marking bills and coins, then calculate its value

## Marking bills + calculate value
# loop through the color contours and draw a rectangle around them
for cnt in contours_red:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 45000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, 'Red', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        red_count+=5000

for cnt in contours_green:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 45000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, 'Green', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        green_count+=10000

for cnt in contours_blue:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 45000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, 'Blue', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        blue_count+=1000

for cnt in contours_yellow:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 45000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(img, 'Yellow', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
        yellow_count+=50000


## Marking Coins + calculate value of coins by its radius
total_coin = 0

if circles is not None:
  for circle in circles[0]:
    x, y, r = int(circle[0]), int(circle[1]), int(circle[2])
    
    # draw circle around detected coins
    cv2.circle(img, (x, y), r, (255, 255, 255), 5)

    if r >= 130:
      value = 500
      total_coin += 500
    elif r >= 110:
      value = 100
      total_coin += 100
    elif r >= 100:
      value = 50
      total_coin += 50
    else:
      value = 10
      total_coin += 10

    # print coin value at detected coins.
    cv2.putText(img, str(value), (x-20, y+10), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 5)


## Print total values for each coins and bills

# print total amount of coins with yellow text in top left corner
cv2.putText(img, "total coins: "+str(total_coin)+"won", (10, 70), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 255), 5)

# print total amount of bills bellow coins
total_bill = blue_count + red_count + green_count + yellow_count
cv2.putText(img, "total bills: "+str(total_bill)+"won", (10, 140), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 255), 5)


cv2.namedWindow("Detected money", cv2.WINDOW_NORMAL)
cv2.imshow("Detected money", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
