#!~/bin/python
# Python spectral indicies
# Corey Mutnik 5/31/16

# in ipython type history to see what you typed in that session
#history

from pysynphot import spectrum, observation
import numpy.polynomial.polynomial as poly
import matplotlib.gridspec as gridspec
import scipy.optimize as optimized
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.io import fits
from glob import glob
import numpy as np
import pysynphot
import os

'''
def rebin_spec(wave, specin, wavenew):
    """Rebin data for direct comparison"""
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
def normalize_spt_feature(wave_array, flux_array, normval):
    micron_value = np.where(abs(wave_array - normval) == min(abs(wave_array - normval)))[0][0]
    norm_den = (float)((wave_array[micron_value] * flux_array[micron_value])**(-1))
    norm_flux = []
    for i in range(0, len(wave_array)):
        norm_flux.append(wave_array[i] * flux_array[i] * norm_den)
    return np.array(norm_flux) 
def eval_poly(x, a,b,c,d,e):
    return (a + b*x + c*x**2 + d*x**3 + e*x**4)

# make list of all fits files
#dir_path = u'/Users/cmutnik/work/astro/finished_with_fixed_names'
dir_path = '/Users/cmutnik/work/astro/finished_with_fixed_names'
globpath = os.path.join(dir_path, '*.fits')
filelist = glob(globpath)
filelist.sort()
'''

def eval_linfit(x, m,b):
    return(m*x + b)

# degree of polynomial
polydeg = 4 


# 160616 - fixed variance issues
# 160624 - added new feature limits (from mike)
def Ca_II_EW(inwave,influx):
    global EW_caii, uncertainty_caii
    # Ca II (0.866 \mum)
    # Feature limits: 0.860-0.875
    low_lim,high_lim = 0.860, 0.875
    # First continuum level: 0.862-0.864
    fc1,fc2 = 0.862, 0.864
    # Second continuum level: 0.870-0.873
    sc1,sc2 = 0.870, 0.873

    ##
    # Corrected Feature Limits
    ##
    FL1, FL2 = 0.8655, 0.8673

    # define window of region (was used for plotting)
    #window = (low_lim <= inwave) & (high_lim >= inwave)
    #wave_window = inwave[window]
    #flux_window = influx[window]

    # continuum regions
    continuum1 = (fc1 <= inwave) & (fc2 >= inwave)
    continuum2 = np.where((sc1 <= inwave) & (sc2 >= inwave))[0]

    # mask regions for unweighted linear fit
    wave4linfit = np.append(inwave[continuum1], inwave[continuum2])
    flux4linfit = np.append(influx[continuum1], influx[continuum2])

    # initial guesses
    a,b = 1.,1.
    
    linparam,lincovar = optimized.curve_fit(eval_linfit, wave4linfit, flux4linfit, p0=[a,b])
    #print linparam
    
    lifit_plot = eval_linfit(wave4linfit, linparam[0], linparam[1]) # plot fit against the x_data
    #limits_continuum, = plt.plot(wave4linfit, lifit_plot, label='Linear Fit', color='red')
    
    # only use region between first and second continuum regions
    #feature_within_limits = (fc2 <= inwave) & (sc1 >= inwave)# old limits
    feature_within_limits = (FL1 <= inwave) & (FL2 >= inwave)# using new limits mike sent 6/24/16

    wave_within_limits = inwave[feature_within_limits]
    flux_within_limits = influx[feature_within_limits]

    # calculate EW
    flux_cont = eval_linfit(wave_within_limits, linparam[0], linparam[1])
    delta_wave = np.diff(wave_within_limits)
    # add the last value to the end of array, so they are same shape
    delta_wave = np.append(delta_wave, delta_wave[-1])

    # convert wavelength from microns to angstrom
    delta_wave *= 1e4
    EW_caii = (  (1.0 - (flux_within_limits / flux_cont)) * delta_wave).sum()

    # ERROR CALCULATION
    sig = np.std(flux4linfit)
    sigc = sig * (lincovar[0,0]**2 + lincovar[1,1]**2)**0.5
    #sigc = sig * (lincovar[0,0]**2 + lincovar[1,0]**2 + lincovar[0,1]**2 + lincovar[1,1]**2)**0.5

    #variance_caii = (( (sig**2 / flux_cont**2) + (flux_within_limits**2 / flux_cont**4)*sigc**2 ) * delta_wave**2).sum()
    # variance above fails (gives nan) due to flux_cont^-4, so modify below
    variance_caii = (( (sig / flux_cont)**2 + ((sigc * flux_within_limits / flux_cont)**2 * flux_cont**-2) ) * delta_wave**2).sum()
    uncertainty_caii = np.sqrt(variance_caii)
    print 'sig   sigc   variance   uncertainty'
    print sig, sigc, variance_caii, uncertainty_caii
