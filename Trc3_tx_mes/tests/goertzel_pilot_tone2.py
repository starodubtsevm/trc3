from math import cos, sin, pi
import timeit
import pylab


SAMPLE_RATE = 2000
WINDOW_SIZE = 80
target_freqs = [900, 400, 600]
input_signal = [0] * WINDOW_SIZE

#----------------------------------------------------------------------

def goertzel(samples, sample_rate, freqs):

    window_size = len(samples)
    f_step_normalized = 1.0 / window_size
    bins = []

    for i in range (len(freqs)):
        bins.append(int(WINDOW_SIZE * freqs[i] / SAMPLE_RATE))

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
        results.append(int(d2**2 + d1**2 - w_real * d1 * d2))
        freqs.append(int(f * sample_rate))

    return freqs, results, bins

def plot_results(freqs, results, Time, bins):

    pylab.title('Goertzel algo results')
    pylab.plot(freqs, results, 'o')
    print (freqs, results, bins)

    pylab.show()

def gen_time_ticks():

    Time = []
    for num in range (WINDOW_SIZE):
        Time.append((1 / SAMPLE_RATE) * num)

    return Time

def gen_sin(freq, Time):

    sine_wave = []
    for t in Time:
        sine_wave.append(sin(2 * 3.14 * freq * t))

    return sine_wave

def Hann_filter(input_signal):

    sine_wave_temp =[]
    for i in range (len(input_signal)):
        multiplier = 0.5 * (1 - cos(2*pi*i/WINDOW_SIZE))
        x = multiplier * input_signal[i]
        sine_wave_temp.append(x)

    return sine_wave_temp

#----------------------------------------------------------------------

Time = gen_time_ticks()

for num in range (len(target_freqs)):
    print (target_freqs[num])
    y = gen_sin(target_freqs[num], Time)
    input_signal= [a + b for a, b in zip(input_signal, y)]

sine_waves_after_Hann_filter = Hann_filter(input_signal)
freqs, results, bins = goertzel(sine_waves_after_Hann_filter, SAMPLE_RATE, target_freqs)
plot_results(freqs, results, Time, bins)


