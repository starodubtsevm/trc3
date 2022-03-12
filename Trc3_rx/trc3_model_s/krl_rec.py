import sys

sys.path.insert(0, '..')

from fir_filter import *
from limiter import *
from am_det import *
from comparator import *
from dc_blocker import *
from filt_mean import *
import const as c
"""
Trc3 receiver
"""


class krl_receiver(object):
    def __init__(self, fc, fm):
        """initialization"""
        self.fc = fc
        self.fm = fm
        self.lim = limiter(-150000, 150000)  #limiter
        self.hz8_fir = fir(f_8)  # 8Hz bpf
        self.hz12_fir = fir(f_12)  # 12Hz bpf
        self.fir_15 = fir(f_14)  # 15Hz lpf
        self.in_filter = fir(f_600)  # 400-800 Hz
        self.am_det8 = am_det_env()
        self.am_det12 = am_det_env()
        self.am_det_inp = am_det_coherent(fc, c.fs)
        self.comp8 = comparator(30, 48, 5)  #comparator 8Hz
        self.comp12 = comparator(30, 48, 5)  #comparator 12Hz
        self.comp_sn = comparator(30, 20, 5)  #comparator sn unit
        self.sn_8filt = mean_filt(30)
        self.sn_12filt = mean_filt(30)
        self.filt_8hz = mean_filt(25)
        self.filt_12hz = mean_filt(25)
        self.filt_det = mean_filt(25)  # meaning for mesuariment