def Mg_I_1tac7_EW(inwave,influx):
    global EW_mgi_1tac7, uncertainty_mgi_1tac7
    # Mg i (1.711 \mum)
    # Feature limits: 1.695-1.726
    low_lim,high_lim = 1.695, 1.726
    # First continuum level: 1.702-1.708
    fc1,fc2 = 1.702, 1.708
    #Second continuum level: 1.715-1.720
    sc1,sc2 = 1.715, 1.720

    ##
    # Corrected Feature Limits
    ##
    FL1, FL2 = 1.7098, 1.7130

    # define window of region (was used for plotting)
    #window = (low_lim <= inwave) & (high_lim >= inwave)
    #wave_window = inwave[window]
    #flux_window = influx[window]

    # continuum regions
    continuum1 = (fc1 <= inwave) & (fc2 >= inwave)
    continuum2 = np.where((sc1 <= inwave) & (sc2 >= inwave))[0]

    # mask regions for unweighted linear fit
    wave4linfit = np.append(inwave[continuum1], inwave[continuum2])
    flux4linfit = np.append(influx[continuum1], influx[continuum2])

    # initial guesses
    a,b = 1.,1.
    
    linparam,lincovar = optimized.curve_fit(eval_linfit, wave4linfit, flux4linfit, p0=[a,b])
    #print linparam
    
    lifit_plot = eval_linfit(wave4linfit, linparam[0], linparam[1]) # plot fit against the x_data
    #limits_continuum, = plt.plot(wave4linfit, lifit_plot, label='Linear Fit', color='red')
    
    # only use region between first and second continuum regions
    #feature_within_limits = (fc2 <= inwave) & (sc1 >= inwave)# old limits
    feature_within_limits = (FL1 <= inwave) & (FL2 >= inwave)# using new limits mike sent 6/24/16
    
    wave_within_limits = inwave[feature_within_limits]
    flux_within_limits = influx[feature_within_limits]

    # calculate EW
    flux_cont = eval_linfit(wave_within_limits, linparam[0], linparam[1])
    delta_wave = np.diff(wave_within_limits)
    # add the last value to the end of array, so they are same shape
    delta_wave = np.append(delta_wave, delta_wave[-1])

    # convert wavelength from microns to angstrom
    delta_wave *= 1e4
    EW_mgi_1tac7 = (  (1.0 - (flux_within_limits / flux_cont)) * delta_wave).sum()

    #--------------- ERROR CALCULATION
    sig = np.std(flux4linfit)
    sigc = sig * (lincovar[0,0]**2 + lincovar[1,1]**2)**0.5
    #sigc = sig * (lincovar[0,0]**2 + lincovar[1,0]**2 + lincovar[0,1]**2 + lincovar[1,1]**2)**0.5

    #variance_mgi_1tac7 = (( (sig**2 / flux_cont**2) + (flux_within_limits**2 / flux_cont**4)*sigc**2 ) * delta_wave**2).sum()
    # variance above fails (gives nan) due to flux_cont^-4, so modify below
    variance_mgi_1tac7 = (( (sig / flux_cont)**2 + ((sigc * flux_within_limits / flux_cont)**2 * flux_cont**-2) ) * delta_wave**2).sum()

    uncertainty_mgi_1tac7 = np.sqrt(variance_mgi_1tac7)
    print 'sig   sigc   variance   uncertainty'
    print sig, sigc, variance_mgi_1tac7, uncertainty_mgi_1tac7
