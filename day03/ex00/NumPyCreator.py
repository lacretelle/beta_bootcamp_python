import numpy as np

class NumPyCreator:
    def from_list(self, lst):
        return np.array(lst)

    def from_tuple(self, tpl):
        return np.array(tpl)

    def from_iterable(self, itr):
        return np.array(itr)

    def from_shape(self, shape, value=0):
        lst = []
        i = 0
        while i < shape[0]:
            tmp = []
            j = 0
            while j < shape[1]:
                tmp.append(value)
                j += 1
            lst.append(tmp)
            i += 1
        return np.array(lst)

    def random(self, shape):
        return (np.array(np.random.rand(shape[0], shape[1])))

    def identity(self, n):
        return (np.array(np.identity(n)))
