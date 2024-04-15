# galaxyredshift

To determine the redshift of an object given its observed spectrum.

If a source moves away from the observer, the spectral lines get shifted toward the red end of the spectrum (& blue for blueshift)
eg: Galaxy appears green in the SDSS telescope

  
The spectrum of the Green pea galaxy (a Rapidly star-forming galaxy) is observed. The spectrum has a Gaussian profile 
(as shown in the spec.png - https://github.com/aryaa-9/galaxyredshift/blob/main/fitted_data.png).
If we select the strongest peak which is the forbidden Oxygen O(III) peaks in the range 6450 and 6600 nm 
(selectedwavelengths.png - https://github.com/aryaa-9/galaxyredshift/blob/main/selectedwavelegth.png, 
we can determine the redshift, as well as find the speed of the galaxy (non-relativistic case)

Considering the O(III) lines (4959 and 5007 lines), we can fit a non-linear function made by adding two Gaussian functions, and then find the peak positions 
(as shown in the spec_data.png -  https://github.com/aryaa-9/galaxyredshift/blob/main/fitted_data.png), and hence, the redshift
