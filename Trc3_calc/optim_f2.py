

f_c = [420, 480, 565, 720, 780]
B = 25
M_MAX = 20
#250 Hz Fs


def fs_max(m, fc):
    return round((2 * fc - B) / m, 1)


def fs_min(m, fc):
    return round((2 * fc + B) / (m + 1), 1)

for f in f_c:
    print ("--------------------------------")
    print("fs = ", f, " Hz")
    print ("--------------------------------")
    for m in range(1, M_MAX):
        print(m, fs_max(m, f), fs_min(m, f))
