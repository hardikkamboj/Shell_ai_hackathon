#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:24:48 2020

@author: hardik
"""

import pandas as pd
import numpy as np
import os
from glob import glob



#store here the directory where the files of wind data are present
wind_data_folder = '/home/hardik/shell.ai hackathon/resources/Shell_Hackathon Dataset/Wind Data'
# all the files in the folder
files = glob(os.path.join(wind_data_folder + '/*.csv'))

# print(len(files))

data_frames = {}
for file in files:
    name = file[-8:-4]
    data_frames[name] = pd.read_csv(file)
    

# for temp in sorted(data_frames):
#     print('Shape of {} data is {}'.format(temp,data_frames[temp].shape))
    

final_df = pd.concat([data_frames['2007'],data_frames['2008']])
# print(final_df.shape)
    
for temp in sorted(data_frames)[2:]:
    final_df = pd.concat([final_df,data_frames[temp]])
    
# print(final_df.shape)   

final_df.to_csv('full_wind_data.csv') 
    
    
    
    
    

    