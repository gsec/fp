# -*- coding: utf-8 -*-


from scipy import *
from scipy import optimize
from matplotlib import rc
from numpy import *
import matplotlib.pyplot as plt

# from fitting import *
from pylab import *

rc('font', family = 'serif', serif = 'STIXGeneral')
#fig = plt.figure(num=None, figsize=(7, 5), dpi=150, facecolor='w', edgecolor='k')

#fig.suptitle(u"Untersuchung der Linearit\xe4t von Messsignal zu Polarisationsstrom", fontsize=14, fontweight='bold')
print "Lese Daten ein"
txt_filename_to_open_10C=["07-relaxation-10C-6V.dat", "07-relaxation-10C-7,5V.dat", "07-relaxation-10C-9V.dat", "07-relaxation-10C-10,5V.dat", "07-relaxation-10C-12V-2.dat"]
txt_filename_to_open_20C=["07-relaxation-20C-3V.dat", "07-relaxation-20C-5V.dat", "07-relaxation-20C-5,5V.dat", "07-relaxation-20C-6V.dat", "07-relaxation-20C-7,5V.dat", "07-relaxation-20C-9V.dat", "07-relaxation-20C-10,5V.dat", "07-relaxation-20C-12V.dat"]
txt_filename_to_open_40C=["07-relaxation-40C-6V.dat", "07-relaxation-40C-7,5V.dat", "07-relaxation-40C-9V.dat", "07-relaxation-40C-10,5V.dat", "07-relaxation-40C-12V.dat"]
txt_filename_to_open_60C=["07-relaxation-60C-6V.dat", "07-relaxation-60C-7,5V-2.dat", "07-relaxation-60C-9V.dat", "07-relaxation-60C-10,5V.dat", "07-relaxation-60C-12V.dat", ]
print "Daten eingelesen"


plotdata = genfromtxt(txt_filename_to_open_20C[-1])
t=plotdata[:,0]
S=plotdata[:,1]
plt.figure(num=None, figsize=(7, 5), dpi=150, facecolor='w', edgecolor='k')
title(u"Signalh\xf6he zur Bestimmung der Wassergeschwindigkeit")
plt.plot(t,S,"b",label=u"Messwerte")
plt.plot([2.31045,2.31045],[0.09,-0.063632], ":", color="black") #t0
plt.plot([2.36518,2.36518],[-0.7,-0.256112], ":", color="black") #t1 y-0.271857
plt.plot([2.56015,2.56015],[-0.7,-0.0878945], ":" , color="black") #t2 y-0.106817
plt.plot([2.62773,2.62773],[0.09,-0.0402104], ":", color="black") #t3 y-0.0402104
plt.plot([4.98992,4.98992],[0.09,-0.312263], ":", color="black") #t4/5 y-0.0402104
plt.plot([4.82387,4.82387],[0.09,-0.0645425], ":", color="black") #t4 y-0.0645425
plt.plot([5.22997,5.22997],[-0.7,-0.608184], ":", color="black") #t5 y-0.582223
plt.plot([13.7493,13.7493],[-0.7,-0.481135], ":" , color="black") #t6 y-0.481135
text(1.77129,0.0268, u"$t_0$", va="center", ha="right")
text(1.96474,-0.493808, u"$t_1$", va="center", ha="right")
text(2.78691,-0.493808, u"$t_2$", va="center", ha="left")
text(2.78691,0.0268, u"$t_3$", va="center", ha="left")
text(4.14,0.0268, u"$t_4$", va="center", ha="right")
text(5.495,-0.3, u"$t_{4/5}$", va="center", ha="left")
text(5.301,-0.654, u"$t_5$", va="center", ha="left")
text(14,-0.645, u"$t_6$", va="center", ha="left")

plt.xlabel(u"Zeit $t[\mathrm{s}]$")
plt.ylabel(u"Signalh\xf6he $S2[\mathrm{V}]$")

plt.savefig("06-wassergeschwindigkeit.pdf")
show()

