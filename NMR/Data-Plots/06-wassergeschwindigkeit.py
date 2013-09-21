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

fig.suptitle(u"Untersuchung der Linearit\xe4t von Messsignal zu Polarisationsstrom", fontsize=14, fontweight='bold')

txt_filename_to_open_10C=["07-relaxation-10C-6V.dat", "07-relaxation-10C-7,5V.dat", "07-relaxation-10C-9V.dat", "07-relaxation-10C-10,5V.dat", "07-relaxation-10C-12V-2.dat"]
txt_filename_to_open_20C=["07-relaxation-20C-3V.dat", "07-relaxation-20C-5V.dat", "07-relaxation-20C-5,5V.dat", "07-relaxation-20C-6V.dat", "07-relaxation-20C-7,5V.dat", "07-relaxation-20C-9V.dat", "07-relaxation-20C-10,5V.dat", "07-relaxation-20C-12V.dat"]
txt_filename_to_open_40C=["07-relaxation-40C-6V.dat", "07-relaxation-40C-7,5V.dat", "07-relaxation-40C-9V.dat", "07-relaxation-40C-10,5V.dat", "07-relaxation-40C-12V.dat"]
txt_filename_to_open_60C=["07-relaxation-60C-6V.dat", "07-relaxation-60C-7,5V-2.dat", "07-relaxation-60C-9V.dat", "07-relaxation-60C-10,5V.dat", "07-relaxation-60C-12.dat", ]


# Signal=zeros(len(txt_filename_to_open))
# Fehler=zeros(len(txt_filename_to_open))

for n in range(len(txt_filename_to_open_10C)):
	data = genfromtxt(txt_filename_to_open_10C[n])
	print "n: ", n
	x=data[:,0]
	y=data[:,1]

	# fitfunc = lambda p, x: 0*x+p[0]
	# errfunc = lambda p, x, y: fitfunc(p, x) - y
	# p0 = [0]
	# pbest, success = optimize.leastsq(errfunc, p0, args=(x, y))
	# print "pbest :", pbest
	# Signal[n] = abs(pbest[0])

	# total=0
	# for k in data[:,1]:
		# total += k
	# mittel = total/len(data)
	# print "mittel:", mittel
	
	# abweichung=0
	# for k in data[:,1]:
		# abweichung += (mittel-k)**2
	# print "abweichung:", abweichung
	# Fehler[n] = sqrt(abweichung)/sqrt(len(data))
	
	plt.figure(n)
	plt.plot(x,y,"b")
	#plt.plot(x,mittel,"g")
	# plt.plot(x,fitfunc(pbest,x),"r")
	# plt.plot(x,fitfunc(pbest,x)-Fehler[n],"r--")
	# plt.plot(x,fitfunc(pbest,x)+Fehler[n],"r--")
	show()




# print "Signal: ", Signal
# # print "Fehler: ", Fehler
# I_pol = array([1.3,1.5,1.7,1.9,2.1,2.3,2.5])
# # Abweichung = array(Fehler)


# fitfunc = lambda p, I_pol: p[0]*I_pol+p[1]
# errfunc = lambda p, I_pol, Signal: fitfunc(p, I_pol) - Signal
# p0 = [0, 0]
# pbest, success = optimize.leastsq(errfunc, p0, args=(I_pol, Signal))


# # print "Steigung :", pbest[0], "+-",pbest[0]*0.02

# ax = fig.add_subplot(111)
# #subplots_adjust(top=0.90, right=0.96)

# B_pol = I_pol*5.65/(8.6*2.5)

# #####Abhängigkeit Magnetfeld#####
# plt.errorbar(B_pol, Signal, xerr=B_pol*0.0288, yerr=Signal*0.045, label=u"Messdaten mit Fehler", fmt="r.") #aus Schwankung yerr=Abweichung,
# ax.plot(B_pol, fitfunc(pbest, I_pol), "b", label="ausgleichene Gerade")

# ax.plot([B_pol[0],B_pol[-1]], [Signal[0]-Signal[0]*0.045,Signal[-1]+Signal[-1]*0.045], "b--", label="Fehlergeraden")
# ax.plot([B_pol[0],B_pol[-1]], [Signal[0]+Signal[0]*0.045,Signal[-1]-Signal[-1]*0.045], "b--")

# ax.set_xlabel(u"Magnetfeld im Polarisator $B[\mathrm{T}]$")
# ax.set_ylabel(u"Signalst\xe4rke $U_\mathrm{SH}[\mathrm{mV}]$")

#####Abhängigkeit Polarisationsstromstärke####
# plt.errorbar(I_pol, Signal, xerr=I_pol*0.02, yerr=Signal*0.045, label=u"Messdaten mit Fehler", fmt="r.") #aus Schwankung yerr=Abweichung,
# ax.plot(I_pol, fitfunc(pbest, I_pol), "b", label="ausgleichene Gerade")

# ax.plot([I_pol[0],I_pol[-1]], [Signal[0]-Signal[0]*0.045,Signal[-1]+Signal[-1]*0.045], "b--", label="Fehlergeraden")
# ax.plot([I_pol[0],I_pol[-1]], [Signal[0]+Signal[0]*0.045,Signal[-1]-Signal[-1]*0.045], "b--")
# ax.set_xlabel(u"Polarisationsstrom $I_\mathrm{pol}[\mathrm{A}]$")



ax.legend(loc=0)

fig.savefig("04-signal-polarisationsstrom.pdf")

show()

