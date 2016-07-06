#!/cmutnik/bin/python
# Python script to generate histogram of observed stars (optical) spectral classes 
# Corey Mutnik 3/14/16
# modified 7/5/16

#from numpy.random import normal
import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt

# open data
spt_data = ascii.read('rebinned_color_no_double_count.txt')

# for histogram
ind = np.arange(len(spt_data['binned']))  # the x locations for the groups
width = 0.35       # the width of the bars

# PLOT
plt.clf()
fig, ax = plt.subplots()

# to adjust margin on left side of plot
fig.subplots_adjust(left=0.125)# ,wspace=0.6)

ax.set_ylim(0,11)
rects2 = ax.bar(ind + width, spt_data['binned'], width, color=spt_data['color'])

# add some text for labels, title and axes ticks
ax.set_ylabel('Number of Stars')
ax.set_xlabel('Spectral Type')
ax.set_title('Spectral Composition of Library')
ax.set_xticks(ind + 1.5*width)
ax.set_xticklabels((spt_data['class']))

#plt.show()
plt.savefig('histogram_of_spt_classes_color_46total.png')



