from time import *
from time import sleep
from prep_model import *
from krl_rec import *
from plot2 import *

print("")
print("fs = " + str(fs) + " Hz")
print("fs2 = " + str(fs2) + " Hz")
print("")

#- Конфигурирование генераторов
print("------------------------------------")
print("старт расчета смеси входных сигналов")
print("")

prep = time()
buf_mix_signals, Signals = mix_signals()
print("время расчета - %s sec " % (time() - prep))

print("")
print("сгенерированные сигналы")
print("")
print(*Signals, sep="\n")
print("------------------------------------")
print("")
#------------------------------------

#- Конфигурирование и запуск приемника
print("старт модели измерителей АРС и КРЛ")
print("")
print(f"приемник {f_rx} Гц {f_mod} Гц")
print("")

rx = time()
krl_rec1 = krl_receiver(f_rx, f_mod)
krl_rec_out_buffers = krl_rec1.proc(buf_mix_signals)
print("время расчета - %s sec " % (time()-rx))

print("")
print("------------------------------------")
#------------------------------------

#--Построение графиков---------------
#plot = time.time()
print("построение выходных графиков")

to_plot(krl_rec_out_buffers, mix_signals)
#plotSpectrum(mix_signals)

#print("время расчета - %s sec " % (time.time()-plot))
print("")
print("------------------------------------")
#------------------------------------
