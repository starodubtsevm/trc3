import time
from conf_model import *
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

krl_rec = krl_receiver(565, 8)
out_buffers = krl_rec.proc(buf_mix_signals)

print("")
print("время расчета - %s sec " % (time.time()-rx))
print("------------------------------------")
#------------------------------------

#--Построение графиков---------------
plot = time.time()
print("старт построения выходных графиков")
to_plot(out_buffers, mix_signals)

#plotSpectrum(mix_signals)
print("время расчета - %s sec " % (time.time()-plot))
print("")
print("------------------------------------")
#------------------------------------
