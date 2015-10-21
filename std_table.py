# use code from std.py to make table
# Corey Mutnik
# 10/5/15



from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import os
import scipy.stats #for signal to noise


dir_path = u'/Users/corey/work/astro/finished_8_3_15'

# first test with single fits file

globpath = os.path.join(dir_path, '*merge.fits')
filelist = glob(globpath)
filelist.sort() # so we are know which file we are working with

for i in range(len(filelist)):
    spec = fits.open(filelist[i])


    spec = fits.open('CD25-11942_7_1_15_merge.fits')
    data = spec[0].data
    wave_ = data[0]
    flux_ = data[1]

    def normalize(wave_array, flux_array):
        norm_value = np.where(abs(wave_array - 1.10) == min(abs(wave_array-1.10)))[0][0]
        norm_den = (float)((wave_array[norm_value] * flux_array[norm_value])**(-1))
        norm_flux = []
        for i in range(0, len(wave_array)):
            norm_flux.append(wave_array[i] * flux_array[i] * norm_den)
        return norm_flux

    '''
    # for continuum, micron range 2.025 - 2.162
    lower = np.where(abs(wave_ - 2.025) == min(abs(wave_ - 2.025)))[0][0]
    upper = np.where(abs(wave_ - 2.162) == min(abs(wave_ - 2.162)))[0][0]
    '''
    # change continuum to 2.118 - 2.133 microns
    lower = np.where(abs(wave_ - 2.118) == min(abs(wave_ - 2.118)))[0][0]
    upper = np.where(abs(wave_ - 2.133) == min(abs(wave_ - 2.133)))[0][0]


    norm_flux_continuum = normalize(wave_, flux_)[lower:upper]#[6106:6488]
    standard_deviation = np.std(norm_flux_continuum)

    # sigma = sqrt( sum of (x -  mean(x))^2 / n) ... might be n-1 not n
    summed = 0.0
    for i in range(len(norm_flux_continuum)):
        x = float(norm_flux_continuum[i])
        xbar = np.mean(norm_flux_continuum)
        n = float(len(norm_flux_continuum))
        summed += (x-xbar)**2
    sigma = np.sqrt(summed/(n))

    # NOTE: SNR == SNR2 == SNR3
    SNR = np.mean(norm_flux_continuum) / sigma
    #print SNR

    # different way to get snr
    std = np.std(norm_flux_continuum)
    SNR2 = np.mean(norm_flux_continuum) / std

    #third way to get snr
    SNR3 = scipy.stats.signaltonoise(norm_flux_continuum)#, axis=None)
    #print SNR3



    #plt.clf()
    #plt.plot(wave_[lower:upper], norm_flux_continuum)
    #plt.show()
