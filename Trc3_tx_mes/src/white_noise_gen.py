from math import sqrt
import random
from prep_model import *


#---------------------------------------
class white_noise(object):
    def __init__(self, A=0):
        """initialization"""
        self.ampl = A * 40

        if A == 0:
            return

        else:
            global inp_sig_buff
            noise_avg_watts = self.ampl
            mean_noise = 0
            noise_volts = np.random.normal(mean_noise,
             sqrt(noise_avg_watts), len(Time))

            inp_signal_buff = [
                a + b for a, b in zip(inp_sig_buff, noise_volts) ]
