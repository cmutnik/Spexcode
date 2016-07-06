#!/cmutnik/bin/python
# Python script to generate histogram of observed stars (optical) luminosity classes 
# Corey Mutnik 3/14/16


import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt

# open data
spt_data = ascii.read('rebinned_lum.txt')
'''
note
include protostar
not including HIP 79987 (HD 146899)
(GSC observed with old and new spex)
'''

# for histogram
ind = np.arange(len(spt_data['binned']))  # the x locations for the groups
width = 0.35       # the width of the bars

# PLOT
#fig = plt.figure()
#fig.subplots_adjust(left=0.125)# ,wspace=0.6)
plt.clf()

fig, ax = plt.subplots()
# to adjust margin on left side of plot
fig.subplots_adjust(left=0.125)# ,wspace=0.6)

#ax.set_ylim(0,14)
rects2 = ax.bar(ind + width, spt_data['binned'], width, color='w')

# add some text for labels, title and axes ticks
ax.set_ylabel('Number of Stars')
ax.set_xlabel('Spectral Type')
ax.set_xticks(ind + 1.5*width)
ax.set_xticklabels((spt_data['class']))

#plt.show()
plt.savefig('histogram_of_lum_classes.pdf')

