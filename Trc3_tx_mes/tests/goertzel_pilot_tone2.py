from math import cos, sin, pi
import timeit
import pylab


SAMPLE_RATE = 2000
WINDOW_SIZE = 361
target_freqs = [420, 480, 565, 720, 780, 393, 803]
input_signal = [0] * WINDOW_SIZE
two_pi = 2 * pi

#----------------------------------------------------------------------

def goertzel(samples, input_freqs):

    freqs = []
    results = []
    bins = []
    f_step_normalized = 1.0 / WINDOW_SIZE

    freqs = []
    f_step_normalized = 1.0 / window_size
    n_range = range(0, window_size)

    for i in range (len(in_freqs)):
        bins.append(round(WINDOW_SIZE * in_freqs[i] / SAMPLE_RATE))

    for k in bins:
        # Bin frequency and coefficients for the computation
        f = k * f_step_normalized
        w_real = 2.0 * cos(two_pi * f)
        w_imag = sin(two_pi * f)
        # Doing the calculation on the whole sample

        
    for num, freq in enumerate(input_freqs):

        bins.append(round(WINDOW_SIZE * freq / SAMPLE_RATE))
        f_normalized = bins[num] * f_step_normalized
        w_real = 2.0 * cos(two_pi * f_normalized)
        w_imag = sin(two_pi * f_normalized)
        d1, d2 = 0.0, 0.0
        for sample in samples:
            y = sample + w_real * d1 - d2
            d2, d1 = d1, y
        results.append(round(d2 * d2 + d1 * d1 - w_real * d1 * d2))
        freqs.append(round(f_normalized * SAMPLE_RATE))

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
        sine_wave.append(sin(two_pi * freq * t))
    return sine_wave

def Hann_filter(input_signal):

    sine_wave =[]
    for tick, value in enumerate(input_signal):
        sine_wave.append(0.5 * (1 - cos(two_pi * tick / WINDOW_SIZE)) * (value))
    return sine_wave

#----------------------------------------------------------------------

Time = gen_time_ticks()

# Working signals
for num in range (len(target_freqs)):
    y = gen_sin(target_freqs[num], Time)
    input_signal= [a + b for a, b in zip(input_signal, y)]


sine_waves_after_Hann_filter = Hann_filter(input_signal)
freqs, results, bins = goertzel(sine_waves_after_Hann_filter, target_freqs)
plot_results(freqs, results, Time, bins)

