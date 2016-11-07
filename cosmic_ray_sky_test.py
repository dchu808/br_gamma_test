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
    no_cr_quality = pf.getdata('/u/devinchu/OSIRIS/cosmic_ray_sky_test/cr_skies/no_cosmic_ray/'+file_name, ext=2)
    
    # print no_cr_quality[10,10,5]
    # print no_cr_quality
    
    ##old cosmic ray
    ##uses clean cosmic ray from develop branch
    old_cr_data, header = pf.getdata('/u/devinchu/OSIRIS/cosmic_ray_sky_test/cr_skies/old_cosmic_ray/'+file_name, header=True)
    old_cr_quality = pf.getdata('/u/devinchu/OSIRIS/cosmic_ray_sky_test/cr_skies/old_cosmic_ray/'+file_name, ext=2)
    
    ##new cosmic ray
    ##uses clean cosmic ray from develop branch
    new_cr_data, header = pf.getdata('/u/devinchu/OSIRIS/cosmic_ray_sky_test/cr_skies/new_cosmic_ray/'+file_name, header=True)
    new_cr_quality = pf.getdata('/u/devinchu/OSIRIS/cosmic_ray_sky_test/cr_skies/new_cosmic_ray/'+file_name, ext=2)
    
    ##plot figure
    ##plot a pretty empty channel, with cosmic rays
    fig = plt.figure(figsize = (16,8))
    fig.suptitle(file_name, fontsize=18)

    ax1 = fig.add_subplot(2,3,1)
    cax = ax1.imshow(no_cr_data[:,:,5], cmap="hot", origin="lower",interpolation="nearest",vmin=0.,vmax=.51)
    ax1.set_title('Continuum Ch 5 - No Cosmic Ray')
    # plt.colorbar(cax,fraction=0.046, pad=0.04)
    
    ax2 = fig.add_subplot(2,3,2)
    cax = ax2.imshow(old_cr_data[:,:,5], cmap="hot", origin="lower",interpolation="nearest",vmin=0.,vmax=.51)
    ax2.set_title('Old Cosmic Ray')

    ax3 = fig.add_subplot(2,3,3)
    cax = ax3.imshow(new_cr_data[:,:,5], cmap="hot", origin="lower",interpolation="nearest",vmin=0.,vmax=.51)
    ax3.set_title('New Cosmic Ray')
    
    ax4 = fig.add_subplot(2,3,4)
    cax = ax4.imshow(no_cr_data[:,:,153], cmap="hot", origin="lower",interpolation="nearest",vmin=0.,vmax=.51)
    ax4.set_title('OH Lines Ch 153')
    
    ax5 = fig.add_subplot(2,3,5)
    cax = ax5.imshow(old_cr_data[:,:,153], cmap="hot", origin="lower",interpolation="nearest",vmin=0.,vmax=.51)
    ax5.set_title('Old Cosmic Ray')
    
    ax6 = fig.add_subplot(2,3,6)
    cax = ax6.imshow(new_cr_data[:,:,153], cmap="hot", origin="lower",interpolation="nearest",vmin=0.,vmax=.51)
    ax6.set_title('New Cosmic Ray')
    
    plt.show()
    # pp = PdfPages(file_name[0:24]+'.pdf')
    # pp.savefig()
    # pp.close()