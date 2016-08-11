# Python script to analyze spectral features of Yng and Old stars
# Corey Mutnik 160725
# Modified to include all 6 cool star features: 160804

###
# General procedure
###
# open data
# mask out regions
# rebin
# normalize
# remove portions that are throwing off fit
# get coeffs
# fit polynomial
# divide spectra by poly

from pysynphot import spectrum, observation
import numpy.polynomial.polynomial as poly
import matplotlib.gridspec as gridspec
from astropy.io import fits, ascii
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np
import pysynphot
import pdb #py debugger


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


def plot_telluric_lines():
    '''Regions of high telluric absorption are maked in plots using gray bands of varying darkness'''
    # Filling light gray
    plt.axvspan(0.92, 0.95, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.11, 1.16, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.415, 1.49, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.91, 2.05, facecolor='gray', alpha=0.25, lw=0)
    # fill dark gray
    plt.axvspan(1.35, 1.415, facecolor='gray', alpha=0.5, lw=0)
    plt.axvspan(1.8, 1.91, facecolor='gray', alpha=0.5, lw=0)   # polynomial fit
    plt.axvspan(2.50, 2.88, facecolor='gray', alpha=0.5, lw=0)


def eval_poly(x, a,b,c,d,e):
    return (a + b*x + c*x**2 + d*x**3 + e*x**4)


def observed_poly_fit_quotient():
    plt.clf()
    #plt.figure(1)
    gs = gridspec.GridSpec(3,1)
    # Overlapping Plots
    #ax1 = plt.subplot(211)
    ax1 = plt.subplot(gs[:,:])
    ax1 = plt.subplot(gs[:2, :])
    #ax1.set_xlim([0.7, 2.55]) # wavelength range of Spex
    ax1.set_xlim([np.min(wave_obs),np.max(wave_obs)])
    ax1.set_title('observed ' + starclass +' with polynomial overlay')

    # observed star in green: obs_star = 'GSC 06793-00994'
    obs_legend = obs_name + ' (Yng)'
    polyorder = 'Fit order: ' + str(polydeg)

    plt.plot(wave_mask_obs, norm_obs_flux, lw=0.5, color='green', label=obs_legend)
    plt.plot(wave_mask_obs, poly_obs, lw=1, color='red',label=polyorder)
    #std_legend = stand_name + ' (R09)'
    #plt.plot(rebinned_raywave, norm_ray_flux, lw=0.5, color='blue', label=std_legend)
    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    #plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda (1.1\mu m)$')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m)')
    plt.setp( ax1.get_xticklabels(), visible=False) 

    # Ratio Subplot
    #ax2 = plt.subplot(212, sharex=ax1) # share x axis
    ax2 = plt.subplot(gs[2, :])
    #ax2.set_xlim([0.7, 2.55]) # wavelength range of Spex
    ax2.set_xlim([np.min(wave_obs),np.max(wave_obs)])
    ax2.set_ylim([-0.5,2])
 
    plt.plot(wave_mask_obs, divide_obs, color='orange', label='Ratio')
    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('Observed / Fit ')

    # make these tick labels invisible
    plt.setp( ax2.get_xticklabels(), visible=True)  
    plt.grid(False)
    plt.savefig('figs/polyfitted/yng/'+starclass+seqnum+'observed_polyfit.png')


