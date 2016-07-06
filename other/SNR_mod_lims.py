#!/cmutnik/bin/python
# to plot S/N vs Integration Time by reading in csv

from astropy.io import ascii
from astropy.table import Table
import matplotlib.ticker as ticker
import numpy as np
import matplotlib.pyplot as plt


# read in csv file starting from second row so row of column titles isnt used
tabdat = ascii.read("paper.table.csv", data_start=1)
tabnames = ascii.read("paper.table.csv") # to use correct colnames in table t
#print tabdat

J_mag = tabdat['col7']
SNR = tabdat['col8']
exptime = tabdat['col9']


# FLIP COLORBAR AND X-AXIS
plt.clf()
fig, ax = plt.subplots()
plt.scatter(exptime, SNR, c=np.array(J_mag), alpha=0.4)
plt.colorbar().set_label('Brightness (Jmag)')
plt.xlabel('Integration Time')
plt.ylabel('SNR')
plt.xlim(-50,1250)
plt.ylim(90,240)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
# to adjust margin on left side of plot
fig.subplots_adjust(left=0.125)
#fig.subplots_adjust(left=0.1, wspace=0.6)

plt.savefig('snr_exptime_cutoff.pdf')

#plt.axhline(y=95, xmin=-200, xmax=1500, linewidth=0.5, color = 'r')
#plt.savefig('snr_exptime_line_cutoff.pdf')
