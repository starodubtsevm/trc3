import const as c

#https://ccrma.stanford.edu/~jos/fp/DC_Blocker_Software_Implementations.html
# y = x - xm1 + 0.995 * ym1;
#  xm1 = x;
#  ym1 = y;
# DC blocker
#Here, x denotes the current input sample, and y denotes the current output sample.
#The variables xm1 and ym1 hold once-delayed input and output samples, respectively
#(and are #typically initialized to zero). In this implementation, the pole is fixed
#at R=0.995 , which corresponds to an adaptation time-constant of approximately
#1/(1-R) = 200 samples. A smaller R value allows faster tracking of
#``wandering dc levels'', but at the cost of greater low-frequency attenuation


#---------------------------------------
class dc_block(object):

    def __init__(self):
        """initialization"""
        self.xm1 = 0
        self.ym1 = 0

    def proc(self, sample):
        """blocking direct current"""

        y = sample - self.xm1 + 0.9 * self.ym1
        self.xm1 = sample
        self.ym1 = y

        return y
