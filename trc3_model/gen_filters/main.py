import numpy as np
from calc import *
from plot import *
from print_to_file import *
from print_to_file2 import *
import time
import os

#-входной (канальный фильтр)
freqs_KRL = 420, 480, 565, 720, 780  # частоты фильтра КРЛ
band_KRL = 24  # полоса пропускания фильтра
ntaps_KRL = 1000  # порядок фильтра
fs_KRL = 4000  # частота дискретизации

#-фильтр АРС (канал измерения)
freqs_ARS = 75, 125, 175, 225, 275, 325  # частоты фильтра АРС
band_ARS = 15  # полоса пропускания фильтра
ntaps_ARS = 150  # порядок фильтра
fs_ARS = 4000  # частота дискретизации

#-фильтр КРЛ (канал измерения)
freqs_KRLi = 420, 480, 565, 720, 780  # частоты фильтра
band_KRLi = 24  # полоса пропускания фильтра
ntaps_KRLi = 200  # порядок фильтра
fs_KRLi = 4000  # частота дискретизации

#-фильтры 8 и 12 Гц
freqs_MOD = 8, 12  # частоты фильтра
band_MOD = 2  # полоса пропускания фильтра
ntaps_MOD = 100  # порядок фильтра
fs_MOD = 100  # частота дискретизации

#--------------------------------------------------------------------------
res = []
start_time = time.time()

##-Очистка каталогов для генерации результатов
cat = ['./Graphics/', "./FIR_models/", "./Headers", "../FIR_models"]

[os.system("rm -rf " + cat[i]) for i in range(len(cat))]
[os.mkdir(cat[i]) for i in range(len(cat))]

#-расчет и формирование *.h файлов входных фильтров-КРЛ-------------------
for i in range(len(freqs_KRL)):
    taps_KRL = bpf_fir(ntaps_KRL, freqs_KRL[i] - band_KRL / 2,
                       freqs_KRL[i] + band_KRL / 2, fs_KRL)
    y = [int(taps_KRL[i] * 32768) for i in range(len(taps_KRL))]

    prn_headers(y, freqs_KRL[i], len(taps_KRL), fs_KRL, '')  # *.h файлы
    prn_model_files(y, freqs_KRL[i], len(taps_KRL), fs_KRL, '')  #  *.py файлы
    plot_fr(y, freqs_KRL[i], band_KRL, ntaps_KRL, fs_KRL, '')  # графики АЧХ

#-расчет и формирование *.h файлов измерительных фильтров-КРЛ-------------
for i in range(len(freqs_KRLi)):
    taps_KRLi = bpf_fir(ntaps_KRLi, freqs_KRLi[i] - band_KRLi / 2,
                        freqs_KRLi[i] + band_KRLi / 2, fs_KRLi)
    y = [int(taps_KRLi[i] * 32768) for i in range(len(taps_KRLi))]

    prn_headers(y, freqs_KRLi[i], len(taps_KRLi), fs_KRLi, 'I')  # *.h файлы
    prn_model_files(y, freqs_KRLi[i], len(taps_KRLi), fs_KRLi,
                    'I')  # *.py файлов
    plot_fr(y, freqs_KRLi[i], band_KRLi, ntaps_KRLi, fs_KRLi,
            'I')  # графики АЧХ

#-расчет и формирование *.h файлов измерительных фильтров-АРС-------------
for i in range(len(freqs_ARS)):
    taps_ARS = bpf_fir(ntaps_ARS, freqs_ARS[i] - band_ARS / 2,
                       freqs_ARS[i] + band_ARS / 2, fs_ARS)
    y = [int(taps_ARS[i] * 32768) for i in range(len(taps_ARS))]

    prn_headers(y, freqs_ARS[i], len(taps_ARS), fs_ARS, '')  # *.h файлы
    prn_model_files(y, freqs_ARS[i], len(taps_ARS), fs_ARS, '')  # *.py файлов
    plot_fr(y, freqs_ARS[i], band_ARS, ntaps_ARS, fs_ARS, '')  # графики АЧХ

#-расчет и формирование *.h файлов фильтров-8 и 12 Гц---------------------
for i in range(len(freqs_MOD)):
    taps_MOD = bpf_fir(ntaps_MOD, freqs_MOD[i] - band_MOD / 2,
                       freqs_MOD[i] + band_MOD / 2, fs_MOD)
    y = [int(taps_MOD[i] * 32768) for i in range(len(taps_MOD))]

    prn_headers(y, freqs_MOD[i], len(taps_MOD), fs_MOD, '')  # *.h файлы
    prn_model_files(y, freqs_MOD[i], len(taps_MOD), fs_MOD, '')  # *.py файлы
    plot_fr(y, freqs_MOD[i], band_MOD, ntaps_MOD, fs_MOD, '')  # графики АЧХ

os.system("rm -rf ../FIR_models/")
os.system("cp -R ./FIR_models/  ../FIR_models/")
os.system("xviewer ./Graphics/")

print(time.time() - start_time, "seconds")
