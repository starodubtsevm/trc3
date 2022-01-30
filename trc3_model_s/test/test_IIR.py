import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from IIR2Filter import IIR2Filter

FilterMains = IIR2Filter(4, [1500],
                         rs=50,
                         filterType='lowpass',
                         design='cheby1',
                         rp=2,
                         fs=4000)

#sos = FilterMains.COEFFS

sos = np.array([[3742, 7483,  3742,  1, 2717,  4983],
                [16384,32768, 16384, 1, 20898, 13986]])

w, h = signal.sosfreqz(sos, 2000, fs=4000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w, 20 * np.log10(np.maximum(abs(h), 1e-5)))
ax.set_title('Chebyshev Type II bandpass frequency response')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Amplitude [dB]')
ax.axis((10, 2000, -100, 20))
ax.grid(which='both', axis='both')
plt.show()

#sos = FilterMains.COEFFS*32768
print (sos/2)
