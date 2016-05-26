#!/cmutnik/bin/python
# to plot S/N vs Integration Time by reading in csv

from astropy.io import ascii
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt


# read in csv file starting from second row so row of column titles isnt used
tabdat = ascii.read("paper.table.csv", data_start=1)
tabnames = ascii.read("paper.table.csv") # to use correct colnames in table t
#print tabdat

J_mag = tabdat['col7']
SNR = tabdat['col8']
exptime = tabdat['col9']


# AS SINGLE PLOT
fig = plt.figure()
# to adjust margin on left side of plot
fig.subplots_adjust(left=0.125)
#fig.subplots_adjust(left=0.1, wspace=0.6)

plt.clf()
#area_ = np.pi * (0.002 * np.array(J_mag))**2
plt.scatter(J_mag, SNR, c=np.array(exptime), alpha=0.4)#, s=area_)
plt.colorbar().set_label('Integration Time')
plt.xlabel('Brightness (Jmag)')
plt.ylabel('SNR')
#plt.show()
plt.savefig('snr_brightness2.pdf')


# FLIP COLORBAR AND X-AXIS
plt.clf()
plt.scatter(exptime, SNR, c=np.array(J_mag), alpha=0.4)
plt.colorbar().set_label('Brightness (Jmag)')
plt.xlabel('Integration Time')
plt.ylabel('SNR')
#plt.show()
plt.savefig('snr_exptime2.pdf')
