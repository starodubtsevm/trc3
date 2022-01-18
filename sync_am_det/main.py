from krl_rec import*
from ars_gen import*
from white_noise_gen import*
from plot2 import*


#-Start Model config----------------------------

out_buffers = [ [], [], [], [], [], [], [], [], [], [], [] ]

#-Track line circuit---------------------------
krl_rec  = krl_receiver(420, 12) 							# rec krl signal
krl_gen  = ask_gen(420, 3500, 12)							# gen krl signal

#-Interferences-------------------------------
#krl_gen  = ask_gen(420, 1600, 1)							# gen krl signal2 
#ars_gen1 = ars_gen(75, 0)									# gen ars signal1
#ars_gen2 = ars_gen(125, 0)									# gen ars signal2
#noise_gen = white_noise(0)									# gen noise signal

sync_det = ask_det_sync(420)

#-End Model config----------------------------

#-Start Main loop------------------------------
count_decimation = 0 

for i in range(sim_point):

#-----main-cycle--------------------------------
	#count_decimation += 1
	out_buffers[0].append(krl_rec.chan_fir.proc(c.inp_signal_buff[i]))# filtered signal
	sin,cos = sync_det.proc(out_buffers[0][i])
	out_buffers[1].append(sin)								# local gen sin 
	out_buffers[2].append(cos)								# local gen cos
'''
	if count_decimation == 80:										# decimation by 80 @ 8000 Hz
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
'''
#-End Main loop---------------------------------

#-----plot-results-----------------------------------------------------------

#for i in range (10):
#	print(len(out_buffers[i]))

to_plot (out_buffers, c.inp_signal_buff)

