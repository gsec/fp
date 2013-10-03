# -*- coding: utf-8 -*-

from pylab import *
from scipy import *
from scipy.optimize import *
import matplotlib.pyplot as plt
from matplotlib import rc
from numpy import *

rc('font', family = 'serif', serif = 'STIXGeneral')
fig = plt.figure(num=None, figsize=(7, 5), dpi=150, facecolor='w', edgecolor='k')
fig.suptitle(u'Amplitudenverh\xe4ltnisse $T=4.2\,\mathrm{K}$ und $T=2.1\,\mathrm{K}$ \xfcber $1/B$', fontsize=14, fontweight='bold')
#def f(U):
#   return 297.0 -25.87*U + 1.908*U**2 - 0.4020*U**3;

data = genfromtxt("4,2-Laengsspannung.dat")
data2 = genfromtxt("2,1-Laengsspannung.dat")
#print data[100:,1]

B = data[:4764,1]
B2 = data2[:4733,1]
#U_H = data[:,2]/10 * 1e-3
#I_H = (data[:,3]/10 * 2e-3)/4981

U_xx = data[:4764,2]
U_xx2 = data2[:4733,2]
delta=0.005

ax = fig.add_subplot(111)
ax.plot(1/B, U_xx, "b", label=u'L\xe4ngsspannung $4.2\,\mathrm{K}$')
ax.plot([0,0],[0,0], "r", label=u'L\xe4ngsspannung $2.1\,\mathrm{K}$')
ax.plot([0.866379,0.866379],[1.701799,(1.251997+1.237223)/2], "g:")
ax.plot([0.866379-delta,0.866379+delta],[1.701799,1.701799], "g")
ax.plot([0.866379-delta,0.866379+delta],[(1.251997+1.237223)/2,(1.251997+1.237223)/2], "g")

ax.plot([0.998327,0.998327],[1.41903,(1.237223+1.180711)/2], "g:")
ax.plot([0.998327-delta,0.998327+delta],[1.41903,1.41903], "g")
ax.plot([0.998327-delta,0.998327+delta],[(1.237223+1.180711)/2,(1.237223+1.180711)/2], "g")

ax.plot([1.12913,1.12913],[1.243282,(1.180711+1.118118)/2], "g:")
ax.plot([1.12913-delta,1.12913+delta],[1.243282,1.243282], "g")
ax.plot([1.12913-delta,1.12913+delta],[(1.180711+1.118118)/2,(1.180711+1.118118)/2], "g")
ax.yaxis.label.set_color('blue')
ax.set_xlim(0.8,1.25)
ax.set_ylim(1,2)

#ax.set_xlim(0.9,1.1)
#ax.set_ylim(1,2)
ax.set_xlabel(u"Magnetfeld $1/B [\mathrm{1/T}]$")
ax.set_ylabel(u"L\xe4ngsspannung $U_{xx,4.2} [\mathrm{V}]$")


ax2 = ax.twinx()
ax2.plot(1/B2, U_xx2, "r", label=u'L\xe4ngsspannung $2.1\,\mathrm{K}$')
ax2.plot([0.866634,0.866634],[0.906952,(0.313095+0.371855)/2], "g--")
ax2.plot([0.866634-delta,0.866634+delta],[0.906952,0.906952], "g")
ax2.plot([0.866634-delta,0.866634+delta],[(0.313095+0.371855)/2,(0.313095+0.371855)/2], "g")

ax2.plot([0.996291,0.996291],[0.737017,(0.371855+0.399199)/2], "g--")
ax2.plot([0.996291-delta,0.996291+delta],[0.737017,0.737017], "g")
ax2.plot([0.996291-delta,0.996291+delta],[(0.371855+0.399199)/2,(0.371855+0.399199)/2], "g")

ax2.plot([1.12888,1.12888],[0.611532,(0.399199+0.406189)/2], "g--")
ax2.plot([1.12888-delta,1.12888+delta],[0.611532,0.611532], "g")
ax2.plot([1.12888-delta,1.12888+delta],[(0.399199+0.406189)/2,(0.399199+0.406189)/2], "g")

ax2.yaxis.label.set_color('red')
ax2.set_xlim(0.8,1.25)
ax2.set_ylim(0,1)

#ax2.set_xlim(0.9,1.1)
#ax2.set_ylim(0,1)
#ax2.plt.ylim([0,10])

ax2.set_ylabel(u"L\xe4ngsspannung $U_{xx,2.1} [\mathrm{V}]$")

ax.legend(loc=1)
#ax2.legend(loc=0)

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

fig.savefig("12-4,2-2,1-zyklotron-1-B.pdf")

show()
