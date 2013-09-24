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

txt_filename_to_open=["05-phasenraum-045mV-minmax-FM.dat"]

data1 = [i.strip().split() for i in open(txt_filename_to_open[0]).readlines()]
theo_data=[i.strip().split() for i in open("ThFreData_von_Mathematica.dat").readlines()]
ex_data=[i.strip().split() for i in open("ExFreData_von_Mathematica.dat").readlines()]

# print theo_data

t1=[]; t2=[]; S1=[]; S2=[]

for i in range(len(data1[read_start-1:])):
    t1=append(t1,float(data1[read_start-1+i][0])) 
    S1=append(S1,float(data1[read_start-1+i][1]))
    

if  Alle_Daten_plotten == True :
    plt.figure(0)
    plt.xlabel(u"Frequenz [Hz]")
    plt.ylabel(u"Signal [arb.u.]")
    title("Frequenzsweep mit 45mV Einstrahlspannung")
    font = {'family' : 'serif',
            'weight' : 'normal',
            'size'   : 20}
    #plt.xlim([0.049,0.0885])
    plt.ylim([-1,1.5])
    matplotlib.rc('font', **font)
    subplots_adjust(left=0.18, bottom=0.12, right=0.96, top=0.92, wspace=0.2, hspace=0.2)
    # plt.plot(t1,S1,"b.", label="off")
    plt.plot(t1,ex_data,"r.", label="Messpunkte")
    plt.plot(t1,theo_data,"b.", label="Theorie")
    plt.plot([1300,1700],[0.1721,0.1721],"k--")
    s=0.05
    plt.plot([1477,1477,1477,1544,1544,1544],[0.0035-s,0.0035+s,0.0035,0.0035,0.0035-s,0.0035+s],"r")
    plt.text(1510,-0.1,r'$\nu_\mathrm{Halb}$',va="center",ha="center",color="red")
    # plt.plot([0,1],[0,0],"k--")

    plt.legend(loc=1)	
    show()
 
# # Verschiebung anpassen  
# t=t1-0.0053548
# S=S1

# def biegen(kl,x):
    # return 2.0/kl[1]/kl[0]*x+x**2/kl[0]**2/kl[1]

# # fitfunc = lambda p, x: p[0] * cos(2*pi*p[1]*x+p[2])+p[3]
# # 
# # p0 = [5.0e-02, 2.6e3, -1.9, 1.8e-4]

# kl0=[1,1]
# def resiuum(kl):
    # y=copy(S)
    
    # tide=0
    # newpoints=2.0/kl[1]/kl[0]*y+y**2/kl[0]**2/kl[1]
    # print "----------------------"
    # print "alte Punkte:",y
    # print "mit PArametern:", kl
    # print "neue Punkte:", newpoints
    # for n in range(len(t)):
        # if (t[n]>0.04000373 and t[n]<0.264918):
            # tide+=y[n]
    # print "Flaeche: ",tide
    # return abs(tide)        
    
# #klbest= optimize.fmin(resiuum,kl0)
# # print "klbest: ", klbest
# # 0.264918
# # 0.04000373
# plotx=linspace(0,0.4,6400)
# ploty=exp(-4.5*plotx)

# plt.figure(0)
# plt.xlabel(u"Intensit\xe4t [mV]")
# plt.ylabel(u"Signal [arb.u.]")
# title("Spindrehungskurve")
# font = {'family' : 'serif',
        # 'weight' : 'normal',
        # 'size'   : 20}
# #plt.xlim([0.049,0.0885])
# plt.ylim([-0.85,0.85])
# plt.xlim([0,0.4])
# matplotlib.rc('font', **font)
# subplots_adjust(left=0.18, bottom=0.12, right=0.96, top=0.92, wspace=0.2, hspace=0.2)
# # plt.plot(t,S,"r.", label="Messpunkte")
# plt.plot(t,biegen([0.85,1.14],S),"r.", label="symmetrisierte Messpunkte") #{k -> 0.85, l -> 1.14};
# plt.plot(t,theo_data,"b.", label="theorie")
# # plt.plot(plotx,ploty,"r.", label="exp")
# # plt.plot(t,biegen([1,1],S),"g.", label="Messpunkte")
# # plt.plot(t1,S1,"b.", label="Messpunkte")
# # plt.plot(t2,S2,"r.", label="Messpunkte")
# # plt.plot([0,1],[0,0],"k--")

