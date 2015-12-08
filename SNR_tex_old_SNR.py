# script for plotting the signal to noise ratio with object name (in latex table format)
# Corey Mutnik
# 8/10/15


from astropy.io import fits
import matplotlib.pyplot as plt
from glob import glob
import os
import numpy as np

dir_path = u'/Users/corey/work/astro/finished_8_3_15'
globpath = os.path.join(dir_path, '*.fits')
filelist = glob(globpath)
filelist.sort()

f = open('SNR_table', 'w+')

for i in range(0, len(filelist)):
    spectra = fits.getdata(filelist[i])

    # avg SNR over continuum region (min_, max_)
    min_ = np.where(abs(spectra[0] - 2.025) == min(abs(spectra[0] - 2.025)))[0][0]
    max_ = np.where(abs(spectra[0] - 2.162) == min(abs(spectra[0] - 2.162)))[0][0]
    snr = []
    for j in range(min_, max_):
        snr.append(spectra[1][j] / spectra[2][j])
    sum_snr = 0.0
    for j in range(0, len(snr)):
        sum_snr += snr[j]
    avg_snr = sum_snr / len(snr)

    file_name = os.path.basename(filelist[i])
    to_write = file_name + ' & ' + str(avg_snr) + '\n'
    
    f.write(to_write)

    #print file_name + ' & ' + str(avg_snr)
    #print repr(file_name).rjust(2), repr(' & ').rjust(3), repr(avg_snr).rjust(4)

f.close()




