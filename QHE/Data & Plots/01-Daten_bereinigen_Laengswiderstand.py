# Using the magic encoding
# -*- coding: utf-8 -*-

# 1. just copy the .dat file in the folder of this file 
# add a txt_filename_to_open
# execute "python make_plot_from_NextNano_output.py
# first collum on the input file is name of data




import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes
from mpl_toolkits.axes_grid.inset_locator import mark_inset
from matplotlib.ticker import AutoMinorLocator, AutoLocator

txt_filename_to_open=[]
line=[]
colors = [(1.0, 0.0, 0.0), (0.75, 0, 0.75)]
# ------------------  Eingaben  ------------
txt_filename_to_open.append("1,5-Laengsspannung.dat")
line.append(1)
# ------------------------------------------

for n in range(len(txt_filename_to_open)):
    txt_file = [i.strip().split() for i in open(txt_filename_to_open[n]).readlines()]


    #txt_file.remove(txt_file[0])
    U_laengs_up=[]
    I_up=[]
    B_up=[]
    U_laengs_down=[]
    I_down=[]
    B_down=[]
    for i in range(321,4717): #321-4716 und 5025-9436
        U_laengs_up=append(U_laengs_up,float(txt_file[i][2])/10*0.001)
        I_up=append(I_up,float(txt_file[i][3])/10*0.002/4981)
        B_up=append(B_up,float(txt_file[i][1]))
    for i in range(5025,9426): #321-4716 und 5025-9436
        U_laengs_down=append(U_laengs_down,float(txt_file[i][2])/10*0.001)
        I_down=append(I_down,float(txt_file[i][3])/10*0.002/4981)
        B_down=append(B_down,float(txt_file[i][1]))       
    # print xdata
    # print ydata
    # for i in range(len(U_laengs)):

    Abstand=zeros(100)
    for shift in range(20,60):
        R_H_up=U_laengs_up/I_up
        R_H_down=U_laengs_down/I_down
        B_up_copy=copy(B_up)
        B_down_copy=copy(B_down)
        #print shift
        for i in range(len(B_up_copy)):
            B_up_copy[i]-=shift/1000.0
        for i in range(len(B_up_copy)):
            B_down_copy[i]+=shift/1000.0
            
        R_H_all=append(R_H_up,R_H_down)
        B_all=append(B_up_copy,B_down_copy)
        
        indices=range(len(R_H_all))
        indices.sort(key = B_all[:].__getitem__)
        
        R_H_sorted = copy(R_H_all)
        B_sorted=copy(B_all)
        for i in range(len(R_H_all)):
            R_H_sorted[i]=R_H_all[indices[i]]
            B_sorted[i]=B_all[indices[i]]
        #print R_H_sorted
                        
        
        for i in range(len(R_H_sorted)-1):
            # if abs(B_sorted[i]-B_sorted[i+1])<0.3:
            Abstand[shift]+=abs((B_sorted[i]-B_sorted[i+1])*(R_H_sorted[i]-R_H_sorted[i+1]))
        
print shift, " - ", Abstand  

Abstand_min=1e99
shift_min=0     
for i in range(len(Abstand)):
    if Abstand[i]>0:
        if Abstand[i]<Abstand_min:
            shift_min=i
            Abstand_min=Abstand[i]
#print shift_min," - ", Abstand[shift_min]
        
#shift_min = 37 #37 für unten, 24 für oben

R_H_up=U_laengs_up/I_up
R_H_down=U_laengs_down/I_down
#shift_min=37

for i in range(len(B_up)):
    B_up[i]-=shift_min/1000.0
for i in range(len(B_up)):
    B_down[i]+=shift_min/1000.0
    
print "Daten geschiftet um: ", shift_min," - ", Abstand[shift_min]
     
R_H_all=append(R_H_up,R_H_down)
B_all=append(B_up,B_down)

indices=range(len(R_H_all))
indices.sort(key = R_H_all[:].__getitem__)

R_H_sorted = copy(R_H_all)
B_sorted=copy(B_all)
for i in range(len(R_H_all)):
    R_H_sorted[i]=R_H_all[indices[i]]
    B_sorted[i]=B_all[indices[i]]
#print R_H_sorted
                
Abstand=0.0
for i in range(len(R_H_sorted)-1):
    Abstand+=abs(B_sorted[i]-B_sorted[i+1])
        
ax = gca()
#ax.set_xlabel(txt_file[0][0])
#ax.set_ylabel(txt_file[0][1])
ax.set_ylabel(u'Hallwiderstand [$\\Omega$]')
ax.set_xlabel(u'Magnetfeldstärke [T]')
title("Hallwiderstand")
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 20}
matplotlib.rc('font', **font)
xdata=B_sorted
ydata=R_H_sorted
ax.plot(xdata,ydata,"x",color=colors[n],label=txt_filename_to_open[n][0:5])
print txt_filename_to_open[n]
ax.xaxis.set_minor_locator( AutoMinorLocator(5))
ax.legend(loc=1)	
show()

f = open('1,5-Laengswiderstand-Magnetfeld_bereinigt.dat', 'w+')

for i in range(len(B_sorted)):
    f.write(str(B_sorted[i])+"\t"+str(R_H_sorted[i])+"\n")
f.close
