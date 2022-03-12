import matplotlib.pyplot as plt
from scipy import fft, arange
import numpy as np
from pylab import figure
import const as c


def to_plot(out_buffers, inp_signal_buff):

    figure(1)
    ax1 = plt.subplot(611)
    plt.plot(c.t, inp_signal_buff)
    ax1.set_title('Input signal  ' + str("fs = ") + str(c.fs) + " Hz")
    plt.xticks([])

    ax2 = plt.subplot(612, sharex=ax1)
    plt.plot(c.t, out_buffers[0])
    ax2.set_title('After channel filter output  ' + str("fs = ") + str(c.fs) +
                  " Hz")

    ax4 = plt.subplot(613)
    plt.plot(c.t, out_buffers[2])
    ax4.set_title('After ask det output  ' + str("fs = ") + str(c.fs) + " Hz")

    ax5 = plt.subplot(614)
    plt.plot(c.t2, out_buffers[3], label='8Hz')
    ax5.set_title('filters outputs 8 & 12 Hz ' + str("fs = ") + str(c.fs2) +
                  " Hz")
    plt.xticks([])

    ax6 = plt.subplot(614)
    plt.plot(c.t2, out_buffers[7], label='12Hz')
    plt.xticks([])

    ax7 = plt.subplot(615)
    plt.plot(c.t2, out_buffers[4], label='8Hz')
    plt.xticks([])

    ax8 = plt.subplot(615)
    plt.plot(c.t2, out_buffers[8], label='12Hz')
    plt.xticks([])

    ax9 = plt.subplot(616)
    plt.plot(c.t2, out_buffers[5], label='8Hz')

    ax10 = plt.subplot(616)
    plt.plot(c.t2, out_buffers[9], label='12Hz')

    ax11 = plt.subplot(616)
    plt.plot(c.t2, out_buffers[6], label='8Hz')

    ax12 = plt.subplot(616)
    plt.plot(c.t2, out_buffers[10], label='12Hz')

    for ax in ax7, ax8, ax9, ax10, ax11, ax12:
        ax.grid(True)

    for ax in ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12:
        ax.legend()


def plotSpectrum(y):
    """
	Function to plot the time domain and frequency domain signal
	"""
    figure(2)
    plt.ylim(0, 80)
    plt.xlim(0, 2000)
    plt.grid(True)
    #plt.legend()
    plt.magnitude_spectrum(y, Fs=c.fs, scale='dB')
    plt.ylabel('Уровень (dB)')
    plt.xlabel('Частота (Hz)')
