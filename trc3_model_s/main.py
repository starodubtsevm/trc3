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
krl_rec  = krl_receiver(565, 8) 				# rec krl signal
krl_gen  = gen(565, 3500,8)				# gen krl signal

#-Interferences-------------------------------
krl_gen  = gen(480, 1000, 12)					# generator krl signal2
krl_gen  = gen(420,0,8)					# gen krl signal3
krl_gen  = gen(720,0, 12)					# gen krl signal4

ars_gen1 = gen(75, 0)					# gen ars signal1
ars_gen2 = gen(125, 0)					# gen ars signal2
noise_gen = white_noise(0)						# gen noise signal

print ("")
#-End Model config----------------------------
print ("--- %s seconds -end preparing--" % (time.time() - start_time))

print ("fs = " + str(fs)+" Hz")
print ("fs2 = " + str(fs2)+" Hz")
#-Start Main loop------------------------------
COUNT_DECIM = 0
II = 0
for i in range(sim_point):

#-----main-cycle--------------------------------
	COUNT_DECIM += 1
	out_buffers[0].append(krl_rec.chan_fir.proc(c.inp_signal_buff[i]))# filtered signal
	out_buffers[1].append(krl_rec.det2.proc(c.inp_signal_buff[i]))# signal after ask det  out_buffers[0][i]
	out_buffers[2].append(krl_rec.dc_b.proc(out_buffers[1][i]))# signal after dc blocker

	if COUNT_DECIM == c.dec_coef:					# decimation
#- channel
		out_buffers[3].append(krl_rec.det3.proc(out_buffers[2][i]))# signal after second detector
		out_buffers[4].append(krl_rec.fir_5.proc(out_buffers[3][II]))# signal after dc blocker
		#out_buffers[5].append(krl_rec.comp8.proc(out_buffers[4][II]))# signal comp
		#out_buffers5[6].append(krl_rec.comp8.proc(out_buffers[5][II]))# signal after comp 8 Hz
		II+=1
		COUNT_DECIM = 0

#-End Main loop---------------------------------

#-----plot-results-----------------------------------------------------------

#for i in range (10):
#	print(len(out_buffers[i]))

to_plot (out_buffers, c.inp_signal_buff)

#plotSpectrum(out_buffers[8])

#plotSpectrum(c.inp_signal_buff)

plt.show()
