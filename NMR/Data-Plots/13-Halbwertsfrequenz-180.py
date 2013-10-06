import numpy as np
from scipy import optimize  
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import AutoMinorLocator, AutoLocator
rc('font', family = 'serif', serif = 'STIXGeneral')
# ------------------  Eingaben  ------------
Alle_Daten_plotten = True #True
Einen_Datensatz_schoen_plotten = False
read_start=14 # Erste Zeile, die eingelesen wird
abgelesene_Werte_plotten = False #False 
# ------------------------------------------

# txt_filename_to_open=["05-phasenraum-045mV-minmax-FM.dat"]

# data1 = [i.strip().split() for i in open(txt_filename_to_open[0]).readlines()]
ex_data=[i.strip().split() for i in open("180DrehungEx_von_Mathematica.dat").readlines()]
theo_data=[i.strip().split() for i in open("180DrehungTheo_von_Mathematica.dat").readlines()]

x1=[]; x2=[]; y1=[]; y2=[]

for i in range(len(ex_data)):
    x1=append(x1,float(ex_data[i][0])) 
    y1=append(y1,float(ex_data[i][1]))

for i in range(len(theo_data)):
    x2=append(x2,float(theo_data[i][0])) 
    y2=append(y2,float(theo_data[i][1]))    
 
plt.figure(0)
plt.xlabel(u"Frequenz [Hz]")
plt.ylabel(u"Signal [arb.u.]")
title("Frequenzsweep mit 45mV Einstrahlspannung")
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 20}
#plt.xlim([0.049,0.0885])
#plt.ylim([-1,1.5])
matplotlib.rc('font', **font)
subplots_adjust(left=0.18, bottom=0.12, right=0.96, top=0.92, wspace=0.2, hspace=0.2)
# plt.plot(t1,S1,"b.", label="off")
plt.plot(x1,y1,"r.", label="Messpunkte")
plt.plot(x2,y2,"b.", label="Theoretisch erwarteter Verlauf")
plt.plot([1300,1700],[0.1721,0.1721],"k--")
s=0.05
plt.plot([1477,1477,1477,1544,1544,1544],[0.0035-s,0.0035+s,0.0035,0.0035,0.0035-s,0.0035+s],"r")
plt.text(1510,-0.1,r'$\nu_\mathrm{Halb}$',va="center",ha="center",color="red")
# plt.plot([0,1],[0,0],"k--")

plt.legend(loc=1)	
show()
