import  const as c
import numpy as np

#---------------------------------------
class mean_filt(object):

	def __init__(self, lenght):
		"""initialization"""
		self.sum = [0 for i in range(lenght)]

	def proc(self, sample):
		"""demodulation"""

		self.sum.insert(0,sample)
		self.sum.pop()

		y = abs(np.mean(self.sum))
		return y
