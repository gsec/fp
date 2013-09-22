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
    z=0; nj=0
    for n in range(len(txt_filename_to_open)):
        # print "reed file #", n
        data = [i.strip().split() for i in open(txt_filename_to_open[n]).readlines()]

        for i in range(len(data[read_start-1:])):
            if nj==200:
                nj=0
                Frequenz[z]=float(data[read_start-1+i][0])
                Amplitude[z]=10+n*5
                Signal[z]=float(data[read_start-1+i][1])
                z+=1
            nj+=1
    for n in range(len(Amplitude)):
        if Amplitude[n]==0:
            Frequenz=Frequenz[0:n]
            Amplitude=Amplitude[0:n]
            Signal=Signal[0:n]
            break
       
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
print type(matplotlib.colors.Normalize(abs(Signal)))
ax.scatter(Frequenz, Amplitude, Signal,s=50, c=abs(Signal), cmap="jet")#, rstride=1, cstride=1, cmap=cm.coolwarm,
        #linewidth=0, antialiased=False)
# #ax.set_zlim(-1.01, 1.01)

# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show() 
        # Plots+=1    
        # plt.figure(Plots)
        # plt.xlabel(data[read_start-2][0:3])
        # plt.ylabel(data[read_start-2][3:6])
        # title(data[6])
        # font = {'family' : 'serif',
                # 'weight' : 'normal',
                # 'size'   : 20}
        # matplotlib.rc('font', **font)
        # subplots_adjust(left=0.18, bottom=0.12, right=0.96, top=0.92, wspace=0.2, hspace=0.2)
        # plt.plot(t,S,color="blue",label="Messwerte")
        # plt.legend(loc=0)	
        # # plt.savefig("Hallsteigung.pdf")
        # show()
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










