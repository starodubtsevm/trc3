import time
"""
sync AM detector

"""
class gen(object):
    def __init__(self, fc, A = 0, fm = 0):
        """initialization"""
        if A == 0: return
        from numpy import pi, cos, sin
        import const as c
        from const import t
        self.fc = fc
        self.fm = fm
        self.A = A
        omega_fc   = 2*pi*fc

    def proc(self,sample):
    """demodulator"""

       '''Локальный генератор cos и sin'''
        sin_sig =  [(self.A*cos(omega_fc*t[i]) for i in range (len(t))]
        cos_sig =  [(self.A*cos(omega_fc*t[i]) for i in range (len(t))]

        y_0  = sample * sin_sig
        y_90 = sample * cos_sig


        return res

