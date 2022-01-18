import const as c

#---------------------------------------
class comparator(object):
	def __init__(self, threshold_min,threshold_max, delay):
		"""initialization"""
		self.thres_min = threshold_min
		self.thres_max = threshold_max
		self.prev = 0
		self.tick = 1.0/c.fs
		self.delay = (delay * 1e-3)/self.tick
		self.delay_count = 0

	def proc(self, sample):
		"""comparing"""
		if self.delay_count > 0:
			self.delay_count -= 1
			return self.prev
		else:
			if sample >= self.thres_max:
				self.prev = self.thres_max
				self.delay_count = self.delay
				return self.thres_max

			else:
				#if sample <= self.thres_min:
				self.prev = 0
				self.delay_count = self.delay
				return 0

