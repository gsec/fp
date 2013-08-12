# Using the magic encoding
# -*- coding: utf-8 -*-

from numpy import *
from pylab import *
from scipy import optimize  
from scipy import stats
import numpy as np
import inspect  
import matplotlib.pyplot as plt
import scipy.odr, scipy.special, scipy.stats
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes
from mpl_toolkits.axes_grid.inset_locator import mark_inset
from matplotlib.ticker import AutoMinorLocator, AutoLocator
from scipy.odr.odrpack import Model
pi=3.1415926

# --- data import ---
number_of_files=19
filenames=[]
for i in range(number_of_files):
	name=str(i*20)+".dat"
	name="A2623_LT_"+name
	filenames.append(name)
print filenames

data=[]
for i in range(number_of_files):
	data.append(loadtxt(filenames[i]))
	
xdata=array([0.0]*number_of_files)
ydata=array([0.0]*number_of_files)
for i in range(number_of_files):
	xdata[i]=(i*20)
	ydata[i]=(data[i][1])  
print data[1]
print xdata
print ydata



# colors = [(0.0, 0.75, 0.75),(0.0, 0.5, 0.0),(0.75, 0.75, 0),(1.0, 0.0, 0.0), (0.75, 0, 0.75)]
#raw_input("Press Enter to continue...")




p1_0 = [0,0,0,0,0,0]
fit1 = lambda p, x: (p[1]*cos(2*(x*pi/180+p[0]))+p[3])*(1+x*p[5])#-x**2*p[6])
def residuals1(p, x, y):
	err = y-fit1(p,x)
	return err
def residual_var1(pbest,xdata,ydata):
	sum=0.0
	for i in range(len(xdata)):
		sum+=(residuals1(pbest, xdata[i], ydata[i]))**2
	return sum
out = optimize.leastsq(residuals1, p1_0, args=(xdata, ydata), full_output=1)
p1=out[0]	
print "p1: ", p1
print "residual_var1(p1,xdata,ydata): ", residual_var1(p1,xdata,ydata)/(len(xdata)-len(p1))
dy=sqrt(residual_var1(p1,xdata,ydata)/(len(xdata)-len(p1)))
dx=1
print "Standardabweichung der Punkte: ", sqrt(residual_var1(p1,xdata,ydata)/(len(xdata)-len(p1)))
print dy

# +++++++++++++++++++++++++++++++
x=xdata[8:12]
y=ydata[8:12]

p2_0 = [0,0,0]	
fit2 = lambda p, x: p[0]+p[1]*x+p[2]*(x)**2


def polynom(p,x) :
	# A gaussian peak with:
	#   Constant Background          : p[0]
	#   Peak height above background : p[1]
	#   Central value                : p[2]
	#   Standard deviation width     : p[3]
	return p[0]+p[1]*x+p[2]*(x)**2
func=polynom
p_guess = (0,0,0)

# Load data for ODR fit
data = scipy.odr.RealData(x=x, y=y, sx=dx, sy=dy)
# Load model for ODR fit
model = scipy.odr.Model(func)

## Now fit model to data
#	job=10 selects central finite differences instead of forward differences
#		when doing numerical differentiation fo function
#	maxit is maximum number of iterations
fit = scipy.odr.ODR(data, model, p_guess, maxit=5000,job=10)      
output = fit.run()
p = output.beta 	# 'beta' is an array of the parameter estimates
p4=p
cov = output.cov_beta   # parameter covariance matrix
uncertainty = output.sd_beta # parameter standard uncertainties
print "***"
print "p(180)_best: ",p
print "p4_best: ",p4
print "uncertainty: ", uncertainty
print len(x), len(y)
print "***"

# +++++++++++++++++++++++++++++++
x=xdata[3:7]
y=ydata[3:7]

p2_0 = [0,0,0]	
fit2 = lambda p, x: p[0]+(p[1]*x)+(p[2]*(x**2))
	
p_guess = (1,1,1)

# Load data for ODR fit
data = scipy.odr.RealData(x=x, y=y, sx=dx, sy=dy)
# Load model for ODR fit
model = scipy.odr.Model(func)

## Now fit model to data
#	job=10 selects central finite differences instead of forward differences
#		when doing numerical differentiation fo function
#	maxit is maximum number of iterations
fit = scipy.odr.ODR(data, model, p_guess, maxit=5000,job=10)      
output = fit.run()
p = output.beta 	# 'beta' is an array of the parameter estimates
p5=p
cov = output.cov_beta   # parameter covariance matrix
uncertainty = output.sd_beta # parameter standard uncertainties
print "***"
print "p(90)_best: ",p

print "uncertainty: ", uncertainty
print "***"

# ++++++++++++++++++++++++
def residuals2(p, x, y):
	err = y-fit2(p,x)
	return err
	
def residual_var2(pbest,xdata,ydata):
	sum=0.0
	for i in range(len(xdata)):
		sum+=(residuals2(pbest, xdata[i], ydata[i]))**2
	return sum	
	
out = optimize.leastsq(residuals2, p2_0, args=(xdata[7:12], ydata[7:12]), full_output=1)
p2=out[0]
out = optimize.leastsq(residuals2, p2_0, args=(xdata[3:7], ydata[3:7]), full_output=1)
p3=out[0]

