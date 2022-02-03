import time
import matplotlib.pyplot as plt
from conf_model import*
from am_det import *
from krl_rec import *
from plot2 import *
from sig_gen import *
from spectr_analyzer import *
from white_noise_gen import *

#import sys
#sys.stderr = open('./err.txt', 'w')

prep = time.time()
print("preparing signals")
#-Start Model config-------------------------

out_buffers = []
[out_buffers.append([]) for i in range(18)]

#--Конфигурирование приемника

krl_rec = krl_receiver(565, 8)  # rec krl signal

#- Конфигурирование генераторов

Signals = [[420, 3 * 1024, 8 ],
           [480, 0 * 1024, 12],
           [565, 1 * 1024, 8 ],
           [720, 1 * 1024, 12],
           [780, 1 * 1024, 8 ],
           [ 75, 3 * 1024, 0 ],
           [125, 0 * 1024, 0 ],
           [175, 2 * 1024, 0 ],
           [225, 0 * 1024, 0 ],
           [275, 1 * 1024, 0 ],
           [325, 1.5 * 1024, 0 ]]

mix_signals = [0] * sim_point

for signal in Signals:
    if signal[1] > 0:
        y = sig_gen(signal)
        mix_signals= [a + b for a, b in zip(mix_signals, y)]

print("- %s seconds -end prep--" % (time.time() - prep))
print("")

#-End Model config----------------------------

print("fs = " + str(fs) + " Hz")
print("fs2 = " + str(fs2) + " Hz")

#-Start Main loop------------------------------
calc = time.time()
print("start calculaton model")

COUNT_DECIM = 0

for tick in mix_signals:

    #-----main-cycle--------------------------------
    COUNT_DECIM += 1

    y_0, y_90 = krl_rec.am_det_inp.mux(tick)
    out_buffers[0].append(tick)

    f_ars, u_ars = krl_rec.s_a.proc(tick)

    u_ars75 = krl_rec.filt_ars75.proc(u_ars[0])
    u_ars125 = krl_rec.filt_ars125.proc(u_ars[1])
    u_ars175 = krl_rec.filt_ars175.proc(u_ars[2])
    u_ars225 = krl_rec.filt_ars225.proc(u_ars[3])
    u_ars275 = krl_rec.filt_ars275.proc(u_ars[4])
    u_ars325 = krl_rec.filt_ars325.proc(u_ars[5])

    out_buffers[1].append(u_ars75)
    out_buffers[2].append(u_ars125)
    out_buffers[3].append(u_ars175)
    out_buffers[4].append(u_ars225)
    out_buffers[5].append(u_ars275)
    out_buffers[6].append(u_ars325)

    if COUNT_DECIM == dec_coef:  # fs = 100
        y_dem = krl_rec.am_det_inp.demod(y_0, y_90)

        y_det_filt = krl_rec.filt_det.proc(y_dem)

        y_f8Hz = krl_rec.hz8_fir.proc(y_dem)
        y_f12Hz = krl_rec.hz12_fir.proc(y_dem)

        y_ask_det8 = krl_rec.am_det8.proc(y_f8Hz)
        y_ask_det12 = krl_rec.am_det12.proc(y_f12Hz)

        y_f8 = krl_rec.filt_8hz.proc(y_ask_det8)
        y_f12 = krl_rec.filt_12hz.proc(y_ask_det12)
        out_buffers[11].append(y_f8)
        out_buffers[12].append(y_f12)

        y_comp8 = krl_rec.comp8.proc(y_f8)
        y_comp12 = krl_rec.comp12.proc(y_f12)
        out_buffers[13].append(y_comp8)
        out_buffers[14].append(y_comp12)

        COUNT_DECIM = 0

#-End Main loop---------------------------------

#-----plot-results------------------------------

#for i in range (10):
#    print(len(out_buffers[i]))
print ("")
print("--- %s seconds -end calc--" % (time.time() - calc))
print("start plotting model")
to_plot(out_buffers, mix_signals)

#plotSpectrum(mix_signals)

plt.show()
