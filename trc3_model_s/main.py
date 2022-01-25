import time
import matplotlib.pyplot as plt
from krl_rec import*
from white_noise_gen import*
from plot2 import*
from sig_gen import*
from am_sync_det import*
from dc_blocker import*
from ask_det import*
import const as c

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
krl_gen  = gen(780, 3500, 8)					# gen krl signal4

ars_gen1 = gen(75, 20000)					# gen ars signal1
ars_gen2 = gen(125, 20000)					# gen ars signal2
noise_gen = white_noise(3000)						# gen noise signal

print ("")
#-End Model config----------------------------

print ("fs = " + str(fs)+" Hz")
print ("fs2 = " + str(fs2)+" Hz")
#-Start Main loop------------------------------
COUNT_DECIM = 0
for i in range(sim_point):

#-----main-cycle--------------------------------
	COUNT_DECIM += 1
	y_in = krl_rec.in_filter.proc(c.inp_signal_buff[i])# filtered signal
	out_buffers[0].append (y_in)
	y_0, y_90 = krl_rec.det2.mux(y_in)# signal after mux0 mux90

	if COUNT_DECIM == c.dec_coef:# fs = 100
		y_dem = krl_rec.det2.demod(y_0, y_90)# signal after demodulator
		out_buffers[1].append(y_dem)
		y_f8Hz = krl_rec.hz8_fir.proc(y_dem)
		y_f12Hz = krl_rec.hz12_fir.proc(y_dem)
		out_buffers[2].append(y_f8Hz)
		out_buffers[3].append(y_f12Hz)
		y_ask_det8 = krl_rec.ask_det8.proc(y_f8Hz)
		y_ask_det12 = krl_rec.ask_det12.proc(y_f12Hz)
		
		y_f8 = krl_rec.hz10_fir8.proc(y_ask_det8)
		y_f12 = krl_rec.hz10_fir12.proc(y_ask_det12)
		y_comp8 = krl_rec.comp8.proc(y_f8)
		y_comp12 = krl_rec.comp12.proc(y_f12)
		out_buffers[4].append(y_comp8)
		out_buffers[5].append(y_comp12)

		COUNT_DECIM = 0

#-End Main loop---------------------------------

#-----plot-results-----------------------------------------------------------

#for i in range (10):
#	print(len(out_buffers[i]))
print ("--- %s seconds -end preparing--" % (time.time() - start_time))
to_plot (out_buffers, c.inp_signal_buff)


plotSpectrum(c.inp_signal_buff)

plt.show()