def rayner_poly_fit_quotient():
    plt.clf()
    #plt.figure(1)
    gs = gridspec.GridSpec(3,1)
    # Overlapping Plots
    ax1 = plt.subplot(gs[:,:])
    ax1 = plt.subplot(gs[:2, :])
    ax1.set_xlim([np.min(wave_irtf_bin),np.max(wave_irtf_bin)])
    ax1.set_title(starclass +' standard (' + stand_name + ')with polynomial overlay')
    # observed star in green: obs_star = 'GSC 06793-00994'
    std_legend = stand_name + ' (Old)'
    polyorder = 'Fit order: ' + str(polydeg)

    plt.plot(wave_irtf_bin, norm_irtf_flux, lw=0.5, color='blue', label=std_legend)
    plt.plot(wave_irtf_bin, poly_irtf, lw=1, color='red',label=polyorder)

    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    #plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda (1.1\mu m)$')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m)')
    plt.setp( ax1.get_xticklabels(), visible=False) #   

    # Quotient Subplot
    ax2 = plt.subplot(gs[2, :])
    #ax2.set_xlim([0.7, 2.55]) # wavelength range of Spex
    ax2.set_xlim([np.min(wave_irtf_bin),np.max(wave_irtf_bin)])
    ax2.set_ylim([-0.5,2])
    plt.plot(wave_irtf_bin, divide_irtf, color='orange', label='Ratio') 
    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('R09 / Fit ')#   
    # make these tick labels invisible
    plt.setp( ax2.get_xticklabels(), visible=True)  
    plt.grid(False)
    plt.savefig('figs/polyfitted/old/'+starclass+seqnum+'rayner_polyfit.png')


def Yng_Old_overlay():
    plt.clf()
    #plt.figure(1)
    fig = plt.figure()
    fig.subplots_adjust(left=0.125)
    gs = gridspec.GridSpec(3,1)
    # Overlapping Plots
    #ax1 = plt.subplot(211)
    ax1 = plt.subplot(gs[:,:])
    ax1 = plt.subplot(gs[:2, :])
    ax1.set_xlim([0.7, 2.55]) # wavelength range of Spex
    #ax1.set_xlim([np.min(wave_obs),np.max(wave_obs)])
    ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
    ax1.set_title(starclass)

    # observed star in green: obs_star = 'GSC 06793-00994'
    obs_legend = obs_name + ' (Yng)'
    std_legend = stand_name + ' (Old)'

    plt.plot(wave_irtf_bin, norm_irtf_flux, lw=0.5, color='black', label=std_legend)
    plt.plot(wave_mask_obs, norm_obs_flux, lw=0.5, color='red', label=obs_legend)

    #std_legend = stand_name + ' (R09)'
    #plt.plot(rebinned_raywave, norm_ray_flux, lw=0.5, color='blue', label=std_legend)
    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    #plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda (1.1\mu m)$')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m)')
    plt.setp( ax1.get_xticklabels(), visible=False) 

    # Ratio Subplot
    #ax2 = plt.subplot(212, sharex=ax1) # share x axis
    ax2 = plt.subplot(gs[2, :])
    ax2.set_xlim([0.7, 2.55]) # wavelength range of Spex
    #ax2.set_xlim([np.min(wave_obs),np.max(wave_obs)])
    ax2.set_ylim([0.5,1.5])
    #ax2.set_ylim([0,2])

    ax2.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
 
    plt.plot(wave_mask_obs, divide_obs, color='black', label='Ratio')
    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('Yng / Old')

    # make these tick labels invisible
    plt.setp( ax2.get_xticklabels(), visible=True)  
    plt.grid(False)
    plt.savefig('figs/ratio/'+starclass+seqnum+'observed_polyfit.png')
    #plt.show()


