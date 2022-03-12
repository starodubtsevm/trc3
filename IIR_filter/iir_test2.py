import numpy as np
import scipy as sp
import scipy.signal as signal
import matplotlib.pyplot as plt
import timeit

sampling_frequency = 2000.0        # Sampling frequency in Hz
nyq = sampling_frequency * 0.5  # Nyquist frequency
passband_frequencies = (3.0, 15.0)  # Filter cutoff in Hz
stopband_frequencies = (1.0, 50.0)
max_loss_passband = 3 # The maximum loss allowed in the passband
min_loss_stopband = 30 # The minimum loss allowed in the stopband
x = np.random.random(size=(5000, 12500)) # Random data to be filtered

order, normal_cutoff = signal.buttord(passband_frequencies, stopband_frequencies, max_loss_passband, min_loss_stopband, fs=sampling_frequency)

#iir_b, iir_a = signal.butter(order, normal_cutoff, btype="bandpass", fs=sampling_frequency)
#print (iir_b, iir_a)

iir_b = [6.46699403e-06,  0.00000000e+00, -1.94009821e-05,  0.00000000e+00, 1.94009821e-05, 0.00000000e+00, -6.46699403e-06]
iir_a = [ 1., -5.92323081,  14.62035594, -19.24899576,  14.25716156, -5.63260554,   0.92731461]

w, h = signal.freqz(iir_b, iir_a, worN=np.logspace(0, 3, 100), fs=sampling_frequency)
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Butterworth IIR bandpass filter fit to constraints')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')
plt.grid(which='both', axis='both')
plt.show()
