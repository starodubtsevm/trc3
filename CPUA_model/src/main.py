from time import time
from prep_model import fs, fs2
from krl_rec import *
from plot2 import *

prep = time()
# ------------------------------------
print("------------------------------------")
print("")
print("FS = " + str(fs) + " Hz")
print("FS2 = " + str(fs2) + " Hz")
print("WINDOW_FFT = " + str(window))
print("")

# Конфигурирование генераторов
print("------------------------------------")
print("старт расчета смеси входных сигналов")
print("")

buf_mix_signals, Signals = input_signals(mix_signals, xSignals)
print("время расчета - %s sec " % round((time() - prep), 3))

print("")
print("сгенерированные сигналы")
print("")
print(*Signals, sep="\n")
print("------------------------------------")
print("")
# ------------------------------------

# Конфигурирование и запуск приемника 1
print("старт модели измерителей АРС и КРЛ")
print("")
print(f"приемник {f_rx} Гц {f_mod} Гц")
print("")

rx = time()
receiver1 = CrlReceiver(f_rx, f_mod)
crl_rec_out_buffers1 = receiver1.proc(buf_mix_signals)
print("время расчета - %s sec " % round((time()-rx), 3))
print("")
print("------------------------------------")
# ------------------------------------

# Конфигурирование и запуск приемника 2
print("старт модели измерителей АРС и КРЛ")
print("")
print(f"приемник {720} Гц {12} Гц")
print("")

rx = time()
receiver2 = CrlReceiver(720, 12)
crl_rec_out_buffers2 = receiver2.proc(buf_mix_signals)
print("время расчета - %s sec " % round((time()-rx), 3))
print("")
print("------------------------------------")
# ------------------------------------

# --Построение графиков---------------
#plot = time.time()
print("построение выходных графиков")

to_plot(crl_rec_out_buffers1, input_signals, 1)
to_plot(crl_rec_out_buffers2, input_signals, 2)

#print("время расчета - %s sec " % (t   ime.time()-plot))
print("")
print("------------------------------------")
# ------------------------------------
