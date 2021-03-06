#!/cmutnik/bin/python
# Python script to generate histogram of observed stars (optical) spectral classes 
# Corey Mutnik 3/14/16

from astropy.io import ascii
import matplotlib.pyplot as plt
import numpy as np

# open data
spt_data = ascii.read('rebinned.txt')

# for histogram
ind = np.arange(len(spt_data['binned']))  # the x locations for the groups
width = 0.35       # the width of the bars

# PLOT
plt.clf()

fig, ax = plt.subplots()
ax.set_ylim(0,14)
rects2 = ax.bar(ind + width, spt_data['binned'], width, color='w')

# add some text for labels, title and axes ticks
ax.set_ylabel('Number of Stars')
ax.set_xlabel('Spectral Type')
ax.set_title('Spectral Composition of Library')
ax.set_xticks(ind + 1.5*width)
ax.set_xticklabels((spt_data['class']))

#plt.show()
plt.savefig('histogram_of_spt_classes.png')
