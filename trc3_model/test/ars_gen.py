import numpy as np
import const as c
import operator

"""
Ars generator
"""
class ars_gen(object):
	def __init__(self, fc, A):
		"""initialization"""
		self.fc = fc
		self.A = A
		self._data = []

		for i in range(len(c.t)):
			self._data.append(self.A * np.cos(2 * np.pi * self.fc * c.t[i])+\
			0.01*self.A * np.cos(2 * np.pi * (self.fc*2) * c.t[i])+\
			0.001*self.A* np.cos(2 * np.pi * (self.fc*3) * c.t[i]))

		c.inp_signal_buff = [a + b for a, b in zip(c.inp_signal_buff, self._data)]
