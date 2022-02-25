import sys
from time import sleep
sys.path.insert(0, '..')

from fir_filter import *
from am_det import *
from comparator import *
from filt_mean import *
from spectr_analyzer import *
from prep_model import *
"""
Trc3 receiver
"""

class krl_receiver(object):
    def __init__(self, fc, fm):
        """initialization"""
        self.fc = fc
        self.fm = fm

        self.hz8_fir = fir(f_8)  # 8Hz bpf
        self.hz12_fir = fir(f_12)  # 12Hz bpf
        self.fir_15 = fir(f_14)  # 15Hz lpf
        self.in_filter = fir(f_600)  # 400-800 Hz

        self.am_det8 = am_det_env()
        self.am_det12 = am_det_env()
        self.am_det_inp = am_det_coherent(fc, fs)
        self.comp8 = comparator(tr * 1.6, tr, 5)  #comparator 8Hz
        self.comp12 = comparator(tr * 1.6, tr, 5)  #comparator 12Hz
        self.comp_sn = comparator(30, 20, 5)  #comparator sn unit
        self.sn_8filt = mean_filt(30)
        self.sn_12filt = mean_filt(30)
        self.filt_8hz = mean_filt(25)
        self.filt_12hz = mean_filt(25)
        self.s_a = spectr_analyzer()


    def proc(self,mix_signals: list) ->list:

        out_buffers = []
        [out_buffers.append([]) for i in range(18)]

        COUNT_DECIM = 0
        COUNT_TOTAL = 0
        COUNT_FFT = 0

        print("")
        print("fs = " + str(fs) + " Hz")
        print("fs2 = " + str(fs2) + " Hz")
        print("")

        for tick in mix_signals:

            COUNT_DECIM += 1
            COUNT_TOTAL += 1
            progress(COUNT_TOTAL)
            y_in_flt = self.in_filter.proc(tick)
            out_buffers[0].append(tick)
            y_0, y_90 = self.am_det_inp.mux(y_in_flt)

            if COUNT_FFT < WINDOW_FFT - 1:
                self.s_a.fill_buf(tick)
                COUNT_FFT += 1
            else:
                COUNT_FFT = 0
                f_ars, u_ars = self.s_a.proc()
                for i in range (len(u_ars)):
                    out_buffers[i+1].append(u_ars[i])

            if COUNT_DECIM == DEC_COEF:
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

#        for i in range (18):
#            print(len(out_buffers[i]))

        print("")
        return(out_buffers)

