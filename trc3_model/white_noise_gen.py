import numpy as np
import random
import const as c
import operator

#---------------------------------------
class white_noise(object):

	def __init__(self, A):
		"""initialization"""
		self.ampl = A
		self._data = []
		self.res = []

		for i in range(len(c.t)):
			self._data.append(self.ampl*np.random.randn())

		c.inp_signal_buff = [a + b for a, b in zip(c.inp_signal_buff, self._data)]


