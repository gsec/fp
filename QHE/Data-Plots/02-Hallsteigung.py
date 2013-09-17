# Using the magic encoding
# -*- coding: utf-8 -*-

# 1. just copy the .dat file in the folder of this file 
# add a txt_filename_to_open
# execute "python make_plot_from_NextNano_output.py
# first collum on the input file is name of data




import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import AutoMinorLocator, AutoLocator

txt_filename_to_open=[]
line=[]
colors = [(1.0, 0.0, 0.0), (0.75, 0, 0.75)]
# ------------------  Eingaben  ------------
Eingaben=['4,2-Hallwiderstand-Magnetfeld_bereinigt.dat','3,0-Hallwiderstand-Magnetfeld_bereinigt.dat','2,1-Hallwiderstand-Magnetfeld_bereinigt.dat','1,5-Hallwiderstand-Magnetfeld_bereinigt.dat']

Fall=3
txt_filename_to_open.append(Eingaben[Fall])
line.append(1)
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
plt.ylim([0,16000])
plt.xlim([0,9])
title("Hallwiderstand")
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 20}
matplotlib.rc('font', **font)
subplots_adjust(left=0.18, bottom=0.12, right=0.96, top=0.92, wspace=0.2, hspace=0.2)
    
xdata=B
ydata=U_H
plt.plot(xdata,ydata,color=colors[0],label="Messwerte")
plt.plot([0, 1.6*2.5], [0, 2800*2.5], 'b-', lw=2, label="Fit")
plt.plot([0, 1.6*2.5], [0, 2800*2.5+200], 'b--', lw=1, label="Fehlergeraden")
plt.plot([0, 1.6*2.5], [0, 2800*2.5-200], 'b--', lw=1)
plt.legend(loc=0)	
#plt.savefig("02-Hallsteigung.pdf")
show()


# f = open(Ausgaben[Fall], 'w+')

# for i in range(len(B_sorted)):
    # f.write(str(B_sorted[i])+"\t"+str(R_H_sorted[i])+"\n")
# f.close
