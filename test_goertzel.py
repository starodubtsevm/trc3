import numpy as np
import pylab

# generating test signals
SAMPLE_RATE = 2000
WINDOW_SIZE = 1024
t = np.linspace(0, 1, SAMPLE_RATE)[:WINDOW_SIZE]
sine_wave = np.sin(2*np.pi*75*t) + np.sin(2*np.pi*125*t) + np.sin(2*np.pi*780*t)

sine_wave2 = []
for i in range (len(sine_wave)): 

	multiplier = 0.5 * (1 - np.cos(2*np.pi*i/WINDOW_SIZE))
	x = multiplier * sine_wave[i]
	sine_wave2.append(x)
sine_wave = sine_wave2
print (sine_wave)

