#!/usr/bin/python3
from time import *
from prep_model import *
from krl_rec import *
from plot2 import *

def create_signals():
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
        print("время расчета - %s sec " % round((time() - prep),2))

        print("")
        print("сгенерированные сигналы")
        print("")
        print(*Signals, sep="\n")
        print("------------------------------------")
        print("")
        return buf_mix_signals, Signals


def create_receiver(buff_mix_signals):
        #- Конфигурирование и запуск приемника
        print("старт модели измерителей АРС и КРЛ")
        print("")
        print(f"приемник {f_rx} Гц {f_mod} Гц")
        print("")

        rx = time()
        krl_rec1 = krl_receiver(f_rx, f_mod)
        krl_rec_out_buffers = krl_rec1.proc(buf_mix_signals)
        print("время расчета - %s sec " % round((time()-rx),2))
        print("")
        print("------------------------------------")
        return krl_rec_out_buffers

def plot_results(krl_rec_out_buffers):
        #--Построение графиков---------------
        #plot = time.time()
        print("построение выходных графиков")

        to_plot(krl_rec_out_buffers, mix_signals)
        #plotSpectrum(mix_signals)

        #print("время расчета - %s sec " % (t   ime.time()-plot))
        print("")
        print("------------------------------------")
        return 0

buf_mix_signals, Signals = create_signals()
krl_rec_out_buffers = create_receiver(buf_mix_signals)
plot_results(krl_rec_out_buffers)


