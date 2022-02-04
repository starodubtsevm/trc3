from sig_gen import sig_gen
import configparser

config = configparser.ConfigParser()
f = config.read("../config_model.ini")  # читаем конфиг
s = config.sections()

simulation_time = config['Simulation_time']['t']
fs = config['Fs']['fs']
fs2 = config['Fs2']['fs2']

xSignals = []

type_of_signal = ['KRL_signals', 'ARS_signals']

number_freqs = [['f1','f2','f3','f4','f5'],
                ['f1','f2','f3','f4','f5','f6']]

##print(len(number_freqs[1]))
##exit()
#for sig in range (len(type_of_signal)):
#    for n in range (len(number_freqs[sig])):
#        for i in range (len(n[sig])):
#            k_f = config[type_of_signal[sig]][number_freqs[n][i]]
#            l = [int(i) for i in k_f.split(",")]
#            xSignals.append(l)
#exit()

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

f_rx = config['RX']['f']
f_rx = int(f_rx)

f_mod = config['RX']['fmod']
f_mod = int(f_mod)

tr = config['RX']['tr']
tr = int(tr)

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

def progress(percent=0, width=40):
    percent = int(percent/(sim_point/100))
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',f' {percent:.0f}%',
    sep='', end='', flush=True)

