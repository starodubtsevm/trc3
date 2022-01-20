import numpy as np
import pylab
import math

# generating test signals
def goertzel(samples, sample_rate, *freqs):

    window_size = len(samples)
    f_step = sample_rate / float(window_size)
    f_step_normalized = 1.0 / window_size

    # Calculate all the DFT bins we have to compute to include frequencies
    # in `freqs`.
    bins = set()

    for f_range in freqs:
        f_start, f_end = f_range
        k_start = int(math.floor(f_start / f_step))
        k_end = int(math.ceil(f_end / f_step))

        bins = bins.union(range(k_start, k_end))
        print (bins)

SAMPLE_RATE = 4000
WINDOW_SIZE = 1024
t = np.linspace(0, 1, SAMPLE_RATE)[:WINDOW_SIZE]
sine_wave = np.sin(2*np.pi*75*t) + np.sin(2*np.pi*125*t) + np.sin(2*np.pi*780*t)

sine_wave3 = []
for i in range (len(sine_wave)):
    multiplier = 0.5 * (1 - np.cos(2*np.pi*i/WINDOW_SIZE))
    x = multiplier * sine_wave[i]
    sine_wave3.append(x)
sine_wave = sine_wave3

#goertzel(sine_wave, SAMPLE_RATE, (73, 78), (123, 128), (775,785))

print ((math.log(1024,2))*0.83)

