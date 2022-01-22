import numpy as np
import const as c

"""
Ask generator
"""
class gen(object):
	def __init__(self, fc, A = 0, fm = 0):
		"""initialization"""
		self.fc = fc
		self.fm = fm
		self.A = A
		omega_fc = 2*np.pi*fc
		_2omega_fc = 2*np.pi*2*fc
		_3omega_fc = 2*np.pi*3*fc

		omega_fm = 2*np.pi*fm

		if A == 0: return
		if self.fm == 0:
			self.M = 0.0
		else:
			self.M = 1.0

		_data = [(self.A*np.cos(omega_fc*c.t[i])*\
		(1 + self.M * np.cos(omega_fm * c.t[i])) + \
		0.01*self.A*np.cos(_2omega_fc*c.t[i])*\
		(1 + self.M * np.cos(omega_fm * c.t[i])) + \
		0.001*self.A*np.cos(_3omega_fc*c.t[i])*\
		(1 + self.M * np.cos(omega_fm * c.t[i])))\
		for i in range (len(c.t))]

		c.inp_signal_buff = [a + b for a, b in zip(c.inp_signal_buff, _data)]

