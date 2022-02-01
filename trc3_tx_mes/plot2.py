import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from pylab import figure
import const as c


def to_plot(out_buffers, inp_signal_buff):

    figure(1)

    ax2 = plt.subplot(311)
    ax2.plot(c.t, out_buffers[0])
    ax2.set_title('Вход модуля контроля сигналов КРЛ и АРС )  ' +
                  str("fs = ") + str(c.fs) + " Hz")
    ax2.grid(True)

    ax7 = plt.subplot(312)
    ax7.plot(c.t2, out_buffers[11], label='8Hz')
    ax7.plot(c.t2, out_buffers[12], label='12Hz')
    ax7.plot(c.t2, out_buffers[13], label='8Hz')
    ax7.plot(c.t2, out_buffers[14], label='12Hz')
    ax7.set_title('Сигналы на выходе контроля сигнала КРЛ ' + str("fs = ") +
                  str(c.fs2) + " Hz")
    ax7.grid(True)
    ax7.legend()

    ax12 = plt.subplot(313)
    ax12.plot(c.t, out_buffers[1], label='75 Гц')
    ax12.plot(c.t, out_buffers[2], label='125 Гц')
    ax12.plot(c.t, out_buffers[3], label='175 Гц')
    ax12.plot(c.t, out_buffers[4], label='225 Гц')
    ax12.plot(c.t, out_buffers[5], label='275 Гц')
    ax12.plot(c.t, out_buffers[6], label='325 Гц')

    ax12.set_title('Сигналы на выходе модуля контроля уровня сигналов АРС\
      '+ str("fs = ") + str(c.fs) + " Hz")
    ax12.grid(True)
    ax12.legend()


def plotSpectrum(y):
    """
	Function to plot the time domain and frequency domain signal
	"""
    figure(2)
    plt.ylim(0, 100)
    plt.xlim(0, 2000)
    plt.grid(True)
    #plt.legend()
    plt.magnitude_spectrum(y, Fs=c.fs, scale='dB')
    plt.ylabel('Уровень (dB)')
    plt.xlabel('Частота (Hz)')
