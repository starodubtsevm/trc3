import numpy as np
from calc import*
from plot import*
from print_to_file import*
from print_to_file2 import*

#-входной (канальный фильтр)
freqs_KRL = 420, 480, 565, 720, 780		# частоты фильтра КРЛ
band_KRL  = 24					# полоса пропускания фильтра
ntaps_KRL = 1000					# порядок фильтра
fs_KRL = 8000

#-фильтр АРС (канал измерения)
freqs_ARS = 75, 125, 175, 225, 275, 325	# частоты фильтра АРС
band_ARS  = 15					# полоса пропускания фильтра
ntaps_ARS = 150					# порядок фильтра
fs_ARS = 1000

#-фильтры 8 и 12 Гц
freqs_MOD = 8, 12
band_MOD = 2
ntaps_MOD = 80
fs_MOD = 100

#-ФНЧ
LPF_cut = 15				# частота среза фнч после детектора
ntaps_LPF = 100				# порядок фильтра
fs_LPF = 100

#--------------------------------------------------------------------------
res = []

#-расчет и формирование *.h файлов входных фильтров-КРЛ---------------------
for i in range (len(freqs_KRL)):
	taps_KRL = bpf_fir(ntaps_KRL, freqs_KRL[i] - band_KRL/2,
	freqs_KRL[i] + band_KRL/2,fs_KRL)
	y = [int(taps_KRL[i] * 32768) for i in range(len(taps_KRL))]
	res.append(y)

	prn_headers(y,freqs_KRL[i], len(taps_KRL),fs_KRL)	# формирование *.h файлов
	prn_model_files(y,freqs_KRL[i], len(taps_KRL),fs_KRL)	# формирование *.py файлов
	plot_fr(y, freqs_KRL[i], band_KRL, ntaps_KRL,fs_KRL)	# формирование графиков АЧХ

#-расчет и формирование *.h файлов входных фильтров-АРС---------------------
for i in range (len(freqs_ARS)):
	taps_ARS = bpf_fir(ntaps_ARS, freqs_ARS[i] - band_ARS/2,
	freqs_ARS[i] + band_ARS/2,fs_ARS)
	y = [int(taps_ARS[i] * 32768) for i in range(len(taps_ARS))]
	res.append(y)

	prn_headers(y,freqs_ARS[i], len(taps_ARS),fs_ARS)	# формирование *.h файлов
	prn_model_files(y,freqs_ARS[i], len(taps_ARS),fs_ARS)	# формирование *.py файлов
	plot_fr(y, freqs_ARS[i], band_ARS, ntaps_ARS,fs_ARS)	# формирование графиков АЧХ

#-расчет и формирование *.h файлов фильтров-8 и 12 Гц---------------------
for i in range (len(freqs_MOD)):
	taps_MOD = bpf_fir(ntaps_MOD, freqs_MOD[i] - band_MOD/2,
	freqs_MOD[i] + band_MOD/2,fs_MOD)
	y = [int(taps_MOD[i] * 32768) for i in range(len(taps_MOD))]
	res.append(y)

	prn_headers(y,freqs_MOD[i], len(taps_MOD),fs_MOD)	# формирование *.h файлов
	prn_model_files(y,freqs_MOD[i], len(taps_MOD),fs_MOD)	# формирование *.py файлов
	plot_fr(y, freqs_MOD[i], band_MOD, ntaps_MOD,fs_MOD)	# формирование графиков АЧХ

#-расчет и формирование *.h файлов фильтра низких частот (ФНЧ)------------
taps_LPF = lpf_fir(ntaps_LPF, LPF_cut,fs_LPF)
y = [int(taps_LPF[i] * 32768) for i in range(len(taps_LPF))]
res.append(y)

prn_headers(y,0, len(taps_LPF),fs_LPF)		# формирование *.h файлов
prn_model_files(y,LPF_cut, len(taps_LPF),fs_LPF)	# формирование *.py файлов
plot_fr2(y, LPF_cut, ntaps_LPF,fs_LPF)		# формирование графиков АЧХ


