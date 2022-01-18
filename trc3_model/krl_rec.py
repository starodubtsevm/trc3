import sys
sys.path.insert(0, '..')

from fir_filter import*
from limiter import*
from ask_det import*
from comparator import*
from ask_gen2 import*
import const as c

"""
Trc3 receiver
"""
class krl_receiver(object):
	def __init__(self, fc, fm):
		"""initialization"""
		self.fc = fc
		self.fm = fm
		self.lim = limiter(-15000, 15000) #limiter
		self.det = ask_det() # ask detector
		self.hz8_fir = fir(f_8)# 8Hz filter_buf
		self.hz12_fir = fir(f_12)# 12Hz filter_buf
		self.det8 = ask_det() # ask detector 8Hz
		self.det12 = ask_det() # ask detector 12Hz
		self.hz10fir8 = fir(f_15) # ask 8 Hz
		self.hz10fir12 = fir(f_15)#  ask 12 Hz
		self.comp8 = comparator(100,180,2) #comparator 8Hz
		self.comp12 = comparator(100,150,2) #comparator 12Hz

		freqs = {
			420:f_420,
			480:f_480,
			565:f_565,
			720:f_720,
			780:f_780
			}
		self.chan_fir = fir(freqs[self.fc]) #.channel filter
