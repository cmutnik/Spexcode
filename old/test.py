from astropy.io import fits
import matplotlib.pyplot as plt
from glob import glob
import os
import numpy as np

dir_path = u'/Users/corey/work/astro/finished_8_3_15'
globpath = os.path.join(dir_path, '*_merge.fits')
filelist = glob(globpath)
filelist.sort()

f = open('ZZZ_TEST1.tex', 'w+')
for var in range(0, len(filelist)):
    specdat = fits.open(filelist[var])
    header = 0
    header = specdat[0].header
    gap = ' & '
    breakl = ' \\' + '\\' + '\n'
    avg_snr = 1
    file_name = os.path.basename(filelist[var])
    instrument = header['INSTR']    
    if instrument == 'uSpeX':
        table_data2 = str(file_name) + gap + header['TCS_RA'] + gap + header['TCS_DEC'] + gap + '[spt_type]'+ gap + header['DATE_OBS'] + gap + '[J mag]' + gap + str(avg_snr) + gap + str(header['ITOT']) + gap + header['A0VSTD'] + gap + '[Teff]' + gap + '[log(g)]' + breakl
    elif instrument == 'SpeX':
        table_data2 = str(file_name) + gap + header['RA'] + gap + header['DEC'] + gap + '[spt_type]'+ gap + header['DATE_OBS'] + gap + '[J mag]' + gap + str(avg_snr) + gap + str(header['ITOT']) + gap + header['A0VSTD'] + gap + '[Teff]' + gap + '[log(g)]' + breakl
    else:
        table_data2 = "Data not taken with SpeX or uSpeX, check header['INSTR']"
    f.write(table_data2)
    #f.close()
f.close()
    
    
'''
f = open('ZZZ_TEST1.tex', 'w+')
specdat = fits.open(filelist[0])
header = specdat[0].header
gap = ' & '
breakl = ' \\' + '\\' + '\n'
avg_snr = 1
file_name = os.path.basename(filelist[0])
instrument = header['INSTR']    
if instrument == 'uSpeX':
    table_data2 = str(file_name) + gap + header['TCS_RA'] + gap + header['TCS_DEC'] + gap + '[spt_type]'+ gap + header['DATE_OBS'] + gap + '[J mag]' + gap + str(avg_snr) + gap + str(header['ITOT']) + gap + header['A0VSTD'] + gap + '[Teff]' + gap + '[log(g)]' + breakl
elif instrument == 'SpeX':
    table_data2 = str(file_name) + gap + header['RA'] + gap + header['DEC'] + gap + '[spt_type]'+ gap + header['DATE_OBS'] + gap + '[J mag]' + gap + str(avg_snr) + gap + str(header['ITOT']) + gap + header['A0VSTD'] + gap + '[Teff]' + gap + '[log(g)]' + breakl
else:
    table_data2 = "Data not taken with SpeX or uSpeX, check header['INSTR']"
f.write(table_data2)
f.close()
'''
