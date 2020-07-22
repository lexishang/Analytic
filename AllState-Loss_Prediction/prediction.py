#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:08:10 2020

@author: qtangzhu
"""

#import prediction_lib as pred
#from prediction_lib_class import loss_prediction_eng, Model_Lasso, Model_Ridge
from prediction_lib_class_ABC import loss_prediction_eng, Model_Lasso, Model_Ridge


# step 1 load data
data_path='~/pythoncourse/AllState'
file_train='training_120.csv'
file_test='test.csv'

# =============================================================================
# # the following code uses definition function to finish the steps
# df=pred.load_data(data_path,file_train,file_test)
# 
# # step 2 data processing
# pred.data_processing()
# 
# # step 3 - loss prediction
# pred.loss_prediction()
# 
# # the above code uses definition function to finish the steps
# =============================================================================

# =============================================================================
# # the following code uses class loss_prediction_eng to finish the steps
# 
# # step 0 set up the eng
# pred_eng=loss_prediction_eng()
# pred_eng.setup_eng(data_path, file_train, file_test)
# 
# # step 1 load data
# pred_eng.load_data()
# 
# # step 2 data preprocessing
# pred_eng.data_processing()
# 
# # step 3 loss prediction
# pred_eng.loss_prediction()
# =============================================================================

# the following code you can choose the model as you wish
pred_eng_list=[]
#pred_eng_list.append(loss_prediction_eng())
pred_eng_list.append(Model_Lasso())
pred_eng_list.append(Model_Ridge())

for pred_eng in pred_eng_list:

    pred_eng.setup_eng(data_path, file_train, file_test)
    
    # step 1 load data
    pred_eng.load_data()
    
    # step 2 data preprocessing
    pred_eng.data_processing()
    
    # step 3 loss prediction
    pred_eng.loss_prediction(pred_eng.X, pred_eng.y)