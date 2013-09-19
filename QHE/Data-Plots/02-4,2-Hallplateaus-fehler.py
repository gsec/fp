# -*- coding: utf-8 -*-

from pylab import *
from scipy import *
from scipy.optimize import *
import matplotlib.pyplot as plt
from matplotlib import rc
from numpy import *

rc('font', family = 'serif', serif = 'STIXGeneral')
fig = plt.figure(num=None, figsize=(7, 5), dpi=150, facecolor='w', edgecolor='k')
fig.suptitle(r"Hallplateaus bei $T=4.2\,$K", fontsize=14, fontweight='bold', y=1)

data = genfromtxt("4,2-Hallwiderstand-Magnetfeld_bereinigt.dat")


B = data[:8500,0]								
#U_H = data[:,2]/10 * 1e-3
#I_H = (data[:,3]/10 * 2e-3)/4981

R_H = data[:8500,1]
fehlerR=0.05
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

subplots_adjust(top=0.87, right=0.96)
ax.plot(B*100, R_H, "b", label=u"Messwerte $R_\mathrm{H}$")
ax.plot(B*100, R_H-fehlerR*R_H, "b:", label=u"Fehler der Messwerte")
ax.plot(B*100, R_H+fehlerR*R_H, "b:")
ax.plot([0,0],[0,0], "r", label=u"Anzahl von Messpunkten")
ax.plot([0,0],[0,0], "g--", label=u"Niveau der Hall-Plateaus")
ax.plot([0,0],[0,0], "g:", label=u"Fehler der Hall-Plateaus")

ax.set_xlabel(u"Magnetfeld $B[T]$")
ax.set_ylabel(u"Hallwiderstand $R_{\mathrm{Hall}}[\Omega]$")

ax.xaxis.label.set_color('blue')

ax2 = ax.twiny()
ax2.plot(counts,Mittelwertkandidaten, "r", label=u"liste")
ax2.xaxis.label.set_color('red')
ax2.set_xlabel(r"Anzahl $N$")

ax.legend(loc=4)
#ax2.legend(loc=4)

ax2.plot([0,760],[Mittelwertkandidaten[wertmaximum1],Mittelwertkandidaten[wertmaximum1]], "g--", label=u"Niveau der Hall-Plateaus")
ax2.plot([0,410],[Mittelwertkandidaten[wertmaximum2],Mittelwertkandidaten[wertmaximum2]], "g--")
ax2.plot([0,300],[Mittelwertkandidaten[wertmaximum3],Mittelwertkandidaten[wertmaximum3]], "g--")
ax2.plot([0,250],[Mittelwertkandidaten[wertmaximum4],Mittelwertkandidaten[wertmaximum4]], "g--")
ax2.plot([0,220],[Mittelwertkandidaten[wertmaximum5],Mittelwertkandidaten[wertmaximum5]], "g--")
ax2.plot([0,195],[Mittelwertkandidaten[wertmaximum6],Mittelwertkandidaten[wertmaximum6]], "g--")
ax2.plot([0,180],[Mittelwertkandidaten[wertmaximum7],Mittelwertkandidaten[wertmaximum7]], "g--")

ax2.plot([0,760],[Mittelwertkandidaten[wertmaximum1]+fehlerR*Mittelwertkandidaten[wertmaximum1],Mittelwertkandidaten[wertmaximum1]+fehlerR*Mittelwertkandidaten[wertmaximum1]], "g:", label=u"Fehler der Hall-Plateaus")
ax2.plot([0,410],[Mittelwertkandidaten[wertmaximum2]+fehlerR*Mittelwertkandidaten[wertmaximum2],Mittelwertkandidaten[wertmaximum2]+fehlerR*Mittelwertkandidaten[wertmaximum2]], "g:")
ax2.plot([0,300],[Mittelwertkandidaten[wertmaximum3]+fehlerR*Mittelwertkandidaten[wertmaximum3],Mittelwertkandidaten[wertmaximum3]+fehlerR*Mittelwertkandidaten[wertmaximum3]], "g:")
ax2.plot([0,250],[Mittelwertkandidaten[wertmaximum4]+fehlerR*Mittelwertkandidaten[wertmaximum4],Mittelwertkandidaten[wertmaximum4]+fehlerR*Mittelwertkandidaten[wertmaximum4]], "g:")
ax2.plot([0,220],[Mittelwertkandidaten[wertmaximum5]+fehlerR*Mittelwertkandidaten[wertmaximum5],Mittelwertkandidaten[wertmaximum5]+fehlerR*Mittelwertkandidaten[wertmaximum5]], "g:")
ax2.plot([0,195],[Mittelwertkandidaten[wertmaximum6]+fehlerR*Mittelwertkandidaten[wertmaximum6],Mittelwertkandidaten[wertmaximum6]+fehlerR*Mittelwertkandidaten[wertmaximum6]], "g:")
ax2.plot([0,180],[Mittelwertkandidaten[wertmaximum7]+fehlerR*Mittelwertkandidaten[wertmaximum7],Mittelwertkandidaten[wertmaximum7]+fehlerR*Mittelwertkandidaten[wertmaximum7]], "g:")

