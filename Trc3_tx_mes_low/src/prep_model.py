from sig_gen import sig_gen
import configparser
import os

EXAMPLE_CONFIG = """
# конфигурационный файл для построения модели измерителей КРЛ и АРС
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
f= 565
fmod= 8
tr= 43
"""

def read_config() -> list:

    xSignals = []
    type_data = ('KRL_signals', 'ARS_signals')
    PATH = "../config_model.ini"

    try:
        config = configparser.ConfigParser()
        configuration = config.read(PATH)

        SIMULATION_TIME = int(config['Simulation_time']['t'])
        FS = int(config['Fs']['fs'])
        FS2 = int(config['Fs2']['fs2'])
        F_RX = int(config['RX']['f'])
        F_MOD = int(config['RX']['fmod'])
        TR = int(config['RX']['tr'])
#        WINDOW_F = int(config['FFT']['window'])
#        BINS =

        for count, data in enumerate(type_data):
            freqs = list(config[type_data[count]])
            for freq in freqs:
                string = config[data][freq]
                xSignals.append([int(item) for item in string.split(",")])
    except Exception:
        print("Ошибка чтения файла конфигурации!")
        try:
            os.system("rm -rf PATH")
            out_file = open(PATH, "wt")
            out_file.write(EXAMPLE_CONFIG)
            out_file.close
            print("Создаю новый конфигурационный файл... " + PATH)
            print("Настройте конфигурационный файл.")
            exit()
        except:
            print("Ошибка работы с файлом!")
            exit()
    return SIMULATION_TIME, FS, FS2, F_RX, F_MOD, TR, xSignals


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
