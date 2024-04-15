import numpy as np
import scipy.signal
from astropy.io import fits
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# The equation for a Gaussian:
# 
# G($x$) = $\frac{A}{\sigma\sqrt{2\pi}}e^{\frac{-(x-\mu)^2}{2\sigma^2}}$
# 
# A = amplitude
# 
# $\sigma$ = describes the width of the line
# 
# $x$ = is the array of values our gaussian spans
# 
# $\mu$ = the actual center of our gaussian


def gauss(x, A, mean, sig):
    #This function returns a Gaussian Profile
    gaussian=((A/(sig*np.sqrt(2*np.pi)))*(np.exp(-((x-mean)**2)/(2*(sig**2)))))
    return gaussian

def nonlinearfunc(xvals, amp1, amp2, m1, m2, w1, cont):
    #combining two gaussians
    return gauss(xvals, amp1, m1, w1)+gauss(xvals, amp2, m2, w1)+cont

def fitdata(wave, spec, amp1, amp2, m1, m2, w1, cont):
    #fits two gaussian profiles to a sectrum to determine the amplitudes, line centers, widths, and the continuum level of the input spectrum
    
    print("================================================================================================================")
    print("Performing the least squares fit: ")
    
    popt,pcov=curve_fit(nonlinearfunc, wave, spec, p0=[amp1, amp2, m1, m2, w1, cont])
    errs=np.sqrt(np.diag(pcov))
    
    print("================================================================================================================")
    print("Printing the best fitting parameters and 1 std errors: ")
    print("________________________________________________________________________________________________________________")
    print('line 1 Amp: ' + str(popt[0])+' Amp_err: ' + str(errs[0])+'\n')
    print('line 2 Amp: ' + str(popt[1])+' Amp_err: ' + str(errs[1])+'\n')
    print('line 1 Wavelength: ' + str(popt[2])+' Mean_4959_err: ' + str(errs[2])+'\n')
    print('line 2 wavelength: ' + str(popt[3])+' Mean_5007_err: ' + str(errs[3])+'\n')
    print('line width: ' + str(popt[4])+' Sigma_err: ' + str(errs[4])+'\n')
    print('Continuum level: ' + str(popt[5])+' Cont_err: ' + str(errs[5])+'\n')
    
    print("================================================================================================================")
    print("Printing the observed and modeled data: ")
    ymodel=nonlinearfunc(wave, *popt)
    
    plt.scatter(wave, spec, label='data', color='tab:pink')
    plt.plot(wave, ymodel, label='model', color='k')
    plt.vlines(popt[2], ymin=0.0, ymax=spec.max(), linestyles='--', alpha=0.75, linewidth=1.0)
    plt.vlines(popt[3], ymin=0.0, ymax=spec.max(), linestyles='--', alpha=0.75, linewidth=1.0)
    
    plt.legend()
    plt.show()
    return popt, pcov

def getredshift(lamo, lame):
    #reutrn the redshift of a source given the observed and rest frame wavelengths
    return (lamo-lame)/lame


hdul=fits.open('spec-0532-51993-0497.fits')
spec=hdul[1].data['flux']
waves=10**hdul[1].data['loglam']


sub_i=np.where((waves>6450)&(waves<6600))
sub_spec=spec[sub_i]
sub_wave=waves[sub_i]

fig=plt.figure()
fig.set_size_inches(25,10)
plt.plot(sub_wave, sub_spec)
plt.show()


specpeaks=scipy.signal.find_peaks(sub_spec, height=35)[0]
print(sub_wave[specpeaks])


popt_, pcov_=fitdata(sub_wave, sub_spec, 40, 130, *sub_wave[specpeaks], 5.0, 4.0)

l03_4959_e=4958.911
l03_5007_e=5006.843

src_redshift1=getredshift(popt_[2], l03_4959_e)
print(src_redshift1)

src_redshift2=getredshift(popt_[3], l03_5007_e)
print(src_redshift2)
