import numpy as np
import random
import const as c


#---------------------------------------
class white_noise(object):

    def __init__(self, A=0):
        """initialization"""
        self.ampl = A

        if A == 0: return
        _data = [self.ampl*np.random.randn()\
        for i in range (len(c.t))]

        c.inp_signal_buff = [a + b for a, b in zip(c.inp_signal_buff, _data)]
        del _data
