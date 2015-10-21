# use latex table using astropy
# 9/11/15

from astropy.io import fits
from astropy.io import ascii
from astropy.table import Table
import sys
import numpy as np
from glob import glob
import os

dir_path = u'/Users/corey/work/astro/finished_with_fixed_names'
globpath = os.path.join(dir_path, '*_merge.fits')
filelist = glob(globpath)
filelist.sort()
data_rows = []
docname = 'test_tab.tex'

for i in range(0, len(filelist)):
    
    specdat = fits.open(filelist[i])
    spectra = specdat[0].data
    header = specdat[0].header

    # Calculate SNR over range
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

    instrument = header['INSTR']
    Object = file_name
    Spectral_Type = '?'
    UT_Date = header['Date_OBS']
    J_mag = np.where(abs(spectra[0] - 1.25) == min(abs(spectra[0] - 1.25)))[0][0]
    S_N = avg_snr
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
    list_data[6] = S_N
    list_data[7] = Total_Exp
    list_data[8] = A0V
    list_data[9] = Teff
    list_data[10] = logg

    data_rows.append(list_data)

t = Table(rows=data_rows, names=('Object', 'RA', 'Dec', 'Spectral Type', 'UT Date', 'J mag, flux(1.25 microns)', 'S/N', 'Total Exp. Time (s)', 'A0Vstandard', 'Teff', 'log(g)'), meta={'name': 'first table'})

t.write(docname, format='latex')
