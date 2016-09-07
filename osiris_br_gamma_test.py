##test br gamma line is gas on different parts of detector
##does different part of detector lead to different reading?
## D. Chu - 2016-09-06

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import astropy.io
from astropy.io import fits
import pyfits as pf

##step 1 is read the .conf (config) file
##the .conf file is generated during the UCLA Galactic Center Group data analysis
##it marks the center positions of object in the different data cubes

def test(width = 5, start = 175, finish = 190):
    ##width is size of box in pixel, centered around center pixels - make this an odd number
    ##start and finish represent the end points of the spectral channels to sample
    ##ideally, this will be general and can take a .conf file (maybe? - depends on what we want to do)
    ##get list of file names from the .conf file
    files_list = np.genfromtxt('gas_130727_version2.conf', dtype=('S30'),delimiter=',',deletechars='',skip_footer=9)
    # print files_list
    # print files_list[0]
    ##get the centers of the gas from each file, also in the .conf file
    ##as of note, the .conf file has been modified to fit this array
    centers_array = np.loadtxt('gas_130727_version2.conf',skiprows=1)
    # print centers_array[0]
    # print centers_array[0][0]
    # print centers_array[0][1]
    # print centers_array.shape
    
    ##now with the list of files and the coordinates of the center positions
    ##the files can be looked at individually
    
    ##for now, start with 1st file - will make this a loop to loop through all files
    # data_cube_file = fits.open('test_data/'+files_list[0])
    # data_cube = data_cube_file[0].data
    
    # data_cube, header = pf.getdata('test_data/'+files_list[0], header=True)
    # noise = pf.getdata('test_data/'+files_list[0], ext=1)
    # quality = pf.getdata('test_data/'+files_list[0], ext=2)
    
    #print len(files_list)
    
    ##make an array of the pixels, centered around the center pixel
    box_width = (width - 1)/2
    
    ##loop through all the files to run the calculation
    for i in range(len(files_list)):
        data_cube, header = pf.getdata('test_data/'+files_list[i], header=True)
        noise = pf.getdata('test_data/'+files_list[i], ext=1)
        quality = pf.getdata('test_data/'+files_list[i], ext=2)
        
        ##make an array of x-pixels, centered around the center x-pixel, with a width given above
        x_array = np.arange(centers_array[i][0] - box_width,centers_array[i][0] + box_width + 1,step = 1)
        ##make an array of y-pixels, centered around the center y-pixel, with a width given above
        y_array = np.arange(centers_array[i][1] - box_width,centers_array[i][1] + box_width + 1,step = 1)
        
        ##make a smaller data cube, only including those pixels and spectral channels specified above
        ##make a cut only included given x-pixels, y-pixels, and spectral channels
        new_data_cube = data_cube[centers_array[i][0] - box_width:centers_array[i][0] + box_width + 1,
            centers_array[i][1] - box_width:centers_array[i][1] + box_width + 1,
            start:finish+1]
            
        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        ax1.imshow(np.sum(new_data_cube, axis=2), cmap="hot", origin="lower")
        #norm=LogNorm()
        print np.sum(new_data_cube, axis=2)
        plt.show()
    
    
    # print data_cube
    # print data_cube.shape[0]
    # print data_cube.shape[1]
    # print data_cube.shape[2]
    ##format is [x_pixel,y_pixel,spectral channel]
    # print data_cube[centers_array[0][0],centers_array[0][1],181]
    
    ##make an array of the pixels, centered around the center pixel
    # box_width = (width - 1)/2
    # print box_width
    ##make an array of x-pixels, centered around the center x-pixel, with a width given above
    # x_array = np.arange(centers_array[0][0] - box_width,centers_array[0][0] + box_width + 1,step = 1)
    ##test
    # x_array = np.arange(20 - box_width,20 + box_width + 1,step = 1)
    # print centers_array[0][0]
    # print x_array
    
    ##make an array of y-pixels, centered around the center y-pixel, with a width given above
    # y_array = np.arange(centers_array[0][1] - box_width,centers_array[0][1] + box_width + 1,step = 1)
    ##test
    # y_array = np.arange(35 - box_width,35 + box_width + 1,step = 1)
    # print centers_array[0][1]
    # print y_array
    
    #make a smaller data cube, only including those pixels and spectral channels specified above
    # new_data_cube = data_cube[centers_array[0][0] - box_width:centers_array[0][0] + box_width + 1,
    #     centers_array[0][1] - box_width:centers_array[0][1] + box_width + 1,
    #     start:finish+1]
    
    ##test    
    # new_data_cube = data_cube[20 - box_width:20 + box_width + 1,
    #     35 - box_width:35 + box_width + 1,
    #     start:finish+1]
        
    # print new_data_cube.shape[0]
    # print new_data_cube.shape[1]
    # print new_data_cube.shape[2]
    
    ##make a meshgrid for these pixel positions
    # (xi,yi) = np.meshgrid(x_array,y_array)
    # print (xi,yi)
    #
    ##need to sum over spectral channels at that pixel
    ##start at the initial spectral channel specified at the input
    # spec_chan_start = start
    # print spec_chan_start
    # spaxel_sum = 0.
    # while spec_chan_start < finish:
    #     spaxel_sum += data_cube[centers_array[0][0],centers_array[0][1],spec_chan_start]
    #     spec_chan_start += 1
    #     print spec_chan_start
    # print spaxel_sum
    
    # fig = plt.figure()
    # ax1 = fig.add_subplot(1,1,1)
    # ax1.imshow(np.median(data_cube, axis=2), cmap="hot", norm=LogNorm(), origin="lower")
    # plt.show()
    
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.imshow(np.sum(new_data_cube, axis=2), cmap="hot", norm=LogNorm(), origin="lower")
    print np.sum(new_data_cube, axis=2)
    plt.show()
		