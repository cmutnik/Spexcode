# script to compare observed spectra to rayners spectra and take difference
# G4V stars
# Corey Mutnik - 2/4/16

import pysynphot
from pysynphot import spectrum, observation
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def rebin_spec(wave, specin, wavenew):
    '''Rebin data for direct comparison'''
    spec = spectrum.ArraySourceSpectrum(wave=wave, flux = specin)
    f = np.ones(len(wave)) # returns array of ones with size given
    filt = spectrum.ArraySpectralElement(wave, f, waveunits='angstrom')
    obs = observation.Observation(spec, filt, binset=wavenew, force='taper')
    return obs

def normalize_flux(wave_array, flux_array):
    micron_value = np.where(abs(wave_array - 1.10) == min(abs(wave_array - 1.10)))[0][0]
    norm_den = (float)((wave_array[micron_value] * flux_array[micron_value])**(-1))
    norm_flux = []
    for i in range(0, len(wave_array)):
        norm_flux.append(wave_array[i] * flux_array[i] * norm_den)
    return np.array(norm_flux)

# Plotting Functions
def plot_telluric_lines():
    '''Regions of high telluric absorption are maked in plots using gray bands of varying darkness'''
    # Filling light gray
    plt.axvspan(0.92, 0.95, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.11, 1.16, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.415, 1.49, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.91, 2.05, facecolor='gray', alpha=0.25, lw=0)
    # fill dark gray
    plt.axvspan(1.35, 1.415, facecolor='gray', alpha=0.5, lw=0)
    plt.axvspan(1.8, 1.91, facecolor='gray', alpha=0.5, lw=0)

def observed_rayner_difference(fn='G4V_observed_Rayner.png'):
    plt.clf()
    plt.figure(1)
    # Overlapping Plots
    ax1 = plt.subplot(211)
    ax1.set_xlim([0.7, 2.55]) # wavelength range of Spex
    ax1.set_title('G4V Stars')
    plt.plot(spectra[0], norm_obs_flux, lw=0.5, color='green')
    plt.plot(rebinned_raywave, norm_ray_flux, lw=0.5, color='blue')
    plot_telluric_lines()
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda (1.1\mu m)$')
    plt.text(2.20, 0.52, 'Observed',color='green', fontsize=15)# observed stars green:obs_star='GSC 06793-00994'
    plt.text(2.20, 0.12, 'Rayner',color='blue', fontsize=15)# Rayner's star in blue: Ray_star = 'HD 214850'
    plt.setp( ax1.get_xticklabels(), visible=False) 

    # Difference Subplot
    ax2 = plt.subplot(212, sharex=ax1) # share x axis
    ax2.set_xlim([0.7, 2.55]) # wavelength range of Spex
    plt.plot(spectra[0], flux_difference, color='red')
    plt.text(2.20, 0.22, 'Difference',color='red', fontsize=15)
    plot_telluric_lines()
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda (1.1\mu m)$')
    plt.setp( ax2.get_xticklabels(), visible=True)  
    plt.grid(False)
    #plt.show()
    plt.savefig(fn)


###
# Use Functions Above To Execute Code Below
###

# open observed data
observed = u'/Users/cmutnik/work/astro/finished_with_fixed_names/GSC 06793-00994.fits'
spectra = fits.getdata(observed)

# open rayner G4V star data from IRTF Spectral Library
rayner_data = fits.getdata('G4V_HD214850_Rayner.fits')
rayner_wave = rayner_data[0]
rayner_flux = rayner_data[1]


# Must Rebin data since: len(norm_flux) != len(raynorm_flux)
rebinned_raywave = rebin_spec(rayner_wave, rayner_flux, spectra[0]).binwave
rebinned_rayflux = rebin_spec(rayner_wave, rayner_flux, spectra[0]).binflux


# normalize data
norm_obs_flux = normalize_flux(wave_array=spectra[0], flux_array=spectra[1])
norm_ray_flux = normalize_flux(rebinned_raywave,rebinned_rayflux)
print '\n', len(norm_ray_flux) == len(norm_obs_flux)


# Calculate difference between observed and rayner stars
flux_difference = norm_obs_flux - norm_ray_flux


# Call plotting function
observed_rayner_difference()
#share_xaxis_method()


