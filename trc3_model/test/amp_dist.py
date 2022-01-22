import numpy as np
import const as c
import operator


"""
Amplifier with distorshn
"""
class amp(object):
	def __init__(self, k):
		"""initialization"""
		self.k = k
		self.res = []
		self.x =0
		#self.y2 = 1+x+(x**2)/2+(x**3)/6+(x**4)/24

		for x  in range (c.sim_point): 
			self.res.append(1 + c.inp_signal_buff[x] + \
			0.00001*(c.inp_signal_buff[x]**2)/2.0 +
			0.000001*(c.inp_signal_buff[x]**3)/6.0 +
			0.0000001*(c.inp_signal_buff[x]**4)/24.0)

		c.inp_signal_buff = self.res
