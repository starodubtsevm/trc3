import matplotlib.pyplot as plt
import numpy as np
from scipy import fft, arange
from prepare import *

def to_plot (signal_buf,filter_buf, lim_buf, ask_det_buf, hz8_fir_buf, hz12_fir_buf, ask_det8_buf, ask_det12_buf,
             filt_ask8_buf, filt_ask12_buf, comp8_buf, comp12_buf):

	fig, axs = plt.subplots(3, 3,sharex=True)
	fig.subplots_adjust(hspace=0.1)

	axs[0,0].plot(t, signal_buf)
	axs[0,0].set_xlabel('Input signal')
	plt.grid(True)

	axs[1,0].plot(t, filter_buf)
	axs[1,0].set_xlabel('After channel filter output')
	plt.grid(True)

	axs[2,0].plot(t, ask_det_buf)
	axs[2,0].set_xlabel('After ask det output')

	axs[0,1].plot(t2, hz8_fir_buf, label='channel 8 Hz')
	axs[0,1].set_ylim(-3000, 3000)
	axs[0,1].set_xlabel('filters outputs')

	axs[0,1].plot(t2, hz12_fir_buf, label='channel 12 Hz')
	axs[0,1].set_ylim(-3000, 3000)
	axs[0,1].set_xlabel('filters outputs')

	axs[1,1].plot(t2, ask_det8_buf)
	axs[1,1].set_ylim(-10, 1000)
	axs[1,1].set_xlabel('detectors outputs')

	axs[1,1].plot(t2, ask_det12_buf)
	axs[1,1].set_ylim(-10, 1000)
	axs[1,1].set_xlabel('det outputs')
	

	axs[2,1].plot(t2, filt_ask8_buf)
	axs[2,1].set_xlabel('det filter output')

	axs[2,1].plot(t2, filt_ask12_buf)
	
	axs[2,1].plot(t2, comp8_buf, label='channel 8 Hz')
	axs[2,1].plot(t2, comp12_buf, label='channel 12 Hz')
	
	fig.legend(loc='right')

	plt.show()

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

