from scipy.signal import firwin


#Расчет коэффициентов FIR
def bpf_fir(ntaps, lowcut, highcut, fs, window='hamming'):
    nyq = 0.5 * fs

    taps = firwin(ntaps, [lowcut, highcut],
                  nyq=nyq,
                  pass_zero=False,
                  window=window,
                  scale=False)
    return taps


def lpf_fir(ntaps, fcut, fs, window='blackman'):
    nyq = 0.5 * fs
    fn = fs / 2

    taps = firwin(ntaps, fcut, nyq=nyq)
    return taps


def hpf_fir(ntaps, fcut, fs, window='hamming'):
    nyq = 0.5 * fs
    fn = fs / 2

    taps = firwin(ntaps, fcut, nyq=nyq, pass_zero=False)
    return taps