def plot_Na_I_2tac2_feat():
    obs_legend = obs_name + ' (Yng V)'
    std_legend = stand_name + ' (Old '+ old_spttype +')'
    plt.clf()
    gs = gridspec.GridSpec(3,1)
    # Overlapping Plots
    ax1 = plt.subplot(gs[:,:])
    ax1 = plt.subplot(gs[:2, :])

    #ax1.set_title('Continuum Removed: Na I')
    ax1.set_title(starclass[:-1]+': Na I (2.206$\mu$m)')

    plt.plot(wave_irtf_bin, divide_irtf, color='black', label=std_legend)
    plt.plot(wave_mask_obs, divide_obs, color='red', label=obs_legend)

    plot_telluric_lines()
    plt.axvline(x=2.206, color='b')

    #lowery,uppery = np.mean(divide_obs, axis=0)-0.4, np.mean(divide_obs, axis=0)+0.4
    lowery,uppery = np.min(divide_obs)*0.9, np.max(divide_obs)*1.1
    ax1.set_ylim([lowery,uppery])

    #ax1.set_xlim([np.min(wave_obs),np.max(wave_obs)])
    ax1.set_xlim([2.185,2.230])
    #ax1.set_xlim([2.204,2.211])

    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    #plt.ylabel('Continuum Removed Spectra')
    #plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m) + constant')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m)')
    plt.setp( ax1.get_xticklabels(), visible=False) #

    # Quotient Subplot
    ax2 = plt.subplot(gs[2, :])
    #ax2.set_xlim([0.7, 2.55]) # wavelength range of Spex
    #ax2.set_xlim([np.min(wave_irtf_bin),np.max(wave_irtf_bin)])
    #ax2.set_ylim([-0.5,2])
    ax2.plot(wave_mask_obs,continuum_removed, label='Ratio', color='k')
    ax2.set_xlim([2.185,2.230])
    #ax2.set_xlim([2.204,2.211])
    
    # Set y-limits of Ratio plot
    #ax2.set_ylim([-.25,.25])
    
    plt.axvline(x=2.206, color='b')

    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('Yng / Old ')#   
    # make these tick labels invisible
    plt.setp( ax2.get_xticklabels(), visible=True)  
    plt.grid(False)
    plt.savefig('figs/NaI_2tac2_160808/'+starclass+seqnum+'testNaI.png')
def plot_Ca_II_feat():
    # Ca II (0.866 \mum)
    obs_legend = obs_name + ' (Yng V)'
    std_legend = stand_name + ' (Old '+ old_spttype +')'
    plt.clf()
    gs = gridspec.GridSpec(3,1)
    # Overlapping Plots
    ax1 = plt.subplot(gs[:,:])
    ax1 = plt.subplot(gs[:2, :])

    #ax1.set_title('Continuum Removed: Na I')
    ax1.set_title(starclass[:-1]+': Ca II (0.866$\mu$m)')

    plt.plot(wave_irtf_bin, divide_irtf, color='black', label=std_legend)
    plt.plot(wave_mask_obs, divide_obs, color='red', label=obs_legend)

    plot_telluric_lines()
    plt.axvline(x=0.866, color='b')

    # Set ylimits all plots this way
    #lowery,uppery = np.mean(divide_obs, axis=0)-0.4, np.mean(divide_obs, axis=0)+0.4
    lowery,uppery = np.min(divide_obs)*0.9, np.max(divide_obs)*1.1
    ax1.set_ylim([lowery,uppery])
    
    #ax1.set_xlim([np.min(wave_obs),np.max(wave_obs)])
    ax1.set_xlim([0.860, 0.875])

    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    #plt.ylabel('Continuum Removed Spectra')
    #plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m) + constant')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m)')
    plt.setp( ax1.get_xticklabels(), visible=False) #

    # Quotient Subplot
    ax2 = plt.subplot(gs[2, :])
    #ax2.set_xlim([0.7, 2.55]) # wavelength range of Spex
    #ax2.set_xlim([np.min(wave_irtf_bin),np.max(wave_irtf_bin)])
    #ax2.set_ylim([-0.5,2])
    ax2.plot(wave_mask_obs,continuum_removed, label='Ratio', color='k')
    ax2.set_xlim([0.860, 0.875])
    #ax2.set_xlim([2.204,2.211])
    
    # Set y-limits of Ratio plot
    #ax2.set_ylim([-.25,.25])
    
    plt.axvline(x=0.866, color='b')

    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('Yng / Old ')#   
    # make these tick labels invisible
    plt.setp( ax2.get_xticklabels(), visible=True)  
    plt.grid(False)
    plt.savefig('figs/CaII_160808/'+starclass+seqnum+'_CaII.png')
