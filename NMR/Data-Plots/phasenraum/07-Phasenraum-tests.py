import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize  
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
from matplotlib.ticker import AutoMinorLocator, AutoLocator
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.collections import PolyCollection
from matplotlib.colors import colorConverter
rc('font', family = 'serif', serif = 'STIXGeneral')



# ------------------  Eingaben  ------------
Alle_Daten_plotten = True #True
Einen_Datensatz_schoen_plotten = False
read_start=14 # Erste Zeile, die eingelesen wird
abgelesene_Werte_plotten = False #False 
# ------------------------------------------

Plots=0

# dataset=zeros(18)
# for i in range(18):
	# filename="05-phasenraum-0"+str(10+5*i)+"mV-minmax-FM.dat"
	# dataset[i]=float(filename)
	

fig = plt.figure()
ax = fig.gca(projection='3d')

verts=[]
zdata = np.arange(10,100,5)
# for z in zdata:
	# data = genfromtxt("05-phasenraum-040mV-minmax-FM.dat")
	# #data = genfromtxt(dataset[z])
	# xdata = data[:,0]
	# ydata = data[:,1]
	# verts.append(list(zip(xdata,ydata)))
	
data = genfromtxt("05-phasenraum-040mV-minmax-FM.dat")

xdata = data[:,0]
ydata = data[:,1]
verts.append(list(zip(xdata,ydata)))

	
poly = PolyCollection(verts)
#poly.set_alpha(0.7)
ax.add_collection3d(poly, zs=zdata, zdir='y')

ax.set_xlabel('X')
ax.set_xlim3d(1200, 1800)
ax.set_ylabel('Y')
ax.set_ylim3d(0, 100)
ax.set_zlabel('Z')
ax.set_zlim3d(-0.8, 0.6)

plt.show() 
# ------- Alle Daten Plotten ---------------
# if Alle_Daten_plotten==True:
    # txt_filename_to_open=[]
    # for i in range(18):
        # filename="05-phasenraum-0"+str(10+5*i)+"mV-minmax-FM.dat"
        # txt_filename_to_open.append(filename)
    # txt_filename_to_open.append("05-phasenraum-100mV-minmax-FM.dat")
    # print txt_filename_to_open
 
    
    # Frequenz=zeros(125000)
    # Amplitude=zeros(125000) 
    # Signal=zeros(125000)
    # z=0; nj=0
    # for n in range(len(txt_filename_to_open)):
        # print "reed file #", n
        # data = [i.strip().split() for i in open(txt_filename_to_open[n]).readlines()]

        # for i in range(len(data[read_start-1:])):
            # if nj==200:
                # nj=0
                # Frequenz[z]=float(data[read_start-1+i][0])
                # Amplitude[z]=10+n*5
                # Signal[z]=float(data[read_start-1+i][1])
                # z+=1
            # nj+=1
    # for n in range(len(Amplitude)):
        # if Amplitude[n]==0:
            # Frequenz=Frequenz[0:n]
            # Amplitude=Amplitude[0:n]
            # Signal=Signal[0:n]
            # break
       

   
# fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax = Axes3D(fig)
#verts = [zip(Frequenz, Amplitude, Signal)]

# ax = fig.gca(projection='3d')

# cc = lambda arg: colorConverter.to_rgba(arg, alpha=0.6)


#Datensaetze getrennt einlesen
# xs = Frequenz
# verts = []
# zs = Amplitude
# for z in zs:
    # ys = zeros(len(xs))
    # ys[0], ys[-1] = 1200, 1800
    # verts.append(list(zip(Frequenz, Signal)))



# poly = PolyCollection(verts)
# #poly.set_alpha(0.7)
# ax.add_collection3d(poly, zs=zs, zdir='y')


# #ax.plot_surface(Frequenz, Amplitude, Signal, rstride=10, cstride=10)#, rstride=1, cstride=1, cmap=cm.coolwarm, #Signal,s=50, c=abs(Signal), cmap="jet"
# #ax.add_collection3d(Poly3DCollection(verts))
# #poly = PolyCollection(verts)
        # #linewidth=0, antialiased=False)
# # #ax.set_zlim(-1.01, 1.01)

# ax.set_xlabel('X')
# ax.set_xlim3d(1200, 1800)
# ax.set_ylabel('Y')
# ax.set_ylim3d(0, 100)
# ax.set_zlabel('Z')
# ax.set_zlim3d(-0.8, 0.6)


# # ax.zaxis.set_major_locator(LinearLocator(10))
# # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# # fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show() 
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

show()










