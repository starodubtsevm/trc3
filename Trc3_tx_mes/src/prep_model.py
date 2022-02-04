from sig_gen import sig_gen
import configparser

config = configparser.ConfigParser()
f = config.read("config_model.ini")  # читаем конфиг
s = config.sections()

simulation_time = config['Simulation_time']['t']
fs = config['Fs']['fs']
fs2 = config['Fs2']['fs2']

xSignals = []

k_f = config['KRL_signals']['f1']
l = [int(i) for i in k_f.split(",")]
xSignals.append(l)
k_f = config['KRL_signals']['f2']
l = [int(i) for i in k_f.split(",")]
xSignals.append(l)
k_f = config['KRL_signals']['f3']
l = [int(i) for i in k_f.split(",")]
xSignals.append(l)
k_f = config['KRL_signals']['f4']
l = [int(i) for i in k_f.split(",")]
xSignals.append(l)
k_f = config['KRL_signals']['f5']
l = [int(i) for i in k_f.split(",")]
xSignals.append(l)
k_f = config['ARS_signals']['f1']
l = [int(i) for i in k_f.split(",")]
xSignals.append(l)
k_f = config['ARS_signals']['f2']
l = [int(i) for i in k_f.split(",")]
xSignals.append(l)
k_f = config['ARS_signals']['f3']
l = [int(i) for i in k_f.split(",")]
xSignals.append(l)
k_f = config['ARS_signals']['f4']
l = [int(i) for i in k_f.split(",")]
xSignals.append(l)
k_f = config['ARS_signals']['f5']
l = [int(i) for i in k_f.split(",")]
xSignals.append(l)
k_f = config['ARS_signals']['f6']
l = [int(i) for i in k_f.split(",")]
xSignals.append(l)


simulation_time = int(simulation_time)
fs = int(fs)
fs2 = int(fs2)

dec_coef = fs / fs2

sim_point = int(simulation_time / (1.0 / fs))
sim_point2 = int(simulation_time / (1.0 / fs2))

Time=[]
Time2=[]

for t in range (0, sim_point):
    Time.append(t*1.0/fs)
    
for t in range (0, sim_point2):
    Time2.append(t*1.0/fs2)

def mix_signals()->list:

    mix_signals = [0]*sim_point
    
    for signal in xSignals:
            if int(signal[1]) > 0:
                y = sig_gen(signal,Time)
                mix_signals= [a + b for a, b in zip(mix_signals, y)]

    return mix_signals, xSignals

