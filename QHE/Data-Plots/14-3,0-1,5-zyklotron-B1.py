# -*- coding: utf-8 -*-

from pylab import *
from scipy import *
from scipy.optimize import *
import matplotlib.pyplot as plt
from matplotlib import rc
from numpy import *

rc('font', family = 'serif', serif = 'STIXGeneral')
fig = plt.figure(num=None, figsize=(7, 5), dpi=150, facecolor='w', edgecolor='k')

#def f(U):
#   return 297.0 -25.87*U + 1.908*U**2 - 0.4020*U**3;

data = genfromtxt("3,0-Laengsspannung.dat")
data2 = genfromtxt("1,5-Laengsspannung.dat")
#print data[100:,1]

B = data[:4795,1]
B2 = data2[:4706,1]
#U_H = data[:,2]/10 * 1e-3
#I_H = (data[:,3]/10 * 2e-3)/4981

U_xx = data[:4795,2]
U_xx2 = data2[:4706,2]

ax = fig.add_subplot(111)
ax.plot(1/B, U_xx, "b", label=u'L\xe4ngsspannung $4.2\,\mathrm{K}$')
ax.plot([1.261642,1.261642],[0.420798+0.65,0.32332+0.65], "g:")
ax.plot([1.129482,1.129482],[0.564149+0.65,0.345374+0.65], "g:")
ax.plot([0.997019,0.997019],[0.789982+0.65,0.343169+0.65], "g:")
ax.yaxis.label.set_color('blue')
ax.set_xlim(0.9,1.3)
ax.set_ylim(0.9,1.9)

#ax.set_xlim(0.9,1.1)
#ax.set_ylim(1,2)
ax.set_xlabel(u"Magnetfeld $B$")
ax.set_ylabel(u"L\xe4ngsspannung $U_{\mathrm{xx,4.2}}$")


ax2 = ax.twinx()
ax2.plot(1/B2, U_xx2, "r", label=u'L\xe4ngsspannung $2.1\,\mathrm{K}$')
ax2.plot([1.256264,1.256264],[0.51469,0.343928], "g--")
ax2.plot([1.127322,1.127322],[0.610938,0.323747], "g--")
ax2.plot([0.996463,0.996463],[0.745995,0.28649], "g--")
ax2.yaxis.label.set_color('red')
ax2.set_xlim(0.9,1.3)
ax2.set_ylim(0.25,1.25)

#ax2.set_xlim(0.9,1.1)
#ax2.set_ylim(0,1)
#ax2.plt.ylim([0,10])

ax2.set_ylabel(u"L\xe4ngsspannung $U_{xx,2.1}$")

ax.legend(loc=0)
ax2.legend(loc=0)

# y = log(data[:,1]/(8e-3*1.63e-3*2.74e-3))
# y = log(data[:,1]*(1.63e-3*2.74e-3)/(8e-3*4.2e-3))

#X = x[0:14]
#Y = y[0:14]

#fitfunc = lambda p, x: p[0]*x + p[1]
#errfunc = lambda p, x, y: fitfunc(p, x) - y
#P, success = leastsq(errfunc, [1, 1], args=(X, Y))




#plot(x, fitfunc(P, x), "r", label="Ausgleichsgerade")
#plot(x, -0.0105*x + 0.9, "r--", label="Fehlergerade")
#plot(x, -0.0077*x + 0.65, "r--")

#plot([207, 207], [0.0, -4.5], "k", label="Inversionstemperatur")

#fitfunc = lambda p, x: p[0] + p[1]*x + p[2]*x**2+ p[3]*x**3 + p[4]*x**4 + p[5]*x**5
#errfunc = lambda p, x, y: fitfunc(p, x) - y
#p, success = leastsq(errfunc, [1, 1, 1, 0, 1, 1, 1, 1, 1], args=(x, y))
#R = linspace(min(x), max(x), 1000)
#plot(R, fitfunc(p, R), label="Ausgleichende Kurve")

#errorbar(x, y, yerr=len(x)*[0.04], xerr=len(x)*[1], fmt="g.", label="Messpunkte mit Fehlerbalken")

fig.savefig("11-4,2-2,1-zyklotron-B.pdf")

show()