#############Plotausgabe einzelne Datensätze################
# for n in range(len(txt_filename_to_open_10C)):
	# data = genfromtxt(txt_filename_to_open_10C[n])
	# print "n: ", n
	# x=data[:,0]
	# y=data[:,1]

	# # fitfunc = lambda p, x: 0*x+p[0]
	# # errfunc = lambda p, x, y: fitfunc(p, x) - y
	# # p0 = [0]
	# # pbest, success = optimize.leastsq(errfunc, p0, args=(x, y))
	# # print "pbest :", pbest
	# # Signal[n] = abs(pbest[0])

	# # total=0
	# # for k in data[:,1]:
		# # total += k
	# # mittel = total/len(data)
	# # print "mittel:", mittel
	
	# # abweichung=0
	# # for k in data[:,1]:
		# # abweichung += (mittel-k)**2
	# # print "abweichung:", abweichung
	# # Fehler[n] = sqrt(abweichung)/sqrt(len(data))
	
	# plt.figure(n)
	# plt.plot(x,y,"b")
	# #plt.plot(x,mittel,"g")
	# # plt.plot(x,fitfunc(pbest,x),"r")
	# # plt.plot(x,fitfunc(pbest,x)-Fehler[n],"r--")
	# # plt.plot(x,fitfunc(pbest,x)+Fehler[n],"r--")
	# show()

#Ausgelesenen Daten t_0, t_4/5 und S2(t_5) für versch. Temp
U_10C=[6, 7.5, 9, 10.5, 12]
t0_10C=[2.16793, 1.9889, 2.57485, 2.58797, 2.25455]
t45_10C=[8.11812, 6.52864, 6.2954, 5.71866, 5.04327] #+-0.1 oder weniger
S2_10C=array([-0.158296, -0.237996, -0.304631, -0.367881, -0.376368]) #+-0.5
t_10C=zeros(len(t0_10C))
for n in range(len(t0_10C)):
	t_10C[n] = t45_10C[n] - t0_10C[n]

x_10C=t_10C[1:]
y_10C=log(-S2_10C[1:])
fitfunc_10C = lambda p, x_10C: p[0]*x_10C+p[1]
errfunc_10C = lambda p, x_10C, y_10C: fitfunc_10C(p, x_10C) - y_10C
p0_10C = [0, 0]
pbest_10C, success = optimize.leastsq(errfunc_10C, p0_10C, args=(x_10C, y_10C))

	
U_20C=[3, 5, 5.5, 6, 7.5, 9, 10.5, 12]
t0_20C=[2.61265, 2.98289, 3.10219, 2.88426, 3.11598, 3.58009, 2.79085, 2.31167]
t45_20C=[17.2228, 9.87958, 9.15325, 8.33759, 7.37425, 7.1318, 5.82228, 4.97296]
S2_20C=array([-0.0816444, -0.234033, -0.275615, -0.3048, -0.397649, -0.467761, -0.504209, -0.566957])
t_20C=zeros(len(t0_20C))
for n in range(len(t0_20C)):
	t_20C[n] = t45_20C[n] - t0_20C[n]

x_20C=t_20C[3:]
y_20C=log(-S2_20C[3:])
fitfunc_20C = lambda p, x_20C: p[0]*x_20C+p[1]
errfunc_20C = lambda p, x_20C, y_20C: fitfunc_20C(p, x_20C) - y_20C
p0_20C = [0, 0]
pbest_20C, success = optimize.leastsq(errfunc_20C, p0_20C, args=(x_20C, y_20C))

	
U_40C=[6, 7.5, 9, 10.5, 12]
t0_40C=[2.16341, 2.1447, 2.3484, 2.43944, 1.99155]
t45_40C=[7.59739, 6.38701, 5.90827, 5.48485, 4.67129]
S2_40C=array([-0.375838, -0.451071, -0.50015, -0.577783, -0.621533])
t_40C=zeros(len(t0_40C))
for n in range(len(t0_40C)):
	t_40C[n] = t45_40C[n] - t0_40C[n]

y_40C=log(-S2_40C)
fitfunc_40C = lambda p, t_40C: p[0]*t_40C+p[1]
errfunc_40C = lambda p, t_40C, y_40C: fitfunc_40C(p, t_40C) - y_40C
p0_40C = [0, 0]
pbest_40C, success = optimize.leastsq(errfunc_40C, p0_40C, args=(t_40C, y_40C))


	
U_60C=[6, 7.5, 9, 10.5, 12]
t0_60C=[2.07094, 2.35512, 2.75853, 2.00029, 2.37761]
t45_60C=[7.34816, 6.60237, 6.256, 5.04066, 5.03794]
S2_60C=array([-0.477061, -0.526905, -0.595208, -0.588385, -0.622906])
t_60C=zeros(len(t0_60C))
for n in range(len(t0_60C)):
	t_60C[n] = t45_60C[n] - t0_60C[n]

