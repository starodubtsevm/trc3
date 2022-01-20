import math

def goertzel(samples, sample_rate, *freqs):
    """
    Implementation of the Goertzel algorithm, useful for calculating individual
    terms of a discrete Fourier transform.
    `samples` is a windowed one-dimensional signal originally sampled at `sample_rate`.
    The function returns 2 arrays, one containing the actual frequencies calculated,
    the second the coefficients `(real part, imag part, power)` for each of those frequencies.
    For simple spectral analysis, the power is usually enough.
    Example of usage :
        
        freqs, results = goertzel(some_samples, 44100, (400, 500), (1000, 1100))
    """
    window_size = len(samples)
    f_step = sample_rate / float(window_size)
    f_step_normalized = 1.0 / window_size
    # Calculate all the DFT bins we have to compute to include frequencies
    # in `freqs`.
    bins = set()
    #for f_range in freqs:
    #    f_start, f_end = f_range
    #    k_start = int(math.floor(f_start / f_step))
    #    k_end = int(math.ceil(f_end / f_step))
     #   if k_end > window_size - 1: raise ValueError('frequency out of range %s' % k_end)
     #   bins = bins.union(range(k_start, k_end))
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
        results.append((
            0.5 * w_real * d1 - d2, 
            w_imag * d1,
            d2**2 + d1**2 - w_real * d1 * d2)
        )
        freqs.append(f * sample_rate)
    return freqs, results

if __name__ == '__main__':
    import numpy as np
    import pylab

    # generating test signals
    SAMPLE_RATE = 2000
    WINDOW_SIZE = 160
    t = np.linspace(0, 1, SAMPLE_RATE)[:WINDOW_SIZE]
    sine_wave = 4.35*np.sin(2*np.pi*75*t) + 2.59*np.sin(2*np.pi*125*t) + np.sin(2*np.pi*325*t)

    sine_wave3 = []
    for i in range (len(sine_wave)):
        multiplier = 0.5 * (1 - np.cos(2*np.pi*i/WINDOW_SIZE))
        x = multiplier * sine_wave[i]
        sine_wave3.append(x)
    sine_wave = sine_wave3

    # applying Goertzel on those signals, and plotting results
    freqs, results = goertzel(sine_wave, SAMPLE_RATE, (75, 75), (122, 128), (322,328))

    pylab.subplot(2, 2, 1)
    pylab.title('Sine wave 75Hz+125Hz+325Hz (after Hann)')
    pylab.plot(t, sine_wave)

    pylab.subplot(2, 2, 3)
    pylab.title('Goertzel Algo')
    pylab.plot(freqs, np.array(results)[:, 0], 'o')
    print (freqs,np.array(results)[:, 2])
    #pylab.ylim([0,300000])

    pylab.show()

