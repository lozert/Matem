from PIL import Image
import numpy as np

img = Image.open('snow.jpg')
img = img.convert('L') # серые

# img.show()

img1 = img.crop((100, 100, 250, 250)) # кропнутое изображени

zoom = 3
img2 = Image.new('L', (img1.width * zoom, img1.height * zoom), 'black')
np_img1 = np.asarray(img1, dtype=int)
np_img2 = np.asarray(img2, dtype=int)
np_img2[::zoom, ::zoom] = np_img1
Image.fromarray(np_img2.astype('uint8')).show()

for i in range(0, np_img2.shape[0] - zoom + 1, zoom):
    for j in range(0, np_img2.shape[1] - zoom, zoom):
        for x in range(1, zoom):
            np_img2[i][j+x] = np_img2[i][j] + ((np_img2[i][j+ zoom] - np_img2[i][j]) / (zoom)) * x 
           
       
for j in range(np_img2.shape[1]):
    for i in range(0, np_img2.shape[0]-zoom , zoom):
        for y in range(1, zoom):
            np_img2[i+y][j] = np_img2[i][j] + ((np_img2[i + zoom][j] - np_img2[i][j]) / (zoom)) * y
           

Image.fromarray(np_img2.astype('uint8')).show()