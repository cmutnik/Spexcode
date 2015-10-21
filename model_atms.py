# script to plot merged fits files with model atmosphere
# Corey Mutnik
# 7/20/15

import pysynphot
from pysynphot import observation
from pysynphot import spectrum
#from PyAstronomy import pyasl
from pysynphot import units

import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np
import pdb

spectra = fits.getdata('HIP_77909_7_1_15_merge.fits')

#for now round temps to nearest 500K and log(g) to nearest 0.5
#sp = pysynphot.Icat('phoenix_v16', Teff, metallicity, log_g) #for objects beolw 5000K
model_spec = pysynphot.Icat('ck04models', Teff=11500, metallicity=0.0, log_g=4.5) #for objects above 5000K
model_wave = model_spec.wave
model_flux = model_spec.flux
print model_spec.fluxunits
print model_spec.waveunits

# DO NOT USE THIS, it only changes the unit objects...it does NOT recompute the internally kept units
#convert = spectrum.SourceSpectrum.convert(model_spec, 'micron')
def micron_to_angstrom(wavelength_array):
    return wavelength_array/1.0e-4
def angstrom_to_micron(wavelength_array):
    return wavelength_array * 1.0e-4

convert_model_wave = angstrom_to_micron(model_wave)


def rebin_spec(wave, specin, wavenew):
    spec = spectrum.ArraySourceSpectrum(wave=wave, flux = specin)
    f = np.ones(len(wave)) # returns array of ones with size given
    filt = spectrum.ArraySpectralElement(wave, f, waveunits='angstrom')
    obs = observation.Observation(spec, filt, binset=wavenew, force='taper')
    return obs.binflux

#pdb.set_trace()

#rebinned_model_flux = rebin_spec(convert_model_wave, model_flux, spectra[0]) # ca'nt increase precision ------------
rebinned_flux = rebin_spec(spectra[0], spectra[1], convert_model_wave)




# to normalizew model spectra                        -------------------------create new array that encompasses only where the model isn't zero
norm_model_wave = np.where(abs(convert_model_wave - 1.10) == min(abs(convert_model_wave - 1.10)))[0][0]
norm_model_den = (float)((convert_model_wave[norm_model_wave] * model_flux[norm_model_wave])**(-1))
norm_model_flux = []
for i in range(0, len(convert_model_wave)):
    norm_model_flux.append(convert_model_wave[i] * model_flux[i] * norm_model_den)


# to normalize observed spectra
#
##      replace spectra[1] with rebinned_flux ?____________________
#
norm_wave = np.where(abs(spectra[0] - 1.10) == min(abs(spectra[0]-1.10)))[0][0]
norm_den = (float)((spectra[0][norm_wave] * spectra[1][norm_wave])**(-1))
norm_flux = []
for i in range(0, len(spectra[0])):
    norm_flux.append(spectra[0][i] * spectra[1][i] * norm_den)
#print norm_flux
# ?----------------------------------------------------------------?
# wave has to high of precision so we must normalize observed flux with model wavelength
## or convolve observed wavelength down?
#
norm_den2 = (float)((convert_model_wave[norm_model_wave] * rebinned_flux[norm_model_wave])**(-1))
norm_flux2 = []
for i in range(0, len(convert_model_wave)):
    norm_flux2.append(convert_model_wave[i] * rebinned_flux[i] * norm_den2)


#plt.plot(convert_model_wave, norm_model_flux, 'r-') # fails
#plt.plot(convert_model_wave, norm_flux2, 'g')
#plt.xlim(0.58, 2.6)
#plt.show()







    
print len(rebinned_flux)
#plt.plot(spectra[0], rebinned_flux, 'g') # now our wavelength array is to long
plt.plot(convert_model_wave, rebinned_flux, 'g', convert_model_wave, model_flux, 'r-')
plt.xlim(0.58, 2.6)
plt.show()



'''
file_name = os.path.basename(spectra)


y_pos = 1 + j
plt.plot(spectra[0], norm_flux)
plt.text(2, y_pos, file_name)
plt.title('Title')
plt.xlabel('Wavelength $\mu$m')
plt.ylabel('$\lambda f_\lambda / \lambda f_\lambda (1.1\mu m) + $ constant')
plt.xlim(0.58, 2.6)
#plt.grid(True)
#plt.savefig('pdf.pdf')
plt.show()
'''
