# Coin_recognizer


#### Basic information
distance from target : 20cm  
picture source : Galaxy S10+, zoom level 2  
version :
- Python 3.9.16
- cv2 4.7.0
- numpy 1.26.2


#### Team Memeber Introduction  
---
__We are team os81__
- 정준호 (Team Leader) / <https://github.com/juno-gachon> / Major in Computer Engineering
- 정수연 / <https://github.com/yeoxxy> / Major in English Literature&Language (Double Major in Software)
- 정준묵 / <https://github.com/Mooki2> / Major in Software
- 정호준 / <https://github.com/Hostoday> / Major in Software  


#### About Project
---
Discover the coins by detecting the circle in the image and classify them into 500won, 100won, 50won, and 10won according to the radius of the coin. Print the values of the coins the user has classified on top of the image so that the user knows how much the coins are, depending on their size. From the image of mixed bills and coins, the coins are sorted by extracting a circle. The bills are sorted together depending on their shape(rectangle) so that how much each bill is. <br></br>

#### Purpose of the development
---
To utilize technologies such as extracting raw materials from images learned through open-source SW lectures and to develop programs that can be used in practice through them <br></br>

#### Result
---
The results are pretty decent even though not perfect. There are limitations in recognition when coins are present alongside bills, so it's not flawless. However, ultimately, you can measure the amounts of bills and coins in the image, as shown in the photo.<br></br>

![coin_recognization result](https://github.com/juno-gachon/coin_recognizer/blob/master/image/coin_result.jpg)

![bill_recognization_result](https://github.com/juno-gachon/coin_recognizer/blob/master/image/bill_result.jpg)
<br></br>

#### The problem we were facing when we developed or what features we wanted to add later
---
Specifying the color range was difficult because each image's brightness was different. During development, 'color_detection' was designated according to the images we would mainly use. In actual use, we thought that modifications were needed so that the program could work well in other images. <br></br>

#### Run method
---
By default, this code is __python-based__ and must be installed in your environment when running (see basic information at the top of the _readme.md file_ for Python's version)

1. open command line or terminal
2. run file coin_recognizer.py with Python
3. If you want to use the program personally in addition to the image provided by 'coin_recognizer', modify the src part  
```src =  cv2.imread("Attach the image path that you want to detect or categorize")```

The program detects circular objects that exist in the image and classifies the coins using their radii. It calculates the sum of the value of the coins in the image. (For bills, it is classified using the color of the rectangle.)<br></br>

#### References
---
- <https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/>
- <https://pyimagesearch.com/2014/08/04/opencv-python-color-detection/>
- <https://github.com/tom9744/HCI_CoinCalculator>

