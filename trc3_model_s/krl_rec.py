import sys
sys.path.insert(0, '..')

from fir_filter import*
from iir_filter import*
from limiter import*
from ask_det import*
from am_sync_det import*
from comparator import*
from dc_blocker import*
from mean_filter import*
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
		self.hz8_fir = fir(f_8)# 8Hz
		self.hz12_fir = fir(f_12)# 12Hz 
		self.comp8 = comparator(40,45,10) #comparator 8Hz
		self.comp12 = comparator(30,35,10) #comparator 12Hz
		self.comp_sn = comparator(25,35,5) #comparator 8Hz
		self.in_filter = fir(f_600)# 400-800 Hz
		self.ask_det8 = ask_det()
		self.ask_det12 = ask_det()
		self.det2 = s_am_det(fc, c.fs)# input sync AM det
		self.fir_15 = fir(f_15)# 15Hz 
		self.sn_8filt = mean_filt(50)
		self.sn_12filt = mean_filt(50)
		self.filt_8hz = mean_filt(50)
		self.filt_12hz = mean_filt(50)
		self.filt_det = mean_filt(100)

