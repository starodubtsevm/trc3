


# freq, mod
def rec (f, fmod):

	krl_f = {
		"420Hz": "файл фильтра 420 Гц",
		"480Hz": "файл фильтра 480 Гц",
		"565Hz": "файл фильтра 565 Гц",
		"720Hz": "файл фильтра 720 Гц",
		"780Hz": "файл фильтра 780 Гц",
		"8Hz"  : "файл фильтра 8   Гц",
		"12Hz" : "файл фильтра 12  Гц"
    	    }
	return (krl_f[f],krl_f[fmod])

krl_rec = rec("420Hz", "12Hz")

print (krl_rec)

# freq, mod
def gen (f, fmod, A):

	gen_f = {
		"420Hz": 420,
		"480Hz": 480,
		"565Hz": 565,
		"720Hz": 720,
		"780Hz": 780,
		"8Hz"  : 8,
		"12Hz" : 12
    	    }
	return (gen_f[f], gen_f[fmod], A)

krl_gen = gen("420Hz", "12Hz", 1600)

print (krl_gen)
