import cv2

src = cv2.imread("image/coins.jpg")
img = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 원 검출을 통한 동전 탐색
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1 = 250, param2 = 50, minRadius= 75, maxRadius = 150)

for circle in circles[0]:
  x, y, r = int(circle[0]), int(circle[1]), int(circle[2])
  cv2.circle(img, (x, y), r, (255, 255, 255), 5)

# radius에 따른 동전 분류
  if r >= 120:
    value = 500
  elif r >= 110:
    value = 100
  elif r >= 100:
    value = 50
  else:
    value = 10

  # 사진 위에 동전 값 출력
  cv2.putText(img, str(value), (x, y), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 5)

cv2.namedWindow("Detected Coins", cv2.WINDOW_NORMAL)
cv2.imshow("Detected Coins", img)
cv2.waitKey(0)
cv2.destroyAllWindows()