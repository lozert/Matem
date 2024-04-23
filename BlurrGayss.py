

import numpy as np 
import matplotlib as mpl
import cv2
from matplotlib import pyplot as plt
import namefile 
import time 

start = time.time()

b = 1 # коэффициент фильтра
low_gayss_matrix = np.array([[0.00000067 , 0.00002292 , 0.00019117 , 0.00038771 , 0.00019117 , 0.00002292 , 0.00000067 ],
                            [0.00002292 , 0.00078633 , 0.00655965 , 0.01330373 , 0.00655965 , 0.00078633 , 0.00002292 ],
                            [0.00019117 , 0.00655965 , 0.05472157 , 0.11098164 , 0.05472157 , 0.00655965 , 0.00019117 ],
                            [0.00038771 , 0.01330373 , 0.11098164 , 0.22508352 , 0.11098164 , 0.01330373 , 0.00038771 ],
                            [0.00019117 , 0.00655965 , 0.00655965 , 0.11098164 , 0.05472157 , 0.00655965 , 0.00019117 ],
                            [0.00002292 , 0.00078633 , 0.00655965 , 0.01330373 , 0.00655965 , 0.00078633 , 0.00002292 ],
                            [0.00000067 , 0.00002292 , 0.00019117 , 0.00038771 , 0.00019117 , 0.00002292 , 0.00000067 ]])

img = cv2.imread(namefile.file)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype('float32') / 255 #  Создание тензора изображения

color_img = img.shape[2]
height_img = img.shape[0]
width_img = img.shape[1]
height_filter = low_gayss_matrix.shape[0]
width_filter = low_gayss_matrix.shape[1]

# Растяжение изображения для маски фильтра
new = np.zeros((height_img + int((width_filter+1) /2) , width_img + int((width_filter+1)/2) , color_img))
for i in range(color_img):
    new[ 1: -int(len(low_gayss_matrix)/2), 1: -int(len(low_gayss_matrix[0])/2), i] = img[:,:,i]


#Новое изобжраение
y = np.zeros((height_img, width_img, color_img))
count_color = 0

#теснение

# Свёртка матрицы 
while(count_color < color_img):
    for i in range(int(height_filter / 2), new.shape[0] - int(height_filter / 2)):
        for j in range(int(width_filter / 2), new.shape[1] - int(width_filter / 2)):
            
            small_matrix = np.zeros((height_filter, width_filter))
            small_matrix = new[i-int(height_filter / 2):i + int((height_filter+1) / 2),  j-int(width_filter/2):j+ int((width_filter+1)/2), count_color]

            y[i- int(height_filter/2)][j- int(width_filter/2)][count_color] = (b * small_matrix * low_gayss_matrix).sum()

    count_color += 1
      

end = time.time() - start
print(end)

plt.imshow(y)
plt.show()


# PIL_img = T.ToPILImage()(y)



# # print(pic.shape)
# # # convert this torch tensor to PIL image 
# # PIL_img = T.ToPILImage()(pic)

# # # display result
# PIL_img.show()