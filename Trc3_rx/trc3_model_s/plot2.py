import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
#from scipy import fft, arange
import numpy as np
from pylab import figure
import const as c


def to_plot(out_buffers, inp_signal_buff):

    figure(1)
    ax1 = plt.subplot(611)
    ax1.plot(c.t, inp_signal_buff)
    ax1.set_title('Вход приемника (сигнал + помехи)  ' + str("fs = ") +
                  str(c.fs) + " Hz")
    ax1.grid(True)

    ax2 = plt.subplot(612, sharex=ax1)
    ax2.plot(c.t, out_buffers[0])
    ax2.set_title('Сигнал на выходе канального фильтра (400 - 800 Гц)  ' +
                  str("fs = ") + str(c.fs) + " Hz")
    ax2.grid(True)

    ax3 = plt.subplot(613)
    ax3.plot(c.t2, out_buffers[1])
    ax3.plot(c.t2, out_buffers[2])
    ax3.set_title('Сигнал на выходе когерентного детектора  ' + str("fs = ") +
                  str(c.fs2) + " Hz")
    ax3.grid(True)

    ax5 = plt.subplot(614)
    ax5.plot(c.t2, out_buffers[3], label='8Hz')
    ax5.plot(c.t2, out_buffers[4], label='12Hz')
    ax5.set_title('Сигналы на выходах фильтров 8 и 12 Гц ' + str("fs = ") +
                  str(c.fs2) + " Hz")
    ax5.grid(True)
    ax5.legend()

    ax7 = plt.subplot(615)
    ax7.plot(c.t2, out_buffers[5], label='8Hz')
    ax7.plot(c.t2, out_buffers[6], label='12Hz')
    ax7.plot(c.t2, out_buffers[7], label='8Hz')
    ax7.plot(c.t2, out_buffers[8], label='12Hz')
    ax7.set_title('Сигналы на входах\выходах компараторов ' + str("fs = ") +
                  str(c.fs2) + " Hz")
    ax7.grid(True)
    ax7.legend()

    ax11 = plt.subplot(616)
    ax11.plot(c.t2, out_buffers[9], label='уровень сигнал\шум 8 Гц')
    ax11.plot(c.t2, out_buffers[10], label='уровень сигнал\шум 12 Гц')
    plt.ylim(0, 40)
    ax11.set_title('Индикатор сигнал/шум в канале (разницы\
     уровней в каналах 8 и 12 Гц '+ str("fs = ")\
     + str(c.fs2) + " Hz")
    ax11.grid(True)
    ax11.legend()

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
