# Using the magic encoding
# -*- coding: utf-8 -*-

# 1. just copy the .dat file in the folder of this file 
# add a txt_filename_to_open
# execute "python make_plot_from_NextNano_output.py
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import AutoMinorLocator, AutoLocator
from scipy.interpolate import interp1d

rc('font', family = 'serif', serif = 'STIXGeneral')
txt_filename_to_open=[]
line=[]
colors = [(1.0, 0.0, 0.0), (0.75, 0, 0.75), (0, 0, 0)]
# ------------------  Eingaben  ------------
Eingaben=['4-4,2-Laengsspannung-9-0_geschnitten.dat','10-3,0-Laengsspannung-9-0_geschnitten.dat','14-2,1-Laengsspannung-9-0_geschnitten.dat','18-1,5-Laengsspannung-9-0_geschnitten.dat']
Fall=0
txt_filename_to_open.append(Eingaben[Fall])
line.append(1)
# ------------------------------------------
txt_file = [i.strip().split() for i in open(txt_filename_to_open[0]).readlines()]
U_laengs=[]
I=[]
B=[]

for i in range(len(txt_file)):
    U_laengs=append(U_laengs,float(txt_file[i][2])/10*0.001)
    I=append(I,float(txt_file[i][3])/10*0.002/4981)
    B=append(B,float(txt_file[i][1]))
    
R_laengs=[]
B_inv=[]
for i in range(len(B)):
    B_inv=append(B_inv,1.0/B[i])
    R_laengs=append(R_laengs,U_laengs[i]/I[i])

f2 = interp1d(B_inv, R_laengs)#, kind='cubic'
print min(B_inv)
Bmin=0.111
Bmax=3.0
steps=4064.0*16
B_inv_intpol=linspace(Bmin,Bmax,steps)
#print B_inv_Bsort[::100]
R_laengs_intpol=f2(B_inv_intpol)
R_abl=[]
B_abl=[]
for i in range(len(B_inv_intpol)-1):
    R_abl=append(R_abl,R_laengs_intpol[i+1]-R_laengs_intpol[i])
    B_abl=append(B_abl,(B_inv_intpol[i+1]+B_inv_intpol[i])/2)
    
R_DFT=np.fft.fft(R_abl)
#B_per=1/np.fft.fftfreq(B_abl.size)






# -- plot ---
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
 

xdata=B_inv
ydata=R_laengs
# plt.plot(xdata,ydata,"x",color=colors[0],label="Messwerte")
# plt.plot(B_inv_intpol,R_laengs_intpol,color=colors[1],label="Interpolation")
# print B_abl,R_abl
plt.plot(B_abl,R_abl*100,color=colors[2],label="Interpolation")
plt.legend(loc=0)



plt.figure(2)
#plt.set_xlabel(txt_file[0][0])
#plt.set_ylabel(txt_file[0][1])
plt.ylabel(u'$|\mathrm{DFT}|^2$ des Längswiderstandes')
plt.xlabel(u'Frequenz der Oszillationen $[T]$')#\\frac{1}{B}$-Frequenz des Längswiderstandes [T]$
plt.ylim([0,4])
plt.xlim([0,60])
title(u'Fourietransformation des Längswiderstandes')
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 20}
matplotlib.rc('font', **font)
subplots_adjust(left=0.11, bottom=0.13, right=0.95, top=0.92, wspace=0.2, hspace=0.2)
   

  

xdata=np.fft.fftfreq(B_abl.size,B_abl[1]-B_abl[0])[1:len(B_abl)/2]#[0:len(B_abl)/2]
ydata=((abs(R_DFT))[1:len(B_abl)/2]**2)/1e9
print  "len(B_inv_intpol): ", len(B_inv_intpol)
print  "xdata: ", xdata
print  "len(B_inv_intpol): ", len(B_inv_intpol)
plt.plot(xdata,ydata,color=colors[0],label="$|\mathrm{DFT}|^2$")
plt.plot([7.28,7.28],[0,3.418],"--")
plt.plot([7.28-0.35,7.28+0.35],[3.418,3.418],"-",color="blue")
plt.plot([7.28-0.35,7.28-0.35],[3.418-0.025,3.418+0.025],"-",color="blue")
plt.plot([7.28+0.35,7.28+0.35],[3.418-0.025,3.418+0.025],"-",color="blue")
plt.legend(loc=0)
#plt.savefig("06-Fourietransformation.pdf")
show()


# f = open(Ausgaben[Fall], 'w+')

# for i in range(len(B_sorted)):
    # f.write(str(B_sorted[i])+"\t"+str(R_H_sorted[i])+"\n")
# f.close
