import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ImageProcessor:
    def load(self, path):
        img = mpimg.imread(path)
        size = img.shape
        print ("Loading image of dimensions {} x {}".format(size[0], size[1]))
        return img

    def display(self, array):
        plt.imshow(array)
        plt.show()
        return
