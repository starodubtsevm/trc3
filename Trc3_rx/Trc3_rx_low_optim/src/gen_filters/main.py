import numpy as np
from calc import *
from plot import *
from print_to_file import *
from print_to_file2 import *
import time
import os

#-фильтры 8 и 12 Гц для приема КРЛ
freqs_MOD = 8, 12  # центральные частоты
band_MOD = 1  # полоса пропускания фильтра
ntaps_MOD = 50  # порядок фильтра
fs_MOD = 50  # частота дискретизации

#-ФНЧ после когерентного детектора
LPF_cut = 14  # частота среза
ntaps_LPF = 42  # порядок фильтра
fs_LPF = 2000  # частота дискретизации

BPF_IN = 600  # центральная частота входного фильтра
BAND_BPF_IN = 460  # полоса пропускания фильтра
ntaps_BPF_IN = 45  # порядок фильтра
fs_BPF_IN = 2000  # частота дискретизации

#--------------------------------------------------------------------------
res = []
start_time = time.time()

##-Очистка каталогов для генерации результатов
cat = ['./Graphics/', "./Headers", "../FIR_models", "./FIR_models"]

[os.system("rm -rf " + cat[i]) for i in range(len(cat))]
[os.mkdir(cat[i]) for i in range(len(cat))]

#--------------------------------------------------------------------------
#-расчет и формирование *.h файлов входного полосового фильтра
taps_BPF_IN = bpf_fir(ntaps_BPF_IN, BPF_IN - BAND_BPF_IN / 2,
                       BPF_IN + BAND_BPF_IN / 2, fs_BPF_IN,"fixed")

prn_headers(taps_BPF_IN, BPF_IN, len(taps_BPF_IN), fs_BPF_IN, '')  # *.h файлов
prn_model_files(taps_BPF_IN, BPF_IN, len(taps_BPF_IN), fs_BPF_IN, '')  # *.py файлов
plot_fr(taps_BPF_IN, BPF_IN, BAND_BPF_IN, ntaps_BPF_IN, fs_BPF_IN, '')  # графики АЧХ

#-расчет и формирование *.h файлов фильтров-8 и 12 Гц---------------------
for i in range(len(freqs_MOD)):
    taps_MOD = bpf_fir(ntaps_MOD, freqs_MOD[i] - band_MOD / 2,
                       freqs_MOD[i] + band_MOD / 2, fs_MOD,"fixed")

    prn_headers(taps_MOD, freqs_MOD[i], len(taps_MOD), fs_MOD, '')  # *.h файлов
    prn_model_files(taps_MOD, freqs_MOD[i], len(taps_MOD), fs_MOD, '')  # *.py файлов
    plot_fr(taps_MOD, freqs_MOD[i], band_MOD, ntaps_MOD, fs_MOD, '')  # графики АЧХ

#-расчет и формирование *.h файлов фильтра низких частот (ФНЧ)------------
taps_LPF = lpf_fir(ntaps_LPF, LPF_cut, fs_LPF,"fixed")

prn_headers(taps_LPF, LPF_cut, len(taps_LPF), fs_LPF, 'L')  # *.h файлов
prn_model_files(taps_LPF, LPF_cut, len(taps_LPF), fs_LPF, '')  # *.py файлов
plot_fr2(taps_LPF, LPF_cut, ntaps_LPF, fs_LPF, 'L')  # графики АЧХ

os.system("rm -rf ../FIR_models/")
os.system("cp -R ./FIR_models/  ../FIR_models/")
os.system("xviewer ./Graphics/")

print(time.time() - start_time, "seconds")
