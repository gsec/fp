# -*- coding: utf-8 -*-


from scipy import *
from scipy import optimize
from matplotlib import rc
from numpy import *
import matplotlib.pyplot as plt

# from fitting import *
from pylab import *


zeta = 0.03
eta = 0.04
r = 0.015*10**(-2)
R = 0.207
n = 720
mu_0 = 1.25663706*10**(-6)


c = (mu_0*n)/R * ( 8/(5*sqrt(5)) * (1- zeta**2/(60*R)) - (31*zeta**2 - 36*eta**2)/(125*R**4)*r**2 )
fehler_c = 0.01*c

print "c: ", c

g = 5.585694713
h = 6.62606957*10**(-34) #Js
steigung = 36125.0*(1000**2) #Hz^2/A^2
steigung_fehler = 22.0*(1000**2)

mu_k = sqrt( (steigung*h**2)/(2*g**2*c**2) )
mu_k_fehler = sqrt(((1.0/2*((steigung*h**2)/(2*g**2*c**2))**(-1.0/2)*h**2/(2*g**2*c**2))**2 *steigung_fehler**2) + ((sqrt(steigung/2)*h/(g*c**2))**2 * fehler_c**2) )



mu_p_lit = 1.410606743*10**(-26) #J/T
mu_k_lit = 5.05078353*10**(-27) #J/T

print "mu_k: ", mu_k, "+-", mu_k_fehler
print "mu_k_lit: ", mu_k_lit

t = 4458*1000 #Hz^2
t_fehler = 80*1000 

B_S = sqrt( ( t*h**2 )/( 2 *g**2 *mu_k**2  ) )
B_S_fehler = sqrt( (1.0/2 * (( t *h**2 )/( 2 *g**2 *mu_k**2 ))**(-1.0/2) * ( t*h**2 )/( 2 *g**2 *mu_k**3 ))**2 * mu_k_fehler**2 + 
			( 1.0/2 * ( (t*h**2)/(2*g**2*mu_k**2) )**(-1.0/2) * h**2/(2*g**2*mu_k**2) )**2 * t_fehler**2 )

print "B_S: ", B_S, "+-", B_S_fehler

m_2 = 3434*10**(2)*1000
m_2_fehler = 27*10**(2)*1000

cos_phi = ( m_2*h**2 )/( 4*g**2 *mu_k**2 *c*B_S )
phi = arccos(cos_phi)
phi_fehler = sqrt(( (1.0/(sqrt( 1-cos_phi**2 )) * h**2/( 4*g**2 *mu_k**2 *c*B_S ))**2 *m_2_fehler**2 )+ 
			((1.0/(sqrt( 1-cos_phi**2 )) * (m_2*h**2)/( 4*g**2 *mu_k**2 *c*B_S**2 ))**2 * B_S_fehler**2 ))


print "phi: ", phi, "+-", phi_fehler
print "phi in Grad", phi/pi * 180, "+-", phi_fehler/pi * 180
print "rest", m_2/cos_phi
print cos_phi

