import numpy as np
from calc import *
from plot import *
from print_to_file import *
from print_to_file2 import *
import time
import os

#-общий входной фильтр (КРЛ)
freqs_KRLg = 600  # центральная частота
band_KRLg = 440  # полоса пропускания фильтра
ntaps_KRLg = 100  # порядок фильтра
fs_KRLg = 4000  # частота дискретизации

#-фильтры 8 и 12 Гц для приема КРЛ
freqs_MOD = 8, 12  # центральные частоты
band_MOD = 2  # полоса пропускания фильтра
ntaps_MOD = 100  # полоса пропускания фильтра
fs_MOD = 100  # частота дискретизации

#-ФНЧ после когерентного детектора
LPF_cut = 14  # частота среза
ntaps_LPF = 400  # порядок фильтра
fs_LPF = 4000  # частота дискретизации

#--------------------------------------------------------------------------
res = []
start_time = time.time()

##-Очистка каталогов для генерации результатов
cat = ['./Graphics/', "./Headers", "../FIR_models", "./FIR_models"]

[os.system("rm -rf " + cat[i]) for i in range(len(cat))]
[os.mkdir(cat[i]) for i in range(len(cat))]

#--------------------------------------------------------------------------
#-расчет и формирование *.h файлов группового входных фильтра-КРЛ----------
taps_KRLg = bpf_fir(ntaps_KRLg, freqs_KRLg - band_KRLg / 2,
                    freqs_KRLg + band_KRLg / 2, fs_KRLg)
y = [int(taps_KRLg[i] * 32768) for i in range(len(taps_KRLg))]

prn_headers(y, freqs_KRLg, len(taps_KRLg), fs_KRLg, '')  # *.h файлов
prn_model_files(y, freqs_KRLg, len(taps_KRLg), fs_KRLg, '')  # *.py файлы
plot_fr(y, freqs_KRLg, band_KRLg, ntaps_KRLg, fs_KRLg, '')  # графики АЧХ

#-расчет и формирование *.h файлов фильтров-8 и 12 Гц---------------------
for i in range(len(freqs_MOD)):
    taps_MOD = bpf_fir(ntaps_MOD, freqs_MOD[i] - band_MOD / 2,
                       freqs_MOD[i] + band_MOD / 2, fs_MOD)
    y = [int(taps_MOD[i] * 32768) for i in range(len(taps_MOD))]

    prn_headers(y, freqs_MOD[i], len(taps_MOD), fs_MOD, '')  # *.h файлов
    prn_model_files(y, freqs_MOD[i], len(taps_MOD), fs_MOD, '')  # *.py файлов
    plot_fr(y, freqs_MOD[i], band_MOD, ntaps_MOD, fs_MOD, '')  # графики АЧХ

#-расчет и формирование *.h файлов фильтра низких частот (ФНЧ)------------
taps_LPF = lpf_fir(ntaps_LPF, LPF_cut, fs_LPF)
y = [int(taps_LPF[i] * 32768) for i in range(len(taps_LPF))]

prn_headers(y, LPF_cut, len(taps_LPF), fs_LPF, 'L')  # *.h файлов
prn_model_files(y, LPF_cut, len(taps_LPF), fs_LPF, '')  # *.py файлов
plot_fr2(y, LPF_cut, ntaps_LPF, fs_LPF, 'L')  # графики АЧХ

os.system("rm -rf ../FIR_models/")
os.system("cp -R ./FIR_models/  ../FIR_models/")

print(time.time() - start_time, "seconds")