y_60C=log(-S2_60C)
fitfunc_60C = lambda p, t_60C: p[0]*t_60C+p[1]
errfunc_60C = lambda p, t_60C, y_60C: fitfunc_60C(p, t_60C) - y_60C
p0_60C = [0, 0]
pbest_60C, success = optimize.leastsq(errfunc_60C, p0_60C, args=(t_60C, y_60C))


fehlerx = 0.05
fehlery = (0.02*2)/sqrt(2)


plt.figure(num=None, figsize=(7, 5), dpi=150, facecolor='w', edgecolor='k')
title(u"Bestimmung der Relaxationszeit in Abh\xe4nigigkeit der Temperatur")

xlim(2, 6.5)
#ylim(-0.7, 0)

errorbar(t_10C, log(-S2_10C), xerr= fehlerx, yerr=log(fehlery/abs(S2_10C)+1.05), color="black", label=u"Messdaten f\xfcr $13.86\pm 0.94$\u00b0C mit ausgleichender Kurve und Fehlerkurven", fmt=".")
plot(t_10C, fitfunc_10C(pbest_10C, t_10C), "k")#, label=u"ausgleichene Gerade f\xfcr $10\mathrm{C}$")
plot([t_10C[1],t_10C[-1]],[log(-S2_10C[1])-log(fehlery/abs(S2_10C[1])+1.05), log(-S2_10C[-1])+log(fehlery/abs(S2_10C[-1])+1.05)], "k:")#, label=u"Fehlergeraden $10\mathrm{C}$")
plot([t_10C[1],t_10C[-1]],[log(-S2_10C[1])+log(fehlery/abs(S2_10C[1])+1.05), log(-S2_10C[-1])-log(fehlery/abs(S2_10C[-1])+1.05)], "k:")
print "Steigung 10C :", pbest_10C[0]
print "Fehler max Gerade 10C :", ((log(-S2_10C[-1])+log(fehlery/abs(S2_10C[-1])+1.05))-(log(-S2_10C[1])-log(fehlery/abs(S2_10C[1])+1.05)))/(t_10C[-1]-t_10C[1])
print "Fehler min Gerade 10C :", ((log(-S2_10C[-1])-log(fehlery/abs(S2_10C[-1])+1.05))-(log(-S2_10C[1])+log(fehlery/abs(S2_10C[1])+1.05)))/(t_10C[-1]-t_10C[1])

errorbar(t_20C, log(-S2_20C), xerr=fehlerx, yerr=log(fehlery/abs(S2_20C)+1.05), color="blue", label=u"Messdaten f\xfcr $34.00\pm 0.10$\u00b0C mit ausgleichender Kurve und Fehlerkurven", fmt=".")
plot(t_20C, fitfunc_20C(pbest_20C, t_20C), "b")#, label=u"ausgleichene Gerade f\xfcr $10\mathrm{C}$")
plot([t_20C[3],t_20C[-1]],[log(-S2_20C[3])-log(fehlery/abs(S2_20C[3])+1.05), log(-S2_20C[-1])+log(fehlery/abs(S2_20C[-1])+1.05)], "b:")#, label=u"Fehlergeraden $20\mathrm{C}$")
plot([t_20C[3],t_20C[-1]],[log(-S2_20C[3])+log(fehlery/abs(S2_20C[3])+1.05), log(-S2_20C[-1])-log(fehlery/abs(S2_20C[-1])+1.05)], "b:")
print "Steigung 20C :", pbest_20C[0]
print "Fehler max Gerade 20C :", ((log(-S2_20C[-1])+log(fehlery/abs(S2_20C[-1])+1.05))-(log(-S2_20C[3])-log(fehlery/abs(S2_20C[3])+1.05)))/(t_20C[-1]-t_20C[3])
print "Fehler min Gerade 20C :", ((log(-S2_20C[-1])-log(fehlery/abs(S2_10C[-1])+1.05))-(log(-S2_20C[3])+log(fehlery/abs(S2_20C[3])+1.05)))/(t_20C[-1]-t_20C[3])

