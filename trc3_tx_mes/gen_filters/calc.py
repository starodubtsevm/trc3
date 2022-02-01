from scipy.signal import firwin


#Расчет коэффициентов FIR
def bpf_fir(ntaps, lowcut, highcut, fs, point = "fixed"):
    nyq = 0.5 * fs
    taps = firwin(ntaps, [lowcut, highcut],
                  nyq=nyq,
                  pass_zero=False,
                  scale=False)
    if str(point) =="fixed":
        return [int(taps[i] * 32768) for i in range(len(taps))]
    else:
        return taps


def lpf_fir(ntaps, fcut, fs, point = "fixed"):
    nyq = 0.5 * fs
    fn = fs / 2
    taps = firwin(ntaps, fcut, nyq=nyq)
    if str(point) =="fixed":
        return [int(taps[i] * 32768) for i in range(len(taps))]
    else:
        return taps


def hpf_fir(ntaps, fcut, fs ,point = "fixed"):
    nyq = 0.5 * fs
    fn = fs / 2
    taps = firwin(ntaps, fcut, nyq=nyq, pass_zero=False)
    if str(point) =="fixed":
        return [int(taps[i] * 32768) for i in range(len(taps))]
    else:
        return taps
