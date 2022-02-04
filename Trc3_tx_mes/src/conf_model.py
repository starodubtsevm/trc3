from sig_gen import sig_gen

simulation_time = 4  # time of simulation

fs = 4000.0  # main sampling frequency
fs2 = 100.0  # sampling frequency 2
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
    Signals = [["Частота ","Амплитуда ","Модуляция"],
               [420, 3 * 1024, 8 ],
               [480, 0 * 1024, 12],
               [565, 1 * 1024, 8 ],
               [720, 1 * 1024, 12],
               [780, 1 * 1024, 8 ],
               [ 75, 3 * 1024, 0 ],
               [125, 0 * 1024, 0 ],
               [175, 2 * 1024, 0 ],
               [225, 0 * 1024, 0 ],
               [275, 1 * 1024, 0 ],
               [325, 1.5 * 1024, 0 ]]

    mix_signals = [0]*sim_point

    for signal in Signals:
        if isinstance(signal[1], int):
            if signal[1] > 0:
                y = sig_gen(signal,Time)
                mix_signals= [a + b for a, b in zip(mix_signals, y)]

    return mix_signals, Signals
