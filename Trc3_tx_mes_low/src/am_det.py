from math import cos, sin, sqrt
from prep_model import *
from fir_filter import *

"""
set of AM detectors
"""

class am_det_coherent(object):
    "coherent AM dector"

    def __init__(self, f_c):
        """initialization"""
        self.A = 10000
        self.BUFF = 40
        self.omega_fc = 6.28 * f_c
        self.f_y_0 = fir(f_14)  # sync AM det channel 0
        self.f_y_90 = fir(f_14)  # sync AM det channel 90
        self.buff_ds_0 = [0 for i in range(self.BUFF)]
        self.buff_ds_90 = [0 for i in range(self.BUFF)]
        self.tick = 0
        self.count = 0
        self.sum_0 = 0
        self.sum_90 = 0

    def mux(self, sample):
        """demodulator"""
        '''Локальный генератор cos и sin'''
        sin_sig = (self.A * sin(self.omega_fc * Time[self.tick]))
        cos_sig = (self.A * cos(self.omega_fc * Time[self.tick]))
        '''Умножение sample на cos и sin '''
        y_0 = sample * sin_sig
        y_90 = sample * cos_sig
        yy_0 = self.f_y_0.proc(y_0)
        yy_90 = self.f_y_90.proc(y_90)
        '''Понижение частоты дискретизации усреднением'''
        if self.count == self.BUFF - 1:
            for i in range(self.BUFF - 1):
                self.sum_0 += self.buff_ds_0[i]
                self.sum_90 += self.buff_ds_90[i]
                self.sum_0 = self.sum_0 / self.BUFF
                self.sum_90 = self.sum_90 / self.BUFF
            self.buff_ds_0 = [0 for i in range(self.BUFF)]
            self.buff_ds_90 = [0 for i in range(self.BUFF)]
            self.count = 0
        else:
            self.buff_ds_0[self.count] = yy_0
            self.buff_ds_90[self.count] = yy_90
            self.count += 1
        self.tick += 1

        return self.sum_0, self.sum_90

    def demod(self, yy_0, yy_90):
        '''Возведение в квадрат в канале 0 и 90 градусов'''
        y_0_square = int(yy_0 * yy_0) >> 15
        y_90_square = int(yy_90 * yy_90) >> 15
        '''Извлечение квадратного корня (результат)'''

        return sqrt (y_0_square + y_90_square)

#---------------------------------------
class am_det_env(object):
    "envelop AM detector"

    def __init__(self):
        """initialization"""

    def proc(self, sample):
        """demodulation"""

        return abs(sample)