# plt.legend(loc=1)	 
# show()

# # f = file('kl-Daten.dat', 'w')
# # for n in range(len(S)):
    # # f.write(str(biegen([-0.64,-1.58],S)[n])+'\n')
# # f.close()










# # ------- Alle Daten Plotten ---------------
# if Alle_Daten_plotten==True:
    # txt_filename_to_open=["05-phasenraum-AM-1500Hz-minmax.dat"]
        

    # data = [i.strip().split() for i in open(txt_filename_to_open[0]).readlines()]

    # t=[]
    # S=[]

    # for i in range(len(data[read_start-1:])):
        # t=append(t,float(data[read_start-1+i][0]))
        # S=append(S,float(data[read_start-1+i][1]))
    
    # k=-1
    # l=1
    
    # #fitfunc = lambda p, x: p[0]+p[1]*x+p[2]*x**2
    # def biegen(p,x):
        # return 1.0/p[0]-1-2.0/p[0]/p[1]*x+x**2/p[1]
        
    # def symmetrie(p, x, y): 
        # # print "----"
        # # print "p", p
        # # print x
        # # print y
        # Tide=0.0
        # for n in range(len(x)):
            # if (x[n]>0.02856 and x[n]<0.3929):
                # Tide+=biegen(p,y[n])**2
        # print p,Tide
        # return Tide
    # p=[random.random()*2,random.random()*2]
    # Tidebest=100000
    # while (True):
        # p=[(random.random()+1)*4,random.random()*1.1]
        # if abs(symmetrie(p,t,S))<Tidebest:
            # Tidebest=symmetrie(p,t,S)
            # print symmetrie(p,t,S)
            # Plots+=1    
            # plt.figure(Plots)
            # plt.xlabel("Frequenz [Hz]")
            # plt.ylabel("Signal [arb.u.]")
            # title("verschobene Resonanzkurven")
            # font = {'family' : 'serif',
                    # 'weight' : 'normal',
                    # 'size'   : 20}
            # #plt.xlim([0.049,0.0885])
            # plt.ylim([-1,0.4])
            # matplotlib.rc('font', **font)
            # subplots_adjust(left=0.18, bottom=0.12, right=0.96, top=0.92, wspace=0.2, hspace=0.2)
            # plt.plot(t,S,"b.", label="Messpunkte")
            # plt.plot(t,biegen([1.3,0.2],S),"r.", label="Messpunkte")

            # plt.plot([0,1],[0,0],"k--")

            # plt.legend(loc=1)	
            # show()
                        
            
            
        

    # # # pbest, success = optimize.leastsq(residuals, p0, args=(t, S))
    # # pbest, success = optimize.anneal(residuals, p0,args=(t,S))#,schedule='fast')#, T0=1e-0,Tf=1e-50,lower=[0,-10,1],upper=[0,10,1]
    # Spins=((1-S/k)**2-1)/l
    
    # Plots+=1    
    # plt.figure(Plots)
    # plt.xlabel("Frequenz [Hz]")
    # plt.ylabel("Signal [arb.u.]")
    # title("verschobene Resonanzkurven")
    # font = {'family' : 'serif',
            # 'weight' : 'normal',
            # 'size'   : 20}
    # #plt.xlim([0.049,0.0885])
    # plt.ylim([-1,0.4])
    # matplotlib.rc('font', **font)
    # subplots_adjust(left=0.18, bottom=0.12, right=0.96, top=0.92, wspace=0.2, hspace=0.2)
    # plt.plot(t,S,"b.", label="Messpunkte")
    # plt.plot(t,biegen([1.3,0.2],S), label="Messpunkte")

    # plt.plot([0,1],[0,0],"k--")

    # plt.legend(loc=1)	
    # show()
# # ------------------------------------------ 









