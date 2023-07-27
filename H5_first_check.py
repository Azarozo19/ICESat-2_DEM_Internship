# In[1]:

import os, glob, h5py, glob, sys, warnings, tqdm
import pandas as pd
import numpy as np
import geopandas as gp
from pyproj import Transformer
from pyproj import proj
import matplotlib.pyplot as plt
from timeit import default_timer as timer


sys.path.append(r'C:\Users\Sebastian\U\Spatial\Internship\Bodo_website\ICESat-2_SVDA-main\python')

#from SVDA_helper_functions import *
from SVDA_functions import *

#The ATL03_20200320133708_12950614_003_01.h5 file is 4.7GB and is available at https://nsidc.org/data/ATL03
ATL03_input_path = r'C:\Users\Sebastian\U\Spatial\ATL03\ATL03_20191030041540_05080506_005_01.h5'
ATL03 = h5py.File(ATL03_input_path,'r')

# new list "gtr", filled with every key that starts with "gt"
gtr = [g for g in ATL03.keys() if g.startswith('gt')]

# Retrieve datasets
for b in gtr:
    start = timer()
    attribute_lat_ph = b + '/heights/lat_ph'
    lat_ph = np.asarray(ATL03[attribute_lat_ph])
    attribute_lon_ph = b + '/heights/lon_ph'
    lon_ph = np.asarray(ATL03[attribute_lon_ph])
    attribute_h_ph = b + '/heights/h_ph'
    h_ph = np.asarray(ATL03[attribute_h_ph])
    #print(len(h_ph))
    attribute_signal_conf_ph = b + '/heights/signal_conf_ph'
    signal_conf_ph = np.asarray(ATL03[attribute_signal_conf_ph])
    #print(len(signal_conf_ph))

    ind, = np.where((lat_ph > 30.8) & (lat_ph < 32.1))
    #ind2, = np.where(signal_conf_ph[:,0] > 0)
    #ind = np.intersect1d(ind, ind2)
    fig, ax = plt.subplots(figsize=(10,6))
    #[::10]
    ax.scatter(lat_ph[ind], h_ph[ind], c=signal_conf_ph[:,0][ind], s=0.6); 
    ax.set_title(f'{b}')
    ax.set_ylabel('Elevation [m]')
    ax.set_xlabel('Latitude [°]')
    end = timer()
    print(f'done in {(end-start):.1f}s\n\n')







