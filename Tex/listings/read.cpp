#include <string>
#include <fstream>
#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {
	fstream fBWeights;
	fBWeights.open("./+bweights", fstream::in);
	fstream fOutput;
	fOutput.open("./output.dat", fstream::out);
	fstream fBand;
	fBand.open("./+band", fstream::in);
	fstream fPiPlus;
	fPiPlus.open("./piPlus.dat", fstream::out);
	fstream fPiMinus;
	fPiMinus.open("piMinus.dat", fstream::out);
	
	string line;
	char line2[2560];
	int i, countLine, startPos, endPos, kIter, kpoints, area = 0;
	double kx[480], ky[480], kz[480];	
	bool even = false;
	
	getline(fBand, line);
	while(getline(fBand, line)) {	
		if(countLine % 2 == 0){
                	endPos = 0;
			startPos = line.find_first_of("-0123456789", endPos);
			endPos = line.find(" ", startPos);
			kx[i] = atof(line.substr(startPos, endPos-startPos).c_str());

			startPos = line.find_first_of("-0123456789", endPos);
			endPos = line.find(" ", startPos);
			ky[i] = atof(line.substr(startPos, endPos-startPos).c_str());

			startPos = line.find_first_of("-0123456789", endPos);
			endPos = line.find(" ", startPos);
			kz[i] = atof(line.substr(startPos, endPos-startPos).c_str());

			//cout << kx[i] << " " << ky[i] << " " << kz[i] << '\n';
			i++;
		}
		countLine++;
	}
	fBand.close();
	cout << "Max kpoints : " << i << endl;
	
	fBWeights.getline(line2, 2560);
	fBWeights.getline(line2, 2560);
	double k, E;
	double weights[56];

	cout << kx[0] << '\t' << ky[0] << '\t' << kz[0] << endl;	
	
	while(fBWeights) {	
		fBWeights >> k >> E;
		//cout << k << "\t" << E << endl;

		for(int i=0; i<56; i++) {
			fBWeights >> weights[i];
		}	
	
		if((weights[4] + weights[18] + weights[32] + weights[46]) > 0.7 && E < 20) {
			kIter++;
			if(kIter % 2 == 0) {
				fOutput <<  kx[kpoints] << '\t' <<  ky[kpoints] << '\t' << kz[kpoints] << '\t'  << E << '\t' << k << endl;
				if(E < 0.05 && area < 1) {
					fPiMinus << kx[kpoints] << " " <<  ky[kpoints] << " " << kz[kpoints] << " " << E << " " << k << '\n';
				} else if(E > 0.05 && area < 1) {
					fPiPlus << kx[kpoints] << " " <<  ky[kpoints] << " " << kz[kpoints] << " " << E << " " << k << '\n';
				} else if(E > 0.05 && area == 1) {
					fPiPlus << kx[kpoints] << " " <<  ky[kpoints] << " " << kz[kpoints] << " " << E << " " << k << '\n';
				} else if(E < 0.05 && area == 1) {
					fPiMinus << kx[kpoints] << " " <<  ky[kpoints] << " " << kz[kpoints] << " " << E << " " << k << '\n';
				} else if(E < 0.05 && area > 1) {
					fPiMinus << kx[kpoints] << " " <<  ky[kpoints] << " " << kz[kpoints] << " " << E << " " << k << '\n';
				} else if(E > 0.05 && area > 1) {
					fPiPlus << kx[kpoints] << " " <<  ky[kpoints] << " " << kz[kpoints] << " " << E << " " << k << '\n';
				}
				
				if(k == 0.9106836 && area == 0 && !even) {
					area++;
					cout << "Area change : " << area << '\n';
				}
				if(k == 2.5185994 && area == 1 && !even) {
					area++;
					cout << "Area change : " << area << '\n';
				}
				
				if(even) {	
					kpoints++;
					even = false;
				} else {
					even = true;
				}
			}
		}	

		fBWeights.getline(line2, 2560);
	}
	cout << "Loop : " << kIter << endl; 
	cout << "kpoints : " << kpoints << endl;	
	cout << "Output.dat has been created"<< endl;	
	cout << "PiPlus.dat has been created"<< endl;	
	cout << "PiMinus.dat has been created"<< endl;	

	fBWeights.close();
	fOutput.close();
}
