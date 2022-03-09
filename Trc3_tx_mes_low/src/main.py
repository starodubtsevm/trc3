from time import time
from prep_model import *
from krl_rec import *
from plot2 import *

prep = time()
# ------------------------------------
print("------------------------------------")
print("")
print("Fs = " + str(fs) + " Hz")
print("Fs2 = " + str(fs2) + " Hz")
print("WINDOW_FFT = " + str(WINDOW_FFT))
print("")

# Конфигурирование генераторов
print("------------------------------------")
print("старт расчета смеси входных сигналов")
print("")

buf_mix_signals, Signals = input_signals(mix_signals, xSignals)
print("время расчета - %s sec " % round((time() - prep),2))

print("")
print("сгенерированные сигналы")
print("")
print(*Signals, sep="\n")
print("------------------------------------")
print("")
# ------------------------------------

# Конфигурирование и запуск приемника
print("старт модели измерителей АРС и КРЛ")
print("")
print(f"приемник {f_rx} Гц {f_mod} Гц")
print("")

rx = time()
krl_rec1 = KrlReceiver(f_rx, f_mod)
krl_rec_out_buffers = krl_rec1.proc(buf_mix_signals)
print("время расчета - %s sec " % round((time()-rx), 2))

print("")
print("------------------------------------")
# ------------------------------------

# --Построение графиков---------------
#plot = time.time()
print("построение выходных графиков")

to_plot(krl_rec_out_buffers, input_signals, 1)
#plotSpectrum(mix_signals)

#print("время расчета - %s sec " % (t   ime.time()-plot))
print("")
print("------------------------------------")
# ------------------------------------
