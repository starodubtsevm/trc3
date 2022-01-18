import numpy as np
import const as c

"""
Ask generator
"""
class ask_gen(object):
	def __init__(self, fc, A, fm):
		"""initialization"""
		self.fc = fc
		self.fm = fm
		self.A = A
		self._data = []
		self.res = []
		self.temp = 0
		self.a = 1

		for i in range(len(c.t)):
			self._data.append(self.A * np.cos(2 * np.pi * self.fc * c.t[i]) * self.a)
			self.temp+=1.0/c.fs
			if self.temp >= 1/2*(1.0/self.fm):
				self.temp = 0
				self.a ^= 1

		for x, y in zip(self._data,c.inp_signal_buff):
			self.res+=[x+y]

		c.inp_signal_buff = self.res
