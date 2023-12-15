# Coin_recognizer
<p align="center">
  <img src="C:\Users\User\OneDrive\바탕 화면\공부 자료\대학\2023\2023-2\오픈소스SW\coin_recognizer\image\coin_result.jpg">
</p>

![coin_recognization result](https://github.com/juno-gachon/coin_recognizer/blob/master/image/coin_result.jpg)

![bill_recognization_result](https://github.com/juno-gachon/coin-recognizer/blob/master/image/bill_result.jpg)


#### Basic information
distance from target : 20cm  
picture source : Galaxy S10+, zoom level 2  
version :
- Python 3.9.16
- cv2 4.7.0

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

#### The problem we were facing when we developed or what features we wanted to add later
---
Specifying the color range was difficult because each image's brightness was different. During development, 'color_detection' was designated according to the images we would mainly use. In actual use, we thought that modifications were needed so that the program could work well in other images. <br></br>
