import sys
sys.path.append('./FIR_models')
import time
import const as c
from FIR_10 import *
from FIR_8 import *
from FIR_12 import *
from FIR_15 import *
from FIR_420 import *
from FIR_480 import *
from FIR_565 import *
from FIR_720 import *
from FIR_780 import *
from FIR_600 import *

class fir(object):
	def __init__(self, h):
		"""initialization"""
		self.index= 0
		self.h = h
		self.size= len(self.h)
		self._data = [0]*self.size

	def proc(self,sample):
		"""sample processed """
		if len(self._data) == self.size:
			self._data[self.index] = sample
		else:
			self._data.append(sample)
		self.index = (self.index + 1) % self.size
		acc = 0	# accumulator
		indx = self.index

		for j in range (self.size):
			acc += self._data[indx] * self.h[j]
			if indx == ((self.size)-1):
				indx = 0
			else:
				indx += 1
		return (int(acc)/32768) # result to 16 bit value