def plot_Mg_I_1tac7_feat():
    # Mg i (1.711 \mum)

    obs_legend = obs_name + ' (Yng V)'
    std_legend = stand_name + ' (Old '+ old_spttype +')'
    plt.clf()
    gs = gridspec.GridSpec(3,1)
    # Overlapping Plots
    ax1 = plt.subplot(gs[:,:])
    ax1 = plt.subplot(gs[:2, :])

    #ax1.set_title('Continuum Removed: Na I')
    ax1.set_title(starclass[:-1]+': Mg I (1.711$\mu$m)')

    plt.plot(wave_irtf_bin, divide_irtf, color='black', label=std_legend)
    plt.plot(wave_mask_obs, divide_obs, color='red', label=obs_legend)

    plot_telluric_lines()
    plt.axvline(x=1.711, color='b')

    #lowery,uppery = np.mean(divide_obs, axis=0)-0.4, np.mean(divide_obs, axis=0)+0.4
    lowery,uppery = np.min(divide_obs)*0.9, np.max(divide_obs)*1.1
    ax1.set_ylim([lowery,uppery])

    #ax1.set_xlim([np.min(wave_obs),np.max(wave_obs)])
    ax1.set_xlim([1.695, 1.726])
    #ax1.set_xlim([2.204,2.211])

    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    #plt.ylabel('Continuum Removed Spectra')
    #plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m) + constant')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m)')
    plt.setp( ax1.get_xticklabels(), visible=False) #

    # Quotient Subplot
    ax2 = plt.subplot(gs[2, :])
    #ax2.set_xlim([0.7, 2.55]) # wavelength range of Spex
    #ax2.set_xlim([np.min(wave_irtf_bin),np.max(wave_irtf_bin)])
    #ax2.set_ylim([-0.5,2])
    ax2.plot(wave_mask_obs,continuum_removed, label='Ratio', color='k')
    ax2.set_xlim([1.695, 1.726])
    #ax2.set_xlim([2.204,2.211])
    
    # Set y-limits of Ratio plot
    #ax2.set_ylim([-.25,.25])
    
    plt.axvline(x=1.711, color='b')

    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('Yng / Old ')#   
    # make these tick labels invisible
    plt.setp( ax2.get_xticklabels(), visible=True)  
    plt.grid(False)
    plt.savefig('figs/MgI_1tac7_160808/'+starclass+seqnum+'_MgI_1tac7.png')
def plot_Mg_I_1tac5_feat():
    # Mg I (1.485 \mum)
    obs_legend = obs_name + ' (Yng V)'
    std_legend = stand_name + ' (Old '+ old_spttype +')'
    plt.clf()
    gs = gridspec.GridSpec(3,1)
    # Overlapping Plots
    ax1 = plt.subplot(gs[:,:])
    ax1 = plt.subplot(gs[:2, :])

    #ax1.set_title('Continuum Removed: Na I')
    ax1.set_title(starclass[:-1]+': Mg I (1.485$\mu$m)')

    plt.plot(wave_irtf_bin, divide_irtf, color='black', label=std_legend)
    plt.plot(wave_mask_obs, divide_obs, color='red', label=obs_legend)

    plot_telluric_lines()
    plt.axvline(x=1.485, color='b')

    #lowery,uppery = np.mean(divide_obs, axis=0)-0.4, np.mean(divide_obs, axis=0)+0.4
    lowery,uppery = np.min(divide_obs)*0.9, np.max(divide_obs)*1.1
    ax1.set_ylim([lowery,uppery])

    #ax1.set_xlim([np.min(wave_obs),np.max(wave_obs)])
    ax1.set_xlim([1.475, 1.4975])
    #ax1.set_xlim([2.204,2.211])

    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    #plt.ylabel('Continuum Removed Spectra')
    #plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m) + constant')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m)')
    plt.setp( ax1.get_xticklabels(), visible=False) #

    # Quotient Subplot
    ax2 = plt.subplot(gs[2, :])
    #ax2.set_xlim([0.7, 2.55]) # wavelength range of Spex
    #ax2.set_xlim([np.min(wave_irtf_bin),np.max(wave_irtf_bin)])
    #ax2.set_ylim([-0.5,2])
    ax2.plot(wave_mask_obs,continuum_removed, label='Ratio', color='k')
    ax2.set_xlim([1.475, 1.4975])
    #ax2.set_xlim([2.204,2.211])
    
    # Set y-limits of Ratio plot
    #ax2.set_ylim([-.25,.25])
    
    plt.axvline(x=1.485, color='b')

    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('Yng / Old ')#   
    # make these tick labels invisible
    plt.setp( ax2.get_xticklabels(), visible=True)  
    plt.grid(False)
    plt.savefig('figs/MgI_1tac5_160808/'+starclass+seqnum+'_MgI_1tac5.png')
