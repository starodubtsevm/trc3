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

		for x, y in zip(self._data,c.inp_signal_buff):
			self.res+=[x+y]

		c.inp_signal_buff = self.res


