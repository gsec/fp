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

Plots=0


# ------- Alle Daten Plotten ---------------
if Alle_Daten_plotten==True:
    txt_filename_to_open=["05-phasenraum-010mV-maxmin-FM.dat","05-phasenraum-010mV-minmax-FM.dat"]
        

    data1 = [i.strip().split() for i in open(txt_filename_to_open[0]).readlines()]
    data2 = [i.strip().split() for i in open(txt_filename_to_open[1]).readlines()]

    t1=[]
    t2=[]
    S1=[]
    S2=[]

    for i in range(len(data1[read_start-1:])):
        t1=append(t1,float(data1[read_start-1+i][0]))
        S1=append(S1,float(data1[read_start-1+i][1]))
    for i in range(len(data2[read_start-1:])):
        t2=append(t2,float(data2[read_start-1+i][0]))
        S2=append(S2,float(data2[read_start-1+i][1]))      
    
    #p0=[-0.6,1,1,1500]
    #fit = lambda p, x: p[0]+p[1]*p[2]/(p[2]**2+(x-p[3])**2)
    # p0=[-0.6,1,1500,100]
    # fit = lambda p, x: p[0]+p[1]*exp(-(x-p[2])**2/(2*p[3]**2))
    p0=[-0.6]
    fit = lambda p, x: p[0]
    
    def residuals(p, x, y):
        err = y-fit(p,x)
        return err
    xdata=[]
    ydata=[]
    xdata.extend(t1[:1000])
    xdata.extend(t1[-1000:])
    xdata.extend(t2[:1000])
    xdata.extend(t2[-1000:])
    ydata.extend(S1[:1000])
    ydata.extend(S1[-1000:])
    ydata.extend(S2[:1000])
    ydata.extend(S2[-1000:])   
    print len(xdata)

    out= optimize.leastsq(residuals, p0, args=(xdata, ydata), full_output=1)
    
    Gewicht1=0
    Norm1=0
    for i in range(len(t1)):
        Gewicht1+=(S1[i]-out[0][0])*t1[i]
        Norm1+=S1[i]-out[0][0]
    Gewicht1=Gewicht1/Norm1    
    
    Gewicht2=0
    Norm2=0
    for i in range(len(t2)):
        Gewicht2+=(S2[i]-out[0][0])*t2[i]
        Norm2+=S2[i]-out[0][0]
    Gewicht2=Gewicht2/Norm2    
    
    # print len(t1), len(t2)
    # print Gewicht1
    # print Gewicht2
    # print Gewicht1/Gewicht1
    # print out[0]
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
    plt.plot(t1,S1,"b.")
    plt.plot([Gewicht1],[-0.6],"bo",label="Messpunkte mit dem Gewicht des Peaks")
    plt.plot(t2,S2,"g.")
    plt.plot([Gewicht2],[-0.6],"go",label="Messpunkte mit dem Gewicht des Peaks")
    # plt.plot(t1,linspace(out[0][0],out[0][0],len(t1)),"r",label="Messwerte", linewidth=3)
    print "Gewicht1 ",Gewicht1
    print "Gewicht2 ",Gewicht2
    print "Mittel: ", (Gewicht1+Gewicht2)/2
    print "Verschiebung: ", (Gewicht1-Gewicht2)/2
    plt.legend(loc=4)	
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










