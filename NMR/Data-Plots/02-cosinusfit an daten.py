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

#def f(U):
#   return 297.0 -25.87*U + 1.908*U**2 - 0.4020*U**3;

data1 = genfromtxt("01-Funktionsgenerator-50mV-1,3kHz.dat")
data2 = genfromtxt("01-Funktionsgenerator-50mV-2,6kHz.dat")
data3 = genfromtxt("01-Funktionsgenerator-100mV-1,3kHz.dat")
data4 = genfromtxt("01-Funktionsgenerator-100mV-2,6kHz.dat")

data = data4

t = data[:,0]
U_A = data[:,1]
x = data[:100,0]
y = data[:100,1]
print type(x)



fitfunc = lambda p, x: p[0] * cos(2*pi*p[1]*x+p[2])+p[3]
errfunc = lambda p, x, y: fitfunc(p, x) - y
p0 = [5.0e-02, 2.6e3, -1.9, 1.8e-4]
pbest, success = optimize.leastsq(errfunc, p0, args=(x, y))
#print x 
#print y
print pbest
#print cos(1*x+pbest[2])	
def residual_var(pbest,xdata,ydata):
	sum=0.0
	for i in range(len(xdata)):
		sum+=(errfunc(pbest, xdata[i], ydata[i]))**2
	return sum

print "pbest: ",pbest
# zweiter outout ist die Kovarianzmatrix
out= optimize.leastsq(errfunc, p0, args=(x, y), full_output=1)
cov_x=out[1]
print "cov_x: ",cov_x
# das Residuum des Fits
print "residual_var(pbest,xdata,ydata): ",residual_var(pbest,x,y)
# und das reduzierte chi quadrat berechnen
reduced_chi_square=residual_var(pbest,x,y)/(len(x)-len(pbest))
print "reduced_chi_square: ",reduced_chi_square
# Kovarianzmatrix wird reduziert durch chi quadrat
red_cov_x=cov_x*reduced_chi_square
# in den diagonaleintraegen stehen die Varianzen der Parameter
# sqrt liefert die Standardabweichungen
std_error = np.array([sqrt(red_cov_x[i, i]) for i in range(len(pbest))])
print "std_error: ",std_error




ax = fig.add_subplot(111)
ax.plot(t, U_A, "b", label=u"Messwerte")
x = linspace(0,t[-1],100000)
ax.plot(x, fitfunc(pbest, x), "r")

text(0, -0.052, u'Amplitude', va='center', ha='left')
text(0.025, -0.052, pbest[0], va='center', ha='left')
text(0, -0.058, u'Frequenz', va='center', ha='left')
text(0.025, -0.057, pbest[1], va='center', ha='left')

text(0.09, -0.052, u'Phase', va='center', ha='left')
text(0.115, -0.052, pbest[2], va='center', ha='left')
text(0.09, -0.058, u'Shift', va='center', ha='left')
text(0.115, -0.057, pbest[3], va='center', ha='left')


#ax.set_xlabel(u"Magnetfeld $B$")
#ax.set_ylabel(u"Hallwiderstand $R_{\mathrm{Hall}}$")

#ax.legend(loc=0)

#fig.savefig("03-3,0-Hallplateaus.pdf")
show()


# #################################################################################
# delta = 50
# step = 100

# Mittelwertkandidaten=range(0,16000,step)
# counts = zeros(len(Mittelwertkandidaten))

# print "Laenge Mittelwertkandidaten:", len(Mittelwertkandidaten)

# for i in range(len(Mittelwertkandidaten)):
	# print i
	# for j in R_H:
		# if abs(Mittelwertkandidaten[i]-j) < delta:
			# counts[i]+=1


# maximum1=max(counts[11000/step:16000/step])
# maximum2=max(counts[5000/step:8000/step])
# maximum3=max(counts[3800/step:4200/step])
# maximum4=max(counts[2900/step:3300/step])
# maximum5=max(counts[2300/step:2600/step])
# maximum6=max(counts[1900/step:2200/step])
# maximum7=max(counts[1600/step:1900/step])

# wertmaximum1=argmax(counts[11000/step:16000/step])+11000/step
# wertmaximum2=argmax(counts[5000/step:8000/step])+5000/step
# wertmaximum3=argmax(counts[3800/step:4200/step])+3800/step
# wertmaximum4=argmax(counts[2900/step:3300/step])+2900/step
# wertmaximum5=argmax(counts[2300/step:2600/step])+2300/step
# wertmaximum6=argmax(counts[1900/step:2200/step])+1900/step
# wertmaximum7=argmax(counts[1600/step:1900/step])+1600/step

