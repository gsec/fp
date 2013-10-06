from __future__ import division
import numpy as np
from tmm import *
from scipy import optimize  
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import AutoMinorLocator, AutoLocator
rc('font', family = 'serif', serif = 'STIXGeneral')
import random
# ------------------  Eingaben  ------------
read_start=1 # Erste Zeile, die eingelesen wird
# ------------------------------------------

txt_filename_to_open=["EDataxn_von_Mathematica.dat","TheoData_von_Mathematica.dat"]


data1 = [i.strip().split() for i in open(txt_filename_to_open[0]).readlines()]
data2 = [i.strip().split() for i in open(txt_filename_to_open[1]).readlines()]
theo_data=[i.strip().split() for i in open("ThData_von_Mathematica.dat").readlines()]
# print theo_data

t1=[]; t2=[]; S1=[]; S2=[]

for i in range(len(data1[read_start-1:])):
    t1=append(t1,float(data1[read_start-1+i][0])) 
    S1=append(S1,float(data1[read_start-1+i][1]))
    
for i in range(len(data2[read_start-1:])):
    t2=append(t2,float(data2[read_start-1+i][0]))
    S2=append(S2,float(data2[read_start-1+i][1]))

plt.figure(0)
plt.xlabel(u"Intensit\xe4t [mV]")
plt.ylabel(u"Signal [arb.u.]")
title("Spindrehungskurve")
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 20}
#plt.xlim([0.049,0.0885])
plt.ylim([-1,0.4])
matplotlib.rc('font', **font)
subplots_adjust(left=0.18, bottom=0.12, right=0.96, top=0.92, wspace=0.2, hspace=0.2)
plt.plot(t1,S1,"b.", label="Messpunkte")
plt.plot(t2,S2,"r.", label="Theoretisch erwarteter Verlauf")
# plt.plot([0,1],[0,0],"k--")

plt.legend(loc=0)	
 
show()



