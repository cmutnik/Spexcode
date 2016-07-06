# script to compare observed spectra to rayners spectra and take difference
# ___ stars
# Corey Mutnik - 2/4/16

import pysynphot
from pysynphot import spectrum, observation
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec


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

def observed_rayner_difference():
    plt.clf()
    plt.figure(1)
    gs = gridspec.GridSpec(3,1)
    # Overlapping Plots
    #ax1 = plt.subplot(211)
    ax1 = plt.subplot(gs[:,:])
    ax1 = plt.subplot(gs[:2, :])
    #ax1.set_xlim([0.7, 2.55]) # wavelength range of Spex
    ax1.set_xlim([np.min(spectra[0]),np.max(spectra[0])])
    ax1.set_ylim([0,9])
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
    plt.savefig(starclass+seqnum+'difference_observed_standard.png')


###
# Use Functions Above To Execute Code Below
###

VALUES = [['F0V', 'HD 137130', 'F0V(n)_HD108519_rayner.fits', 'HD 108519 (F0V(n))', '_'], ['F1V', 'HIP 79369', 'F1V_HD213135_rayner.fits', 'HD 213135', '_'], ['F3V', 'HIP 82319', 'F3V_HD26015_rayner.fits', 'HD 26015', '_1of2_'], ['F3V', 'HD 146743', 'F3V_HD26015_rayner.fits', 'HD 26015', '_2of2_'], ['F5V', 'HD 148153', 'F5V_HD27524_rayner.fits', 'HD 27524', '_1of2_'], ['F5V', 'HD 148153', 'F5V_HD218804_rayner.fits', 'HD 218804', '_2of2_'], ['F7V', 'HIP 78977', 'F7V_HD126660_rayner.fits', 'HD 126660', '_'], ['F8V', 'HIP 71982', 'F8V_HD27383_rayner.fits', 'HD 27383', '_1of4_'], ['F8V', 'HIP 71982', 'F8V_HD219623_rayner.fits', 'HD 219623', '_2of4_'], ['F8V', 'HD 142113', 'F8V_HD27383_rayner.fits', 'HD 27383', '_3of4_'], ['F8V', 'HD 142113', 'F8V_HD219623_rayner.fits', 'HD 219623', '_4of4_'], ['G0V', 'HIP 61412', 'G0V_HD109358_rayner.fits', 'HD 109358', '_1of2_'], ['G0V', 'HD 148040', 'G0V_HD109358_rayner.fits', 'HD 109358', '_2of2_'], ['G2V', 'HD 133748', 'G2V_HD76151_rayner.fits', 'HD 76151', '_'], ['G4V', 'GSC 06793-00994', 'G4V_HD214850_rayner.fits', 'HD 214850', '_'], ['G5V', 'HBC 649', 'G5V_HD165185_rayner.fits', 'HD 165185', '_'], ['G7V', 'GSC 06793-01406', 'G7IV_HD20618_rayner.fits', 'HD 20618 (G7IV)', '_1of3_'], ['G7V', 'GSC 06793-01406', 'G7IV_HD114946_rayner.fits', 'HD 114946 (G7IV)', '_2of3_'], ['G7V', 'GSC 06793-01406', 'G8V_HD75732_rayner.fits', 'HD 75732 (G8V)', '_3of3_'], ['G9V', 'GSC 06213-00306AB', 'G9III_HD222093_rayner.fits', 'HD 222093 (G9III)', '_'], ['K0V', 'CD-25 11942', 'K0V_HD145675_rayner.fits', 'HD 145675', '_1of8_'], ['K0V', 'ScoPMS 214', 'K0V_HD145675_rayner.fits', 'HD 145675', '_2of8_'], ['K0V', 'ScoPMS 214', 'K2III_HD137759_rayner.fits', 'HD 137759 (K2III)', '_3of8_'], ['K0V', 'ScoPMS 214', 'K2IIIFe-1_HD2901_rayner.fits', 'HD 2901 (K2IIIFe-1)', '_4of8_'], ['K0V', 'HD 141813', 'K0V_HD145675_rayner.fits', 'HD 145675', '_5of8_'], ['K0V', 'HD 141813', 'K1IIIFe-0.5_HD36134_rayner.fits', 'HD 36134 (K1IIIFe-0.5)', '_6of8_'], ['K0V', 'HD 141813', 'K1III_HD25975_rayner.fits', 'HD 25975 (K1III)', '_7of8_'], ['K0V', 'HD 141813', 'K1IIIbCN1.5Ca1_HD91810_rayner.fits', 'HD 91810 (K1IIIbCN1.5Ca1)', '_8of8_'], ['K0III', 'HD 14311', 'K0III_HD100006_rayner.fits', 'HD 100006', '_'], ['K2V', 'ScoPMS 44', 'K2V_HD3765_rayner.fits', 'HD 3765', '_1of2_'], ['K2V', 'ScoPMS 44', 'K2III_HD137759_rayner.fits', 'HD 137759 (K2III)', '_2of2_'], ['K4V', 'GSC 06793-00797', 'K4V_HD45977_rayner.fits', 'HD 45977', '_'], ['K5V', 'ScoPMS 45', 'K5V_HD36003_rayner.fits', 'HD 36003', '_'], ['K6V', 'GSC 06208-00834', 'K6IIIa_HD3346_rayner.fits', 'HD 3346 (K6IIIa)', '_1of2_'], ['K6V', 'GSC 06208-00834', 'K7V_HD237903_rayner.fits', 'HD 237903 (K7V)', '_2of2_'], ['K9V', 'Sco 160900.7-19085', 'K7V_HD237903_rayner.fits', 'HD 237903 (K7V)', '_'], ['K0IV', 'GSC 06801-00186', 'K0III_HD100006_rayner.fits', 'HD 100006 (K0III)', '_1of4_'], ['K0IV', 'GSC 06801-00186', 'K0V_HD145675_rayner.fits', 'HD 145675 (K0V)', '_2of4_'], ['K0IV', 'GSC 06801-00186 (oldSpx)', 'K0III_HD100006_rayner.fits', 'HD 100006 (K0III)', '_3of4_'], ['K0IV', 'GSC 06801-00186 (oldSpx)', 'K0V_HD145675_rayner.fits', 'HD 145675 (K0V)', '_4of4_'], ['M0V', 'GSC 06213-00194', 'M0V_HD19305_rayner.fits', 'HD 19305', '_'], ['M1V', 'RXJ 1602.0-2221', 'M1V_HD42581_rayner.fits', 'HD 42581', '_'], ['M2.5V', 'ScoPMS 008b', 'M2.5V_Gl381_rayner.fits', 'Gl 381', '_1of2_'], ['M2.5V', 'ScoPMS 008b', 'M2.5V_Gl581_rayner.fits', 'Gl 581', '_2of2_'], ['M4V', 'ScoPMS 46', 'M4V_Gl213_rayner.fits', 'Gl 213', '_1of2_'], ['M4V', 'ScoPMS 46', 'M4V_Gl299_rayner.fits', 'Gl 299', '_2of2_'], ['SC5.5-C71e', 'HIP 78721', 'SC5.5Zr0.5_HD44544_rayner.fits', 'HD 44544 (SC5.5Zr0.5)', '_']] 


# generate_all_plots
for i in range(len(VALUES)):
    starclass = VALUES[i][0]
    obs_name = VALUES[i][1]
    standard_file = VALUES[i][2]
    stand_name = VALUES[i][3]
    seqnum = VALUES[i][4]
    observed = u'/Users/cmutnik/work/astro/finished_with_fixed_names/' + obs_name + '.fits'
    spectra = fits.getdata(observed)    
    standard_dir = u'/Users/cmutnik/work/astro/plots/compare/obs_vs_IRTF/IRTF_fits/' + standard_file
    rayner_data = fits.getdata(standard_dir)
    rayner_wave = rayner_data[0]
    rayner_flux = rayner_data[1]    
    rebinned_raywave = rebin_spec(rayner_wave, rayner_flux, spectra[0]).binwave
    rebinned_rayflux = rebin_spec(rayner_wave, rayner_flux, spectra[0]).binflux 
    norm_obs_flux = normalize_flux(wave_array=spectra[0], flux_array=spectra[1])
    norm_ray_flux = normalize_flux(rebinned_raywave,rebinned_rayflux)  
    flux_difference = norm_obs_flux - norm_ray_flux 
    observed_rayner_difference()



