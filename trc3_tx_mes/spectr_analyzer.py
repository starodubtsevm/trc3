import math
import timeit
import numpy as np
import pylab
import const as c


class spectr_analyzer(object):
    def __init__(self):
        """initialization"""
        self.WINDOW_SIZE = 160
        self.BINS = {3,5,7,9,11,13}
        self.SAMPLE_RATE = c.fs
        self._data = [0] * self.WINDOW_SIZE
        self.index = self.WINDOW_SIZE
        self.results = [0]*6
        self.freqs = [0]*6
        self.f_step_normalized = 1.0 / self.WINDOW_SIZE

    def proc(self,sample):

        if self.index == 160:
            self._data.append(sample)
            self.index = 0

            filt_signal = []
            for i in range (self.WINDOW_SIZE):
                multiplier = 0.5 * (1 - np.cos(2*np.pi*i/self.WINDOW_SIZE))
                x = multiplier * sample
                filt_signal.append(x)

            # For all the bins, calculate the DFT term
            n_range = range(0, self.WINDOW_SIZE)
            N = 0
            for k in self.BINS:
                # Bin frequency and coefficients for the computation
                f = k * self.f_step_normalized
                w_real = 2.0 * math.cos(2.0 * math.pi * f)
                w_imag = math.sin(2.0 * math.pi * f)
                # Doing the calculation on the whole sample
                d1, d2 = 0.0, 0.0
                for n in n_range:
                    y  = self._data[n] + w_real * d1 - d2
                    d2, d1 = d1, y
                    # Storing results `(real part, imag part, power)`
                self.results[N] = int((d2**2 + d1**2 - w_real * d1 * d2)/1000000)
                self.freqs[N] = int(f * c.fs)
                N+=1

            return self.freqs, self.results

        else:
            self._data[self.index] = sample
            self.index += 1

            return self.freqs, self.results
