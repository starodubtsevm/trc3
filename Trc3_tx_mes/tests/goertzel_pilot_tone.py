from math import cos, sin, pi
import timeit
import pylab

def goertzel(samples, sample_rate, FREQ):

    window_size = len(samples)
    f_step_normalized = 1.0 / window_size
    bins = {36}
    print (bins)

    # For all the bins, calculate the DFT term
    n_range = range(0, window_size)
    freqs = []
    results = []
    for k in bins:
        # Bin frequency and coefficients for the computation
        f = k * f_step_normalized
        w_real = 2.0 * cos(2.0 * pi * f)
        w_imag = sin(2.0 * pi * f)
        # Doing the calculation on the whole sample
        d1, d2 = 0.0, 0.0
        for n in n_range:
            y  = samples[n] + w_real * d1 - d2
            d2, d1 = d1, y
        # Storing results `(real part, imag part, power)`
        results.append((0,0,
            #0.5 * w_real * d1 - d2, 
            #w_imag * d1,
            d2**2 + d1**2 - w_real * d1 * d2))
        freqs.append(int(f * sample_rate))

    return freqs, results

def print_results(*args):

    pylab.subplot(2, 2, 1)
    pylab.title('Sine wave after Hann')
    pylab.plot(time, sine_wave)

    pylab.subplot(2, 2, 3)
    pylab.title('Goertzel Algo')
    pylab.plot(freqs, results[0][2], 'o')
    print (freqs,results)

    pylab.show()

if __name__ == '__main__':

    # generating test signals
    SAMPLE_RATE = 2000
    WINDOW_SIZE = 80
    FREQ = 900
    sine_wave = []
    sine_wave_temp = []
    time = []
    
    for n in range (WINDOW_SIZE):
        t = (1 / SAMPLE_RATE) * n
        time.append(t)
        sine_wave.append(sin(2 * 3.14 * FREQ * t))

    for i in range (len(sine_wave)):
        multiplier = 0.5 * (1 - cos(2*pi*i/WINDOW_SIZE))
        x = multiplier * sine_wave[i]
        sine_wave_temp.append(x)
    sine_wave = sine_wave_temp

    freqs, results = goertzel(sine_wave, SAMPLE_RATE, FREQ)
    print_results(freqs, results)