ax2.plot([0,760],[Mittelwertkandidaten[wertmaximum1]-fehlerR*Mittelwertkandidaten[wertmaximum1],Mittelwertkandidaten[wertmaximum1]-fehlerR*Mittelwertkandidaten[wertmaximum1]], "g:")
ax2.plot([0,410],[Mittelwertkandidaten[wertmaximum2]-fehlerR*Mittelwertkandidaten[wertmaximum2],Mittelwertkandidaten[wertmaximum2]-fehlerR*Mittelwertkandidaten[wertmaximum2]], "g:")
ax2.plot([0,300],[Mittelwertkandidaten[wertmaximum3]-fehlerR*Mittelwertkandidaten[wertmaximum3],Mittelwertkandidaten[wertmaximum3]-fehlerR*Mittelwertkandidaten[wertmaximum3]], "g:")
ax2.plot([0,250],[Mittelwertkandidaten[wertmaximum4]-fehlerR*Mittelwertkandidaten[wertmaximum4],Mittelwertkandidaten[wertmaximum4]-fehlerR*Mittelwertkandidaten[wertmaximum4]], "g:")
ax2.plot([0,220],[Mittelwertkandidaten[wertmaximum5]-fehlerR*Mittelwertkandidaten[wertmaximum5],Mittelwertkandidaten[wertmaximum5]-fehlerR*Mittelwertkandidaten[wertmaximum5]], "g:")
ax2.plot([0,195],[Mittelwertkandidaten[wertmaximum6]-fehlerR*Mittelwertkandidaten[wertmaximum6],Mittelwertkandidaten[wertmaximum6]-fehlerR*Mittelwertkandidaten[wertmaximum6]], "g:")
ax2.plot([0,180],[Mittelwertkandidaten[wertmaximum7]-fehlerR*Mittelwertkandidaten[wertmaximum7],Mittelwertkandidaten[wertmaximum7]-fehlerR*Mittelwertkandidaten[wertmaximum7]], "g:")


#text(750, Mittelwertkandidaten[wertmaximum1]+500, r"$\nu = 2$", va='center', ha='center')
#text(300, Mittelwertkandidaten[wertmaximum2]+500, r"$\nu = 4$", va='center', ha='center')
#text(210, Mittelwertkandidaten[wertmaximum3]+500, r"$\nu = 6$", va='center', ha='center')
#text(200, Mittelwertkandidaten[wertmaximum4]+500, r"$\nu = 8$", va='center', ha='center')
#text(190, Mittelwertkandidaten[wertmaximum5]+500, r"$\nu = 10$", va='center', ha='center')
#text(180, Mittelwertkandidaten[wertmaximum6]+500, r"$\nu = 12$", va='center', ha='center')
#text(170, Mittelwertkandidaten[wertmaximum7]+500, r"$\nu = 14$", va='center', ha='center')

#text(700,8000, u"$R_\mathrm{H2}$ bei ", va='center', ha='center')
#text(780,8000, Mittelwertkandidaten[wertmaximum1], va='center', ha='center')
#text(700,7200, u"$R_\mathrm{H4}$ bei ", va='center', ha='center')
#text(780,7200, Mittelwertkandidaten[wertmaximum2], va='center', ha='center')
#text(700,6600, u"$R_\mathrm{H6}$ bei ", va='center', ha='center')
#text(780,6600, Mittelwertkandidaten[wertmaximum3], va='center', ha='center')
#text(700,5800, u"$R_\mathrm{H8}$ bei ", va='center', ha='center')
#text(780,5800, Mittelwertkandidaten[wertmaximum4], va='center', ha='center')
#text(700,5000, u"$R_\mathrm{H10}$ bei ", va='center', ha='center')
#text(780,5000, Mittelwertkandidaten[wertmaximum5], va='center', ha='center')
#text(700,4200, u"$R_\mathrm{H12}$ bei ", va='center', ha='center')
#text(780,4200, Mittelwertkandidaten[wertmaximum6], va='center', ha='center')
#text(700,3600, u"$R_\mathrm{H14}$ bei ", va='center', ha='center')
#text(780,3600, Mittelwertkandidaten[wertmaximum7], va='center', ha='center')


fig.savefig("02-4,2-Hallplateaus-fehler.pdf")

show()
