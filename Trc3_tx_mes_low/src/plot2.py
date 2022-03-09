import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import figure
from prep_model import *


def to_plot(out_buffers, inp_sig_buff,n):

    Time2 = Time[::dec_coef]
    Time3 = Time[::window]
    
    figure(n)

    ax2 = plt.subplot(311)
    ax2.plot(Time, out_buffers[0])
    ax2.set_title('Вход модуля контроля сигналов КРЛ и АРС ' +
                  str("fs = ") + str(fs) + " Hz")
    ax2.grid(True)

    ax7 = plt.subplot(312)
    ax7.plot(Time2, out_buffers[11], label='8Hz')
    ax7.plot(Time2, out_buffers[12], label='12Hz')
    ax7.plot(Time2, out_buffers[13], label='8Hz')
    ax7.plot(Time2, out_buffers[14], label='12Hz')
    ax7.set_title('Сигналы на выходе модуля контроля сигнала КРЛ ' + str("fs = ") +
                  str(fs2) + " Hz")
    ax7.grid(True)
    ax7.legend()

    ax12 = plt.subplot(313)
    for i in range(1,7,1):
        ax12.plot(Time3, out_buffers[i], label=str(25 + i*50)+ " Гц" ,marker="o")
        
    ax12.set_title('Сигналы на выходе модуля контроля сигналов АРС\
      '+ str("fs = ") + str(fs) + " Hz")
    ax12.grid(True)
    ax12.legend()

    plt.show()

def plotSpectrum(y):
    """
	Function to plot the time domain and frequency domain signal
	"""
    figure(2)
    plt.ylim(0, 100)
    plt.xlim(0, 2000)
    plt.grid(True)
    #plt.legend()
    plt.magnitude_spectrum(y, Fs=fs, scale='dB')
    plt.ylabel('Уровень (dB)')
    plt.xlabel('Частота (Hz)')

    plt.show()
