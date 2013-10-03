# -*- coding: utf-8 -*-


from scipy import *
from scipy import optimize
from matplotlib import rc
from numpy import *
import matplotlib.pyplot as plt

# from fitting import *
from pylab import *

rc('font', family = 'serif', serif = 'STIXGeneral')
fig = plt.figure(num=None, figsize=(7, 5), dpi=150, facecolor='w', edgecolor='k')

fig.suptitle(r"Bestimmung des Eichfaktors $U_\mathrm{ES}/U_\mathrm{FG}$", fontsize=14, fontweight='bold')


txt_filename_to_open_mit=["02-Funktionsgenerator-1,3kHz-10mV-mit-ESP.dat", "02-Funktionsgenerator-1,3kHz-20mV-mit-ESP.dat", "02-Funktionsgenerator-1,3kHz-50mV-mit-ESP.dat", "02-Funktionsgenerator-1,3kHz-100mV-mit-ESP.dat", "02-Funktionsgenerator-1,3kHz-200mV-mit-ESP.dat", "02-Funktionsgenerator-1,3kHz-500mV-mit-ESP.dat"]
txt_filename_to_open_ohne=["02-Funktionsgenerator-1,3kHz-10mV-ohne-ESP.dat", "02-Funktionsgenerator-1,3kHz-20mV-ohne-ESP.dat", "02-Funktionsgenerator-1,3kHz-50mV-ohne-ESP.dat", "02-Funktionsgenerator-1,3kHz-100mV-ohne-ESP.dat", "02-Funktionsgenerator-1,3kHz-200mV-ohne-ESP.dat", "02-Funktionsgenerator-1,3kHz-500mV-ohne-ESP.dat", ]



Amplitude_mit=zeros(len(txt_filename_to_open_mit))
Amplitude_ohne=zeros(len(txt_filename_to_open_ohne))


print "=======mit ESP========="
for n in range(len(txt_filename_to_open_mit)):
	data = genfromtxt(txt_filename_to_open_mit[n])
	print "n: ", n
	x=data[:100,0]
	y=data[:100,1]

	fitfunc = lambda p, x: p[0] * cos(2*pi*p[1]*x+p[2])+p[3]
	errfunc = lambda p, x, y: fitfunc(p, x) - y
	p0 = [5.0e-02, 1.3e3, -1.9, 1.8e-4]
	pbest, success = optimize.leastsq(errfunc, p0, args=(x, y))
	print "pbest :", pbest
	Amplitude_mit[n] = abs(pbest[0])
print "Amplituden mit:", Amplitude_mit

print "=======ohne ESP========="
for n in range(len(txt_filename_to_open_ohne)):
	data = genfromtxt(txt_filename_to_open_ohne[n])
	print "n: ", n
	x=data[:100,0]
	y=data[:100,1]

	fitfunc = lambda p, x: p[0] * cos(2*pi*p[1]*x+p[2])+p[3]
	errfunc = lambda p, x, y: fitfunc(p, x) - y
	p0 = [5.0e-02, 1.3e3, -1.9, 1.8e-4]
	pbest, success = optimize.leastsq(errfunc, p0, args=(x, y))
	print "pbest :", pbest
	Amplitude_ohne[n] = abs(pbest[0]/2) # oder *47/(47+50) ??


	
print "Amplituden ohne:", Amplitude_ohne

fitfunc = lambda p, Amplitude_ohne: p[0]*Amplitude_ohne
errfunc = lambda p, Amplitude_ohne, Amplitude_mit: fitfunc(p, Amplitude_ohne) - Amplitude_mit
p0 = [0, 0]
pbest, success = optimize.leastsq(errfunc, p0, args=(Amplitude_ohne, Amplitude_mit))
	

print "Steigung :", pbest[0], "+-",pbest[0]*0.02

ax = fig.add_subplot(111)
subplots_adjust(top=0.90, right=0.96)
plt.errorbar(Amplitude_ohne, Amplitude_mit, xerr=0.02*Amplitude_ohne, yerr=0.02*Amplitude_mit, label=u"Messdaten mit Fehler", fmt="r.")
ax.plot(Amplitude_ohne, fitfunc(pbest, Amplitude_ohne), "b", label="ausgleichene Gerade")
ax.plot(Amplitude_ohne, Amplitude_mit+Amplitude_mit*0.02, "b--", label="Fehlergeraden")
ax.plot(Amplitude_ohne, Amplitude_mit-Amplitude_mit*0.02, "b--")

ax.set_xlabel(u"Spannung der Amplitude am Funtionsgeneragor $U_\mathrm{FG}[\mathrm{mV}]$")
ax.set_ylabel(u"Spannung der Amplitude an der Einstrahlspule $U_\mathrm{ES}[\mathrm{mV}]$")



ax.legend(loc=0)

fig.savefig("03-Effektivwert-es-fg.pdf")

show()