def plot_Al_I_feat():
    # Al i (1.313 \mum)
    obs_legend = obs_name + ' (Yng)'
    std_legend = stand_name + ' (Old '+ old_spttype +')'
    plt.clf()
    gs = gridspec.GridSpec(3,1)
    # Overlapping Plots
    ax1 = plt.subplot(gs[:,:])
    ax1 = plt.subplot(gs[:2, :])

    #ax1.set_title('Continuum Removed: Na I')
    ax1.set_title(starclass[:-1]+': Al I (1.313$\mu$m)')

    plt.plot(wave_irtf_bin, divide_irtf, color='black', label=std_legend)
    plt.plot(wave_mask_obs, divide_obs, color='red', label=obs_legend)

    plot_telluric_lines()
    plt.axvline(x=1.313, color='b')

    #lowery,uppery = np.mean(divide_obs, axis=0)-0.4, np.mean(divide_obs, axis=0)+0.4
    lowery,uppery = np.min(divide_obs)*0.9, np.max(divide_obs)*1.1
    ax1.set_ylim([lowery,uppery])

    #ax1.set_xlim([np.min(wave_obs),np.max(wave_obs)])
    ax1.set_xlim([1.300,1.330])
    #ax1.set_xlim([2.204,2.211])

    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    #plt.ylabel('Continuum Removed Spectra')
    #plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m) + constant')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m)')
    plt.setp( ax1.get_xticklabels(), visible=False) #

    # Quotient Subplot
    ax2 = plt.subplot(gs[2, :])
    #ax2.set_xlim([0.7, 2.55]) # wavelength range of Spex
    #ax2.set_xlim([np.min(wave_irtf_bin),np.max(wave_irtf_bin)])
    #ax2.set_ylim([-0.5,2])
    ax2.plot(wave_mask_obs,continuum_removed, label='Ratio', color='k')
    ax2.set_xlim([1.300,1.330])
    #ax2.set_xlim([2.204,2.211])
    
    # Set y-limits of Ratio plot
    #ax2.set_ylim([-.25,.25])
    
    plt.axvline(x=1.313, color='b')

    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('Yng / Old ')#   
    # make these tick labels invisible
    plt.setp( ax2.get_xticklabels(), visible=True)  
    plt.grid(False)
    plt.savefig('figs/AlI_160808/'+starclass+seqnum+'_AlI.png')
def plot_Na_I_feat():
    # Na i (1.14 \mum)
    obs_legend = obs_name + ' (Yng)'
    std_legend = stand_name + ' (Old '+ old_spttype +')'
    plt.clf()
    gs = gridspec.GridSpec(3,1)
    # Overlapping Plots
    ax1 = plt.subplot(gs[:,:])
    ax1 = plt.subplot(gs[:2, :])

    #ax1.set_title('Continuum Removed: Na I')
    ax1.set_title(starclass[:-1]+': Na I (1.14$\mu$m)')

    plt.plot(wave_irtf_bin, divide_irtf, color='black', label=std_legend)
    plt.plot(wave_mask_obs, divide_obs, color='red', label=obs_legend)

    plot_telluric_lines()
    plt.axvline(x=1.14, color='b')

    #lowery,uppery = np.mean(divide_obs, axis=0)-0.4, np.mean(divide_obs, axis=0)+0.4
    lowery,uppery = np.min(divide_obs)*0.9, np.max(divide_obs)*1.1
    ax1.set_ylim([lowery,uppery])

    #ax1.set_xlim([np.min(wave_obs),np.max(wave_obs)])
    ax1.set_xlim([1.120,1.160])

    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()

    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m)')
    plt.setp( ax1.get_xticklabels(), visible=False) #

    # Quotient Subplot
    ax2 = plt.subplot(gs[2, :])
    ax2.plot(wave_mask_obs,continuum_removed, label='Ratio', color='k')
    ax2.set_xlim([1.120,1.160])
    #ax2.set_ylim([-.25,.25])
    plt.axvline(x=1.14, color='b')

    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('Yng / Old ')#   
    # make these tick labels invisible
    plt.setp( ax2.get_xticklabels(), visible=True)  
    plt.grid(False)
    plt.savefig('figs/NaI_160808/'+starclass+seqnum+'_NaI.png')


