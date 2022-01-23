import time
#from memory_profiler import profile
"""
Ask generator
"""
class gen(object):
	#@profile
	def __init__(self, fc, A = 0, fm = 0):
		"""initialization"""
		if A == 0: return
		from numpy import pi, cos, sin
		import const as c
		from const import t
		self.fc = fc
		self.fm = fm
		self.A = A
		self.A2 = A * 0.01
		self.A3 = A * 0.001
		omega_fc   = 2*pi*fc
		_2omega_fc = 2*pi*2*fc
		_3omega_fc = 2*pi*3*fc
		if self.fm == 0:
			self.M = 0
			omega_fm = 0
		else:
			self.M = 1
			omega_fm = 2*pi*fm
		_data = [(self.A*cos(omega_fc*t[i])*(1 + self.M * cos(omega_fm *t[i]))+\
		self.A2*cos(_2omega_fc*t[i])*(1 + self.M * cos(omega_fm *t[i]))+\
		self.A3*cos(_3omega_fc*t[i])*(1 + self.M * cos(omega_fm *t[i])))\
		for i in range (len(t))]

		c.inp_signal_buff = [a + b for a, b in zip(c.inp_signal_buff, _data)]
		del _data
