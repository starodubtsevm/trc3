from sig_gen import sig_gen
import configparser
import os
import sys

EXAMPLE_CONFIG = """
# конфигурационный файл для построения модели модуля ЦОС процессора А
# config_model.ini
[Simulation_time]
t= 4

[Fs]
fs= 2000

[Fs2]
fs2= 100

[KRL_signals]
f1= 420, 0, 8
f2= 480, 0, 12
f3= 565, 1024, 8
f4= 720, 1024, 12
f5= 780, 2048, 8

[ARS_signals]
f1= 75, 2048, 0
f2= 125, 0, 0
f3= 175, 0, 0
f4= 225, 1024, 0
f5= 275, 1700, 0
f6= 325, 0, 0

[RX]
f= 780
fmod= 8
tr= 43

[RX2]
f= 420
fmod= 12
tr= 43

[FFT]
window=80
bins=3,5,7,9,11,13
"""


def read_config() -> list:

    type_sig = ('KRL_signals', 'ARS_signals')
    PATH = "../config_model.ini"
    xSignals = []

    try:
        config = configparser.ConfigParser()
        configuration = config.read(PATH)

        fs = int(config['Fs']['fs'])
        f_rx = int(config['RX']['f'])
        fs2 = int(config['Fs2']['fs2'])
        f_mod = int(config['RX']['fmod'])
        threshold = int(config['RX']['tr'])
        window = int(config['FFT']['window'])
        simulation_time = int(config['Simulation_time']['t'])
        bins = tuple(map(int, config['FFT']['bins'].split(",")))

        for count, data in enumerate(type_sig):
            freqs = list(config[type_sig[count]])
            for freq in freqs:
                xSignals.append([int(item) 
                for item in config[data][freq].split(",")])

    except KeyError:
        print("Ошибка чтения файла конфигурации!")
        try:
            os.system("rm -rf PATH")
            with open(PATH, "wt") as file:
                file.write(EXAMPLE_CONFIG)

            print("Создаю новый конфигурационный файл... " + PATH)
            print("Проверьте конфигурационный файл.")
            sys.exit()
        except OSError:

            print("Ошибка работы с файлом!")
            sys.exit()

    return simulation_time, fs, fs2, f_rx, f_mod, threshold, xSignals, bins, window


def input_signals(mix_signals, xSignals) -> list:

    for signal in xSignals:
        if signal[1] > 0:
            mix_signals = [a + b for a, b in zip(mix_signals,
            sig_gen(signal, Time))]
    return mix_signals, xSignals


def progress(sim_point, percent=0, width=40):

    percent = int(percent/(sim_point/100))
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']', f' {percent:.0f}%',
    sep='', end='', flush=True)


simulation_time, fs, fs2, f_rx, f_mod, threshold, xSignals, bins, window = read_config()

SIM_POINT = int(simulation_time * fs)
dec_coef = int(fs / fs2)
mix_signals = [0] * SIM_POINT
Time = tuple(n / fs for n in range(0, SIM_POINT))
