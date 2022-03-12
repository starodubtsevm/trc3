import time
import matplotlib.pyplot as plt
from krl_rec import *
from white_noise_gen import *
from plot2 import *

import const as c

from sig_gen import *

print("preparing signals")
#-Start Model config----------------------------

out_buffers = []
[out_buffers.append([]) for i in range(11)]

#-Track line circuit---------------------------
krl_rec = krl_receiver(565, 12)  # rec krl signal
krl_gen = gen(565, 1024, 12)  # gen krl signal 48 mV (ADC 3.3 V, 16 Bit)

#-Interference-------------------------------
krl_gen = gen(480, 10 * 1024, 12)  # gen krl signal 2
krl_gen = gen(420, 10 * 1024, 8)  # gen krl signal 3
krl_gen = gen(720, 1 * 1024, 12)  # gen krl signal 4
krl_gen = gen(780, 1 * 1024, 8)  # gen krl signal 5

ars_gen1 = gen(75, 0 * 1024)  # gen ars signal 1
ars_gen2 = gen(125, 0 * 1024)  # gen ars signal 2

krl_gen = gen(565, 0.3 * 1024, 1)  # gen krl signal IMD

noise_gen = white_noise(2 * 1024)  # gen noise signal

print("")
#-End Model config----------------------------
start_time = time.time()

print("fs = " + str(fs) + " Hz")
print("fs2 = " + str(fs2) + " Hz")
#-Start Main loop------------------------------
COUNT_DECIM = 0
II = 0
for i in range(sim_point):

    #-----main-cycle--------------------------------
    COUNT_DECIM += 1
    out_buffers[0].append(krl_rec.chan_fir.proc(
        c.inp_signal_buff[i]))  # filtered signal
    out_buffers[1].append(krl_rec.det.proc(
        out_buffers[0][i]))  # signal after ask det
    out_buffers[2].append(krl_rec.lim.proc(
        out_buffers[1][i]))  # signal after ask lim

    if COUNT_DECIM == c.dec_coef:  # decimation
        #- 8 Hz channel
        out_buffers[3].append(krl_rec.hz8_fir.proc(
            out_buffers[2][i]))  # signal after 8 Hz filter
        out_buffers[4].append(krl_rec.det8.proc(
            out_buffers[3][II]))  # signal after ask det 8 Hz
        out_buffers[5].append(krl_rec.filt8.proc(
            out_buffers[4][II]))  # signal after flt ask det 8 Hz
        out_buffers[6].append(krl_rec.comp8.proc(
            out_buffers[5][II]))  # signal after comp 8 Hz
        #-12 Hz channel
        out_buffers[7].append(krl_rec.hz12_fir.proc(
            out_buffers[2][i]))  # signal after 12 Hz filter
        out_buffers[8].append(krl_rec.det12.proc(
            out_buffers[7][II]))  # signal after ask det 12 Hz
        out_buffers[9].append(krl_rec.filt12.proc(
            out_buffers[8][II]))  # signal after flt ask det 12 Hz
        out_buffers[10].append(krl_rec.comp12.proc(
            out_buffers[9][II]))  # signal after comp 12 Hz
        II += 1
        COUNT_DECIM = 0

#-End Main loop---------------------------------

#-----plot-results-----------------------------------------------------------

#for i in range (10):
#   print(len(out_buffers[i]))
print("--- %s seconds -end preparing--" % (time.time() - start_time))
to_plot(out_buffers, c.inp_signal_buff)

#plotSpectrum(out_buffers[8])

#plotSpectrum(c.inp_signal_buff)

plt.show()
