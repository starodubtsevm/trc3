import numpy as np
import random
import const as c


#---------------------------------------
class white_noise(object):
    def __init__(self, A=0):
        """initialization"""
        self.ampl = A * 40

        if A == 0:
            return

        else:
            noise_avg_watts = self.ampl
            mean_noise = 0
            noise_volts = np.random.normal(mean_noise,
                                           np.sqrt(noise_avg_watts), len(c.t))
            c.inp_signal_buff = [
                a + b for a, b in zip(c.inp_signal_buff, noise_volts)
            ]
