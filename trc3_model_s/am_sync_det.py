from numpy import pi, cos, sin, sqrt
import const as c
from const import t, t2
from fir_filter import*

"""
sync AM detector
"""
class s_am_det(object):
    def __init__(self, fc, fs):
        """initialization"""
        self.A = 5000
        self.omega_fc = 2*pi*fc
        self.i = 0
        self.lpf_y_0  = fir(f_10) # sync AM det channel 0
        self.lpf_y_90 = fir(f_10) # sync AM det channel 90

    def proc(self,sample):
        """demodulator"""
        
        '''Локальный генератор cos и sin'''
        sin_sig = self.A*sin(self.omega_fc*t[self.i])
        cos_sig = self.A*cos(self.omega_fc*t[self.i])

        '''Умножение sample на cos и sin '''
        y_0  = (sample * sin_sig) / 16384
        y_90 = (sample * cos_sig) / 16384

        '''Фильтрация (ФНЧ) в канале 0 и 90 градусов'''
        yy_0  = self.lpf_y_0.proc(y_0)
        yy_90 = self.lpf_y_90.proc(y_90)

        '''Возведение в квадрат в канале 0 и 90 градусов'''
        y_0_square =   yy_0 * yy_0
        y_90_square =  yy_90 * yy_90

        '''Извлечение квадратного корня (результат)'''
        res = sqrt (y_0_square + y_90_square)

        self.i+=1

        return res


class s_am_det3(object):
    def __init__(self, fc, fs):
        """initialization"""
        self.A = 500
        self.omega_fc = 2*pi*fc
        self.i = 0
        self.lpf_y_0  = fir(f_5) # sync AM det channel 0
        self.lpf_y_90 = fir(f_5) # sync AM det channel 90

    def proc(self,sample):
        """demodulator"""
        
        '''Локальный генератор cos и sin'''
        sin_sig = self.A*sin(self.omega_fc*t2[self.i])
        cos_sig = 0*self.A*cos(self.omega_fc*t2[self.i])

        '''Умножение sample на cos и sin '''
        y_0  = (sample * sin_sig)
        y_90 = (sample * cos_sig)

        '''Фильтрация (ФНЧ) в канале 0 и 90 градусов'''
        yy_0  = self.lpf_y_0.proc(y_0)
        yy_90 = self.lpf_y_90.proc(y_90)

        '''Возведение в квадрат в канале 0 и 90 градусов'''
        y_0_square =   yy_0 * yy_0
        y_90_square =  yy_90 * yy_90

        '''Извлечение квадратного корня (результат)'''
        res = sqrt (y_0_square + y_90_square)

        self.i+=1

        return res
