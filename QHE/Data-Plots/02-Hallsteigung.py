# Using the magic encoding
# -*- coding: utf-8 -*-

# 1. just copy the .dat file in the folder of this file 
# add a txt_filename_to_open
# execute "python make_plot_from_NextNano_output.py
# first collum on the input file is name of data



from scipy import *
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import AutoMinorLocator, AutoLocator

rc('font', family = 'serif', serif = 'STIXGeneral')
txt_filename_to_open=[]
line=[]
colors = [(1.0, 0.0, 0.0), (0.75, 0, 0.75)]
# ------------------  Eingaben  ------------
Eingaben=['4,2-Hallwiderstand-Magnetfeld_bereinigt.dat','3,0-Hallwiderstand-Magnetfeld_bereinigt.dat','2,1-Hallwiderstand-Magnetfeld_bereinigt.dat','1,5-Hallwiderstand-Magnetfeld_bereinigt.dat']

Fall=4
txt_filename_to_open.append(Eingaben[Fall])
line.append(1)
fehlerR=0.02
# ------------------------------------------
txt_file = [i.strip().split() for i in open(txt_filename_to_open[0]).readlines()]

#txt_file.remove(txt_file[0])
U_H=[]
B=[]

for i in range(len(txt_file)):
    B=append(B,float(txt_file[i][0]))
    U_H=append(U_H,float(txt_file[i][1]))



plt.figure(1)
#plt.set_xlabel(txt_file[0][0])
#plt.set_ylabel(txt_file[0][1])
plt.ylabel(u'Hallwiderstand [$\\Omega$]')
plt.xlabel(u'Magnetfeldstärke [T]')
plt.ylim([0,3000])
plt.xlim([0,1.3])
title("Hallwiderstand")
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 20}
matplotlib.rc('font', **font)
subplots_adjust(left=0.18, bottom=0.12, right=0.96, top=0.92, wspace=0.2, hspace=0.2)
    
xdata=B
ydata=U_H

# Datensatz für Fitfunktion
fitx=[]
fity=[]
for i in range(len(B)):
	if B[i] < 0.9999:
		fitx=append(fitx,B[i])
		fity=append(fity,U_H[i])
		# print "i=", i, "B=", B[i], "fitx=", fitx[i], "U_H=", U_H[i]

# Fitfunktion an Daten mit niedrigen B-Feld
fitfunc = lambda p, fitx: p[0]*fitx
errfunc = lambda p, fitx, fity: fitfunc(p, fitx) - fity
p0 = [0]
pbest, success = optimize.leastsq(errfunc, p0, args=(fitx, fity))

steigung_min = ((fitfunc(pbest, fitx)[-1]-fehlerR*fitfunc(pbest, fitx)[-1]) - fitfunc(pbest, fitx)[0])/(fitx[-1] - fitx[0])
steigung_max =  ((fitfunc(pbest, fitx)[-1]+fehlerR*fitfunc(pbest, fitx)[-1]) - fitfunc(pbest, fitx)[0])/(fitx[-1] - fitx[0])
print steigung_min, steigung_max
print "Steigung: ", pbest[0], "+- ", (steigung_max - steigung_min)/2


plt.plot(xdata,ydata,color=colors[0],label="Messwerte")
# plot Fitgerade mit Fehlergeraden aus Fehler in der Widerstandsmessung
plt.plot(fitx, fitfunc(pbest, fitx), "b", label="ausgleichende Ursprungsgerade" + "\n" + "an Messdaten bis $1\mathrm{T}$")
plt.plot([fitx[0],fitx[-1]], [fitfunc(pbest, fitx)[0],fitfunc(pbest, fitx)[-1]-fehlerR*fitfunc(pbest, fitx)[-1]], "b--", label="Fehlergeraden mit Fehler" + "\n" + "aus Widerstandsmessung")
plt.plot([fitx[0],fitx[-1]], [fitfunc(pbest, fitx)[0],fitfunc(pbest, fitx)[-1]+fehlerR*fitfunc(pbest, fitx)[-1]], "b--")
# Fehlerbalken an letzten (Mess-)Datenwert für Fitgerade
plt.errorbar([fitx[-1],fitx[-1]], [fity[-1],fity[-1]], yerr=fehlerR*fity[-1], fmt="r")

# plt.plot([0, 1.6*2.5], [0, 2800*2.5], 'b-', lw=2, label="Fit")
# plt.plot([0, 1.6*2.5], [0, 2800*2.5+200], 'b--', lw=1, label="Fehlergeraden")
# plt.plot([0, 1.6*2.5], [0, 2800*2.5-200], 'b--', lw=1)

plt.legend(loc=0 , prop={'size':16})	
#plt.savefig("02-Hallsteigung.pdf")
show()


# f = open(Ausgaben[Fall], 'w+')

# for i in range(len(B_sorted)):
    # f.write(str(B_sorted[i])+"\t"+str(R_H_sorted[i])+"\n")
# f.close
