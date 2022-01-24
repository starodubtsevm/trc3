import sys
sys.path.insert(0, '..')

from fir_filter import*
from limiter import*
from ask_det import*
from am_sync_det import*
from comparator import*
from dc_blocker import*
import const as c

"""
Trc3 receiver
"""
class krl_receiver(object):
	def __init__(self, fc, fm):
		"""initialization"""
		self.fc = fc
		self.fm = fm
		self.lim = limiter(-1500000, 1500000) #limiter
		self.det = ask_det() # ask detector
		self.hz8_fir = fir(f_8)# 8Hz filter_buf
		self.hz12_fir = fir(f_12)# 12Hz filter_buf
		self.det8 = ask_det() # ask detector 8Hz
		self.det12 = ask_det() # ask detector 12Hz
		self.hz10fir8 = fir(f_10) # ask 8 Hz
		self.hz10fir12 = fir(f_10)#  ask 12 Hz
		self.comp8 = comparator(8,10,2) #comparator 8Hz

		freqs = {
			420:f_420,
			480:f_480,
			565:f_565,
			720:f_720,
			780:f_780
			}
		self.chan_fir = fir(freqs[self.fc]) #.channel filter

		self.det2 = s_am_det(fc, c.fs) # input sync AM det
		self.det3 = s_am_det3(fm, c.fs2) # channel sync AM det

		self.dc_b = dc_block() # dc blocker
		
		self.fir_5 = fir(f_5)# 8Hz filter_buf
		self.fir_10 = fir(f_10)# 8Hz filter_buf
		