def Mg_I_1tac5_EW(inwave,influx):
    global EW_mgi_1tac5, uncertainty_mgi_1tac5
    # Mg i (1.485 \mum)
    # Feature limits: 1.475-1.4975
    low_lim,high_lim = 1.475, 1.4975
    # First continuum level: 1.4775-1.485
    fc1,fc2 = 1.4775, 1.485
    #Second continuum level: 1.491-1.497
    sc1,sc2 = 1.491, 1.497

    ##
    # Corrected Feature Limits
    ##
    FL1, FL2 = 1.4867, 1.4895

    # define window of region (was used for plotting)
    #window = (low_lim <= inwave) & (high_lim >= inwave)
    #wave_window = inwave[window]
    #flux_window = influx[window]

    # continuum regions
    continuum1 = (fc1 <= inwave) & (fc2 >= inwave)
    continuum2 = np.where((sc1 <= inwave) & (sc2 >= inwave))[0]

    # mask regions for unweighted linear fit
    wave4linfit = np.append(inwave[continuum1], inwave[continuum2])
    flux4linfit = np.append(influx[continuum1], influx[continuum2])

    # initial guesses
    a,b = 1.,1.
    
    linparam,lincovar = optimized.curve_fit(eval_linfit, wave4linfit, flux4linfit, p0=[a,b])
    #print linparam
    
    lifit_plot = eval_linfit(wave4linfit, linparam[0], linparam[1]) # plot fit against the x_data
    #limits_continuum, = plt.plot(wave4linfit, lifit_plot, label='Linear Fit', color='red')
    
    # only use region between first and second continuum regions
    #feature_within_limits = (fc2 <= inwave) & (sc1 >= inwave)# old limits
    feature_within_limits = (FL1 <= inwave) & (FL2 >= inwave)# using new limits mike sent 6/24/16
    
    wave_within_limits = inwave[feature_within_limits]
    flux_within_limits = influx[feature_within_limits]

    # calculate EW
    flux_cont = eval_linfit(wave_within_limits, linparam[0], linparam[1])
    delta_wave = np.diff(wave_within_limits)
    # add the last value to the end of array, so they are same shape
    delta_wave = np.append(delta_wave, delta_wave[-1])

    # convert wavelength from microns to angstrom
    delta_wave *= 1e4
    EW_mgi_1tac5 = (  (1.0 - (flux_within_limits / flux_cont)) * delta_wave).sum()

    # ERROR CALCULATION
    sig = np.std(flux4linfit)
    sigc = sig * (lincovar[0,0]**2 + lincovar[1,1]**2)**0.5
    #sigc = sig * (lincovar[0,0]**2 + lincovar[1,0]**2 + lincovar[0,1]**2 + lincovar[1,1]**2)**0.5

    #variance_mgi_1tac5 = (( (sig**2 / flux_cont**2) + (flux_within_limits**2 / flux_cont**4)*sigc**2 ) * delta_wave**2).sum()
    # variance above fails (gives nan) due to flux_cont^-4, so modify below
    variance_mgi_1tac5 = (( (sig / flux_cont)**2 + ((sigc * flux_within_limits / flux_cont)**2 * flux_cont**-2) ) * delta_wave**2).sum()

    uncertainty_mgi_1tac5 = np.sqrt(variance_mgi_1tac5)
    print 'sig   sigc   variance   uncertainty'
    print sig, sigc, variance_mgi_1tac5, uncertainty_mgi_1tac5