# print "Laenge Mittelwertkandidaten:", len(Mittelwertkandidaten)
# print "Maxima:", maximum1, maximum2, maximum3, maximum4, maximum5, maximum6, maximum7
# print "argmax:", wertmaximum1, wertmaximum2, wertmaximum3, wertmaximum4, wertmaximum5, wertmaximum6, wertmaximum7
# print "Mittelwertkandidaten der Maxima:", Mittelwertkandidaten[wertmaximum1], Mittelwertkandidaten[wertmaximum2], Mittelwertkandidaten[wertmaximum3], Mittelwertkandidaten[wertmaximum4], Mittelwertkandidaten[wertmaximum5], Mittelwertkandidaten[wertmaximum6], Mittelwertkandidaten[wertmaximum7]

# #lines = plt.plot(0,12500,2000,12500, "g--")
# #plt.setp(lines, color="g", linewidth=2.0)

# ax = fig.add_subplot(111)
# ax.plot(B*100, R_H, "b", label=u"Messwerte")

# ax.set_xlabel(u"Magnetfeld $B$")
# ax.set_ylabel(u"Hallwiderstand $R_{\mathrm{Hall}}$")

# ax2 = ax.twiny()
# ax2.plot(counts,Mittelwertkandidaten, "r", label=u"liste")

# ax2.set_xlabel(r"Anzahl $N$")

# ax.legend(loc=3)
# ax2.legend(loc=4)

# ax2.plot([0,760],[Mittelwertkandidaten[wertmaximum1],Mittelwertkandidaten[wertmaximum1]], "g--")
# ax2.plot([0,410],[Mittelwertkandidaten[wertmaximum2],Mittelwertkandidaten[wertmaximum2]], "g--")
# ax2.plot([0,300],[Mittelwertkandidaten[wertmaximum3],Mittelwertkandidaten[wertmaximum3]], "g--")
# ax2.plot([0,250],[Mittelwertkandidaten[wertmaximum4],Mittelwertkandidaten[wertmaximum4]], "g--")
# ax2.plot([0,220],[Mittelwertkandidaten[wertmaximum5],Mittelwertkandidaten[wertmaximum5]], "g--")
# ax2.plot([0,195],[Mittelwertkandidaten[wertmaximum6],Mittelwertkandidaten[wertmaximum6]], "g--")
# ax2.plot([0,180],[Mittelwertkandidaten[wertmaximum7],Mittelwertkandidaten[wertmaximum7]], "g--")


# text(750, Mittelwertkandidaten[wertmaximum1]+500, r"$\nu = 2$", va='center', ha='center')
# text(300, Mittelwertkandidaten[wertmaximum2]+500, r"$\nu = 3$", va='center', ha='center')
# text(210, Mittelwertkandidaten[wertmaximum3]+500, r"$\nu = 4$", va='center', ha='center')
# text(200, Mittelwertkandidaten[wertmaximum4]+500, r"$\nu = 5$", va='center', ha='center')
# text(190, Mittelwertkandidaten[wertmaximum5]+500, r"$\nu = 6$", va='center', ha='center')
# text(180, Mittelwertkandidaten[wertmaximum6]+500, r"$\nu = 7$", va='center', ha='center')

# # y = log(data[:,1]/(8e-3*1.63e-3*2.74e-3))
# # y = log(data[:,1]*(1.63e-3*2.74e-3)/(8e-3*4.2e-3))

# #X = x[0:14]
# #Y = y[0:14]

# #fitfunc = lambda p, x: p[0]*x + p[1]
# #errfunc = lambda p, x, y: fitfunc(p, x) - y
# #P, success = leastsq(errfunc, [1, 1], args=(X, Y))




# #plot(x, fitfunc(P, x), "r", label="Ausgleichsgerade")
# #plot(x, -0.0105*x + 0.9, "r--", label="Fehlergerade")
# #plot(x, -0.0077*x + 0.65, "r--")

# #plot([207, 207], [0.0, -4.5], "k", label="Inversionstemperatur")

# #fitfunc = lambda p, x: p[0] + p[1]*x + p[2]*x**2+ p[3]*x**3 + p[4]*x**4 + p[5]*x**5
# #errfunc = lambda p, x, y: fitfunc(p, x) - y
# #p, success = leastsq(errfunc, [1, 1, 1, 0, 1, 1, 1, 1, 1], args=(x, y))
# #R = linspace(min(x), max(x), 1000)
# #plot(R, fitfunc(p, R), label="Ausgleichende Kurve")

# #errorbar(x, y, yerr=len(x)*[0.04], xerr=len(x)*[1], fmt="g.", label="Messpunkte mit Fehlerbalken")



# show()
