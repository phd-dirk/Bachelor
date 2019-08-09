import os
import numpy as np
import math as m

a = 1.42

tMin = -10.;
tMax = 10.;
tSteps = 10;
tStepWidth = (tMax - tMin) / tSteps;

tPrimeMin = -10.;
tPrimeMax = 10.;
tPrimeSteps = tSteps;
tPrimeStepWidth = (tPrimeMax - tPrimeMin) / tSteps;

filename = 'piPlus.txt'
infilehandle = open(filename, 'r')
lines = infilehandle.readlines()
infilehandle.close()

nlines = len(lines)

kvecs = np.zeros((nlines, 3))
energies = np.zeros((nlines))
indices = np.zeros((nlines))
sigma = np.zeros((tSteps, tPrimeSteps))
sigmaMin = 1e10;

E = np.zeros((nlines))

#t = 1.152 
#tPrime = -9.8
t = 2.7 
tPrime = -0.2*t


def f( kvec ):
        result = 2*m.cos( m.sqrt(3)*kvec[1]) + 4*m.cos( (m.sqrt(3))/(2)*kvec[1])*m.cos((3)/(2) * kvec[0]);
        return result;

def eCal( kvec, t, tPrime ) :
        result = t*m.sqrt(3 + f(kvec)) - tPrime*f(kvec);
        return result;

def sigmaCal( kvec, t, tPrime, E):
        result = m.sqrt((eCal(kvec, t, tPrime) - E)*(eCal(kvec, t, tPrime) - E));
	return result	

for i, l in enumerate(lines):
        kx, ky, kz, e, idx = l.strip().split()
        kx = float(kx)
        ky = float(ky)
        kz = float(kz)
        e = float(e)
        idx = float(idx)
        kvecs[i][0] = kx
        kvecs[i][1] = ky
        kvecs[i][2] = kz
        energies[i] = e
        indices[i] = idx


for i,k in enumerate(kvecs):
         kvecs[i] = np.multiply(3.6278976, k)


fOut = open('test2.txt', 'r+')

for i,k in enumerate(kvecs):
        E = eCal(kvecs[i], t, tPrime)
        fOut.write(str(indices[i]))
        fOut.write(' ')
        fOut.write(str(E))
        fOut.write('\n')

fSigmaOut = open('sigma.txt', 'r+')


for i in range(0, nlines):
	sigma[1][1] +=  sigmaCal(kvecs[i], t, tPrime, energies[i]) 
print (sigma[1][1])


for ti in range(0, tSteps):
	t = tMin + ti*tStepWidth
	for tPrimei in range(0, tPrimeSteps):
		tPrime = tPrimeMin + tPrimei*tPrimeStepWidth
		print (t, tPrime, sigma[ti-1][tPrimei-1])
		for i in range(0, nlines):
			sigma[ti][tPrimei] +=  sigmaCal(kvecs[i], t, tPrime, energies[i]) 
print("change")


for ti in range(0, tSteps):
	for tPrimei in range(0, tPrimeSteps):
		fSigmaOut.write(str(sigma[ti][tPrimei]))
		fSigmaOut.write('\n')
		print(sigmaMin, sigma[ti][tPrimei])
		if (sigmaMin > sigma[ti][tPrimei]):
			print("jooo")
			sigmaMin = sigma[ti][tPrimei]
			tMinimum = tMin + ti*tStepWidth
			tPrimeMinimum = tPrimeMin + tPrime*tPrimeStepWidth
			 

print (tMinimum, tPrimeMinimum, sigmaMin)

