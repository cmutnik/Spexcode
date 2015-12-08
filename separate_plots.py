# code3 mod of scripty_ intended to plot spectra of each star seperately
# Corey Mutnik
# 9/11/15-9/30/15 

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import os

dir_path = u'/Users/corey/work/astro/finished_with_fixed_names'
globpath = os.path.join(dir_path, '*.fits')
filelist = glob(globpath)
filelist.sort()

for j in range(0, len(filelist)):
    spectra = fits.getdata(filelist[j])
    norm_wave = np.where(abs(spectra[0] - 1.10) == min(abs(spectra[0]-1.10)))[0][0]
    norm_den = (float)((spectra[0][norm_wave] * spectra[1][norm_wave])**(-1))
    norm_flux = []
    for i in range(0, len(spectra[0])):
        norm_flux.append(spectra[0][i] * spectra[1][i] * norm_den)

    file_name = os.path.basename(filelist[j])[:-5] #[:-5] prints file_name removing '.fits' from each
    #print file_name
    y_pos = 1 + j


    xmax = 2.4195919036865234 # = np.max(spectra[0])
    xmin = 0.80251264572143555 # = np.min(spectra[0])
    to_plot_regions = np.arange(0.0, 3.0 , 0.1)


    figure_name = file_name + '.png'

    '''
    rayner_title = file_name + '(SPT class)'
    plt.title(rayner_title)
    plt.xlim(0.8, 2.5) # what rayner used
    '''
    plt.clf() # clears graph so they dont plot over eachother
    plt.plot(spectra[0], norm_flux, lw=0.5, color='black')
    #plt.text(2, y_pos, file_name)

    plt.title(file_name)
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda (1.1\mu m) + $ constant')
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


#    plt.fill_between(to_plot_regions, 2.5, 2.6, color='gray', alpha=0.5)

    plt.savefig(figure_name)
    #plt.show()
