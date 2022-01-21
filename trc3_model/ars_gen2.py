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
		self.res = []

		for i in range(len(c.t)):
			self._data.append(self.A * np.cos(2 * np.pi * self.fc * c.t[i]))

		for x, y in zip(self._data,c.inp_signal_buff):
			self.res+=[x+y]

		c.inp_signal_buff = self.res
