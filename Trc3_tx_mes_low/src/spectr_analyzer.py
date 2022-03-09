from math import sin, cos, pi
from prep_model import *

class spectr_analyzer(object):
    def __init__(self):
        """initialization"""
        self.WINDOW_SIZE = WINDOW_FFT
        self.BINS = bins
        self.SAMPLE_RATE = fs
        self._data = [0] * self.WINDOW_SIZE
        self.index = 0
        self.results = [0]*6
        self.freqs = [0]*6
        self.f_step_normalized = 1.0 / self.WINDOW_SIZE
        self.twopi = 2*pi
        self.count = 0
        self.fs = fs

    def fill_buf(self, sample: int) -> list:

        self._data[self.index] = sample
        self.index += 1

    def proc(self)->list:
        self.count+=1
        filt_signal = []
        for i in range (self.WINDOW_SIZE):
            multiplier = 0.5 * (1 - cos(self.twopi*i/self.WINDOW_SIZE))
            x = multiplier * self._data[i]
            filt_signal.append(x)

        n_range = range(0, self.WINDOW_SIZE)
        N = 0
        for k in self.BINS:
            # Bin frequency and coefficients for the computation
            f = k * self.f_step_normalized
            w_real = 2.0 * cos(self.twopi * f)
            w_imag = sin(self.twopi * f)
            # Doing the calculation on the whole sample
            d1, d2 = 0.0, 0.0
            for n in n_range:
                y = filt_signal[n] + w_real * d1 - d2
                d2, d1 = d1, y
            self.results[N] = int((d2*d2 + d1*d1 - w_real * d1 * d2)/300000)
            self.freqs[N] = int(f * fs)
            N+= 1

        self.index = 0
        return self.freqs, self.results

