from prep_model import *

#---------------------------------------
class mean_filt(object):
    def __init__(self, length):
        """initialization"""
        self.sum = [0 for i in range(length)]
        self.length = length

    def proc(self, sample):
        """demodulation"""

        self.sum.insert(0, sample)
        self.sum.pop()

        y = (sum(self.sum))/self.length
        return y
