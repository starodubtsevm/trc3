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
		self.M = 1

		for i in range(len(c.t)):
			self._data.append(self.A * np.cos(2 * np.pi * self.fc * c.t[i]) * \
			(1 + self.M * np.cos(2 * np.pi * self.fm * c.t[i])) + \
			self.A * 0.01 * np.cos(2 * np.pi * (2*self.fc) * c.t[i]) * \
			(1 + self.M * np.cos(2 * np.pi * self.fm * c.t[i])) + \
			self.A * 0.001 * np.cos(2 * np.pi * (3*self.fc) * c.t[i]) * \
			(1 + self.M * np.cos(2 * np.pi * self.fm * c.t[i])))

		c.inp_signal_buff = [a + b for a, b in zip(c.inp_signal_buff, self._data)]