def _He_I_lines_unfinished():
    obs_legend = obs_name + ' (Yng)'
    std_legend = stand_name + ' (Old)'
    plt.clf()
    gs = gridspec.GridSpec(3,1)
    # Overlapping Plots
    ax1 = plt.subplot(gs[:,:])
    ax1 = plt.subplot(gs[:2, :])
    ax1.set_xlim([np.min(wave_obs),np.max(wave_obs)])

    plt.plot(wave_mask_obs, divide_obs, color='red', label=obs_legend)
    plt.plot(wave_irtf_bin, divide_irtf, color='black', label=std_legend)

    plot_telluric_lines()
    plt.axvline(x=1.70, color='b')
    plt.axvline(x=1.69, color='b')
    plt.axvline(x=2.05, color='b')
    plt.axvline(x=2.11, color='b')
    plt.axvline(x=2.35, color='b')
    ax1.set_title('Continuum Removed: He I')

    
    plt.legend(prop={"size":10}) #makes legend font size smaller
    #plt.ylabel('Continuum Removed Spectra')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda$ $(1.1\mu$m)')
    plt.setp( ax1.get_xticklabels(), visible=False) #   

    # Quotient Subplot
    ax2 = plt.subplot(gs[2, :])
    #ax2.set_xlim([0.7, 2.55]) # wavelength range of Spex
    #ax2.set_xlim([np.min(wave_irtf_bin),np.max(wave_irtf_bin)])
    #ax2.set_ylim([-0.5,2])
    ax2.plot(wave_mask_obs,continuum_removed, label='Ratio', color='k')
    ax2.set_xlim([1.65,2.40])
    ax2.set_ylim([-.25,.25])
    plt.axvline(x=1.70, color='b')
    plt.axvline(x=1.69, color='b')
    plt.axvline(x=2.05, color='b')
    plt.axvline(x=2.11, color='b')
    plt.axvline(x=2.35, color='b')

    plt.legend(prop={"size":10}) #makes legend font size smaller
    plot_telluric_lines()
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('Yng / Old')#   
    # make these tick labels invisible
    plt.setp( ax2.get_xticklabels(), visible=True)  
    plt.grid(False)
    plt.savefig('figs/HeI_160725/'+starclass+seqnum+'testHeI.png')

#-----DEBUGGER-----
#pdb.set_trace()
#-----DEBUGGER----- 


# read in spectral class list
#spt_listing = ascii.read('_obs_irtf_class.list', delimiter="|")# includes comparison of yng stars w/ low SNR
#spt_listing = ascii.read('_obs_irtf_class_no_lowSNR.list', delimiter="|")# old list
spt_listing = ascii.read('ALLfracdiff.csv', delimiter=',')

# print out column names
spt_listing.colnames
#>> ['YngName', 'YngSpt', 'Oldfits', 'seqnum', 'YngShift', 'stand_name', 'color', 'color', 'OldSpt']



