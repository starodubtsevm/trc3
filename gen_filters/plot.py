import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages as pdf
from scipy.signal import freqz

def plot_fr(y,freqs,band,ntaps,fs):

    lowcut  = freqs - band/2
    highcut = freqs + band/2

    fig = plt.figure(1, figsize=(12, 9))
    plt.clf()

    # First plot the desired ideal response as a green(ish) rectangle.
    rect = plt.Rectangle((lowcut, 0), highcut - lowcut, -90,
        facecolor="#60ff60", alpha=0.2)
    plt.gca().add_patch(rect)

    # Plot the frequency response
    w, h = freqz(y, 1, worN=10000)
    plt.plot((fs * 0.5 / np.pi) * w, 20 * np.log10(abs(h))-90, label="Hamming window")

    plt.xlim(lowcut - 100, highcut + 100)
    plt.ylim(-90, 5)
    plt.grid(True)
    plt.legend()
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain')
    plt.title('АЧХ входного FIR фильтра, %d - %d  Гц %d taps, fs = %d Hz' % (lowcut, highcut, ntaps, fs))

    file_name = str("FIR_" + str(lowcut)+ "-" + str(highcut)+".png")

    plt.savefig('./Graphics/'+ file_name)
    plt.clf()

def plot_fr2(y,fcut,ntaps,fs):


    fig = plt.figure(1, figsize=(12, 9))
    plt.clf()

    # First plot the desired ideal response as a green(ish) rectangle.
    rect = plt.Rectangle((0, 0), fcut, -90, facecolor="#60ff60", alpha=0.2)
    plt.gca().add_patch(rect)

    # Plot the frequency response
    w, h = freqz(y, 1, worN=10000)
    plt.plot((fs * 0.5 / np.pi) * w, 20 * np.log10(abs(h))-90, label="Hamming window")

    plt.xlim(0, fcut + 100 )
    plt.ylim(-90, 5)
    plt.grid(True)
    plt.legend()
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Коефф передачи')
    plt.title('АЧХ FIR ФНЧ, %d  Гц %d taps, fs = %d Hz' % (fcut, ntaps, fs))

    file_name = str("FIR_" + str(fcut) + ".png")

    plt.savefig('./Graphics/'+ file_name)
    plt.clf()
