import cv2

src = cv2.imread("image/coins.jpg")
img = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# detect coins by detecting circles
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1 = 250, param2 = 50, minRadius= 75, maxRadius = 150)

# total amount of coins
total = 0

for circle in circles[0]:
  x, y, r = int(circle[0]), int(circle[1]), int(circle[2])
  
  # draw circle around detected coins
  cv2.circle(img, (x, y), r, (255, 255, 255), 5)

  # distinguish coins by its radius
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
  cv2.putText(img, str(value), (x, y), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 5)

# print total amount of money with yellow text in top left corner
cv2.putText(img, "total: "+str(total)+"won", (10, 70), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 255), 5)


cv2.namedWindow("Detected Coins", cv2.WINDOW_NORMAL)
cv2.imshow("Detected Coins", img)
cv2.waitKey(0)
cv2.destroyAllWindows()