for loopy in range(len(spt_listing)):
#for loopy in range(0,10):
    #if "" mess things up then use this notation: spt_listing['YngSpt'][0][1:-1]
    starclass = spt_listing['YngSpt'][loopy]#[1:-1]
    obs_name = spt_listing['YngName'][loopy]#[1:-1]
    standard_file = spt_listing['Oldfits'][loopy]#[1:-1]
    stand_name = spt_listing['stand_name'][loopy]#[1:-1]
    seqnum = spt_listing['seqnum'][loopy]#[1:-1]
    old_spttype = spt_listing['OldSpt'][loopy]

    
    # degree of polynomial
    polydeg = 4 
    

    ###
    # Open data
    ###
    # open observed data
    observed = u'/Users/cmutnik/work/astro/finished_with_fixed_names/' + obs_name + '.fits'
    spectra = fits.getdata(observed)
    wave_obs = spectra[0]
    flux_obs = spectra[1]
    # open IRTF data
    #standard_dir = u'/Users/cmutnik/work/astro/plots/compare/obs_vs_IRTF/IRTF_fits/' + standard_file
    standard_dir = u'/Users/cmutnik/work/astro/plots/compare/z_rayner_all/' + standard_file
    data_irtf = fits.getdata(standard_dir)
    wave_irtf = data_irtf[0]
    flux_irtf = data_irtf[1]    
    
    
    # mask nan values out of flux arrays
    flux_mask_obs = flux_obs[np.logical_not(np.isnan(flux_obs))]
    flux_mask_irtf = flux_irtf[np.logical_not(np.isnan(flux_irtf))] 

    # mask wave array in same place to preserve dimensions
    wave_mask_obs = wave_obs[np.logical_not(np.isnan(flux_obs))] 
    wave_mask_irtf = wave_irtf[np.logical_not(np.isnan(flux_irtf))]
    # check arrays have same dimension
    #print len(flux_mask_irtf) == len(wave_mask_irtf)
    #>> True
    # to print out new array without extra masked info
    #print np.ma.compressed(rayner_wave_mask)
    

    # Must Rebin data since: len(wave_obs) != len(flux_irtf)
    #wave_irtf_bin = rebin_spec(wave_mask_irtf, flux_mask_irtf, spectra[0]).binwave
    #flux_irtf_bin = rebin_spec(wave_mask_irtf, flux_mask_irtf, spectra[0]).binflux
    wave_irtf_bin = rebin_spec(wave_mask_irtf, flux_mask_irtf, wave_mask_obs).binwave
    flux_irtf_bin = rebin_spec(wave_mask_irtf, flux_mask_irtf, wave_mask_obs).binflux   

    # normalize data
    #norm_obs_flux = normalize_flux(wave_array=wave_obs, flux_array=spectra[1])
    norm_obs_flux = normalize_flux(wave_mask_obs, flux_mask_obs)
    norm_irtf_flux = normalize_flux(wave_irtf_bin, flux_irtf_bin)   
    


    ##
    # Mask out Dark Telluric Region
    ##
    # mask out dark gray telluric regions from Yng spectra
    wave_mask_obs = np.ma.masked_inside(wave_mask_obs, 1.35, 1.415)
    wave_mask_obs = np.ma.masked_inside(wave_mask_obs, 1.8, 1.91)
    wave_mask_obs = np.ma.masked_inside(wave_mask_obs, 2.50, 2.88)
    flux_mask_obs = np.ma.masked_array(norm_obs_flux, wave_mask_obs.mask)

    # mask out dark gray telluric regions from R09 spectra
    wave_mask_irtf = np.ma.masked_inside(wave_irtf_bin, 1.35, 1.415)
    wave_mask_irtf = np.ma.masked_inside(wave_mask_irtf, 1.8, 1.91)
    wave_mask_irtf = np.ma.masked_inside(wave_mask_irtf, 2.50, 2.88)
    flux_mask_irtf = np.ma.masked_array(norm_irtf_flux, wave_mask_irtf.mask)

    '''
    # mask flux difference array
    masked_flux_difference = np.ma.masked_array(flux_ratio, wave_mask_irtf.mask)

    # Mask out 0's
    flux_mask_irtf = np.ma.masked_equal(flux_mask_irtf, 0)
    wave_mask_irtf = np.ma.masked_array(wave_mask_irtf, flux_mask_irtf.mask)
    wave_mask_obs = np.ma.masked_array(wave_mask_obs, flux_mask_irtf.mask)
    flux_mask_obs = np.ma.masked_array(flux_mask_obs, flux_mask_irtf.mask)
    masked_flux_difference = np.ma.masked_array(masked_flux_difference, flux_mask_irtf.mask)
    '''

    '''
    # return all non-zero values
    tmp = np.where(norm_irtf_flux > 0)  
    

    # need to rm the portion of the spec that is throwing off the fit
    wave_irtf_bin = wave_irtf_bin[tmp]
    norm_irtf_flux = norm_irtf_flux[tmp]    
    wave_mask_obs = wave_mask_obs[tmp]
    norm_obs_flux = norm_obs_flux[tmp]  
    '''
    # Mask out 0's
    norm_irtf_flux = np.ma.masked_equal(flux_mask_irtf, 0)
    wave_irtf_bin = np.ma.masked_array(wave_irtf_bin, norm_irtf_flux.mask)
    wave_mask_obs = np.ma.masked_array(wave_mask_obs, norm_irtf_flux.mask)
    norm_obs_flux = np.ma.masked_array(norm_obs_flux, norm_irtf_flux.mask)
    


    #####----------------------------------------------------------------------------------------------------
    ###
    # Mask out 2 smallest irtf wavelength values, to rm vertical line on LHS of plots
    ###
    #min_wave4mask = np.where(abs(wave_irtf_bin - 0.80887) == np.min(abs(wave_irtf_bin - 0.80887)))[0][0]
    # smallest masked out
    val1 = np.min(wave_irtf_bin)
    wave_irtf_bin = np.ma.masked_equal(wave_irtf_bin, val1)
    norm_irtf_flux = np.ma.masked_array(norm_irtf_flux, norm_irtf_flux.mask)
    wave_mask_obs = np.ma.masked_array(wave_mask_obs, norm_irtf_flux.mask)
    norm_obs_flux = np.ma.masked_array(norm_obs_flux, norm_irtf_flux.mask)

    # now 2nd smallest is minimum, mask it
    val2 = np.min(wave_irtf_bin)
    wave_irtf_bin = np.ma.masked_equal(wave_irtf_bin, val2)
    norm_irtf_flux = np.ma.masked_array(norm_irtf_flux, norm_irtf_flux.mask)
    wave_mask_obs = np.ma.masked_array(wave_mask_obs, norm_irtf_flux.mask)
    norm_obs_flux = np.ma.masked_array(norm_obs_flux, norm_irtf_flux.mask)
    #####----------------------------------------------------------------------------------------------------



    # get coeffs
    coefs_obs = poly.polyfit(wave_mask_obs, norm_obs_flux, polydeg)
    coefs_irtf = poly.polyfit(wave_irtf_bin, norm_irtf_flux, polydeg)   

    # pull coefficients from array, to be used as inputs in function
    coef1_obs,coef2_obs,coef3_obs,coef4_obs,coef5_obs = coefs_obs
    coef1,coef2,coef3,coef4,coef5 = coefs_irtf      

    # use calculated coeffs to eval polynomial (generate y value for each x value)
    poly_obs = eval_poly(wave_mask_obs, coef1_obs,coef2_obs,coef3_obs,coef4_obs,coef5_obs) 
    poly_irtf = eval_poly(wave_irtf_bin, coef1,coef2,coef3,coef4,coef5)     

    # divide spectra by fitted poly
    divide_obs = norm_obs_flux / poly_obs
    divide_irtf = norm_irtf_flux / poly_irtf    
    
    ###
    # Zoom in on spectral features
    ### 

    # Calculate ratio between observed and rayner stars
    continuum_removed = divide_obs / divide_irtf

    ###
    # CALL PLOTTING FUNCTIONS
    ###
    Yng_Old_overlay()# UNCOMMENT FOR RATIO PLOTS
    observed_poly_fit_quotient()
    rayner_poly_fit_quotient()
    plot_Na_I_2tac2_feat()
    plot_Ca_II_feat()
    plot_Mg_I_1tac7_feat()
    plot_Mg_I_1tac5_feat()
    plot_Al_I_feat()
    plot_Na_I_feat()
    #_He_I_lines_unfinished()
    print 'finished: '+str(loopy+1)+'/'+str(len(spt_listing))+':\n'+ starclass +'\t'+ obs_name +'\t'+ standard_file +'\t'+stand_name +'\t'+ seqnum


