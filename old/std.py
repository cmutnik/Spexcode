# calculate standard deviation of spectrum across continuum
# Corey Mutnik
# 8/3/15

#####
# unfinished
####

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import os

dir_path = u'/Users/corey/work/astro/finished_8_3_15'

globpath = os.path.join(dir_path, '*merge.fits')
filelist = glob(globpath)
filelist.sort() # so we are know which file we are working with

spectra = fits.getdata(filelist[0])

def normalize(wave_array, flux_array):
    norm_value = np.where(abs(wave_array - 1.10) == min(abs(wave_array-1.10)))[0][0]
    norm_den = (float)((wave_array[norm_value] * flux_array[norm_value])**(-1))
    norm_flux = []
    for i in range(0, len(wave_array)):
        norm_flux.append(wave_array[i] * flux_array[i] * norm_den)

    return norm_flux


norm_flux_continuum = norm_flux[6106:6488]
standard_deviation = np.stp(norm_flux_continuum)
