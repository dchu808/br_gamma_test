##test br gamma line is gas on different parts of detector
##does different part of detector lead to different reading?
## D. Chu - 2016-09-06

import numpy as np
import matplotlib.pyplot as plt
import astropy.io
from astropy.io import fits

##step 1 is read the .conf (config) file
##the .conf file is generated during the UCLA Galactic Center Group data analysis
##it marks the center positions of object in the different data cubes

def test(conf_file_path):
	conf_file = open(conf_file_path,'r')
	##create a dictionary (or list) of files with their centers of the gas location
	files = []
	# files = {}
	##read through the config file
	##first line is a list of the files
	
	##this is only picking up the centers right now...
	for line in conf_file:
		file_list = line[0:2]
	print file_list
		