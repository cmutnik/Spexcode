# calculate average Signal to Noise Ratio over defined region
# Corey Mutnik
# 8/7/15

from astropy.io import fits
import matplotlib.pyplot as plt


spec = fits.open('CD25-11942_7_1_15_merge.fits')
data = spec[0].data
wave_ = data[0]
flux_ = data[1]
error_ = data[2]

SNR_ = []
for theloveofgod in range(0, len(wave_)):
    SNR_.append(flux_[theloveofgod]/error_[theloveofgod])
SNR_sum = 0.0
for var in range(0, len(SNR_)):
    SNR_sum += SNR_[var]
SNR_avg = SNR_sum/len(SNR_)


print wave_
print
print flux_
print
print error_
print
print SNR_
print
print SNR_sum
print
print SNR_avg

#plt.title("S/N plot: generated using spextool methodology")
plt.plot(wave_, SNR_)
plt.show()

