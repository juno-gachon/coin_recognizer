import cv2
import math

src = cv2.imread("image/coins.jpg")
img = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 250, param1 = 350, param2 = 30, minRadius=60, maxRadius = 120)

for circle in circles[0]:
  x, y, r = int(circle[0]), int(circle[1]), int(circle[2])
  cv2.circle(img, (x, y), r, (255, 255, 255), 5)
  cv2.putText(img, str(r), (x, y), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 5)

cv2.namedWindow("Detected Coins", cv2.WINDOW_NORMAL)
cv2.imshow("Detected Coins", img)
cv2.waitKey(0)
cv2.destroyAllWindows()