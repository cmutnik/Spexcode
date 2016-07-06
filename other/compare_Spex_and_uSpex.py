# Python file to plot fits data from Spex and uSpex - to make comparing possible
# Corey Mutnik
# 7/14/15 & 12/8/15
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

# old spex data
spec = fits.getdata('GSC_06801_00186_oldSpx_7_6_15_merge.fits') # spex (red)
wavelength = spec[0]
flux = spec[1]
wave = np.where(abs(wavelength - 1.10) == min(abs(wavelength-1.10)))
wave_val = wave[0]
wave_val = wave_val[0]
f_lambda = flux[wave_val]
lamb = wavelength[wave_val]
norm_den = (float)((lamb * f_lambda)**(-1))
norm_flux = []
for i in range(0, len(wavelength)):
    norm_flux.append(wavelength[i] * flux[i] * norm_den)
'''
if len(wavelength) == len(flux):
    norm_flux = []
    for i in range(0, len(wavelength)):
        norm_flux.append(wavelength[i] * flux[i] * norm_den)
else:
    print 'wavelength and flux arrays are not equal in length'
'''

    
# uspex data
# uspex (green)
spec1 = fits.getdata('GSC_6801-186_7_2_15_merge.fits') 
uwavelength = spec1[0]
uflux = spec1[1]
uwave = np.where(abs(uwavelength - 1.10) == min(abs(uwavelength-1.10)))
uwave_val = uwave[0]
uwave_val = uwave_val[0]
uf_lambda = uflux[uwave_val]
ulamb = uwavelength[uwave_val]
unorm_den = (float)((ulamb * uf_lambda)**(-1))
unorm_flux = []
for i in range(0, len(uwavelength)):
    unorm_flux.append(uwavelength[i] * uflux[i] * unorm_den +1.0) # +1.0 to shift graph
'''
if len(uwavelength) == len(uflux):
    unorm_flux = []
    for i in range(0, len(uwavelength)):
        unorm_flux.append(uwavelength[i] * uflux[i] * unorm_den +1.0) # +1.0 to shift graph
else:
    print 'wavelength and flux arrays are not equal in length'
'''
'''
#--------------------------------------------------------------------
# division between new and old spex (uspex/spex)
# len(norm_flux) chosen since it spans less range than unorm_flux

sub_norm_flux = []
unorm_flux_noshift = []
for i in range(0, len(norm_flux)):
    unorm_flux_noshift.append(uwavelength[i] * uflux[i] * unorm_den)
    sub_norm_flux.append(abs(norm_flux[i] - unorm_flux_noshift[i]))
div_norm_flux = []
for i in range(0, len(norm_flux)):
    div_norm_flux.append(sub_norm_flux[i] / unorm_flux_noshift[i])



# try making unormflux and normflux using the same unorm_den
#then subrtacting or dividing them
#-----------------------------------------------------------------   
'''

# for overlapping spectra graph
unorm_flux_no_shift = []
for i in range(0, len(uwavelength)):
    unorm_flux_no_shift.append(uwavelength[i] * uflux[i] * unorm_den)


def plot_telluric_lines():
    # Filling light gray
    plt.axvspan(0.92, 0.95, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.11, 1.16, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.415, 1.49, facecolor='gray', alpha=0.25, lw=0)
    plt.axvspan(1.91, 2.05, facecolor='gray', alpha=0.25, lw=0)
    # fill dark gray
    plt.axvspan(1.35, 1.415, facecolor='gray', alpha=0.5, lw=0)
    plt.axvspan(1.8, 1.91, facecolor='gray', alpha=0.5, lw=0)



def single_plot_unstacked(fn='compare_single.png'):
    plt.clf()
    plt.plot(wavelength, norm_flux, 'r', uwavelength, unorm_flux, 'g')
    #plt.plot(wavelength, norm_flux, 'r', uwavelength, unorm_flux, 'g', wavelength, div_norm_flux, 'b')
    plt.title('Comparison of Spex and uSpex using GSC 6801-186')
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda (1.1\mu m) + $ constant')
    plt.ylim(0, 3)
    plt.xlim(0.7, 2.55)
    plt.grid(True)
    plt.text(2.25, 1.4, 'uspex') # green
    plt.text(2.25, 0.4, 'spex') # red   
    plot_telluric_lines()
    plt.savefig(fn)




def double_plot_unstacked_and_overlapping(fn='compare_double.png'):
    plt.clf()
    plt.figure(1)
    #plt.subplot(2,1,1)
    ax1 = plt.subplot(211)
    plt.plot(wavelength, norm_flux, 'r', uwavelength, unorm_flux, 'g')
    plot_telluric_lines()
    plt.title('Comparison of Spex and uSpex using GSC 6801-186')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda (1.1\mu m) + constant$')
    plt.ylim(0, 3)
    plt.xlim(0.7, 2.55)
    plt.text(2.25, 1.4, 'uspex')    # green
    plt.text(2.25, 0.4, 'spex')    # red
    plt.setp( ax1.get_xticklabels(), visible=False) 
    #plt.subplot(2,1,2)
    ax2 = plt.subplot(212, sharex=ax1) # share x axis
    plt.plot(uwavelength, unorm_flux_no_shift, 'g', wavelength, norm_flux, 'r')
    plot_telluric_lines()
    plt.xlabel('Wavelength $\mu$m')
    plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda (1.1\mu m)$')
    plt.ylim(0.1, 1.7)
    plt.xlim(0.7, 2.55)
    # make these tick labels invisible
    plt.setp( ax2.get_xticklabels(), visible=True)  
    plt.grid(False)
    plt.savefig(fn) 







single_plot_unstacked('compare_Spex_uSpex_unstacked.png')

double_plot_unstacked_and_overlapping('compare_Spex_uSpex_overlapping_and_unstacked.png')
