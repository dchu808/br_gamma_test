##test different versions of comsic ray module to see effectiveness
## D. Chu - 2016-11-02

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import astropy.io
from astropy.io import fits
import pyfits as pf
from matplotlib.backends.backend_pdf import PdfPages

def plots(file_name):
    ##file name should be the reduced cube
    ##the name will always be the same
    ##don't
    
    ##grab no_cosmic_ray first
    ##this file did not have clean cosmic ray
    no_cr_data, header = pf.getdata('/u/devinchu/OSIRIS/cosmic_ray_sky_test/cr_skies/no_cosmic_ray/'+file_name, header=True)
    # noise = pf.getdata('/u/devinchu/OSIRIS/cosmic_ray_sky_test/cr_skies/old_cosmic_ray/'+file_name, ext=1)
    no_cr_quality = pf.getdata('/u/devinchu/OSIRIS/cosmic_ray_sky_test/cr_skies/old_cosmic_ray/'+file_name, ext=2)
    
    # print no_cr_data[:,:,10]
    
    ##old cosmic ray
    ##uses clean cosmic ray from develop branch
    old_cr_data, header = pf.getdata('/u/devinchu/OSIRIS/cosmic_ray_sky_test/cr_skies/old_cosmic_ray/'+file_name, header=True)
    old_cr_quality = pf.getdata('/u/devinchu/OSIRIS/cosmic_ray_sky_test/cr_skies/old_cosmic_ray/'+file_name, ext=2)
    
    ##new cosmic ray
    ##uses clean cosmic ray from develop branch
    new_cr_data, header = pf.getdata('/u/devinchu/OSIRIS/cosmic_ray_sky_test/cr_skies/new_cosmic_ray/'+file_name, header=True)
    new_cr_quality = pf.getdata('/u/devinchu/OSIRIS/cosmic_ray_sky_test/cr_skies/new_cosmic_ray/'+file_name, ext=2)
    
    ##plot figure
    fig = plt.figure(figsize = (10,16))

    ax1 = fig.add_subplot(2,3,1)
    cax = ax1.imshow(no_cr_data[:,:,10], cmap="hot", origin="lower",interpolation="nearest")
    plt.title(file_name)
    