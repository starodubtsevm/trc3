from math import cos, sin, pi
import timeit
import pylab


#SAMPLE_RATE = 2000
#WINDOW_SIZE = 361
#target_freqs = (420, 480, 565, 720, 780, 393, 803)

FS = 100
WINDOW_SIZE = int(FS * 1.5)
SIMULATION_TIME = 1
SIM_POINT = WINDOW_SIZE
target_freqs = (7,8,9,11,12,13)
input_freqs = [13,14,7,8,16]
A = [4,4,4,8,4]
input_signal = [0] * WINDOW_SIZE 
two_pi = 2 * pi

#----------------------------------------------------------------------

def goertzel(samples, input_freqs):

    freqs = []
    results = []
    f_step_normalized = 1.0 / WINDOW_SIZE

    bins = tuple(WINDOW_SIZE * freq / FS for freq in input_freqs)
    
    for bine in bins:
        f_normalized = bine * f_step_normalized
        freqs.append(f_normalized * FS)
        w_real = 2.0 * cos(two_pi * f_normalized)
        w_imag = sin(two_pi * f_normalized)
        d1, d2 = 0.0, 0.0
        for sample in samples:
            y = sample + w_real * d1 - d2
            d2, d1 = d1, y
        results.append(round(d2 * d2 + d1 * d1 - w_real * d1 * d2))

    return freqs, results, bins

def plot_results(freqs, results, Time, bins):

    pylab.title('Goertzel algo results')
    pylab.plot(freqs, results, 'o')
    print (freqs, results, bins)

    pylab.show()

def gen_time_ticks():

    return tuple(n / FS for n in range(0, SIM_POINT))

def gen_sin(freq, A, Time):

    sine_wave = []
    for t in Time:
        sine_wave.append(A*sin(two_pi * freq * t))
    return sine_wave

def Hann_filter(input_signal):

    sine_wave =[]
    for tick, value in enumerate(input_signal):
        sine_wave.append(0.5 * (1 - cos(two_pi * tick / WINDOW_SIZE)) * (value))
    return sine_wave

#----------------------------------------------------------------------

Time = gen_time_ticks()

# Входная смесь сигналов
for num, freq, in enumerate(input_freqs):
    input_signal= [a + b for a, b in zip(input_signal, gen_sin(freq, A[num], Time))]

pylab.plot(Time, input_signal)
pylab.show()

sine_waves_after_Hann_filter = Hann_filter(input_signal)
freqs, results, bins = goertzel(sine_waves_after_Hann_filter, target_freqs)
plot_results(freqs, results, Time, bins)
