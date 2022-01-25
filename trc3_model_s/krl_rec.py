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
		self.hz8_fir = fir(f_8)# 8Hz filter_buf
		self.hz12_fir = fir(f_12)# 12Hz filter_buf
		self.comp8 = comparator(8,10,2) #comparator 8Hz

		freqs = {
			420:f_420,
			480:f_480,
			565:f_565,
			720:f_720,
			780:f_780
			}
		self.chan_fir = fir(freqs[self.fc])#.channel filter

		self.det2 = s_am_det(fc, c.fs)# input sync AM det

		#self.dc_b = dc_block()# dc blocker

		self.fir_10 = fir(f_15)# 15Hz filter_buf

