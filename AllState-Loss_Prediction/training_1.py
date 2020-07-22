#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:08:10 2020

@author: qtangzhu
"""

#import prediction_lib as pred
#from prediction_lib_class import loss_prediction_eng, Model_Lasso, Model_Ridge
#from prediction_lib_class_ABC import loss_prediction_eng, Model_Lasso, Model_Ridge
import sys
from utility_lib import Allstate_Utility

# step 1 load data
data_path='~/pythoncourse/AllState/loss_records_to_process'
file_train='training.pkl'
file_pred='test.csv'

#ds=Allstate_Utility.load_data(data_path,file_train)

#print(ds[file_train.split('.')[0]].shape)

ds=Allstate_Utility.load_data_from_pickle(data_path,file_train)
print(ds[file_train.split('.')[0]].shape)

# =============================================================================
# ds=Allstate_Utility.data_processing(ds[file_train.split('.')[0]])
# ds=Allstate_Utility.prepare_data_for_model_training(ds[0])
# 
# print(ds['X'].shape)
# print(ds['y'].shape)
# 
# #import pandas as pd
# #import numpy as np
# from prediction_lib import AllState_Prediction_Eng, AllState_Lasso, Allstate_Ridge
# from sklearn.model_selection import train_test_split
# 
# X_train, X_test, y_train, y_test= train_test_split(ds['X'],ds['y'], test_size=0.33, random_state=0)
# ar=AllState_Lasso()
# ar.model_training(X_train, y_train)
# pred=ar.prediction(X_test)
# print(pred)
# =============================================================================
