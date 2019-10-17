from ScrapBooker import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

sc = ScrapBooker()
img = mpimg.imread('./42AI.png')
#plt.imshow(img)
#plt.show()

img_crop = sc.crop(img, (50, 50), [40, 10])
plt.imshow(img_crop)
plt.show()
