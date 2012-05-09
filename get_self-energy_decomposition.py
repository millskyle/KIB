#!/usr/bin/python

import sys
import numpy as np
import scipy
import random
import pylab
from numpy import linalg as LA


inputFile = open(sys.argv[1],'r')  # this gives the projection of the HOMO onto each KS state

inputFile.readline()
inputFile.readline()

diagonal_n = 768

HOMO_DFT = np.zeros(diagonal_n, dtype=np.complex)

for line in inputFile.readlines():

    n, alpha = int(line.split()[0]) - 1, np.complex(float(line.split()[1]), float(line.split()[2]))
    HOMO_DFT[n] = alpha
inputFile.close()


####### 

inputFile = open('sigx.dat','r')

x_array = np.zeros(diagonal_n, dtype=float)
sx_array = np.zeros(diagonal_n, dtype=float)
ch_array = np.zeros(diagonal_n, dtype=float)

for i in range(diagonal_n):
    line = inputFile.readline()
    n = int(line.split()[0]) - 1
    x_array[n] =  float(line.split()[1])
    sx_array[n] = float(line.split()[2])
    ch_array[n] = float(line.split()[3])

sum_x = 0.
sum_sx = 0.
sum_ch = 0.

for i in range(diagonal_n):

    x = x_array[i]
    sx = sx_array[i]
    ch = ch_array[i]
        
    sum_x  +=  HOMO_DFT[i] * x  * np.conj(HOMO_DFT[i])
    sum_sx +=  HOMO_DFT[i] * sx * np.conj(HOMO_DFT[i])
    sum_ch +=  HOMO_DFT[i] * ch * np.conj(HOMO_DFT[i])

inputFile.close()

print 'X: ', np.real(sum_x), 'SX-X: ', np.real(sum_sx), 'CH: ', np.real(sum_ch), 'SX-X + CH: ', np.real(sum_sx+sum_ch)