def Al_I_EW(inwave,influx):
    global EW_ali, uncertainty_ali
    # Al i (1.313 \mum)
    # Feature limits: 1.300-1.330
    low_lim,high_lim = 1.300,1.330
    # First continuum level: 1.305-1.309
    fc1,fc2 = 1.305,1.309
    # Second continuum level: 1.320-1.325
    sc1,sc2 = 1.320,1.325

    ##
    # Corrected Feature Limits
    ##
    FL1, FL2 = 1.3118, 1.3165

    # define window of region (was used for plotting)
    #window = (low_lim <= inwave) & (high_lim >= inwave)
    #wave_window = inwave[window]
    #flux_window = influx[window]

    # continuum regions
    continuum1 = (fc1 <= inwave) & (fc2 >= inwave)
    continuum2 = np.where((sc1 <= inwave) & (sc2 >= inwave))[0]

    # mask regions for unweighted linear fit
    wave4linfit = np.append(inwave[continuum1], inwave[continuum2])
    flux4linfit = np.append(influx[continuum1], influx[continuum2])

    # initial guesses
    a,b = 1.,1.
    
    linparam,lincovar = optimized.curve_fit(eval_linfit, wave4linfit, flux4linfit, p0=[a,b])
    #print linparam
    
    lifit_plot = eval_linfit(wave4linfit, linparam[0], linparam[1]) # plot fit against the x_data
    #limits_continuum, = plt.plot(wave4linfit, lifit_plot, label='Linear Fit', color='red')
    
    # only use region between first and second continuum regions
    #feature_within_limits = (fc2 <= inwave) & (sc1 >= inwave)
    # old limits
    feature_within_limits = (FL1 <= inwave) & (FL2 >= inwave)# using new limits mike sent 6/24/16
    
    wave_within_limits = inwave[feature_within_limits]
    flux_within_limits = influx[feature_within_limits]

    # calculate EW
    flux_cont = eval_linfit(wave_within_limits, linparam[0], linparam[1])
    delta_wave = np.diff(wave_within_limits)
    # add the last value to the end of array, so they are same shape
    delta_wave = np.append(delta_wave, delta_wave[-1])

    # convert wavelength from microns to angstrom
    delta_wave *= 1e4
    EW_ali = (  (1.0 - (flux_within_limits / flux_cont)) * delta_wave).sum()

    # ERROR CALCULATION
    sig = np.std(flux4linfit)
    sigc = sig * (lincovar[0,0]**2 + lincovar[1,1]**2)**0.5
    #sigc = sig * (lincovar[0,0]**2 + lincovar[1,0]**2 + lincovar[0,1]**2 + lincovar[1,1]**2)**0.5

    #variance_ali = (( (sig**2 / flux_cont**2) + (flux_within_limits**2 / flux_cont**4)*sigc**2 ) * delta_wave**2).sum()
    # variance above fails (gives nan) due to flux_cont^-4, so modify below
    variance_ali =(( (sig / flux_cont)**2 + ((sigc * flux_within_limits / flux_cont)**2 * flux_cont**-2) ) * delta_wave**2).sum()

    uncertainty_ali = np.sqrt(variance_ali)
    print 'sig   sigc   variance   uncertainty'
    print sig, sigc, variance_ali, uncertainty_ali
def Na_I_1tac14_EW(inwave,influx):
    global EW_nai, uncertainty_nai
    # Na i (1.14 \mum)
    # Published Feature limits: 1.120-1.160
    low_lim,high_lim = 1.120,1.160
    # First continuum level: 1.125-1.130
    fc1,fc2 = 1.125,1.130
    #Second continuum level: 1.150-1.160
    sc1,sc2 = 1.150,1.160

    ##
    # Corrected Feature Limits
    ##
    FL1, FL2 = 1.137,1.1428

    # define window of region (was used for plotting)
    #window = (low_lim <= inwave) & (high_lim >= inwave)
    #wave_window = inwave[window]
    #flux_window = influx[window]

    # continuum regions
    continuum1 = (fc1 <= inwave) & (fc2 >= inwave)
    continuum2 = np.where((sc1 <= inwave) & (sc2 >= inwave))[0]

    # mask regions for unweighted linear fit
    wave4linfit = np.append(inwave[continuum1], inwave[continuum2])
    flux4linfit = np.append(influx[continuum1], influx[continuum2])

    # initial guesses
    a,b = 1.,1.
    
    linparam,lincovar = optimized.curve_fit(eval_linfit, wave4linfit, flux4linfit, p0=[a,b])
    #print linparam
    
    lifit_plot = eval_linfit(wave4linfit, linparam[0], linparam[1]) # plot fit against the x_data
    #limits_continuum, = plt.plot(wave4linfit, lifit_plot, label='Linear Fit', color='red')
    
    # only use region between first and second continuum regions
    feature_within_limits = (FL1 <= inwave) & (FL2 >= inwave)
    wave_within_limits = inwave[feature_within_limits]
    flux_within_limits = influx[feature_within_limits]

    # calculate EW
    flux_cont = eval_linfit(wave_within_limits, linparam[0], linparam[1])
    delta_wave = np.diff(wave_within_limits)
    # add the last value to the end of array, so they are same shape
    delta_wave = np.append(delta_wave, delta_wave[-1])

    # convert wavelength from microns to angstrom
    delta_wave *= 1e4
    EW_nai = (  (1.0 - (flux_within_limits / flux_cont)) * delta_wave).sum()

    # ERROR CALCULATION
    sig = np.std(flux4linfit)
    sigc = sig * (lincovar[0,0]**2 + lincovar[1,1]**2)**0.5
    #sigc = sig * (lincovar[0,0]**2 + lincovar[1,0]**2 + lincovar[0,1]**2 + lincovar[1,1]**2)**0.5

    #variance_nai = (( (sig**2 / flux_cont**2) + (flux_within_limits**2 / flux_cont**4)*sigc**2 ) * delta_wave**2).sum()
    # variance above fails (gives nan) due to flux_cont^-4, so modify below
    variance_nai =(( (sig / flux_cont)**2 + ((sigc * flux_within_limits / flux_cont)**2 * flux_cont**-2) ) * delta_wave**2).sum()

    uncertainty_nai = np.sqrt(variance_nai)
    print 'sig   sigc   variance   uncertainty'
    print sig, sigc, variance_nai, uncertainty_nai
