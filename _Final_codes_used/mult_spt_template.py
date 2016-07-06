#!~/bin/python
# Python script to determine spectral class of multiple options in literature
# Corey Mutnik 6/30/16

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import matplotlib.ticker as ticker
from glob import glob
import os

def plot_telluric_lines():
    # Filling light gray
    plt.axvspan(0.92, 0.95, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.11, 1.16, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.415, 1.49, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.91, 2.05, facecolor='gray', alpha=0.25, lw=0)
    # fill dark gray
    plt.axvspan(1.35, 1.415, facecolor='gray', alpha=0.5, lw=0)
    plt.axvspan(1.8, 1.91, facecolor='gray', alpha=0.5, lw=0)
    plt.axvspan(2.50, 2.88, facecolor='gray', alpha=0.5, lw=0)
def normalize_flux(wave_array, flux_array):
    micron_value = np.where(abs(wave_array - 2.20) == min(abs(wave_array - 2.20)))[0][0]
    norm_den = (float)((wave_array[micron_value] * flux_array[micron_value])**(-1))
    norm_flux = []
    for i in range(0, len(wave_array)):
        norm_flux.append(wave_array[i] * flux_array[i] * norm_den)
    return np.array(norm_flux)  
def mask_wave_flux(wavein, fluxin):
    # mask dark telluric
    masked_wave = np.ma.masked_inside(wavein, 1.35, 1.415)
    masked_wave = np.ma.masked_inside(masked_wave, 1.8, 1.91)
    masked_wave = np.ma.masked_inside(masked_wave, 2.50, 2.88)
    # apply mask to flux array
    masked_flux = np.ma.masked_array(fluxin, masked_wave.mask)
    return(masked_wave, masked_flux)

# star that has multiple spectral classifications in literature
multi_obj = 'HIP 78977'

# rayner stars to compare it to
compare1 = 'F7V_HD126660.fits'
compare2 = 'F8V_HD219623.fits'


# directory paths
obs_dir_path = '/Users/cmutnik/work/astro/finished_with_fixed_names/'
ray_dir_path = '/Users/cmutnik/work/astro/plots/compare/z_rayner_all/'

# open fits files
spectra = fits.getdata(obs_dir_path + multi_obj + '.fits')
ray1 = fits.getdata(ray_dir_path + compare1)
ray2 = fits.getdata(ray_dir_path + compare2)

# normalize 
obs_flux = normalize_flux(spectra[0], spectra[1])
ray1_flux = normalize_flux(ray1[0], ray1[1])
ray2_flux = normalize_flux(ray2[0], ray2[1])

# apply offset
offset = 2.
ray1_flux += offset
ray2_flux -= offset


# mask arrays
mask_obs_wave, mask_obs_flux = mask_wave_flux(spectra[0], obs_flux)
mask_ray1_wave, mask_ray1_flux = mask_wave_flux(ray1[0], ray1_flux)
mask_ray2_wave, mask_ray2_flux = mask_wave_flux(ray2[0], ray2_flux)

def plot_stacked_offset():
    # plot
    plt.clf()
    fig, ax = plt.subplots()
    fig.subplots_adjust(left=0.125)
    plot_telluric_lines()
    
    plt.plot(mask_obs_wave, mask_obs_flux+offset, 'black', label='Observed')
    #plt.plot(ray1[0], ray1_flux, 'r', label=compare1[:3])
    plt.plot(mask_ray1_wave, mask_ray1_flux, 'r', label=compare1[:3]+' (R09)')

    plt.plot(mask_obs_wave, mask_obs_flux-offset, 'black', label='')
    #plt.plot(ray2[0], ray2_flux, 'b', label=compare2[:3])
    plt.plot(mask_ray2_wave, mask_ray2_flux, 'b', label=compare2[:3]+' (R09)')

    plt.title(multi_obj)
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu m) + $ constant')
    plt.xlabel('Wavelength $\mu$m')
    
    plt.xlim(0.7,2.55)
    plt.grid(True)
    plt.legend()

    plt.savefig(multi_obj+'_stacked_offset.png')

plot_stacked_offset()






def plot_offset():
    # plot
    plt.clf()
    fig, ax = plt.subplots()
    fig.subplots_adjust(left=0.125)
    plot_telluric_lines()

    plt.plot(mask_obs_wave, mask_obs_flux, 'black', label='Observed')
    #plt.plot(ray1[0], ray1_flux, 'r', label=compare1[:3])
    #plt.plot(ray2[0], ray2_flux, 'b', label=compare2[:3])
    plt.plot(mask_ray1_wave, mask_ray1_flux, 'r', label=compare1[:3]+' (R09)')
    plt.plot(mask_ray2_wave, mask_ray2_flux, 'b', label=compare2[:3]+' (R09)')

    plt.legend()
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu m) + $ constant')
    plt.title(multi_obj)
    plt.xlabel('Wavelength $\mu$m')

    plt.xlim(0.7,2.55)
    plt.grid(True)

    #plt.show()
    plt.savefig(multi_obj+'_offset.png')

#plot_offset()

