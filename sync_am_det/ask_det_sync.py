import const as c
import numpy as np

#---------------------------------------
class ask_det_sync(object):

	def __init__(self, F):
		"""initialization"""
		self.T = (1.0/F)*1000000				# приведенный период сигнала
		self.fs = c.fs
		self.A = 1
		self.cycle_count_sin = 0
		self.cycle_count_cos = int(-self.T/4)
		self.sin = 0
		self.cos = 0
		self.y_sin = 1
		self.y_cos = 1

	def local_gen(self):
		'''Локальный генератор cos и sin'''
		
		print (self.cycle_count_sin, self.y_sin)

		if self.cycle_count_sin > int(self.T/2):
			self.y_sin ^= 1
			self.cycle_count_sin = 0

		if self.cycle_count_cos  < int((self.T)/(self.T/4)):
			self.y_cos ^= 1
			self.cycle_count_cos = int(-self.T/4)

		self.cycle_count_sin = self.cycle_count_sin + 1
		self.cycle_count_cos = self.cycle_count_cos + 1

		return self.y_sin, self.y_cos

	def proc(self,sample):
		"""demodulation"""

		self.sin, self.cos = self.local_gen()

		return self.sin, self.cos

