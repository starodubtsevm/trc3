import time
from prep_model import *
from krl_rec import *
from plot2 import *

print("")
print("fs = " + str(fs) + " Hz")
print("fs2 = " + str(fs2) + " Hz")
print("")

#- Конфигурирование генераторов
prep = time.time()
print("------------------------------------")
print("старт расчета смеси входных сигналов")
print("")

buf_mix_signals, Signals = mix_signals()

print("время расчета - %s sec " % (time.time() - prep))
print("")
print("сгенерированные сигналы")
print("")
print(*Signals, sep="\n")
print("------------------------------------")
print("")
#------------------------------------

#- Конфигурирование и запуск приемника
rx = time.time()
print("старт модели измерителей АРС и КРЛ")

krl_rec1 = krl_receiver(565, 8)
krl_rec_out_buffers = krl_rec1.proc(buf_mix_signals)

print("")
print("время расчета - %s sec " % (time.time()-rx))
print("------------------------------------")
#------------------------------------

#--Построение графиков---------------
#plot = time.time()
print("построения выходных графиков")

to_plot(krl_rec_out_buffers, mix_signals)
#plotSpectrum(mix_signals)

#print("время расчета - %s sec " % (time.time()-plot))
print("")
print("------------------------------------")
#------------------------------------
