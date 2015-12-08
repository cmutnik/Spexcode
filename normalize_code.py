# function that normalizes flux
# Corey Mutnik
# 8/3/15

###
# needs to be tested
###


from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import os

dir_path = u'/Users/corey/work/astro/finished_8_3_15'

globpath = os.path.join(dir_path, '*merge.fits')
filelist = glob(globpath)
filelist.sort() # so we are know which file we are working with



def normalize(wave_array, flux_array):
    norm_value = np.where(abs(wave_array - 1.10) == min(abs(wave_array-1.10)))[0][0]
    norm_den = (float)((wave_array[norm_value] * flux_array[norm_value])**(-1))
    norm_flux = []
    for i in range(0, len(wave_array)):
        norm_flux.append(wave_array[i] * flux_array[i] * norm_den)
    return norm_flux


# plots all '*merge.fits' in directory path 
for j in range(0, len(filelist)):
    spectra = fits.getdata(filelist[j])
    normalized_flux = normalize(spectra[0], spectra[1])
    file_name = os.path.basename(filelist[j])
    plt.plot(spectra[0], normalized_flux)
plt.title('Title')
plt.xlabel('Wavelength $\mu$m')
plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda (1.1\mu m) + $ constant')
#plt.ylim(0, 5)
plt.xlim(2.02512764931, 2.16184401512)
plt.grid(True)
#plt.savefig('something.pdf')
plt.show()




