#astropy.stats.funcs.signal_to_noise_oir_ccd(t, source_eps, sky_eps, dark_eps, rd, npix, gain=1.0)



from astropy.stats.funcs import signal_to_noise_oir_ccd


file = fits.open('____.fits')
head = file[0].header

### verify all data are type = float
# t = CCD integration time in seconds (float, or numpy.ndarray)
t_ = head['ITIME'] # Integration time in seconds
t_total = head['ITOT'] # Total integration time (sec)


# source_eps = Number of electrons (photons) or DN per second in the aperture
source_eps = head['LINCRMAX'] # Maximum of linearity correction (DN) 
'''# not needed
flat = fits.open(head['FLAT']) # linearity maximum (DN)
flathead = flat[0].header
source_eps = flathead['LINCRMAX']
'''


# sky_eps =


# dark_eps =


# rd =


# npix = Size of the aperture in pixels
head['AP01RAD'] # Aperture radius in arcseconds  
'''npix = head['SLTH_PIX'] * head['SLTW_PIX'] #this is slit not aperture'''


# gain = 
