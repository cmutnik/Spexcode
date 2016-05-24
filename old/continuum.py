# compressed_code script (script to plot spectra)
# Corey Mutnik
# 7/17/15

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import os

dir_path = u'/Users/corey/work/astro/finished_8_3_15'

globpath = os.path.join(dir_path, '*merge.fits')
filelist = glob(globpath)
filelist.sort() # unnecessary

for j in range(0, len(filelist)):
    spectra = fits.getdata(filelist[j])
    norm_wave = np.where(abs(spectra[0] - 1.10) == min(abs(spectra[0]-1.10)))[0][0]
    norm_den = (float)((spectra[0][norm_wave] * spectra[1][norm_wave])**(-1))
    norm_flux = []
    for i in range(0, len(spectra[0])):
        norm_flux.append(spectra[0][i] * spectra[1][i] * norm_den + j)
    file_name = os.path.basename(filelist[j])
    plt.plot(spectra[0], norm_flux)
'''
    # Remove values of arrays that
    _a = spectra[0][6106:6488]
    _b = spectra[1][6106:6488]
    plt.plot(_a,_b)
'''


# to verify spectra are labeled correctly
    #plt.show()

    
plt.title('Title')
plt.xlabel('Wavelength $\mu$m')
plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda (1.1\mu m) + $ constant')
#plt.ylim(0, 5)
plt.xlim(2.02512764931, 2.16184401512)
plt.grid(True)
#plt.savefig('something.pdf')
plt.show()
