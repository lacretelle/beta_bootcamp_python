import numpy as np

class ScrapBooker:
    
    def crop(self, tab, dim, pos=(0,0)):
        new = tab[pos[0]:dim[0], pos[1]:dim[1]]
        return new

    def thin(self, tab, n, axis):
        if axis == 0:
            return tab[::n, :]
        else:
            return tab[:, ::n]

    def juxtapose(self, tab, n, axis):
        i = 0
        tmp = tab
        while i < n:
            tab = np.concatenate((tab, tmp), axis)
            i += 1
        return tab
