nok = 738

#inf = open("KFe2As2.bands.agr","r")
inf = open("KFe2As2.spaghetti_ene","r")
outf = open("extractbands.dat","w")
window = [-5.0, 5.0]

bands = []

tmp = inf.readline()
bb = 0
outbands = []
while tmp!="":
	while "bandindex:" not in tmp and tmp!="":
		tmp = inf.readline()
	if tmp=="":
		break
	tmpband = []
	outbands.append(0)
	for k in range(nok):
		tmp = inf.readline()
		tmpband.append(float(tmp.split()[4]))
		if tmpband[-1] < window[1] and tmpband[-1] > window[0]:
			outbands[-1] = 1
	bands.append(tmpband)

for k in range(nok):
	outf.write(str(k)+'\t')
	for b in range(len(bands)):
		if outbands[b]==1:
			outf.write(str(bands[b][k])+'\t')
	outf.write('\n')


inf.close()
outf.close()
