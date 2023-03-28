import cv2
img = cv2.imread('lena.jpg')
img2 = cv2.cvtColor( img, cv2.COLOR_BGR2RGB)
b,g,r = cv2.split(img)
img2 = cv2.merge([r, g, b])#融合3个颜色通道生成新图片
