import time
import numpy as np
"""
Ask generator
"""
class gen(object):
    def __init__(self, fc, A=0, fm=0):
        """initialization"""
        if A == 0: return
        from numpy import pi, cos, sin
        import const as c
        from const import t
        self.fc = fc
        self.fm = fm
        self.A = A / 2
        self.A2 = A * 0.01
        self.A3 = A * 0.001
        omega_fc = 6.28 * fc
        _2omega_fc = 2 * omega_fc
        _3omega_fc = 3 * omega_fc
        if self.fm == 0:
            self.M = 0
            omega_fm = 0
        else:
            self.M = 1
            omega_fm = 6.28 * fm

        _data = [self.A*cos(omega_fc*i)*(1 + self.M * cos(omega_fm *i))+\
        self.A2*cos(_2omega_fc*i)*(1 + self.M * cos(omega_fm *i))+\
        self.A3*cos(_3omega_fc*i)*(1 + self.M * cos(omega_fm *i))\
        for i in t]

        c.inp_signal_buff = [a + b for a, b in zip(c.inp_signal_buff, _data)]
        del _data
