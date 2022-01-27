import numpy as np

fs = 4000.0  # main sampling frequency
fs2 = 100.0  # sampling frequency 2
dec_coef = fs / fs2
t_sim = 3  # time of simulation
sim_point = int(t_sim / (1.0 / fs))
sim_point2 = int(t_sim / (1.0 / fs2))
t = np.linspace(0, t_sim, sim_point)
t2 = np.linspace(0, t_sim, sim_point2)

inp_signal_buff = [0] * sim_point
