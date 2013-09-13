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

data = genfromtxt("4,2-Hallspannung.dat")

#print data[100:,1]

B = data[:,1]
U_H = data[:,2]/10 * 1e-3
I_H = (data[:,3]/10 * 2e-3)/4981

R_H = U_H/I_H

delta = 50
step = 100

Mittelwertkandidaten=range(0,16000,step)
counts = zeros(len(Mittelwertkandidaten))

print "Laenge Mittelwertkandidaten:", len(Mittelwertkandidaten)

for i in range(len(Mittelwertkandidaten)):
	print i
	for j in R_H:
		if abs(Mittelwertkandidaten[i]-j) < delta:
			counts[i]+=1


maximum1=max(counts[11000/step:16000/step])
maximum2=max(counts[5000/step:8000/step])
maximum3=max(counts[3800/step:4200/step])
maximum4=max(counts[2900/step:3300/step])
maximum5=max(counts[2300/step:2600/step])
maximum6=max(counts[1900/step:2200/step])
maximum7=max(counts[1600/step:1900/step])

wertmaximum1=argmax(counts[11000/step:16000/step])+11000/step
wertmaximum2=argmax(counts[5000/step:8000/step])+5000/step
wertmaximum3=argmax(counts[3800/step:4200/step])+3800/step
wertmaximum4=argmax(counts[2900/step:3300/step])+2900/step
wertmaximum5=argmax(counts[2300/step:2600/step])+2300/step
wertmaximum6=argmax(counts[1900/step:2200/step])+1900/step
wertmaximum7=argmax(counts[1600/step:1900/step])+1600/step

print "Laenge Mittelwertkandidaten:", len(Mittelwertkandidaten)
print "Maxima:", maximum1, maximum2, maximum3, maximum4, maximum5, maximum6, maximum7
print "argmax:", wertmaximum1, wertmaximum2, wertmaximum3, wertmaximum4, wertmaximum5, wertmaximum6, wertmaximum7
print "Mittelwertkandidaten der Maxima:", Mittelwertkandidaten[wertmaximum1], Mittelwertkandidaten[wertmaximum2], Mittelwertkandidaten[wertmaximum3], Mittelwertkandidaten[wertmaximum4], Mittelwertkandidaten[wertmaximum5], Mittelwertkandidaten[wertmaximum6], Mittelwertkandidaten[wertmaximum7]


ax = fig.add_subplot(111)
ax.plot(B*100, R_H, "x", label=u"Messwerte")
ax.set_xlabel(u"Magnetfeld $B$")
ax.set_ylabel(u"Hallwiderstand $R_{\mathrm{Hall}}$")

ax2 = ax.twiny()
ax2.plot(counts,Mittelwertkandidaten, "r", label=u"liste")
ax2.set_xlabel(r"Anzahl $N$")

ax.legend(loc=2)
ax2.legend(loc=4)

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



show()