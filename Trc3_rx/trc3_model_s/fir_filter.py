import sys
import numpy as np

sys.path.append('./FIR_models')
import time
import const as c
from FIR_8 import *
from FIR_12 import *
from FIR_14 import *
from FIR_600 import *


class fir(object):
    def __init__(self, h):
        """initialization"""

        self.index = 0
        self.h = np.array(h)
        self.size = len(self.h)
        self._data = np.array([0] * self.size)

    def proc(self, sample):
        """sample processed """

        if len(self._data) == self.size:
            self._data[self.index] = sample
        else:
            self._data.append(sample)
        self.index = (self.index + 1) % self.size
        acc = 0  # accumulator
        indx = self.index

        for j in range(self.size):
            acc+= self._data[indx]*self.h[j]
            if indx == ((self.size) - 1):
                indx = 0
            else:
                indx += 1
        return (int(acc) / 32768)  # result to 16 bit value
