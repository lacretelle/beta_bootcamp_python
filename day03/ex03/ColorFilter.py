import numpy as np

class ColorFilter:
    def invert(self, tab):
        return np.invert(tab)

    def to_green(self, tab):

