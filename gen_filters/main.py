import numpy as np
from calc import*
from plot import*
from print_to_file import*
<<<<<<< HEAD
from print_to_file2 import*
import time


=======
>>>>>>> 634d8e28b209609ed55356b0270ae8b9a1a5ba68

#-входной (канальный фильтр)
freqs_KRL = 420, 480, 565, 720, 780		# частоты фильтра КРЛ
band_KRL  = 24					# полоса пропускания фильтра
ntaps_KRL = 1000				# порядок фильтра
fs_KRL = 8000

#-фильтр АРС (канал измерения)
freqs_ARS = 75, 125, 175, 225, 275, 325		# частоты фильтра АРС
band_ARS  = 15					# полоса пропускания фильтра
ntaps_ARS = 150					# порядок фильтра
fs_ARS = 2000

#-фильтр КРЛ (канал измерения)
freqs_KRLi = 420, 480, 565, 720, 780		# частоты фильтра АРС
band_KRLi  = 24					# полоса пропускания фильтра
ntaps_KRLi = 400				# порядок фильтра
fs_KRLi = 4000

#-фильтры 8 и 12 Гц
freqs_MOD = 8, 12
band_MOD = 2
ntaps_MOD = 80
fs_MOD = 100

#-ФНЧ
LPF_cut = 15				# частота среза фнч после детектора
ntaps_LPF = 100				# порядок фильтра
fs_LPF = 100

# ФНЧ на вых генератора
LPFg_cut = 850				# частота среза фнч после генераторов
ntaps_LPFg = 100			# порядок фильтра
fs_LPFg = 8000

#--------------------------------------------------------------------------
res = []
start_time = time.clock()

#-расчет и формирование *.h файлов входных фильтров-КРЛ---------------------
for i in range (len(freqs_KRL)):
	taps_KRL = bpf_fir(ntaps_KRL, freqs_KRL[i] - band_KRL/2,
	freqs_KRL[i] + band_KRL/2,fs_KRL)
	y = [int(taps_KRL[i] * 32768) for i in range(len(taps_KRL))]
	res.append(y)

	prn_headers(y,freqs_KRL[i], len(taps_KRL),fs_KRL,'')	# формирование *.h файлов
	prn_model_files(y,freqs_KRL[i], len(taps_KRL),fs_KRL,'')	# формирование *.py файлов
	plot_fr(y, freqs_KRL[i], band_KRL, ntaps_KRL,fs_KRL,'')	# формирование графиков АЧХ


#-расчет и формирование *.h файлов измерительных фильтров-КРЛ---------------------
for i in range (len(freqs_KRLi)):
	taps_KRLi = bpf_fir(ntaps_KRLi, freqs_KRLi[i] - band_KRLi/2,
	freqs_KRLi[i] + band_KRLi/2,fs_KRLi)
	y = [int(taps_KRLi[i] * 32768) for i in range(len(taps_KRLi))]
	res.append(y)

	prn_headers(y,freqs_KRLi[i], len(taps_KRLi),fs_KRLi,'I')	# формирование *.h файлов
	prn_model_files(y,freqs_KRLi[i], len(taps_KRLi),fs_KRLi,'I')	# формирование *.py файлов
	plot_fr(y, freqs_KRLi[i], band_KRLi, ntaps_KRLi,fs_KRLi,'I')	# формирование графиков АЧХ

print(time.clock() - start_time, "seconds")

#-расчет и формирование *.h файлов измерительных фильтров-АРС---------------------
for i in range (len(freqs_ARS)):
	taps_ARS = bpf_fir(ntaps_ARS, freqs_ARS[i] - band_ARS/2,
	freqs_ARS[i] + band_ARS/2,fs_ARS)
	y = [int(taps_ARS[i] * 32768) for i in range(len(taps_ARS))]
	res.append(y)

	prn_headers(y,freqs_ARS[i], len(taps_ARS),fs_ARS,'')	# формирование *.h файлов
	prn_model_files(y,freqs_ARS[i], len(taps_ARS),fs_ARS,'')	# формирование *.py файлов
	plot_fr(y, freqs_ARS[i], band_ARS, ntaps_ARS,fs_ARS,'')	# формирование графиков АЧХ

#-расчет и формирование *.h файлов фильтров-8 и 12 Гц---------------------
for i in range (len(freqs_MOD)):
	taps_MOD = bpf_fir(ntaps_MOD, freqs_MOD[i] - band_MOD/2,
	freqs_MOD[i] + band_MOD/2,fs_MOD)
	y = [int(taps_MOD[i] * 32768) for i in range(len(taps_MOD))]
	res.append(y)

	prn_headers(y,freqs_MOD[i], len(taps_MOD),fs_MOD,'')	# формирование *.h файлов
	prn_model_files(y,freqs_MOD[i], len(taps_MOD),fs_MOD,'')	# формирование *.py файлов
	plot_fr(y, freqs_MOD[i], band_MOD, ntaps_MOD,fs_MOD,'')	# формирование графиков АЧХ

#-расчет и формирование *.h файлов фильтра низких частот (ФНЧ)------------
taps_LPF = lpf_fir(ntaps_LPF, LPF_cut,fs_LPF)
y = [int(taps_LPF[i] * 32768) for i in range(len(taps_LPF))]
res.append(y)

prn_headers(y,LPF_cut, len(taps_LPF),fs_LPF,'L')		# формирование *.h файлов
prn_model_files(y,LPF_cut, len(taps_LPF),fs_LPF,'')	# формирование *.py файлов
plot_fr2(y, LPF_cut, ntaps_LPF,fs_LPF,'L')		# формирование графиков АЧХ

#-расчет и формирование *.h файлов ФНЧ на выходе генераторов------------
taps_LPFg = lpf_fir(ntaps_LPFg, LPFg_cut,fs_LPFg)
y = [int(taps_LPFg[i] * 32768) for i in range(len(taps_LPFg))]
res.append(y)

prn_headers(y,LPFg_cut, len(taps_LPFg),fs_LPFg,'L')		# формирование *.h файлов
prn_model_files(y,LPFg_cut, len(taps_LPFg),fs_LPFg,'')	# формирование *.py файлов
plot_fr2(y, LPFg_cut, ntaps_LPFg,fs_LPFg,'L')		# формирование графиков АЧХ


