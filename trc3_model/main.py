from krl_rec import*
from white_noise_gen import*
from plot2 import*
import matplotlib.pyplot as plt
import const as c
import time
from sig_gen import*

start_time = time.time()
print ("preparing signals")
#-Start Model config----------------------------

out_buffers = []
[out_buffers.append([]) for i in range (11)]

#-Track line circuit---------------------------
krl_rec  = krl_receiver(420, 12) 				# rec krl signal
krl_gen  = gen(565, 3500, 12)				# gen krl signal

#-Interferences-------------------------------
krl_gen  = gen(480, 3500, 8)					# gen krl signal2
krl_gen  = gen(420, 1700, 12)					# gen krl signal3
krl_gen  = gen(720, 1700, 8)					# gen krl signal4

ars_gen1 = gen(75, 3500)					# gen ars signal1
ars_gen2 = gen(125, 3500)					# gen ars signal2
noise_gen = white_noise(0)						# gen noise signal

print ("")
#-End Model config----------------------------
print ("--- %s seconds -end preparing--" % (time.time() - start_time))

print ("fs = " + str(fs)+" Hz")
print ("fs2 = " + str(fs2)+" Hz")
#-Start Main loop------------------------------
count_decimation = 0
ii = 0
for i in range(sim_point):

#-----main-cycle--------------------------------
	count_decimation += 1
	out_buffers[0].append(krl_rec.chan_fir.proc(c.inp_signal_buff[i]))# filtered signal
	out_buffers[1].append(krl_rec.det.proc(out_buffers[0][i]))# signal after ask det
	out_buffers[2].append(krl_rec.lim.proc(out_buffers[1][i]))# signal after ask lim

	if count_decimation == c.dec_coef:					# decimation
#- 8 Hz channel
		out_buffers[3].append(krl_rec.hz8_fir.proc(out_buffers[2][i]))# signal after 8Hz filter
		out_buffers[4].append(krl_rec.det8.proc(out_buffers[3][ii]))# signal after ask det 8Hz
		out_buffers[5].append(krl_rec.hz10fir8.proc(out_buffers[4][ii]))# signal after flt ask det 8 Hz
		out_buffers[6].append(krl_rec.comp8.proc(out_buffers[5][ii]))# signal after comp 8 Hz
#-12 Hz channel
		out_buffers[7].append(krl_rec.hz12_fir.proc(out_buffers[2][i]))# signal after 12Hz filter
		out_buffers[8].append(krl_rec.det12.proc(out_buffers[7][ii]))# signal after ask det 12 Hz
		out_buffers[9].append(krl_rec.hz10fir12.proc(out_buffers[8][ii]))# signal after flt ask det 12 Hz
		out_buffers[10].append(krl_rec.comp12.proc(out_buffers[9][ii]))# signal after comp 12 Hz
		ii+=1
		count_decimation = 0

#-End Main loop---------------------------------

#-----plot-results-----------------------------------------------------------

#for i in range (10):
#	print(len(out_buffers[i]))

to_plot (out_buffers, c.inp_signal_buff)

#plotSpectrum(out_buffers[8])

plotSpectrum(c.inp_signal_buff)

plt.show()

