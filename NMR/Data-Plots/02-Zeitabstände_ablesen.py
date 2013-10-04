import numpy as np
from scipy import optimize  
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import AutoMinorLocator, AutoLocator
rc('font', family = 'serif', serif = 'STIXGeneral')


# ------------------  Eingaben  ------------
Alle_Daten_plotten = False #True
Einen_Datensatz_schoen_plotten = True
read_start=10 # Erste Zeile, die eingelesen wird
abgelesene_Werte_plotten = False #False #
Signalhoehen_plotten = True
# ------------------------------------------

Plots=0


# ------- Alle Daten Plotten ---------------
if Alle_Daten_plotten==True:
    txt_filename_to_open=[]
    for i in range(10):
        filename="03-Resonanzfrequenz-"+str(i)+".dat"
        txt_filename_to_open.append(filename)
        
    for n in range(len(txt_filename_to_open)):
        data = [i.strip().split() for i in open(txt_filename_to_open[n]).readlines()]

        t=[]
        S=[]

        for i in range(len(data[read_start-1:])):
            t=append(t,float(data[read_start-1+i][0]))
            S=append(S,float(data[read_start-1+i][1]))
            
        Plots+=1    
        plt.figure(Plots)
        plt.xlabel(data[read_start-2][0:3])
        plt.ylabel(data[read_start-2][3:6])
        title(data[6])
        font = {'family' : 'serif',
                'weight' : 'normal',
                'size'   : 20}
        matplotlib.rc('font', **font)
        subplots_adjust(left=0.18, bottom=0.12, right=0.96, top=0.92, wspace=0.2, hspace=0.2)
        plt.plot(t,S,color="blue",label="Messwerte")
        plt.legend(loc=0)	
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
    title("Zeitdifferenz zwischen zwei Resonanzen \n  Analysatorfrequenz:4715023Hz")
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
    fit = lambda p, x: p[0]+p[1]*cos(2*pi*x/0.04)

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
    plt.plot(xdata,fit(out[0],xdata),"b--",label=r'Cosinus-fit mit Periodendauer 0.04s') # ,prop='size':10)
    plt.plot([0.01,0.01],[4700,4712.31],"black",label="abgelesene Resonanzfrequenz")
    plt.plot([0.00,0.01],[4712.31,4712.31],"black")
    plt.legend(loc=0)	
    # plt.savefig("Hallsteigung.pdf")
# ------------------------------------------ 

if Signalhoehen_plotten==True:
    Signalhoehen=array([0.2923985,0.4460165,0.551707,0.5760975,0.6004875,0.6665,0.663496,0.7051985,0.738354,0.715488])
    Fehler_Signalhoehe=([0.0248985,0.0182925,0.012195,0.0101625,0.0101625,0.009191,0.014228,0.0331555,0.022866,0.022866])
    Delta_t=array([0.0024179,0.0049609,0.0064221,0.0077509,0.0094095,0.0104384,0.0116039,0.012877,0.0145956,0.0161026])
    Fehler_t=0.0002
    
    Plots+=1    
    plt.figure(Plots)
    plt.xlabel("Zeitdifferenz $t_{12}$ [s]")
    plt.ylabel("Messsignal $S_2$ [arb. u.]")    
    #plt.xlim([0.002817,0.0203311])
    #plt.ylim([4704.51,4722.39])
    title(u'Signalh\xf6hen im Resonanzfall')
    font = {'family' : 'serif',
            'weight' : 'normal',
            'size'   : 20}
    matplotlib.rc('font', **font)
    subplots_adjust(left=0.13, bottom=0.12, right=0.96, top=0.92, wspace=0.2, hspace=0.2)
    plt.errorbar(Delta_t,Signalhoehen,xerr=0.0002,yerr=Fehler_Signalhoehe,label=u"bestimmte Signalh\xf6hen",fmt='r.')
    xdata=linspace(0,0.02,1000)
    plt.legend(loc=0)	


show()










