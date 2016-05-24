# script for plotting the signal to noise ratio with object name (in latex table format)
# Corey Mutnik
# 8/22/15
# 12:45 - 5:00
#5:00 - 6+1:00
###
# check it is printing correctly corresponding A0V
###


from astropy.io import fits
import matplotlib.pyplot as plt
from glob import glob
import os
import numpy as np

dir_path = u'/Users/corey/work/astro/finished_8_3_15'
globpath = os.path.join(dir_path, '*_merge.fits')
filelist = glob(globpath)
filelist.sort()

f = open('SNR_table_test1.tex', 'w+')

### \b not written properly
breakl = ' \\' + '\\' + '\n'
table_header = '\\begin{table} \n\\begin{tabular}{ c c c c c c c c c c c } \nObject & RA & Dec & Spectral Type & UT Date & J mag & S/N & Total Exp. Time (s) & A0Vstandard & Teff & log(g)' + breakl
f.write(table_header)



for i in range(0, len(filelist)):

    # test not with getdata
#    spectra = fits.getdata(filelist[i])
    specdat = fits.open(filelist[i])
    spectra = specdat[0].data
    header = specdat[0].header

    

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

#    to_write = file_name + ' & ' + str(avg_snr) + '\n'
#    f.write(to_write)
    spec_head = fits.open(filelist[i])
    header = spec_head[0].header
#    print header
#    f.write(header)

    gap = ' & '
    instrument = header['INSTR']
    if instrument == 'uSpeX':
        table_data2 = str(file_name) + gap + header['TCS_RA'] + gap + header['TCS_DEC'] + gap + '[spt_type]'+ gap + header['DATE_OBS'] + gap + '[J mag]' + gap + str(avg_snr) + gap + str(header['ITOT']) + gap + header['A0VSTD'] + gap + '[Teff]' + gap + '[log(g)]' + breakl
    elif instrument == 'SpeX':
        table_data2 = str(file_name) + gap + header['RA'] + gap + header['DEC'] + gap + '[spt_type]'+ gap + header['DATE_OBS'] + gap + '[J mag]' + gap + str(avg_snr) + gap + str(header['ITOT']) + gap + header['A0VSTD'] + gap + '[Teff]' + gap + '[log(g)]' + breakl
    else:
        table_data2 = "Data not taken with SpeX or uSpeX, check header['INSTR']"
    f.write(table_data2)


    
# doesnt work
'''
    if header['INSTR'] == 'uSpeX':
        table_data = str(file_name), ' & ', header['TCS_RA'], ' & ', header['TCS_DEC'], ' & ', '[spt_type]', ' & ', header['DATE_OBS'], ' & ', '[J mag]', ' & ', str(avg_snr), ' & ', str(header['ITOT']), ' & ', header['A0VSTD'], ' & ', '[Teff]', ' & ', '[log(g)]', breakl
    elif header['INSTR'] == 'SpeX':
        table_data = str(file_name), ' & ', header['RA'], ' & ', header['DEC'], ' & ', '[spt_type]', ' & ', header['DATE_OBS'], ' & ', '[J mag]', ' & ', str(avg_snr), ' & ', str(header['ITOT']), ' & ', header['A0VSTD'], ' & ', '[Teff]', ' & ', '[log(g)]', breakl
    else:
        table_data = "Data not taken with SpeX or uSpeX, check header['INSTR']"
    f.write(table_data)
'''
#f.write(table_data)

    
#    print table_data # issues with f.write
#    fits.close()

table_footer = '\end{tabular} \n\end{table}'
f.write(table_footer)

print 'check it is writing the correct A0V - check against notes'
f.close()