errorbar(t_40C, log(-S2_40C), xerr=fehlerx, yerr=log(fehlery/abs(S2_40C)+1.05), color="green", label=u"Messdaten f\xfcr $42.52\pm 0.69$\u00b0C mit ausgleichender Kurve und Fehlerkurven", fmt=".")
plot(t_40C, fitfunc_40C(pbest_40C, t_40C), "g")#, label=u"ausgleichene Gerade f\xfcr $10\mathrm{C}$")
plot([t_40C[0],t_40C[-1]],[log(-S2_40C[0])-log(fehlery/abs(S2_40C[0])+1.05), log(-S2_40C[-1])+log(fehlery/abs(S2_40C[-1])+1.05)], "g:")#, label=u"Fehlergeraden $40\mathrm{C}$")
plot([t_40C[0],t_40C[-1]],[log(-S2_40C[0])+log(fehlery/abs(S2_40C[0])+1.05), log(-S2_40C[-1])-log(fehlery/abs(S2_40C[-1])+1.05)], "g:")
print "Steigung 40C :", pbest_40C[0]
print "Fehler max Gerade 40C :", ((log(-S2_40C[-1])+log(fehlery/abs(S2_40C[-1])+1.05))-(log(-S2_40C[0])-log(fehlery/abs(S2_40C[0])+1.05)))/(t_40C[-1]-t_40C[0])
print "Fehler min Gerade 40C :", ((log(-S2_40C[-1])-log(fehlery/abs(S2_40C[-1])+1.05))-(log(-S2_40C[0])+log(fehlery/abs(S2_40C[0])+1.05)))/(t_40C[-1]-t_40C[0])

errorbar(t_60C, log(-S2_60C), xerr=fehlerx, yerr=log(fehlery/abs(S2_60C)+1.05), color="red", label=u"Messdaten f\xfcr $63.0\pm 2.2$\u00b0C mit ausgleichender Kurve und Fehlerkurven", fmt=".")
plot(t_60C, fitfunc_60C(pbest_60C, t_60C), "r")#, label=u"ausgleichene Gerade f\xfcr $10\mathrm{C}$")
plot([t_60C[0],t_60C[-1]],[log(-S2_60C[0])-log(fehlery/abs(S2_60C[0])+1.05), log(-S2_60C[-1])+log(fehlery/abs(S2_60C[-1])+1.05)], "r:")#, label=u"Fehlergeraden $60\mathrm{C}$")
plot([t_60C[0],t_60C[-1]],[log(-S2_60C[0])+log(fehlery/abs(S2_60C[0])+1.05), log(-S2_60C[-1])-log(fehlery/abs(S2_60C[-1])+1.05) ], "r:")
print "Steigung 50C :", pbest_60C[0]
print "Fehler max Gerade 60C :", ((log(-S2_60C[-1])+log(fehlery/abs(S2_60C[-1])+1.05))-(log(-S2_60C[0])-log(fehlery/abs(S2_60C[0])+1.05)))/(t_60C[-1]-t_60C[0])
print "Fehler min Gerade 60C :", ((log(-S2_60C[-1])-log(fehlery/abs(S2_60C[-1])+1.05))-(log(-S2_60C[0])+log(fehlery/abs(S2_60C[0])+1.05)))/(t_60C[-1]-t_60C[0])

plot([5.55,5.55],[0,-3], ":", color="black")
text(5.57,-0.402, u"$t_\mathrm{max}$", va="center", ha="left")
plt.xlabel(u"Zeitdifferenz $t_v[\mathrm{s}]$")
plt.ylabel(u"logarithmische Signalh\xf6he $S2(t_5)$")

# print "Signal: ", Signal
# # print "Fehler: ", Fehler
# I_pol = array([1.3,1.5,1.7,1.9,2.1,2.3,2.5])
# # Abweichung = array(Fehler)

legend(loc=0, prop={'size':10})
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



#ax.legend(loc=0)

#fig.savefig("04-signal-polarisationsstrom.pdf")
plt.savefig("06-relaxation.pdf")
show()