def Na_I_2tac2_EW(inwave,influx):
    global EW_nai_2tac2, uncertainty_nai_2tac2
    # Na i (2.206 \mum) 
    # Feature limits: 2.185-2.230
    low_lim, high_lim = 2.185,2.230
    # First continuum level: 2.192-2.198
    fc1,fc2 = 2.192,2.198
    # Second continuum level: 2.213-2.220
    sc1,sc2 = 2.213,2.220

    ##
    # Corrected Feature Limits
    ##
    FL1, FL2 = 2.204, 2.211

    # define window of region (was used for plotting)
    #window = (low_lim <= inwave) & (high_lim >= inwave)
    #wave_window = inwave[window]
    #flux_window = influx[window]

    # continuum regions
    continuum1 = (fc1 <= inwave) & (fc2 >= inwave)
    continuum2 = np.where((sc1 <= inwave) & (sc2 >= inwave))[0]

    # mask regions for unweighted linear fit
    wave4linfit = np.append(inwave[continuum1], inwave[continuum2])
    flux4linfit = np.append(influx[continuum1], influx[continuum2])

    # initial guesses
    a,b = 1.,1.
    
    linparam,lincovar = optimized.curve_fit(eval_linfit, wave4linfit, flux4linfit, p0=[a,b])
    #print linparam
    
    lifit_plot = eval_linfit(wave4linfit, linparam[0], linparam[1]) # plot fit against the x_data
    #limits_continuum, = plt.plot(wave4linfit, lifit_plot, label='Linear Fit', color='red')
    
    # only use region between first and second continuum regions
    #feature_within_limits = (fc2 <= inwave) & (sc1 >= inwave)# old limits
    feature_within_limits = (FL1 <= inwave) & (FL2 >= inwave)# using new limits mike sent 6/24/16

    wave_within_limits = inwave[feature_within_limits]
    flux_within_limits = influx[feature_within_limits]

    # calculate EW
    flux_cont = eval_linfit(wave_within_limits, linparam[0], linparam[1])
    delta_wave = np.diff(wave_within_limits)
    # add the last value to the end of array, so they are same shape
    delta_wave = np.append(delta_wave, delta_wave[-1])

    # convert wavelength from microns to angstrom
    delta_wave *= 1e4
    EW_nai_2tac2 = (  (1.0 - (flux_within_limits / flux_cont)) * delta_wave).sum()

    # ERROR CALCULATION
    sig = np.std(flux4linfit)
    sigc = sig * (lincovar[0,0]**2 + lincovar[1,1]**2)**0.5
    #sigc = sig * (lincovar[0,0]**2 + lincovar[1,0]**2 + lincovar[0,1]**2 + lincovar[1,1]**2)**0.5

    #variance_nai_2tac2 = (( (sig**2 / flux_cont**2) + (flux_within_limits**2 / flux_cont**4)*sigc**2 ) * delta_wave**2).sum()
    # variance above fails (gives nan) due to flux_cont^-4, so modify below
    variance_nai_2tac2 = (( (sig / flux_cont)**2 + ((sigc * flux_within_limits / flux_cont)**2 * flux_cont**-2) ) * delta_wave**2).sum()
    
    uncertainty_nai_2tac2 = np.sqrt(variance_nai_2tac2)
    print 'sig   sigc   variance   uncertainty'
    print sig, sigc, variance_nai_2tac2, uncertainty_nai_2tac2





