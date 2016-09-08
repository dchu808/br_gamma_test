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
    ##width is size of box in pixels, centered around center pixels - make this an odd number
    ##start and finish represent the end points of the spectral channels to sample

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
    
    #print len(files_list)
    
    ##make an array of the pixels, centered around the center pixel
    box_width = (width - 1)/2
    
    ##create a matrix to store all the results from the frames
    outputs = np.zeros((len(files_list),width,width))
    
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
        cax = ax1.imshow(np.sum(new_data_cube, axis=2), cmap="hot", origin="lower")
        plt.colorbar(cax)
        plt.title(files_list[i])
        plt.xlabel('Center Y Pixel at %d'%centers_array[i][1])
        plt.ylabel('Center X Pixel at %d'%centers_array[i][0])
        ##clarifying some tickmark labels, have center array be at 0
        x = np.arange(width)
        labels = np.arange(-1*box_width,box_width+1,1)
        plt.xticks(x,labels)
        ##do the same for plot y-axis
        plt.yticks(x,labels)
        #print np.sum(new_data_cube, axis=2)
        outputs[i] = np.sum(new_data_cube, axis=2)
        # print np.sum(new_data_cube, axis=2).shape
        plt.show()
        
    print outputs
    
    ##think about how to compare the different outputs

    
    ##standard deviation
    ##calculate the standard deviation along the summed spectral axis for all the files
    output_std = np.std(outputs,axis=0)
    print output_std
    
    ##plot the standard deviation
    std_fig = plt.figure()
    ax1 = std_fig.add_subplot(1,1,1)
    cax = ax1.imshow(output_std, cmap="hot", origin="lower")
    plt.colorbar(cax)
    plt.title('Standard Deviation')
    plt.show()
    
    ##residuals
    ##compare the residuals between each of the frames
    
