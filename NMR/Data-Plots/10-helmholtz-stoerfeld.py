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
I_HH=array([45,65,80])
nu_posres=array([6826.3, 9480.2, 11473.2])
nu_negres=array([5562.2, 8207.7, 10195.6])



#======================Summe der Frequenzquadrate===============================
nu_sum=nu_posres**2+nu_negres**2
I_sum=I_HH**2

fitfunc_sum = lambda p, I_sum: p[0]*I_sum+p[1]
errfunc_sum = lambda p, I_sum, nu_sum: fitfunc_sum(p, I_sum) - nu_sum
p0_sum = [0, 0]
pbest_sum, success = optimize.leastsq(errfunc_sum, p0_sum, args=(I_sum, nu_sum))


fehlerI_HH=0.02
fehlernu=2

xfehler = 2*I_HH*fehlerI_HH
yfehler = sqrt((2*nu_posres*fehlernu)**2 + (2*nu_negres*fehlernu)**2)

figure(num=None, figsize=(7, 5), dpi=150, facecolor='w', edgecolor='k')
title(u"Bestimmung Betrags des St\xf6rfeldes und Kernmagnetons", fontweight='bold')
errorbar(I_sum, nu_sum, xerr=xfehler, yerr=yfehler, label=u"Messwerte f\xfcr $+I_\mathrm{HH}$", fmt="r.")
plot(I_sum, fitfunc_sum(pbest_sum, I_sum), "b", label="ausgleichene Gerade")
plot([I_sum[0], I_sum[-1]], [nu_sum[0]-yfehler[0], nu_sum[-1]+yfehler[-1]], "b--", label="Fehlergeraden")
plot([I_sum[0], I_sum[-1]], [nu_sum[0]+yfehler[0], nu_sum[-1]-yfehler[-1]], "b--")

m_max=((nu_sum[-1]+yfehler[-1])-(nu_sum[0]-yfehler[0]))/(I_sum[-1]-I_sum[0])
m_min=((nu_sum[-1]-yfehler[-1])-(nu_sum[0]+yfehler[0]))/((I_sum[-1]-I_sum[0]))
y_min=(nu_sum[0]-yfehler[0])-m_max*I_sum[0]
y_max=(nu_sum[0]+yfehler[0])-m_min*I_sum[0]

print "================Differenz der Frequenzquadrate==========="
print "Steigung: ", pbest_sum[0]
print "minimale Steigung: ", m_min
print "maximale Steigung: ", m_max
print "y-Abschnitt: ", pbest_sum[1]
print "y-Abschnitt min: ", y_min
print "y-Abschnitt max: ", y_max
print "--------------------------------"
print "Steigung: ", pbest_sum[0], "+-", (m_max-m_min)/2 
print "y-Abschnitt: ", pbest_sum[1], "+-", (y_max-y_min)/2
print "--------------------------------"

plt.xlabel(u"Spulenstromquadrat $I_\mathrm{HH}^2[\mathrm{mA}^2]$")
plt.ylabel(r"Summe der Frequenzquadrate $(\nu(I_\mathrm{HH})^2+\nu(-I_\mathrm{HH})^2)[\mathrm{Hz}^2]$")

legend(loc=0)

plt.savefig("10-helmholtz-summe.pdf")

show()

#======================Differenz der Frequenzquadrate===========================
nu_diff=nu_posres**2-nu_negres**2
I_diff=I_HH

fitfunc_diff = lambda p, I_diff: p[0]*I_diff+p[1]
errfunc_diff = lambda p, I_diff, nu_diff: fitfunc_diff(p, I_diff) - nu_diff
p0_diff = [0, 0]
pbest_diff, success = optimize.leastsq(errfunc_diff, p0_diff, args=(I_diff, nu_diff))

xfehler = fehlerI_HH
yfehler = sqrt((2*nu_posres*fehlernu)**2 + (2*nu_negres*fehlernu)**2)

figure(num=None, figsize=(7, 5), dpi=150, facecolor='w', edgecolor='k')
title(u"Bestimmung Winkels des St\xf6rfeldes", fontweight='bold')
errorbar(I_diff, nu_diff, xerr=xfehler, yerr=yfehler, label=u"Messwerte f\xfcr $+I_\mathrm{HH}$", fmt="r.")
plot(I_diff, fitfunc_diff(pbest_diff, I_diff), "b", label="ausgleichene Gerade")
plot([I_diff[0], I_diff[-1]], [nu_diff[0]-yfehler[0], nu_diff[-1]+yfehler[-1]], "b--",  label="Fehlergeraden")
plot([I_diff[0], I_diff[-1]], [nu_diff[0]+yfehler[0], nu_diff[-1]-yfehler[-1]], "b--")

m_max=((nu_diff[-1]+yfehler[-1])-(nu_diff[0]-yfehler[0]))/(I_diff[-1]-I_diff[0])
m_min=((nu_diff[-1]-yfehler[-1])-(nu_diff[0]+yfehler[0]))/((I_diff[-1]-I_diff[0]))

print "================Differenz der Frequenzquadrate==========="
print "Steigung: ", pbest_sum[0]
print "minimale Steigung: ", m_min
print "maximale Steigung: ", m_max
print "--------------------------------"
print "Steigung: ", pbest_diff[0], "+-", (m_max-m_min)/2 
print "--------------------------------"

plt.xlabel(u"Spulenstromquadrat $I_\mathrm{HH}[\mathrm{mA}]$")
plt.ylabel(r"Differenz der Frequenzquadrate $(\nu(I_\mathrm{HH})^2+\nu(-I_\mathrm{HH})^2)[\mathrm{Hz}^2]$")


legend(loc=0)

plt.savefig("10-helmholtz-diff.pdf")

show()
