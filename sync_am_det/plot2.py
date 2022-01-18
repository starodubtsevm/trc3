import matplotlib.pyplot as plt
import const as c

def to_plot (out_buffers, inp_signal_buff):

	ax1 = plt.subplot(611)
	plt.plot(c.t, inp_signal_buff)
	ax1.set_title('Input sugnal')
	plt.xticks([])

	ax2 = plt.subplot(612, sharex=ax1)
	plt.plot(c.t, out_buffers[0])
	ax2.set_title('After channel filter output')

	ax3 = plt.subplot(613, sharex=ax1)
	plt.plot(c.t, out_buffers[1])
	ax3.set_title('Local gen signal')


	ax4 = plt.subplot(614, sharex=ax1)
	plt.plot(c.t, out_buffers[2])
	#ax4.set_title('After ask det output')
	plt.show()
'''
	ax5 = plt.subplot(614)
	plt.plot(c.t2, out_buffers[3], label = '8Hz')
	ax5.set_title('filters outputs')
	plt.xticks([])

	ax6 = plt.subplot(614)
	plt.plot(c.t2, out_buffers[7], label = '12Hz')
	plt.xticks([])

	ax7 = plt.subplot(615)
	plt.plot(c.t2, out_buffers[4], label = '8Hz')
	plt.xticks([])

	ax8 = plt.subplot(615)
	plt.plot(c.t2,out_buffers[8], label = '12Hz')
	plt.xticks([])

	ax9 = plt.subplot(616)
	plt.plot(c.t2, out_buffers[5], label = '8Hz')

	ax10 = plt.subplot(616)
	plt.plot(c.t2, out_buffers[9], label = '12Hz')

	ax11 = plt.subplot(616)
	plt.plot(c.t2, out_buffers[6], label = '8Hz')

	ax12 = plt.subplot(616)
	plt.plot(c.t2, out_buffers[10], label = '12Hz')

	for ax in ax7,ax8, ax9, ax10, ax11,ax12:
		ax.grid(True)

	for ax in ax5, ax6, ax7, ax8, ax9, ax10, ax11 ,ax12:
		ax.legend()
'''
	

def to_plotSpectrum(y):

	n = len(y) # length of the signal
	k = arange(n)
	T = n/fs
	frq = k/T # two sides frequency range
	frq = frq[range(n//2)] # one side frequency range
	Y = fft(y)/n # fft computing and normalization
	Y = Y[range(n//2)]

	plt.subplot(2,1,1)
	plt.plot(t, y)
	plt.xlabel('Time')
	plt.ylabel('Amplitude')

	plt.subplot(2,1,2)
	plt.plot(frq, abs(Y),'r') # plotting the spectrum
	plt.xlabel('Freq (Hz)')
	plt.ylabel('|Y(freq)|')