# h1=fit2(p2,180)
# h3=fit2(p3,90)
# h5=p2[2]+2*p2[3]*(180*pi/180+p2[0])	
# h7=p3[2]+2*p3[3]*(90*pi/180+p3[0])
# print "********"
# print 
# print n
# print "h1: ",h1
# print "h3: ",h3
# print "h5: ",h5
# print "h7: ",h7
# print "h5 + h7: ",h5 + h7
# print "h1 - h3: ",h1 - h3
# print (h5 + h7)/(2*(h1 - h3))

# dp2=[1,1,1,1]
# dp3=[1,1,1,1]
# dp22=uncertainty[2]
# dp23=uncertainty[3]
# dp31=uncertainty[1]
# dp32=uncertainty[2]
# dp33=uncertainty[3]
# print dp2[2]
# Varianz = (dp2[1]**2*(p2[2] + p3[2] + 2*p3[3]*(p3[0] + pi/2) + 2*p2[3]*(p2[0] + pi))**2)/(4*(p2[1] - p3[1] + p3[3]*(p3[0] + pi/2)**2 + p2[3]*(p2[0] + pi)**2 + p3[2]*(p3[0] + pi/2) + p2[2]*(p2[0] + pi))**4) + (dp3[1]**2*(p2[2] + p3[2] + 2*p3[3]*(p3[0] + pi/2) + 2*p2[3]*(p2[0] + pi))**2)/(4*(p2[1] - p3[1] + p3[3]*(p3[0] + pi/2)**2 + p2[3]*(p2[0] + pi)**2 + p3[2]*(p3[0] + pi/2) + p2[2]*(p2[0] + pi))**4) + dp3[2]**2*(-((p2[2] + p3[2] + 2*p3[3]*(p3[0] + pi/2) + 2*p2[3]*(p2[0] + pi))*(p3[0] + pi/2))/(2*(p2[1] - p3[1] + p3[3]*(p3[0] + pi/2)**2 + p2[3]*(p2[0] + pi)**2 + p3[2]*(p3[0] + pi/2) + p2[2]*(p2[0] + pi))**2) + 1/(2*(p2[1] - p3[1] + p3[3]*(p3[0] + pi/2)**2 + p2[3]*(p2[0] + pi)**2 + p3[2]*(p3[0] + pi/2) + p2[2]*(p2[0] + pi))))**2 + dp2[2]**2*(-((p2[2] + p3[2] + 2*p3[3]*(p3[0] + pi/2) + 2*p2[3]*(p2[0] + pi)) (p2[0] + pi))/(2*(p2[1] - p3[1] + p3[3]*(p3[0] + pi/2)**2 + p2[3]*(p2[0] + pi)**2 + p3[2]*(p3[0] + pi/2) + p2[2]*(p2[0] + pi))**2) + 1/(2*(p2[1] - p3[1] + p3[3]*(p3[0] + pi/2)**2 + p2[3]*(p2[0] + pi)**2 + p3[2]*(p3[0] + pi/2) + p2[2]*(p2[0] + pi))))**2 + dp3[3]**2*(-((p3[0] + pi/2)**2*(p2[2] + p3[2] + 2*p3[3]*(p3[0] + pi/2) + 2*p2[3]*(p2[0] + pi)))/(2*(p2[1] - p3[1] + p3[3]*(p3[0] + pi/2)**2 + p2[3]*(p2[0] + pi)**2 + p3[2]*(p3[0] + pi/2) + p2[2]*(p2[0] + pi))**2) + (p3[0] + pi/2)/(p2[1] - p3[1] + p3[3]*(p3[0] + pi/2)**2 + p2[3]*(p2[0] + pi)**2 + p3[2]*(p3[0] + pi/2) + p2[2]*(p2[0] + pi)))**2 + dp2[3]**2*(-((p2[0] + pi)**2*(p2[2] + p3[2] + 2*p3[3]*(p3[0] + pi/2) + 2*p2[3]*(p2[0] + pi)))/(2*(p2[1] - p3[1] + p3[3]*(p3[0] + pi/2)**2 + p2[3]*(p2[0] + pi)**2 + p3[2]*(p3[0] + pi/2) + p2[2]*(p2[0] + pi))**2) + (p2[0] + pi)/(p2[1] - p3[1] + p3[3]*(p3[0] + pi/2)**2 + p2[3]*(p2[0] + pi)**2 + p3[2]*(p3[0] + pi/2) + p2[2]*(p2[0] + pi)))**2
	
ax = gca()
ax.set_xlabel("Angle of polarizator")
ax.set_ylabel("Intensity")
title("Polarization of A2623 \n - sample tilted by 45 degree")
font = {'family' : 'serif',
		'weight' : 'normal',
		'size'   : 20}
matplotlib.rc('font', **font)
ax.errorbar(xdata,ydata,color='black',xerr=[dx]*len(xdata),yerr=[dy]*len(ydata),fmt='+',label=u'data')

xfitdata=arange(0,360,1)
ax.plot(xfitdata,fit1(p1,xfitdata),color='black',label='lineare Anpassung')
#ax.plot(xfitdata,fit2(p2,xfitdata),color='black',label='lineare Anpassung')
#ax.plot(xfitdata,fit2(p3,xfitdata),color='black',label='lineare Anpassung')
ax.plot(xfitdata,fit2(p4,xfitdata),color='red',label='lineare Anpassung')
ax.plot(xfitdata,fit2(p5,xfitdata),color='red',label='lineare Anpassung')
ax.xaxis.set_minor_locator( AutoMinorLocator(5))
#ax.legend(loc=1)	
show()




