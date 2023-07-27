#!/usr/bin/env python
# coding: utf-8

# # ATL08 data processing
# 
# Example steps to extract the desired data from an ICESat-2 ATL08 data product. The data are re-structured and organized into a pandas dataframe for each ground track.
# 
# **You will need to adjust the ATL08_input_path and ATL08_output_path in the next field. Also, you will need to change the ROI shapefile name and EPSG code for your own data.**

# In[1]:

import os, glob, h5py, glob, sys, warnings, tqdm
import pandas as pd
import numpy as np
import geopandas as gp
from pyproj import Transformer
from pyproj import proj

#sys.path.append('../python')

#from SVDA_helper_functions import *
from SVDA_functions import *


# Data extraction from ATL03 product (HDF5 formatted files)
# This example uses only a single file, the code can also take a directory full of files

#The ATL03_20200320133708_12950614_003_01.h5 file is 4.7GB and is available at https://nsidc.org/data/ATL03
ATL03_20200428193512 = '/DATA/Seb/internship/ATL03/fill_data/ATL03_20200428193512_05080706_005_01.h5'
ATL03_20200301222304 = '/DATA/Seb/internship/ATL03/fill_data/ATL03_20200301222304_10110606_005_01.h5'
ATL03_20200322211548 = '/DATA/Seb/internship/ATL03/fill_data/ATL03_20200322211548_13310606_005_01.h5'
ATL03_20200207112253 = "/DATA/Seb/internship/ATL03/fill_data/ATL03_20200207112253_06530602_005_01.h5"
ATL03_20210305163815 = "/DATA/Seb/internship/ATL03/fill_data/ATL03_20210305163815_10951002_005_01.h5"
ATL03_20210131181032 = "/DATA/Seb/internship/ATL03/fill_data/ATL03_20210131181032_05921002_005_01.h5"

# Output
ATL03_output_path = '/DATA/Seb/internship/ATL03/pc_pool/hdf/last_ATL'

#Region of interest to be clipped from ATL08 file:
ROI_fname = '/DATA/Seb/internship/ATL03/pc_pool/new_study_area/new_area-polygon.shp'
EPSG = 'epsg:7763'

# In[3]:


All_files = [ATL03_20200428193512, ATL03_20200301222304, ATL03_20200322211548,  ATL03_20200207112253, ATL03_20210305163815, ATL03_20210131181032]
# In[3]:

#for i in range(1):
for i in range (6):
    ATL03_files = list(glob.glob(All_files[i]))
    ATL03_files.sort()
    for fname in ATL03_files:
        ATL03_signal_photons(fname, ATL03_output_path, ROI_fname, EPSG, reprocess=False)







