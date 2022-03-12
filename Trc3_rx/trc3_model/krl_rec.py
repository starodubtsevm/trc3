import sys

sys.path.insert(0, '..')

from fir_filter import *
from limiter import *
from ask_det import *
from comparator import *
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
        self.lim = limiter(-1500000, 1500000)  #limiter
        self.hz8_fir = fir(f_8)  # 8Hz filter_buf
        self.hz12_fir = fir(f_12)  # 12Hz filter_buf
        self.filt8 = mean_filt(50)  # ask 8 Hz
        self.filt12 = mean_filt(50)  #  ask 12 Hz
        self.det = ask_det()  # ask detector
        self.det8 = ask_det()  # ask detector 8Hz
        self.det12 = ask_det()  # ask detector 12Hz
        self.comp8 = comparator(70, 80, 5)  #comparator 8Hz
        self.comp12 = comparator(70, 80, 5)  #comparator 12Hz

        freqs = {420: f_420, 480: f_480, 565: f_565, 720: f_720, 780: f_780}
        self.chan_fir = fir(freqs[self.fc])  #.channel filter
