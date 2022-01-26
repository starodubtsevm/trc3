from numpy import pi, cos, sin, sqrt
import const as c
from const import t, t2
from fir_filter import *
from iir_filter import *
from statistics import mean
"""
sync AM detector
"""


class s_am_det(object):

    def __init__(self, fc, fs):
        """initialization"""
        self.A = 1000
        self.omega_fc = 2 * pi * fc
        self.f_y_0 = fir(f_15)  # sync AM det channel 0
        self.f_y_90 = fir(f_15)  # sync AM det channel 90
        self.i = 0
        self.buff_ds_0 = [0 for i in range(41)]
        self.buff_ds_90 = [0 for i in range(41)]
        self.count = 0
        self.sum_0 = 0
        self.sum_90 = 0

    def mux(self, sample):
        """demodulator"""
        '''Локальный генератор cos и sin'''
        sin_sig = (self.A * sin(self.omega_fc * t[self.i]))
        cos_sig = (self.A * cos(self.omega_fc * t[self.i]))
        '''Умножение sample на cos и sin '''
        y_0 = (sample * sin_sig)
        y_90 = (sample * cos_sig)
        yy_0 = self.f_y_0.proc(y_0)
        yy_90 = self.f_y_90.proc(y_90)
        '''Понижение частоты дискретизации усреднением'''
        if self.count == 39:
            for i in range(39):
                self.sum_0 += self.buff_ds_0[i]
                self.sum_90 += self.buff_ds_90[i]
                self.sum_0 = self.sum_0 / 40
                self.sum_90 = self.sum_90 / 40

            self.buff_ds_0 = [0 for i in range(41)]
            self.buff_ds_90 = [0 for i in range(41)]
            self.count = 0
        else:
            self.buff_ds_0[self.count] = yy_0
            self.buff_ds_90[self.count] = yy_90
            self.count += 1
        self.i += 1

        return self.sum_0, self.sum_90

    def demod(self, yy_0, yy_90):
        '''Фильтрация (ФНЧ) в канале 0 и 90 градусов'''
        #yy_0  = self.f_y_0.proc(buff_0)
        #yy_90 = self.f_y_90.proc(buff_90)
        '''Возведение в квадрат в канале 0 и 90 градусов'''
        y_0_square = yy_0 * yy_0 / 32768
        y_90_square = yy_90 * yy_90 / 32768
        '''Извлечение квадратного корня (результат)'''
        res = y_0_square + y_90_square
        res = sqrt(res)

        return res
