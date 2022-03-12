import sys

sys.path.append('./FIR_models')
from FIR_8 import *
from FIR_12 import *
from FIR_14 import *
from FIR_600 import *


class fir(object):
    def __init__(self, h):
        """initialization"""

        self.index = 0
        self.Coeff = h
        self.size = len(self.Coeff)
        self._data = [0] * len(self.Coeff)

    def proc(self, sample: int)->int:
        """sample processed """

        if len(self._data) == self.size:
            self._data[self.index] = sample
        else:
            self._data.append(sample)
        self.index = (self.index + 1) % self.size
        acc = 0  # accumulator
        indx = self.index

        for coeff in self.Coeff:
            acc+= self._data[indx] * coeff
            if indx == self.size - 1:
                indx = 0
            else:
                indx += 1
        return int(acc) >> 15
