# program to plotl spectrum of F8V star with models
# corey Mutnik - 7/24/15

import pysynphot
from pysynphot import observation
from pysynphot import spectrum
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from glob import glob
import os

dir_path = u'/net/calla.ifa.hawaii.edu/Volumes/indicium/u/cmutnik/work/upperSco_copy/F8V'
globpath = os.path.join(dir_path, '*.fits')
filelist = glob(globpath)
filelist.sort()

spectra = fits.getdata('HIP_71982_6_29_15_II_merge.fits')

# Teff = 6250
model_spec = pysynphot.Icat('phoenix_v16', Teff = 6250, log_g = 4.4, metallicity = 0.0)
model_wave = model_spec.wave
model_flux = model_spec.flux



def ang_to_micron(wavelength_array):
    return wavelength_array * 1.0e-4
model_wave_microns = ang_to_micron(model_wave)



def rebin_spec(wave, specin, wavenew):
    spec = spectrum.ArraySourceSpectrum(wave=wave, flux = specin)
    f = np.ones(len(wave)) # returns array of ones with size given
    filt = spectrum.ArraySpectralElement(wave, f, waveunits='angstrom')
    obs = observation.Observation(spec, filt, binset=wavenew, force='taper')
    return obs
rebinned_wave = rebin_spec(model_wave_microns, model_flux, spectra[0]).binwave
rebinned_flux = rebin_spec(model_wave_microns, model_flux, spectra[0]).binflux


def normalize_flux(wave_array, flux_array):
    micron_value = np.where(abs(wave_array - 1.10) == min(abs(wave_array - 1.10)))[0][0]
    norm_den = (float)((wave_array[micron_value] * flux_array[micron_value])**(-1))
    norm_flux = []
    for i in range(0, len(wave_array)):
        norm_flux.append(wave_array[i] * flux_array[i] * norm_den)
    return norm_flux
norm_obs_flux = normalize_flux(spectra[0], spectra[1])
norm_model_flux = normalize_flux(rebinned_wave, rebinned_flux)


shift_model_flux = []
for j in range(0, len(norm_model_flux)):
    shift_model_flux.append(norm_model_flux[j] + 1.0)



# First figure - observed star with synthetics
x_pos = 1.8
#plt.figure(1)
#plt.subplot(121)
#plt.plot(spectra[0], norm_obs_flux, 'r', rebinned_wave, shift_model_flux, 'g-')
plt.plot(spectra[0], norm_obs_flux, 'r', rebinned_wave, norm_model_flux, 'g-')
plt.xlabel('microns')
plt.ylabel('normalized (1.10) + constant')
plt.title('F8V in red plotted with synthetic') 
plt.ylim(0, 2)
plt.xlim(0.58, 2.6)
plt.grid(True)
plt.text(x_pos, 0.5, 'HIP 71982 in red')
plt.text(x_pos, 1.5, 'Model: Teff=6250, logg=4.4 in green')
plt.show()
#plt.savefig('F8V_phoenix.pdf')



# second figure - observed star with rayers stars
'''
for j in range(0, len(filelist)):
    spec = fits.getdata(filelist[j])
    norm_flux = normalize_flux(spec[0], spec[1])
    norm_flux_shift = []
    for i in range(0, len(norm_flux)):
        norm_flux_shift.append(norm_flux[i] + j)
    file_name = os.path.basename(filelist[j])
    y_pos = 0.5 + j
   
    plt.subplot(122)
    plt.plot(spec[0], norm_flux_shift)
    plt.text(x_pos, y_pos, file_name)
    plt.xlim(0.58, 2.6)
    plt.title('F8V in red')

#plt.savefig('F8V_phoenix.pdf')
plt.show()
'''
