import numpy as np
import const as c

"""
Ask generator
"""
class gen(object):
	def __init__(self, fc, A, fm = 0.0):
		"""initialization"""
		self.fc = fc
		self.fm = fm
		self.A = A
		self._data = []

		if self.fm == 0.0:
			self.M = 0.0
		else:
			self.M = 1.0

		for i in range(len(c.t)):
			self._data.append(self.A*np.cos(2*np.pi*(1*self.fc)*c.t[i])*\
			(1 + self.M * np.cos(2 * np.pi * self.fm * c.t[i])) + \
			0.01*self.A*np.cos(2*np.pi*(2*self.fc)*c.t[i])*\
			(1 + self.M * np.cos(2 * np.pi * self.fm * c.t[i])) + \
			0.001*self.A*np.cos(2*np.pi*(3*self.fc)*c.t[i])*\
			(1 + self.M * np.cos(2 * np.pi * self.fm * c.t[i])))

		c.inp_signal_buff = [a + b for a, b in zip(c.inp_signal_buff, self._data)]
