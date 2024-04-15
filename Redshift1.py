#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'widget')
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.visualization import quantity_support
from specutils import Spectrum1D, SpectralRegion
from specutils.fitting import fit_generic_continuum
quantity_support()


# In[2]:


hdul=fits.open('spec-0532-51993-0497.fits')
data=hdul[1].data


# In[3]:


flux=hdul[1].data['flux']*10**-17*u.Unit('erg cm-2 s-2 AA-1')
wave=10**hdul[1].data['loglam']*u.AA
spec=Spectrum1D(spectral_axis=wave,flux=flux)
spec.spectral_axis,spec.flux

plt.figure()
plt.plot(spec.spectral_axis,spec.flux)
plt.title('Spectrum')
plt.show()


# In[8]:


sfit = fit_generic_continuum(spec)
ycontfit = sfit(spec.spectral_axis)


# In[9]:


plt.figure()
plt.plot(spec.spectral_axis, spec.flux)
plt.plot(spec.spectral_axis, ycontfit)
plt.show()


# In[10]:


plt.figure()
plt.plot(spec.spectral_axis, ycontfit)  # corrected to use spectral_axis
plt.show()


# In[11]:


plt.figure()
plt.plot(spec.spectral_axis, flux - ycontfit)  # corrected to use spectral_axis
plt.show()


# In[12]:


from scipy.interpolate import interp1d

# Interpolate continuum fit
continuum_interpolated = interp1d(spec.spectral_axis, ycontfit)

# Define the wavelength point where you want to find the continuum value
wavelength_point = 5500  # Example wavelength point in Angstroms

# Find the continuum value at the specified wavelength point
continuum_value_at_point = continuum_interpolated(wavelength_point * u.AA)

print(f"At {wavelength_point} Angstroms, continuum value is: {continuum_value_at_point}")


# In[ ]:




