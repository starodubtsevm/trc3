import  const as c
import numpy as np

#---------------------------------------
class ask_det_sync(object):

	def __init__(self, F):
	"""initialization"""
		self.Fcar = F										# частота сигнала
		self.fs = fs
		self.A = 1
		self.cycle_count_sin = 0
		self.cycle_count_cos = -np.pi/2.0
		self.sin = 0
		self.cos = 0

	def local_gen(self,t):
	'''Локальный генератор cos и sin'''
		
		if self.cycle_count_sin < int(((1/self.Fcar)/(np.pi))):
			y_sin = 1
		else:
			y_sin = -1
			self.cycle_count_sin = 0

		if self.cycle_count_cos  < int(((1/self.Fcar)/(np.pi/2.0))):
			y_cos = 1
		else:
			y_sin = -1
			self.cycle_count_sin = (-np.pi/2)

		self.cycle_count_sin = self.cycle_count_sin + 1
		self.cycle_count_cos = self.cycle_count_cos + 1

      return y_sin, y_cos

	def proc(self,):
	"""demodulation"""

		self.sin = self.local_gen()

		return y

