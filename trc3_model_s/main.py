import time
import matplotlib.pyplot as plt
from krl_rec import *
from white_noise_gen import *
from plot2 import *
from sig_gen import *
from dc_blocker import *
from am_det import *
import const as c
import sys

#sys.stderr = open('./err.txt', 'w')


start_time = time.time()
print("preparing signals")
#-Start Model config----------------------------

out_buffers = []
[out_buffers.append([]) for i in range(12)]

#-Track line circuit---------------------------
krl_rec = krl_receiver(565, 8)  # rec krl signal
krl_gen = gen(565, 1 * 1024, 8)  # gen krl signal 48 mV (ADC 3.3 V, 16 Bit)

#-Interference-------------------------------
krl_gen = gen(480, 10 * 1024, 12)  # gen krl signal 2
krl_gen = gen(420, 4 * 1024, 8)  # gen krl signal 3
krl_gen = gen(720, 4 * 1024, 12)  # gen krl signal 4
krl_gen = gen(780, 4 * 1024, 8)  # gen krl signal 5

ars_gen1 = gen(75, 0 * 1024)  # gen ars signal 1
ars_gen2 = gen(125, 0 * 1024)  # gen ars signal 2

krl_gen = gen(565, 0.3 * 1024, 1)  # gen krl signal IMD

noise_gen = white_noise(3 * 1024)  # gen noise signal (50 mV)

print("")
#-End Model config----------------------------
print("fs = " + str(fs) + " Hz")
print("fs2 = " + str(fs2) + " Hz")

#-Start Main loop------------------------------
print("start calculaton model")
COUNT_DECIM = 0
for i in range(sim_point):

    #-----main-cycle--------------------------------
    COUNT_DECIM += 1
    y_in = krl_rec.in_filter.proc(c.inp_signal_buff[i])  # filtered signal
    out_buffers[0].append(y_in)
    y_0, y_90 = krl_rec.am_det_inp.mux(y_in)  # signal after mux0 mux90

    if COUNT_DECIM == c.dec_coef:  # fs = 100
        y_dem = krl_rec.am_det_inp.demod(y_0, y_90)  # signal after demodulator
        out_buffers[1].append(y_dem)

        y_det_filt = krl_rec.filt_det.proc(y_dem)
        out_buffers[2].append(y_det_filt)

        y_f8Hz = krl_rec.hz8_fir.proc(y_dem)
        y_f12Hz = krl_rec.hz12_fir.proc(y_dem)
        out_buffers[3].append(y_f8Hz)
        out_buffers[4].append(y_f12Hz)

        y_ask_det8 = krl_rec.am_det8.proc(y_f8Hz)
        y_ask_det12 = krl_rec.am_det12.proc(y_f12Hz)

        y_f8 = krl_rec.filt_8hz.proc(y_ask_det8)
        y_f12 = krl_rec.filt_12hz.proc(y_ask_det12)
        out_buffers[5].append(y_f8)
        out_buffers[6].append(y_f12)

        y_comp8 = krl_rec.comp8.proc(y_f8)
        y_comp12 = krl_rec.comp12.proc(y_f12)
        out_buffers[7].append(y_comp8)
        out_buffers[8].append(y_comp12)

        y_diff8 = y_det_filt / (y_f8+0.1)
        y_diff12 = y_det_filt / (y_f12+0.1)

        y_sn_8filt = krl_rec.sn_8filt.proc(y_diff8)
        y_sn_12filt = krl_rec.sn_12filt.proc(y_diff12)
        out_buffers[9].append(y_sn_8filt)
        out_buffers[10].append(y_sn_12filt)

        COUNT_DECIM = 0

#-End Main loop---------------------------------

#-----plot-results------------------------------

#for i in range (10):
#    print(len(out_buffers[i]))
print ("")
print("--- %s seconds -end preparing--" % (time.time() - start_time))
print("start plotting model")
to_plot(out_buffers, c.inp_signal_buff)

#plotSpectrum(c.inp_signal_buff)

plt.show()