# open table to access files with names, spt types, wtc
tabdat = ascii.read('Table_for_paper_160624.csv')

#tabdat.colnames
#>>['Object', 'RA', 'DEC', 'Lit. Spectral Type', 'New Spt type', 'UT Date', 'J mag', 'S/N', 'Total Exp. Time (s)', 'A0 standard', 'Teff (K)', 'log(g)', '2Mass designation', 'other name', 'reduction file', 'possible filename (mislabeled)', 'IRTF star used in comparison', 'Notes']

obj = tabdat['Object']
spt_type = tabdat['Lit. Spectral Type']
filenames = tabdat['reduction file']


dir_path = '/Users/cmutnik/work/astro/finished_with_fixed_names/'


# set file to write EW values to
outfile = open('obs_EW_vals_160624.txt', 'w')
# write header to file, for colnames
outfile.write('#spt type_standard_file, EW_caii, uncertainty_caii, EW_nai, uncertainty_nai, EW_ali, uncertainty_ali, EW_mgi_1tac5, uncertainty_mgi_1tac5, EW_mgi_1tac7, uncertainty_mgi_1tac7, EW_nai_2tac2, uncertainty_nai_2tac2\n')
for loopy in range(len(obj)):
    
    # make path to obs fits file
    spectra = dir_path + obj[loopy] + '.fits'

    # output name needs spt type in front so mapping code works w/o mod
    standard_file = spt_type[loopy] +'_'+ obj[loopy]#os.path.basename(filelist[loopy])[:-5]

    # open observed data
    #observed = u'/Users/cmutnik/work/astro/finished_with_fixed_names/' + obs_name + '.fits'
    #spectra = fits.getdata(observed)
    spectra = fits.getdata(spectra)
    wave_obs = spectra[0]
    flux_obs = spectra[1]
    
    # mask nan values out of flux arrays
    flux_mask_obs = flux_obs[np.logical_not(np.isnan(flux_obs))]
    wave_mask_obs = wave_obs[np.logical_not(np.isnan(flux_obs))]

    # open IRTF data
    #data_irtf = fits.getdata(filelist[loopy])
    #wave_irtf = data_irtf[0]
    #flux_irtf = data_irtf[1]
    #flux_mask_irtf = flux_irtf[np.logical_not(np.isnan(flux_irtf))]
    #wave_mask_irtf = wave_irtf[np.logical_not(np.isnan(flux_irtf))]

    # get EW values for each spectral line
    Ca_II_EW(wave_mask_obs,flux_mask_obs)
    Na_I_1tac14_EW(wave_mask_obs,flux_mask_obs)
    Al_I_EW(wave_mask_obs,flux_mask_obs)
    Na_I_2tac2_EW(wave_mask_obs,flux_mask_obs)
    Mg_I_1tac5_EW(wave_mask_obs,flux_mask_obs)
    Mg_I_1tac7_EW(wave_mask_obs,flux_mask_obs)

    # write values to file
    #string_um_up = (standard_file,EW_caii,EW_nai,EW_nai_2tac2,EW_ali,EW_mgi_1tac5,EW_mgi_1tac7,variance_mgi_1tac7)
    string_um_up = (standard_file,EW_caii,uncertainty_caii,EW_nai,uncertainty_nai,EW_ali,uncertainty_ali,EW_mgi_1tac5,uncertainty_mgi_1tac5,EW_mgi_1tac7,uncertainty_mgi_1tac7,EW_nai_2tac2,uncertainty_nai_2tac2)
    string_um_up = str(string_um_up)+'\n'
    outfile.write(string_um_up)
    # print where im at in loop
    print 'Finished: ', (loopy+1),'/',(len(obj))
outfile.close()
