# Using the magic encoding
# -*- coding: utf-8 -*-

# 1. just copy the .dat file in the folder of this file 
# add a txt_filename_to_open
# execute "python make_plot_from_NextNano_output.py
# first collum on the input file is name of data




import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes
from mpl_toolkits.axes_grid.inset_locator import mark_inset
from matplotlib.ticker import AutoMinorLocator, AutoLocator

txt_filename_to_open=[]
line=[]
colors = [(0.0, 0.75, 0.75),(0.0, 0.5, 0.0),(0.75, 0.75, 0),(1.0, 0.0, 0.0), (0.75, 0, 0.75)]
# ------------------  Eingaben  ------------
txt_filename_to_open.append("4,2-Hallspannung.dat")
line.append(1)
# ------------------------------------------

for n in range(len(txt_filename_to_open)):
	txt_file = [i.strip().split() for i in open(txt_filename_to_open[n]).readlines()]
	ax = gca()
	#ax.set_xlabel(txt_file[0][0])
	#ax.set_ylabel(txt_file[0][1])
	ax.set_xlabel(u'wavenumber [$\\mathrm{cm}^{-1}$]')
	ax.set_ylabel(u'intensity [arb.u.]')
	
	#txt_file.remove(txt_file[0])
	xdata=[]
	ydata=[]
	for i in range(len(np.array(txt_file))):
		xdata=append(xdata,float(txt_file[i][0]))
		ydata=append(ydata,float(txt_file[i][line[n]]))
	# print xdata
	# print ydata
	title("FTIR-spectra @ 300K")
	font = {'family' : 'serif',
			'weight' : 'normal',
			'size'   : 20}
	matplotlib.rc('font', **font)
	ax.plot(xdata,ydata,color=colors[n],label=txt_filename_to_open[n][0:5])
	print txt_filename_to_open[n]
	ax.xaxis.set_minor_locator( AutoMinorLocator(5))
ax.legend(loc=1)	
show()
