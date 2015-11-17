# use latex table using astropy
# 9/11/15

from astropy.io import fits
from astropy.io import ascii
from astropy.table import Table
import sys
import numpy as np
from glob import glob
import os
import matplotlib.pyplot as plt
dir_path = u'/Users/corey/work/astro/finished_with_fixed_names'
globpath = os.path.join(dir_path, '*.fits')
filelist = glob(globpath)
filelist.sort()
data_rows = []
docname = 'test_tab2.tex'

for i in range(0, len(filelist)):
    
    specdat = fits.open(filelist[i])
    spectra = specdat[0].data
    header = specdat[0].header
    file_name = os.path.basename(filelist[i])[:-5] #-----------------------ONLY CHANGE: modified filenames to not include '.fits'

    instrument = header['INSTR']
    Object = file_name
    Spectral_Type = '?'
    UT_Date = header['Date_OBS']
    J_mag = np.where(abs(spectra[0] - 1.25) == min(abs(spectra[0] - 1.25)))[0][0]
    #S_N = avg_snr
    A0V = header['A0VSTD']
    Teff = '?'
    logg = '?'
    Total_Exp = header['ITOT']

    if instrument == 'uSpeX':
        RA = header['TCS_RA']
        Dec = header['TCS_DEC']
    elif instrument == 'SpeX':
        RA = header['RA']
        Dec = header['DEC']
    else:
        print 'did this work?'


    #[Object, RA, Dec, Spectral_Type, UT_Date, J_mag, S_N, Total_Exp, A0V, Teff, logg]
    #list_data = np.zeros(11)
    list_data = [str(0)]*11
    list_data[0] = Object
    list_data[1] = RA
    list_data[2] = Dec
    list_data[3] = Spectral_Type
    list_data[4] = UT_Date
    list_data[5] = J_mag
    #list_data[6] = S_N # defined below
    list_data[7] = Total_Exp
    list_data[8] = A0V
    list_data[9] = Teff
    list_data[10] = logg

    data_rows.append(list_data)


    wave_ = spectra[0]
    flux_ = spectra[1]

    def normalize(wave_array, flux_array):
        norm_value = np.where(abs(wave_array - 1.10) == min(abs(wave_array-1.10)))[0][0]
        norm_den = (float)((wave_array[norm_value] * flux_array[norm_value])**(-1))
        norm_flux = []
        for i in range(0, len(wave_array)):
            norm_flux.append(wave_array[i] * flux_array[i] * norm_den)
        return norm_flux
    # change continuum to 2.118 - 2.133 microns
    lower = np.where(abs(wave_ - 2.118) == min(abs(wave_ - 2.118)))[0][0]
    upper = np.where(abs(wave_ - 2.133) == min(abs(wave_ - 2.133)))[0][0]
    norm_flux_continuum = normalize(wave_, flux_)[lower:upper]#[6106:6488]
    standard_deviation = np.std(norm_flux_continuum)
    # Calculate SNR over range
    summed = 0.0
    for i in range(len(norm_flux_continuum)):
        x = float(norm_flux_continuum[i])
        xbar = np.mean(norm_flux_continuum)
        n = float(len(norm_flux_continuum))
        summed += (x-xbar)**2
    sigma = np.sqrt(summed/(n))
    SNR = np.mean(norm_flux_continuum) / sigma
    S_N = SNR
    list_data[6] = S_N

             # attempt to format table properly
t = Table(rows=data_rows, names=('Object', 'RA', 'Dec', 'Spectral Type', 'UT Date', 'J mag, flux(1.25 microns)', 'S/N', 'Total Exp. Time (s)', 'A0Vstandard', 'Teff', 'log(g)'), meta={'Spex': 'Young Stars'}, dtype=('str', 'str', 'str', 'str', 'str', 'f', 'i', 'f', 'str', 'str', 'str') )


t.write(docname, format='latex')
#print t
#print t.colnames
#print t.more()


# SNR VS EXP Time plot
plt.plot(t['Total Exp. Time (s)'], t['S/N'], 'ro')
plt.xlabel('Total Integration Time')
plt.ylabel('SNR')
plt.show()


'''
# commands to fill in table data
# print object name   RA   Dec
# already did x_ = 0 through x_ = 26
x_ = 27
print t[x_][0] + '   ' + t[x_]['RA'] + '   ' + t[x_]['Dec']
'''
