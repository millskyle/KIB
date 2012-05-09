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

inputFile = open(sys.argv[2],'r')  # eqp file

eig_dft_array = []
eig_gw_array = []

for i in range(diagonal_n):
    line = inputFile.readline()
    eig_dft_array.append(float(line.split()[3]))
    eig_gw_array.append(float(line.split()[4]))


for i in range(diagonal_n):
        
     print eig_dft_array[i], eig_gw_array[i], np.real(HOMO_DFT[i]*np.conj(HOMO_DFT[i]))


inputFile.close()

