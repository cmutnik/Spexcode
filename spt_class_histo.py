#!/cmutnik/bin/python
# Python script to generate histogram of observed stars (optical) spectral classes 
# Corey Mutnik 3/14/16

#from numpy.random import normal
import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt
'''
#dfile = ascii.read('Workbook3.csv', delimiter=',')
dfile = ascii.read('Workbook5.csv', delimiter=',')
Names = dfile['Name']
spt_class_list = dfile['Class']
'''
#spt_data = ascii.read('binned_spt_classes.txt')
'''
class	binned
A		8 #9 not including HIP 79987 (HD 146899)
B		12
F		8
G		7 # 6 if we exclude protostellar
K		10  #11 (GSC observed with old and new spex)
M		4
S		1
other	1
'''
# open data
spt_data = ascii.read('rebinned.txt')

# for histogram
ind = np.arange(len(spt_data['binned']))  # the x locations for the groups
width = 0.35       # the width of the bars

# PLOT
plt.clf()
fig, ax = plt.subplots()

# to adjust margin on left side of plot
fig.subplots_adjust(left=0.125)# ,wspace=0.6)

ax.set_ylim(0,14)
rects2 = ax.bar(ind + width, spt_data['binned'], width, color='w')

# add some text for labels, title and axes ticks
ax.set_ylabel('Number of Stars')
ax.set_xlabel('Spectral Type')
ax.set_title('Spectral Composition of Library')
ax.set_xticks(ind + 1.5*width)
ax.set_xticklabels((spt_data['class']))

#plt.show()
plt.savefig('histogram_of_spt_classes.pdf')




'''
gaussian_numbers = normal(size=1000)
#plt.hist(gaussian_numbers)
plt.hist(dfile, bins=20, normed=True)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
'''
