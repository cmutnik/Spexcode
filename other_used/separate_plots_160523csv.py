#!/cmutnik/bin/python
# code3 mod of scripty_ intended to plot spectra of each star seperately, using downloaded csv file
# Corey Mutnik
# 9/11/15-9/30/15
# mod: 5/23/16 

from astropy.io import fits, ascii
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import os

# read in csv file starting from second row so row of column titles isnt used
tabdat = ascii.read("paper.table.160523.csv", data_start=1)
tabdat.colnames

file_names = tabdat['Object']
spttypes = tabdat['Lit. Spectral Type']
# test to make sure reading in csv file works same as glob
'''
dir_path = u'/Users/cmutnik/work/astro/finished_with_fixed_names'
globpath = os.path.join(dir_path, '*.fits')
filelist = glob(globpath)
filelist.sort()

filelisted= []
tablelist = []
for j in range(len(tabdat)):
    fn = file_names[j]+'.fits'
    file_name = os.path.basename(filelist[j])#[:-5]
    filelisted.append(file_name)
    tablelist.append(fn)

filelisted.sort()
tablelist.sort()

len(filelisted) == len(tablelist)

for j in range(len(tabdat)):
    print tablelist[j], ' , ', filelisted[j]
#    print tablelist[j] == filelisted[j]
'''
for j in range(len(tabdat)):
    # use csv rather than glob, to more easily get spt type
    fn = file_names[j]+'.fits'
    fn_dir = '/Users/cmutnik/work/astro/finished_with_fixed_names/' + fn
    
    spectra = fits.getdata(fn_dir)
    norm_wave = np.where(abs(spectra[0]-2.20) == min(abs(spectra[0]-2.20)))[0][0]
    norm_den = (float)((spectra[0][norm_wave] * spectra[1][norm_wave])**(-1))
    norm_flux = []
    for i in range(0, len(spectra[0])):
        norm_flux.append(spectra[0][i] * spectra[1][i] * norm_den)

     #[:-5] prints file_name removing '.fits' from each

    #xmax = np.max(spectra[0])
    #xmin = np.min(spectra[0])
    xmin = 0.7
    xmax = 2.55

    figure_name = file_names[j] + '.pdf'
    plot_title = file_names[j] + ' (' + spttypes[j] + ')'

    fig = plt.figure()
    # to adjust margin on left side of plot
    fig.subplots_adjust(left=0.125)#, wspace=0.6)
    
    plt.clf() # clears graph so they dont plot over eachother
    plt.plot(spectra[0], norm_flux, lw=0.5, color='black')

    plt.title(plot_title)
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda (2.2\mu m)$')
    #plt.ylabel('f$_\lambda$ $(ergs$ $s^{-1} cm^{-2} \AA^{-1})$')

    #plt.ylim(0, 5)
    #plt.xlim(0.58, 2.6)
    #plt.xlim(np.min(spectra[0]), np.max(spectra[0]))
    plt.xlim(xmin, xmax) # dont wanna use xmin/max since it will differ for spex vs uspex data
    #plt.grid(True)

    # Filling light gray
    plt.axvspan(0.92, 0.95, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.11, 1.16, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.415, 1.49, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.91, 2.05, facecolor='gray', alpha=0.25, lw=0)
    # fill dark gray
    plt.axvspan(1.35, 1.415, facecolor='gray', alpha=0.5, lw=0)
    plt.axvspan(1.8, 1.91, facecolor='gray', alpha=0.5, lw=0)

    plt.savefig(figure_name)
    #plt.show()
