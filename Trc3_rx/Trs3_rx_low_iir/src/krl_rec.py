import sys

from fir_filter import *
from am_det import *
from comparator import comparator
from filt_mean import *
from spectr_analyzer import *
from prep_model import *

sys.path.insert(0, '..')
"""
Trc3 receiver
"""


class CrlReceiver(object):
    def __init__(self, fc, fm):
        """initialization"""
        self.fc = fc
        self.fm = fm

        self.hz8_fir = fir(f_8)  # 8Hz bpf
        self.hz12_fir = fir(f_12)  # 12Hz bpf
        self.fir_15 = fir(f_14)  # 15Hz lpf
        #self.in_filter = fir(f_600)  # 400-800 Hz

        self.am_det8 = am_det_env()
        self.am_det12 = am_det_env()
        self.am_det_inp = am_det_coherent(self.fc)
        self.comp8 = comparator(threshold * 1.6, threshold, 5)  #comparator 8Hz
        self.comp12 = comparator(threshold * 1.6, threshold, 5)  #comparator 12Hz
        self.filt_8hz = mean_filt(15)
        self.filt_12hz = mean_filt(15)

    def proc(self, mix_signals: list) -> list:
        """main model loop (ISR)"""
        out_buffers = []
        [out_buffers.append([]) for i in range(18)]

        COUNT_DECIM = 0

        for tick in mix_signals:

            COUNT_DECIM += 1
            out_buffers[0].append(tick)
            y_0, y_90 = self.am_det_inp.mux(tick)

            if COUNT_DECIM == dec_coef:
                y_dem = self.am_det_inp.demod(y_0, y_90)

                y_f8Hz = self.hz8_fir.proc(y_dem)
                y_f12Hz = self.hz12_fir.proc(y_dem)

                y_det8 = self.am_det8.proc(y_f8Hz)
                y_det12 = self.am_det12.proc(y_f12Hz)

                y_f8 = self.filt_8hz.proc(y_det8)
                y_f12 = self.filt_12hz.proc(y_det12)
                out_buffers[11].append(y_f8)
                out_buffers[12].append(y_f12)

                y_comp8 = self.comp8.proc(y_f8)
                y_comp12 = self.comp12.proc(y_f12)
                out_buffers[13].append(y_comp8)
                out_buffers[14].append(y_comp12)

                COUNT_DECIM = 0

        return(out_buffers)
