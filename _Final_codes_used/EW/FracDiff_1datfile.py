#!~/bin/python
'''
Calculate EW vals for comparison of
  Yng and Old stars values used to
  make fractional difference subplots
Corey Mutnik 5/31/16
Original code:
  /Users/cmutnik/work/astro/plots/EW/cool_stars_tab8_EW/EW_spectral_indicies_used.py
Modified on 160802:
  /Users/cmutnik/work/astro/plots/EW/frac_diff/EWvals4YngOldFracDiff.py
Modified on 160810:
  /Users/cmutnik/work/astro/plots/EW/frac_diff/FracDiff_1datfile.py
    Remove old methods and uneeded comments
    Turn 3 dat files into 1, then readin
'''
import matplotlib.gridspec as gridspec
import scipy.optimize as optimized
from astropy.io import ascii, fits
import matplotlib.ticker as ticker
from uncertainties import ufloat
import matplotlib.pyplot as plt
import numpy as np

def eval_linfit(x, m,b):
    return(m*x + b)


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
    #print 'sig   sigc   variance   uncertainty'
    #print sig, sigc, variance_caii, uncertainty_caii
    return(ufloat(EW_caii, uncertainty_caii))

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
    #print 'sig   sigc   variance   uncertainty'
    #print sig, sigc, variance_mgi_1tac7, uncertainty_mgi_1tac7
    return(ufloat(EW_mgi_1tac7, uncertainty_mgi_1tac7))
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
    #print 'sig   sigc   variance   uncertainty'
    #print sig, sigc, variance_mgi_1tac5, uncertainty_mgi_1tac5
    return(ufloat(EW_mgi_1tac5, uncertainty_mgi_1tac5))
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
    #print 'sig   sigc   variance   uncertainty'
    #print sig, sigc, variance_ali, uncertainty_ali
    return(ufloat(EW_ali, uncertainty_ali))
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
    #print 'sig   sigc   variance   uncertainty'
    #print sig, sigc, variance_nai, uncertainty_nai
    return(ufloat(EW_nai, uncertainty_nai))
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
    #print 'sig   sigc   variance   uncertainty'
    #print sig, sigc, variance_nai_2tac2, uncertainty_nai_2tac2
    return(ufloat(EW_nai_2tac2, uncertainty_nai_2tac2))


