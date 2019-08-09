import numpy as np

cell = np.array([[10.01438,0,0],
                 [0,10.01438,0],
                 [0,0,10.01438]])
n=50
kp = [ [0.5, 0.5, 0.5],			#L
       [0.0, 0.0, 0.0],			#Gamma
       [0.5, 1.0, 0.0],			#W
       [0.0, 1.0, 0.0]]			#X
filename = "Y2V2O7.klist_band"

########################################
nk = []
init_len = 0
kcell = 2*3.141592*np.linalg.inv(cell)
for kc in range(len(kp)-1):
  k2 = np.dot( kcell, kp[kc+1] )
  k1 = np.dot( kcell, kp[kc] )
  klen = np.linalg.norm(k2-k1)
  if kc==0:
     init_len = klen
  nk.append(int(n*klen/init_len))

fac = np.array( [abs(x) for x in np.array(kp).flatten() if abs(x)>0 ] ).min()
fac = 1.0/fac

show_tics = [0]+ [sum(nk[:1+x]) for x in range(len(nk)) ]
print show_tics

fout = open(filename,"w")
n_iter=0
for k in range(len(kp[:-1])):
	limit = nk[k]
	if k==len(kp[:-1])-1:
		limit += 1
	for j in range(limit):
		n_iter+=1
		fout.write(str(n_iter).rjust(10))
		for kx in range(3):
			fout.write( str( int( fac*kp[k][kx]*(nk[k]-j) + fac*kp[k+1][kx]*j ) ).rjust(5) )
		fout.write( str( int(fac*nk[k])).rjust(5)+str(1.0).rjust(5) )

#		print (str( (int(fac*kp[k][0])*(nk[k]-j) + int(fac*kp[k+1][0])*j)/(1.0*fac*nk[k]) ).rjust(5)
#					+str( (int(fac*kp[k][1])*(nk[k]-j) + int(fac*kp[k+1][1])*j )/(1.0*fac*nk[k])).rjust(5)
#					+str( (int(fac*kp[k][2])*(nk[k]-j) + int(fac*kp[k+1][2])*j )/(1.0*fac*nk[k])).rjust(5))

		if k==0 and j==0:
			fout.write(" -1.5  1.5")
		fout.write("\n")

fout.write("END \n")

fout.close()