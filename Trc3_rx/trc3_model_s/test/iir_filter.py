#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import scipy.signal as signal
import const as c


class iir(object):

    def __init__(self):
        # FilterMains = IIR2Filter(8,[20],'lowpass',design='cheby1',rp=2,fs=4000)
        #self.COEFFS = np.array([[ 3.74570646e-17,  7.49141293e-17,  3.74570646e-17,  1.00000000e+00, -1.99161043e+00, 9.91665967e-01],
        #                        [ 1.00000000e+00,  2.00000000e+00,  1.00000000e+00,  1.00000000e+00, -1.99260901e+00,  9.92930733e-01],
        #                        [ 1.00000000e+00,  2.00000000e+00,  1.00000000e+00,  1.00000000e+00,  -1.99457250e+00,  9.95271366e-01],
        #                        [ 1.00000000e+00,  2.00000000e+00,  1.00000000e+00,  1.00000000e+00,  -1.99737037e+00,  9.98337084e-01]])

        self.COEFFS = np.array(
            [[0.06429752, 0.12859503, 0.06429752, 1., -0.7341701, 0.37474343],
             [1., 2., 1., 1., 0.216864, 0.80496925]])

        self.acc_input = np.zeros(len(self.COEFFS))
        self.acc_output = np.zeros(len(self.COEFFS))
        self.buffer1 = np.zeros(len(self.COEFFS))
        self.buffer2 = np.zeros(len(self.COEFFS))
        self.input = 0
        self.output = 0

    def proc(self, input):

        #len(COEFFS[0,:] == 1 means that there was an error in the generation
        #of the coefficients and the filtering should not be used
        if len(self.COEFFS[0, :]) > 1:

            self.input = input
            print(self.input)
            self.output = 0

            #The for loop creates a chain of second order filters according to
            #the order desired. If a 10th order filter is to be created the
            #loop will iterate 5 times to create a chain of 5 second order
            #filters.

            for i in range(len(self.COEFFS)):

                self.FIRCOEFFS = self.COEFFS[i][0:3]
                self.IIRCOEFFS = self.COEFFS[i][3:6]

                #Calculating the accumulated input consisting of the input and
                #the values coming from the feedbaack loops (delay buffers
                #weighed by the IIR coefficients).
                self.acc_input[i] = (self.input +
                                     self.buffer1[i] * -self.IIRCOEFFS[1] +
                                     self.buffer2[i] * -self.IIRCOEFFS[2])

                #Calculating the accumulated output provided by the accumulated
                #input and the values from the delay bufferes weighed by the
                #FIR coefficients.
                self.acc_output[i] = (self.acc_input[i] * self.FIRCOEFFS[0] +
                                      self.buffer1[i] * self.FIRCOEFFS[1] +
                                      self.buffer2[i] * self.FIRCOEFFS[2])

                #Shifting the values on the delay line: acc_input->buffer1->
                #buffer2
                self.buffer2[i] = self.buffer1[i]
                self.buffer1[i] = self.acc_input[i]

                self.input = self.acc_output[i]

            self.output = self.acc_output[i]
        print(self.output)
        return self.output