def subplot_fracdiffs_6spec_feats():

    # clear and setup subplots
    plt.clf()
    fig, ax = plt.subplots(3,2)

    # Set ylim of sech subplot, and placement of labels
    #lowx00, highx00 = -6.8, 1# Limits to include outliers
    lowx00, highx00 = -1.25, 0.6# Limits to exclude outliers
    lowx01, highx01 = -1, 5
    lowx10, highx10 = -1.25, 1.5
    lowx11, highx11 = -0.75, 3.75
    lowx20, highx20 = -0.75, 3.25
    lowx21, highx21 = -1.8, 2

    # Change into list to plot with errorbars properly
    #  Array failed...not sure why
    #lumcc = np.array(lumclass_color)

    ###
    # Plot data points in loop, to avoid error thrown by previous function
    # Loop is much slower but works
    # Without loop, function kept throwing error
    #>> "length of rgba sequence should be either 3 or 4"
    ###
    for j in range(len(mapped_val)):
        ax[0,0].errorbar(mapped_val_caii[j], caii_vals[j], yerr=caii_errs[j],fmt='.',color=lumcc[j],capthick=1, mec=lumcc[j], ms=8)
        ax[0,1].errorbar(mapped_val_nai[j], nai_vals[j], yerr=nai_errs[j],fmt='.',color=lumcc[j],capthick=1, mec=lumcc[j], ms=8)
        ax[1,0].errorbar(mapped_val_ali[j], ali_vals[j], yerr=ali_errs[j],fmt='.',color=lumcc[j],capthick=1, mec=lumcc[j], ms=8)
        ax[1,1].errorbar(mapped_val_mgi15[j], mgi_1tac5_vals[j], yerr=mgi_1tac5_errs[j],fmt='.',color=lumcc[j],capthick=1, mec=lumcc[j], ms=8)
        ax[2,0].errorbar(mapped_val_mgi17[j], mgi_1tac7_vals[j], yerr=mgi_1tac7_errs[j],fmt='.',color=lumcc[j],capthick=1, mec=lumcc[j], ms=8)
        ax[2,1].errorbar(mapped_val_nai22[j], nai_2tac2_vals[j], yerr=nai_2tac2_errs[j],fmt='.',color=lumcc[j],capthick=1, mec=lumcc[j], ms=8)


    # Ca II (0.866 um)
    ax[0,0].set_xlim([-0.5,34.5])
    ax[0,0].set_xticks([0,10,20,30])
    ax[0,0].set_xticklabels(([]))
    ax[0,0].set_ylabel(' ')
    ax[0,0].set_ylim([lowx00,highx00]) 
    #ax[0,0].set_ylim([-0.5,1.75])

    # Na I (1.14 um)
    ax[0,1].set_xlim([-0.5,34.5])
    ax[0,1].set_xticks([0,10,20,30])
    ax[0,1].set_xticklabels(([]))
    ax[0,1].set_ylim([lowx01, highx01])

    # Al I (1.31 um)
    ax[1,0].set_xlim([-0.5,34.5])
    ax[1,0].set_xticks([0,10,20,30])
    ax[1,0].set_xticklabels(([]))
    #ax[1,0].set_ylabel('EW: Fractional Difference')
    ax[1,0].set_ylabel('EW$_{Yng}$ - EW$_{Old}$ / EW$_{Old}$')
    ax[1,0].set_ylim([lowx10, highx10])

    # Mg I (1.49 um)
    ax[1,1].set_xlim([-0.5,34.5])
    ax[1,1].set_xticks([0,10,20,30])
    ax[1,1].set_xticklabels(([]))
    ax[1,1].set_ylim([lowx11, highx11])

    # Mg I (1.71 um)
    ax[2,0].set_xlim([-0.5,34.5])
    ax[2,0].set_xticks([0,10,20,30])
    ax[2,0].set_xticklabels((x_spec_list))
    ax[2,0].set_ylabel(' ')
    ax[2,0].set_ylim([lowx20, highx20])
    ax[2,0].set_xlabel('Spectral Type')

    # Na I (2.21 um)
    ax[2,1].set_xlim([-0.5,34.5])
    ax[2,1].set_xticks([0,10,20,30])
    ax[2,1].set_xticklabels((x_spec_list))
    ax[2,1].set_ylim([lowx21, highx21])
    ax[2,1].set_xlabel('Spectral Type')
    

    # Normailze labels so the are in the same position across all subplots
    #norm_text = (15.9-13.75)/(15.9+3.4)
    norm_text = (2.-1.75)/(2.+0.25)
    ax[0,0].annotate( 'Ca II (0.866 $\mu$m)', xy=(2, ( highx00 - ( highx00-lowx00 )*norm_text) ), weight=500 )
    ax[0,1].annotate( 'Na I (1.14 $\mu$m)', xy=(2, ( highx01 - ( highx01-lowx01 )*norm_text) ), weight=500 )
    ax[1,0].annotate( 'Al I (1.31 $\mu$m)', xy=(2, ( highx10 - ( highx10-lowx10 )*norm_text) ), weight=500 )
    ax[1,1].annotate( 'Mg I (1.49 $\mu$m)', xy=(2, ( highx11 - ( highx11-lowx11 )*norm_text) ), weight=500 )
    ax[2,0].annotate( 'Mg I (1.71 $\mu$m)', xy=(2, ( highx20 - ( highx20-lowx20 )*norm_text) ), weight=500 )
    ax[2,1].annotate( 'Na I (2.21 $\mu$m)', xy=(2, ( highx21 - ( highx21-lowx21 )*norm_text) ), weight=500 )

    # Label by lum class
    ax[1,1].annotate( 'V$_{Yng}$ - V$_{Old}$', xy=(2, 2.8), color='black', size=13, weight=1000 )
    ax[1,1].annotate( 'V$_{Yng}$ - III$_{Old}$', xy=(2, 2.5), color='red', size=13, weight=1000 )
    ax[1,1].annotate( 'V$_{Yng}$ - IV$_{Old}$', xy=(2, 2.2), color='orange', size=13, weight=1000 )
    
    
    # set major ytic to show up at integer values
    ax[0,0].yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax[0,1].yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax[1,0].yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax[1,1].yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax[2,0].yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax[2,1].yaxis.set_major_locator(ticker.MultipleLocator(1))

    # set minor ytic to show up every 0.2
    ax[0,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
    ax[0,1].yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
    ax[1,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
    ax[1,1].yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
    ax[2,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
    ax[2,1].yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

    # set minor xtic to show up every 2
    ax[0,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
    ax[0,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))
    ax[1,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
    ax[1,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))
    ax[2,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
    ax[2,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))

    #plt.tight_layout()
    fig.tight_layout()
    fig.subplots_adjust(hspace=.05, bottom=0.075)#, wspace=0.05)

    plt.savefig('subplots/FracDiffEW_160810.png', bbox_inches='tight')



# open table to access files with names, spt types, wtc
yngold = ascii.read('ALLfracdiff.csv')

yngold.colnames
#>>['YngName', 'YngSpt', 'Oldfits', 'seqnum', 'YngShift', 'stand_name', 'color']

obj_yng = yngold['YngName']
spt_type_yng = yngold['YngSpt']
obj_old = yngold['Oldfits']
shift = yngold['YngShift']
#old_name = yngold['stand_name']# For spectral feature plots, not frac diff
#sequmn = yngold['seqnum']# For spectral feature plots, not frac diff

#lumclass_color = yngold['color']
lumcc = [x['color'] for x in yngold]


# directory for fits files
yng_star_dir_path = '/Users/cmutnik/work/astro/finished_with_fixed_names/'
old_star_dir_path = '/Users/cmutnik/work/astro/plots/compare/z_rayner_all/'



# make empty lists for EW values and errors
caii_vals, caii_errs = [], []
nai_vals, nai_errs = [], []
ali_vals, ali_errs = [], []
mgi_1tac5_vals, mgi_1tac5_errs = [], []
mgi_1tac7_vals, mgi_1tac7_errs = [], []
nai_2tac2_vals, nai_2tac2_errs = [], []
for loopy in range(len(obj_yng)):

    # make path to obs fits file
    spec_path_yng = yng_star_dir_path + obj_yng[loopy] + '.fits'
    spec_path_old = old_star_dir_path + obj_old[loopy]

    # Open yng data
    spectra_yng = fits.getdata(spec_path_yng)
    wave_yng = spectra_yng[0]
    flux_yng = spectra_yng[1]
    
    # Mask nan values out of flux arrays
    flux_mask_yng = flux_yng[np.logical_not(np.isnan(flux_yng))]
    wave_mask_yng = wave_yng[np.logical_not(np.isnan(flux_yng))]

    # Repeat for old star data
    data_irtf = fits.getdata(spec_path_old)
    wave_old = data_irtf[0]
    flux_old = data_irtf[1]
    flux_mask_old = flux_old[np.logical_not(np.isnan(flux_old))]
    wave_mask_old = wave_old[np.logical_not(np.isnan(flux_old))]

    ###
    # Get EW values for each spectral line
    ###
    # Ca II
    caii_yng = Ca_II_EW(wave_mask_yng,flux_mask_yng)
    caii_old = Ca_II_EW(wave_mask_old,flux_mask_old)

    # Na I 1.14
    nai_yng = Na_I_1tac14_EW(wave_mask_yng,flux_mask_yng)
    nai_old = Na_I_1tac14_EW(wave_mask_old,flux_mask_old)

    # Al I
    ali_yng = Al_I_EW(wave_mask_yng,flux_mask_yng)
    ali_old = Al_I_EW(wave_mask_old,flux_mask_old)

    # Na I 2.2
    nai_2tac2_yng = Na_I_2tac2_EW(wave_mask_yng,flux_mask_yng)
    nai_2tac2_old = Na_I_2tac2_EW(wave_mask_old,flux_mask_old)

    # Mg I 1.5
    mgi_1tac5_yng = Mg_I_1tac5_EW(wave_mask_yng,flux_mask_yng)
    mgi_1tac5_old = Mg_I_1tac5_EW(wave_mask_old,flux_mask_old)

    # Mg I 1.7
    mgi_1tac7_yng = Mg_I_1tac7_EW(wave_mask_yng,flux_mask_yng)
    mgi_1tac7_old = Mg_I_1tac7_EW(wave_mask_old,flux_mask_old)
    

    # Fractional Differences
    frac_caii = (caii_yng - caii_old) / caii_old
    frac_nai = (nai_yng - nai_old) / nai_old
    frac_ali = (ali_yng - ali_old) / ali_old
    frac_mgi_1tac5 = (mgi_1tac5_yng - mgi_1tac5_old) / mgi_1tac5_old
    frac_mgi_1tac7 = (mgi_1tac7_yng - mgi_1tac7_old) / mgi_1tac7_old
    frac_nai_2tac2 = (nai_2tac2_yng - nai_2tac2_old) / nai_2tac2_old

    ##
    # Append values and uncertainties to separate lists
    ##
    caii_vals.append(frac_caii.nominal_value)
    caii_errs.append(frac_caii.std_dev)

    nai_vals.append(frac_nai.nominal_value)
    nai_errs.append(frac_nai.std_dev)
    
    ali_vals.append(frac_ali.nominal_value)
    ali_errs.append(frac_ali.std_dev)
    
    mgi_1tac5_vals.append(frac_mgi_1tac5.nominal_value)
    mgi_1tac5_errs.append(frac_mgi_1tac5.std_dev)

    mgi_1tac7_vals.append(frac_mgi_1tac7.nominal_value)
    mgi_1tac7_errs.append(frac_mgi_1tac7.std_dev)

    nai_2tac2_vals.append(frac_nai_2tac2.nominal_value)
    nai_2tac2_errs.append(frac_nai_2tac2.std_dev)

    # print where im at in loop
    print 'Finished: ', (loopy+1),'/',(len(obj_yng))

# Mask out values over 3 sigma away from stddev of frac diff error
caii_errs = np.ma.masked_greater_equal(caii_errs, 3*np.std(caii_errs, axis=0))
nai_errs = np.ma.masked_greater_equal(nai_errs, 3*np.std(nai_errs, axis=0))
ali_errs = np.ma.masked_greater_equal(ali_errs, 3*np.std(ali_errs, axis=0))
mgi_1tac5_errs = np.ma.masked_greater_equal(mgi_1tac5_errs, 3*np.std(mgi_1tac5_errs, axis=0))
mgi_1tac7_errs = np.ma.masked_greater_equal(mgi_1tac7_errs, 3*np.std(mgi_1tac7_errs, axis=0))
nai_2tac2_errs = np.ma.masked_greater_equal(nai_2tac2_errs, 3*np.std(nai_2tac2_errs, axis=0))

# Apply mask to feature values
caii_vals = np.ma.masked_array(caii_vals , caii_errs.mask)
nai_vals = np.ma.masked_array(nai_vals , nai_errs.mask)
ali_vals = np.ma.masked_array(ali_vals , ali_errs.mask)
mgi_1tac5_vals = np.ma.masked_array(mgi_1tac5_vals , mgi_1tac5_errs.mask)
mgi_1tac7_vals = np.ma.masked_array(mgi_1tac7_vals , mgi_1tac7_errs.mask)
nai_2tac2_vals = np.ma.masked_array(nai_2tac2_vals , nai_2tac2_errs.mask)


# used to modify X-tics
x_spec_list = ['F0', 'G0', 'K0', 'M0']


EW_spt_type = list(spt_type_yng)
breakup_spt_type = list(map(list, spt_type_yng))
##
# Mapping for observed stars
##
mapped_val = []
for k in range(len(breakup_spt_type)):
    val = 0
    if breakup_spt_type[k][0] == 'F':
        val += 0
    elif breakup_spt_type[k][0] == 'G':
        val += 10
    elif breakup_spt_type[k][0] == 'K':
        val += 20
    elif breakup_spt_type[k][0] == 'M':
        val += 30
    else:
        val += 1000
        print 'what spt type is this:', breakup_spt_type[k][1],' index: ', k
    #print breakup_spt_type[k], val
    
    if breakup_spt_type[k][1] == '1':
        val += 1
    elif breakup_spt_type[k][1] == '2':
        val += 2
    elif breakup_spt_type[k][1] == '3':
        val += 3
    elif breakup_spt_type[k][1] == '4':
        val += 4
    elif breakup_spt_type[k][1] == '5':
        val += 5
    elif breakup_spt_type[k][1] == '6':
        val += 6
    elif breakup_spt_type[k][1] == '7':
        val += 7
    elif breakup_spt_type[k][1] == '8':
        val += 8
    elif breakup_spt_type[k][1] == '9':
        val += 9
    else:
        val += 0
    #print breakup_spt_type[k], val

    # Added shift, so stars w/ same SptTyp don't perfectly overlap
    val += shift[k]
    mapped_val.append(val)


# In order to plot properly, arrays of the same dimension are needed
#   make mapped_val list for each spectral frature
#   and mask them in the correct places
mapped_val_caii = np.ma.masked_array(mapped_val, caii_errs.mask)
mapped_val_nai = np.ma.masked_array(mapped_val, nai_errs.mask)
mapped_val_ali = np.ma.masked_array(mapped_val, ali_errs.mask)
mapped_val_mgi15 = np.ma.masked_array(mapped_val, mgi_1tac5_errs.mask)
mapped_val_mgi17 = np.ma.masked_array(mapped_val, mgi_1tac7_errs.mask)
mapped_val_nai22 = np.ma.masked_array(mapped_val, nai_2tac2_errs.mask)

subplot_fracdiffs_6spec_feats()
