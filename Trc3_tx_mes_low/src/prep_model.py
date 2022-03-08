from sig_gen import sig_gen
import configparser


def read_config() -> list:

    config = configparser.ConfigParser()
    f = config.read("../config_model.ini")  # читаем конфиг
    s = config.sections()
    
    simulation_time = int(config['Simulation_time']['t'])
    fs = int(config['Fs']['fs'])
    fs2 = int(config['Fs2']['fs2'])
    f_rx = int(config['RX']['f'])
    f_mod = int(config['RX']['fmod'])
    tr = int(config['RX']['tr'])

    xSignals = []
    
    for signal in ('f1', 'f2', 'f3', 'f4', 'f5'):
        string = config['KRL_signals'][signal]
        xSignals.append([int(i) for i in string.split(",")])

    for signal in ('f1', 'f2', 'f3', 'f4', 'f5', 'f6'):
        string = config['ARS_signals'][signal]
        xSignals.append([int(i) for i in string.split(",")])

    return simulation_time, fs, fs2, f_rx, f_mod, tr, xSignals


def input_signals(mix_signals, xSignals) -> list:

    for signal in xSignals:
        if int(signal[1]) > 0:
            mix_signals = [a + b for a, b in zip(mix_signals,
            sig_gen(signal, Time))]
    return mix_signals, xSignals


def progress(sim_point, percent=0, width=40):
    percent = int(percent/(sim_point/100))
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']', f' {percent:.0f}%',
    sep='', end='', flush=True)


simulation_time, fs, fs2, f_rx, f_mod, tr, xSignals = read_config()

PERIOD_S = 1.0 / fs
SIM_POINT = int(simulation_time / PERIOD_S)
DEC_COEF = int(fs / fs2)
WINDOW_FFT = 80  
mix_signals = [0] * SIM_POINT
Time = tuple(n * PERIOD_S for n in range(0, SIM_POINT))
