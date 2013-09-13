import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot(111)
line1 = ax1.plot([1,2,3,4],[1,2,3,7], 'r')

ax2 = ax1.twinx()
line3 = ax2.plot([1,2,3,4],[10,20,30,40],'b')

ax3 = ax1.twinx()
line5 = ax3.plot([1,2,3,4],[100,400,500,300],'c')

ax1.set_ylim(ymin=0)
ax2.set_ylim(ymin=0)
ax1.grid(True)

for label in ax1.get_yticklabels():
    label.set_color('r')
for label in ax2.get_yticklabels():
    label.set_color('b')
for label in ax3.get_yticklabels():
    label.set_color('c')

plt.show()