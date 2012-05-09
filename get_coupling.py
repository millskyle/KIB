#!/usr/bin/python

print 'make sure you have core states'
print 'this code assumes n starts at 1'
import sys
import numpy as np
import scipy
import random
import pylab
from numpy import linalg as LA


inputFile = open(sys.argv[1],'r')  # this gives the projection of the HOMO onto each KS state

inputFile.readline()
inputFile.readline()

LHS_DFT = []

diagonal_n = 0

for line in inputFile.readlines():

    n, alpha = int(line.split()[0]) - 1, np.complex(float(line.split()[1]), float(line.split()[2]))
    LHS_DFT.append(alpha)

    diagonal_n += 1
inputFile.close()

LHS_DFT = np.array(LHS_DFT, dtype=np.complex)


inputFile = open(sys.argv[2],'r')  # this gives the projection of the HOMO onto each KS state

inputFile.readline()
inputFile.readline()

RHS_DFT = []

for line in inputFile.readlines():

    n, alpha = int(line.split()[0]) - 1, np.complex(float(line.split()[1]), float(line.split()[2]))
    RHS_DFT.append(alpha)

inputFile.close()

RHS_DFT = np.array(RHS_DFT, dtype=np.complex)


####### 

inputFile = open(sys.argv[3],'r')

eig_dft_array = []
eig_gw_array = []

for i in range(diagonal_n):
    line = inputFile.readline()
    eig_dft_array.append(float(line.split()[3]))
    eig_gw_array.append(float(line.split()[4]))
    
sum_dft = 0.
norm = 0.
sum_gw = 0.


for i in range(diagonal_n):

    omega_dft = eig_dft_array[i]
    omega_gw = eig_gw_array[i]
    norm += LHS_DFT[i]*np.conj(RHS_DFT[i])    
    sum_dft += LHS_DFT[i]*omega_dft*np.conj(RHS_DFT[i])
    sum_gw +=  LHS_DFT[i]*omega_gw*np.conj(RHS_DFT[i])

print norm 
inputFile.close()

print 'DFT: ', np.real(sum_dft), 'GW: ', np.real(sum_gw)
#print np.real(sum_dft), np.real(sum_gw)#, 'delta: ', np.round(np.real(sum_gw) - np.real(sum_dft),3)
