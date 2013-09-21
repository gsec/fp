import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import AutoMinorLocator, AutoLocator
rc('font', family = 'serif', serif = 'STIXGeneral')

txt_filename_to_open=[]
# ------------------  Eingaben  ------------
for i in range(10):
    filename="03-Resonanzfrequenz-"+str(i)+".dat"
    txt_filename_to_open.append(filename)
# Erste Zeile, die eingelesen wird
read_start=10
# ------------------------------------------
for n in range(len(txt_filename_to_open)):
    data = [i.strip().split() for i in open(txt_filename_to_open[n]).readlines()] # hier nacher ein n rein

    t=[]
    S=[]

    for i in range(len(data[read_start-1:])):
        t=append(t,float(data[read_start-1+i][0]))
        S=append(S,float(data[read_start-1+i][1]))
        
    plt.figure(n) # hier nacher ein n rein
    plt.xlabel(data[read_start-2][0:3])
    plt.ylabel(data[read_start-2][3:6])
    title(data[6])
    font = {'family' : 'serif',
            'weight' : 'normal',
            'size'   : 20}
    matplotlib.rc('font', **font)
    subplots_adjust(left=0.18, bottom=0.12, right=0.96, top=0.92, wspace=0.2, hspace=0.2)
    plt.plot(t,S,color="blue",label="Messwerte")
    plt.legend(loc=0)	
    # plt.savefig("Hallsteigung.pdf")
    show()