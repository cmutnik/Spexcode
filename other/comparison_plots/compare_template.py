# script to compare observed spectra to rayners spectra and take difference
# ___ stars
# Corey Mutnik - 2/4/16

import pysynphot
from pysynphot import spectrum, observation
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec


###
# Modify this section of template, for each spectral class
###

###
# Modify this section of template, for each spectral class
###
starclass = 'F5V'
obs_name = 'HD 148153'
standard_file = 'F5V_HD27524_rayner.fits'
stand_name = 'HD 27524'
seqnum = '_1of2_'

###
#----------------------------------------------------------
###



def rebin_spec(wave, specin, wavenew):
    '''Rebin data for direct comparison'''
    spec = spectrum.ArraySourceSpectrum(wave=wave, flux = specin)
    f = np.ones(len(wave)) # returns array of ones with size given
    filt = spectrum.ArraySpectralElement(wave, f, waveunits='angstrom')
    obs = observation.Observation(spec, filt, binset=wavenew, force='taper')
    return obs

def normalize_flux(wave_array, flux_array):
    micron_value = np.where(abs(wave_array - 2.20) == min(abs(wave_array - 2.20)))[0][0]
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


'''
list1 = [1,2,3,4]
list2 = [4,3,2,1]
somecondition = True
plt.figure(1) #create one of the figures that must appear with the chart

gs = gridspec.GridSpec(3,1)

if not somecondition:
    ax = plt.subplot(gs[:,:]) #create the first subplot that will ALWAYS be there
    ax.plot(list1) #populate the "main" subplot
else:
    ax = plt.subplot(gs[:2, :])
    ax.plot(list1)
    ax = plt.subplot(gs[2, :]) #create the second subplot, that MIGHT be there
    ax.plot(list2) #populate the second subplot
plt.show()
'''


def observed_rayner_difference(fn= starclass+seqnum+'difference_observed_standard.png'):
    plt.clf()
    plt.figure(1)
    gs = gridspec.GridSpec(3,1)
    # Overlapping Plots
    #ax1 = plt.subplot(211)
    ax1 = plt.subplot(gs[:,:])
    ax1 = plt.subplot(gs[:2, :])
    #ax1.set_xlim([0.7, 2.55]) # wavelength range of Spex
    ax1.set_xlim([np.min(spectra[0]),np.max(spectra[0])])
    ax1.set_title(starclass)

    # observed star in green: obs_star = 'GSC 06793-00994'
    obs_legend = obs_name + ' (Yng)'
    std_legend = stand_name + ' (R09)'

    plt.plot(spectra[0], norm_obs_flux, lw=0.5, color='green', label=obs_legend)
    plt.plot(rebinned_raywave, norm_ray_flux, lw=0.5, color='blue', label=std_legend)
    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda (2.2\mu m)$')
    plt.setp( ax1.get_xticklabels(), visible=False) 

    # Difference Subplot
    #ax2 = plt.subplot(212, sharex=ax1) # share x axis
    ax2 = plt.subplot(gs[2, :])
    #ax2.set_xlim([0.7, 2.55]) # wavelength range of Spex
    ax2.set_xlim([np.min(spectra[0]),np.max(spectra[0])])
    ax2.set_ylim([-1,1])
    plt.plot(spectra[0], flux_difference, color='red', label='Difference')
    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('Observed - Standard')
    #plt.ylim(0.1, 1.7)
    #plt.xlim(0.7, 2.55)
    # make these tick labels invisible
    plt.setp( ax2.get_xticklabels(), visible=True)  
    plt.grid(False)
    #plt.show()
    plt.savefig(fn)


###
# Use Functions Above To Execute Code Below
###

observed = u'/Users/cmutnik/work/astro/finished_with_fixed_names/' + obs_name + '.fits'
# open observed data
spectra = fits.getdata(observed)

standard_dir = u'/Users/cmutnik/work/astro/plots/compare/obs_vs_IRTF/IRTF_fits/' + standard_file
rayner_data = fits.getdata(standard_dir)
# open rayner star data from IRTF Spectral Library
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



