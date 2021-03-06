import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize  
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
from matplotlib.ticker import AutoMinorLocator, AutoLocator
rc('font', family = 'serif', serif = 'STIXGeneral')



# ------------------  Eingaben  ------------
Alle_Daten_plotten = True #True
Einen_Datensatz_schoen_plotten = False
read_start=14 # Erste Zeile, die eingelesen wird
abgelesene_Werte_plotten = False #False 
# ------------------------------------------

Plots=0


# ------- Alle Daten Plotten ---------------
if Alle_Daten_plotten==True:
    txt_filename_to_open=[]
    for i in range(18):
        filename="05-phasenraum-0"+str(10+5*i)+"mV-minmax-FM.dat"
        txt_filename_to_open.append(filename)
    txt_filename_to_open.append("05-phasenraum-100mV-minmax-FM.dat")
    # print txt_filename_to_open
 
    
    Frequenz=zeros(125000)
    Amplitude=zeros(125000) 
    Signal=zeros(125000)
    z=0
    for n in range(len(txt_filename_to_open)):
        # print "reed file #", n
        data = [i.strip().split() for i in open(txt_filename_to_open[n]).readlines()]

        for i in range(len(data[read_start-1:])):
                Frequenz[z]=float(data[read_start-1+i][0])
                Amplitude[z]=10+n*5
                Signal[z]=float(data[read_start-1+i][1])
                z+=1
    for n in range(len(Amplitude)):
        if Amplitude[n]==0:
            Frequenz=Frequenz[0:n]
            Amplitude=Amplitude[0:n]
            Signal=Signal[0:n]
            break

Plots+=1     
A45_Frequenz=[]
A45_Signal=[]
for n in range(len(Amplitude)):
    if Amplitude[n]==45:
        A45_Frequenz=append(A45_Frequenz,Frequenz[n])
        A45_Signal=append(A45_Signal,Signal[n])
print A45_Signal
       
# --- Theorieteil ---
gamma=0.267522212e9;B1=1.583e-6;vres=1507.0
nu=arange(1300,1700,0.1)
print B1
print gamma
print cos(pi)
Theo_Signal=-((((2*pi*(vres-nu)/gamma/B1))**2+cos(pi*sqrt(1+((2*pi*(vres-nu)/gamma/B1))**2)))/(1+(2*pi*(vres-nu)/gamma/B1)**2))*0.555-0.105


(2*pi*(vres-nu)/gamma/B1)

plt.figure(Plots)
plt.xlabel("Frequenz [Hz]")
plt.ylabel("Messsignal [arb. u.]")
# plt.xlim([0.049,0.0885])
# plt.ylim([-1.02841,0.0441123])Linearit\xe4t
title(u'Resonanzkurve bei $45$mA Einstrahlintensit\xe4t')
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 20}
matplotlib.rc('font', **font)
subplots_adjust(left=0.13, bottom=0.11, right=0.97, top=0.86, wspace=0.2, hspace=0.2)
plt.plot(A45_Frequenz,A45_Signal,".",color="blue",label="Messwerte")
plt.plot(nu,Theo_Signal,".",color="red",label="Messwerte")
# plt.plot([0.0537787,0.0609017],[-0.8,-0.8],color="red",label="abgelesene Zeitdifferenz")
# plt.plot([0.0537787,0.0537787],[-0.8+0.005,-0.8-0.005],color="red")
# plt.plot([0.0537787,0.0537787],[-0.8+0.005,-0.731546],"--",color="red")
# plt.plot([0.0609017,0.0609017],[-0.8+0.005,-0.8-0.005],color="red")
# plt.plot([0.0609017,0.0609017],[-0.8+0.005,-0.543839],"--",color="red")
# plt.text(0.0574,-0.7732,u"$t_{12}$",va="center",ha="center",color="red")
plt.legend(loc=0)	


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










