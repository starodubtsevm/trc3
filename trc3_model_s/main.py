import time
import matplotlib.pyplot as plt
from krl_rec import*
from white_noise_gen import*
from plot2 import*

import const as c

from sig_gen import*
from am_sync_det import*
from dc_blocker import*

start_time = time.time()
print ("preparing signals")
#-Start Model config----------------------------

out_buffers = []
[out_buffers.append([]) for i in range (11)]

#-Track line circuit---------------------------
krl_rec  = krl_receiver(565, 12) 				# rec krl signal
krl_gen  = gen(565, 3500, 12)				# gen krl signal

#-Interferences-------------------------------
krl_gen  = gen(480, 3500, 12)					# generator krl signal2
krl_gen  = gen(420, 3500, 8)					# gen krl signal3
krl_gen  = gen(720, 3500, 12)					# gen krl signal4

ars_gen1 = gen(75, 3500)					# gen ars signal1
ars_gen2 = gen(125, 3500)					# gen ars signal2
noise_gen = white_noise(0)						# gen noise signal

print ("")
#-End Model config----------------------------
print ("--- %s seconds -end preparing--" % (time.time() - start_time))

print ("fs = " + str(fs)+" Hz")
print ("fs2 = " + str(fs2)+" Hz")
#-Start Main loop------------------------------
COUNT_DECIM = 0
for i in range(sim_point):

#-----main-cycle--------------------------------
	COUNT_DECIM += 1
	out_buffers[0].append(krl_rec.chan_fir.proc(c.inp_signal_buff[i]))# filtered signal
	y_0, y_90 = krl_rec.det2.mux(c.inp_signal_buff[i])# downsampling signal after

	if COUNT_DECIM == c.dec_coef:# fs = 100
		y_dem = krl_rec.det2.demod(y_0, y_90)# signal after downsampler
		out_buffers[1].append(y_dem)# signal after demodulator
		COUNT_DECIM = 0

#-End Main loop---------------------------------

#-----plot-results-----------------------------------------------------------

#for i in range (10):
#	print(len(out_buffers[i]))

to_plot (out_buffers, c.inp_signal_buff)

plotSpectrum(out_buffers[1])

#plotSpectrum(c.inp_signal_buff)

plt.show()
