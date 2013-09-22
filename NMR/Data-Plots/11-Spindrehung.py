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
Alle_Daten_plotten = True #True
Einen_Datensatz_schoen_plotten = False
read_start=14 # Erste Zeile, die eingelesen wird
abgelesene_Werte_plotten = False #False 
# ------------------------------------------

Plots=0


# ------- Alle Daten Plotten ---------------
if Alle_Daten_plotten==True:
    txt_filename_to_open=["05-phasenraum-AM-1500Hz-minmax.dat"]
        

    data = [i.strip().split() for i in open(txt_filename_to_open[0]).readlines()]

    t=[]
    S=[]

    for i in range(len(data[read_start-1:])):
        t=append(t,float(data[read_start-1+i][0]))
        S=append(S,float(data[read_start-1+i][1]))
    
    k=-1
    l=1
    
    #fitfunc = lambda p, x: p[0]+p[1]*x+p[2]*x**2
    def biegen(p,x):
        return 1.0/p[0]-1-2.0/p[0]/p[1]*x+x**2/p[1]
        
    def symmetrie(p, x, y): 
        # print "----"
        # print "p", p
        # print x
        # print y
        Tide=0.0
        for n in range(len(x)):
            if (x[n]>0.02856 and x[n]<0.3929):
                if biegen(p,y[n])>0: 
                    Tide+=1
                if biegen(p,y[n])<0: 
                    Tide-=1
        # print Tide
        return Tide
    p=[random.random()*2,random.random()*2]
    # while (abs(symmetrie(p,t,S))>130):
        # p=[random.random()*2,random.random()*2]
        # print p
        # print symmetrie(p,t,S)
    # # pbest, success = optimize.leastsq(residuals, p0, args=(t, S))
    # pbest, success = optimize.anneal(residuals, p0,args=(t,S))#,schedule='fast')#, T0=1e-0,Tf=1e-50,lower=[0,-10,1],upper=[0,10,1]
    Spins=((1-S/k)**2-1)/l
    
    Plots+=1    
    plt.figure(Plots)
    plt.xlabel("Frequenz [Hz]")
    plt.ylabel("Signal [arb.u.]")
    title("verschobene Resonanzkurven")
    font = {'family' : 'serif',
            'weight' : 'normal',
            'size'   : 20}
    #plt.xlim([0.049,0.0885])
    plt.ylim([-1,0.4])
    matplotlib.rc('font', **font)
    subplots_adjust(left=0.18, bottom=0.12, right=0.96, top=0.92, wspace=0.2, hspace=0.2)
    plt.plot(t,S,"b.", label="Messpunkte")
    # plt.plot(t,biegen(p,S),"b.", label="Messpunkte")

    plt.plot([0,1],[0,0],"k--")
    # plt.plot(t2,S2,"g.", label="Messpunkte")
    # plt.plot([1510,1528,1528,1528],[0.39,0.39,0.38,0.40],"r-",linewidth=2, label="Ablesepunkte")
    # plt.plot([1510,1492,1492,1492],[0.39,0.39,0.38,0.40],"r-",linewidth=2)
    # plt.plot([1510,1514,1506,1510],[0.39-0.005,0.37-0.005,0.37-0.005,0.39-0.005],"r-",linewidth=2)
    # plt.plot(t1,linspace(out[0][0],out[0][0],len(t1)),"r",label="Messwerte", linewidth=3)

    plt.legend(loc=1)	
    # plt.savefig("Hallsteigung.pdf")
    show()
# ------------------------------------------ 


# ------- Einen_Datensatz_schoen_plotten ---
if Einen_Datensatz_schoen_plotten==True:
    txt_filename_to_open=[]
    for i in range(10):
        filename="03-Resonanzfrequenz-"+str(i)+".dat"
        txt_filename_to_open.append(filename)

    data = [i.strip().split() for i in open(txt_filename_to_open[7]).readlines()]

    t=[]
    S=[]

    for i in range(len(data[read_start-1:])):
        t=append(t,float(data[read_start-1+i][0]))
        S=append(S,float(data[read_start-1+i][1]))
        
    Plots+=1    
    plt.figure(Plots)
    plt.xlabel("Zeit [s]")
    plt.ylabel("Messsignal [arb. u.]")
    plt.xlim([0.049,0.0885])
    plt.ylim([-1.02841,0.0441123])
    title("Zeitdifferenz zwischen zwei Resonanzen \n  Analysatorfrquenz:4715023Hz")
    font = {'family' : 'serif',
            'weight' : 'normal',
            'size'   : 20}
    matplotlib.rc('font', **font)
    subplots_adjust(left=0.13, bottom=0.11, right=0.97, top=0.86, wspace=0.2, hspace=0.2)
    plt.plot(t,S,color="blue",label="Messwerte")
    plt.plot([0.0537787,0.0609017],[-0.8,-0.8],color="red",label="abgelesene Zeitdifferenz")
    plt.plot([0.0537787,0.0537787],[-0.8+0.005,-0.8-0.005],color="red")
    plt.plot([0.0537787,0.0537787],[-0.8+0.005,-0.731546],"--",color="red")
    plt.plot([0.0609017,0.0609017],[-0.8+0.005,-0.8-0.005],color="red")
    plt.plot([0.0609017,0.0609017],[-0.8+0.005,-0.543839],"--",color="red")
    plt.text(0.0574,-0.7732,u"$t_{12}$",va="center",ha="center",color="red")
    plt.legend(loc=0)	
# ------------------------------------------ 


# ------- Abgelesene Werte plotten----------
if abgelesene_Werte_plotten==True:
    Frequenzen=array([4706.795,4707.792,4709.002,4710.266,4711.791,4712.76,4713.89,4715.023,4716.449,4717.478])
    Delta_t=array([0.0175821,0.0150391,0.0135779,0.0122491,0.0105905,0.0095616,0.0083961,0.007123,0.0054044,0.0038974])
    p0=[1,5,0.04]
    fit = lambda p, x: p[0]+p[1]*cos(2*pi*x/p[2])

    def residuals(p, x, y):
        err = y-fit(p,x)
        return err
    out= optimize.leastsq(residuals, p0, args=(Delta_t, Frequenzen), full_output=1)
    print out[0]
    Plots+=1    
    plt.figure(Plots)
    plt.xlabel("Zeitdifferenz $t_{12}$ [s]")
    plt.ylabel("Frequenzen in [kHz]")    
    plt.xlim([0.002817,0.0203311])
    plt.ylim([4704.51,4722.39])
    title("Bestimmung der Resonanzfrequenz")
    font = {'family' : 'serif',
            'weight' : 'normal',
            'size'   : 20}
    matplotlib.rc('font', **font)
    subplots_adjust(left=0.13, bottom=0.12, right=0.96, top=0.92, wspace=0.2, hspace=0.2)
    plt.errorbar(Delta_t,Frequenzen,xerr=0.0002,yerr=0.002,label="bestimmte Zeitdifferenzen",fmt='r.')
    xdata=linspace(0,0.02,1000)
    plt.plot(xdata,fit(out[0],xdata),"b--",label="Cosinus-fit")
    plt.plot([0.01,0.01],[4700,4712.31],"black",label="abgelesene Resonanzfrequenz")
    plt.plot([0.00,0.01],[4712.31,4712.31],"black")
    plt.legend(loc=0)	
    # plt.savefig("Hallsteigung.pdf")
# ------------------------------------------ 

show()










