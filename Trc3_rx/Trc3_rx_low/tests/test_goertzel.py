import numpy as np
import pylab
import math
import timeit


def goertzel(samples, sample_rate):

    window_size = len(samples)

    #bins = {15,25,35,45,55,65}# 4000 Hz 800 taps 2.4 10
    #bins = {3,5,7,9,11,13}# 4000 Hz 160 taps 0.1 0.15 0.4
    #bins = {30,50,70,90,110,130}# 2000 Hz 800 taps 10 15 40
    #bins = {3,5,7,9,11,13}# 2000 Hz 80 taps 0.1 0.16 0.45
    bins = {6,10,14,18,22,26} # 2000 Hz 160 taps 0.37 0.63 1.62
    #bins = {6,10,14,18,22,26}# 1000 Hz 80 taps 0.35 0.61 1.6
    #bins = {12,20,28,36,44,52}# 1000 Hz 160 taps 1.47 2.49 6.45

    print (bins)

    # For all the bins, calculate the DFT term
    n_range = range(0, window_size)
    freqs = []
    results = []

    for k in bins:
        # Bin frequency and coefficients for the computation
        f = k * f_step_normalized
        w_real = 2.0 * math.cos(2.0 * math.pi * f)
        w_imag = math.sin(2.0 * math.pi * f)
        # Doing the calculation on the whole sample
        d1, d2 = 0.0, 0.0
        for n in n_range:
            y  = samples[n] + w_real * d1 - d2
            d2, d1 = d1, y
        # Storing results `(real part, imag part, power)`
        results.append((0,0,
            #0.5 * w_real * d1 - d2,
            #w_imag * d1,
            d2**2 + d1**2 - w_real * d1 * d2)
        )
        freqs.append(int(f * sample_rate))
    return freqs, results

print(timeit.timeit('goertzel' ,number = 10000, globals = globals()))


