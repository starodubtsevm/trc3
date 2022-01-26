import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from IIR2Filter import IIR2Filter

FilterMains = IIR2Filter(4, [50],
                         rs=50,
                         filterType='lowpass',
                         design='cheby1',
                         rp=2,
                         fs=4000)

sos = FilterMains.COEFFS

#sos = signal.iirfilter(17, [50, 200], rs=60, btype='band', analog=False, ftype='cheby2', fs=2000, output='sos')
w, h = signal.sosfreqz(sos, 2000, fs=4000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w, 20 * np.log10(np.maximum(abs(h), 1e-5)))
ax.set_title('Chebyshev Type II bandpass frequency response')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Amplitude [dB]')
ax.axis((10, 2000, -100, 10))
ax.grid(which='both', axis='both')
plt.show()

#print(FilterMains.COEFFS)
#print(type(FilterMains.COEFFS))
sos = FilterMains.COEFFS
print(sos)
