#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:58:31 2020

@author: lexishang
"""


import numpy as np
from ftplib import FTP
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import current_thread
import itertools 

path_to_loss_records='/home/lexishang/pythoncourse/AllState/loss_records_from_regional_office'
site_list=['allstate_1','allstate_2','allstate_3']
file_list=[]

for site in site_list:
    ftp=FTP('ftp.jobready123.com') # connect to host
    ftp.login(site+'@jobready123.com','Password@123')
    ftp.cwd('/AllState/RegionalOffice/loss_records')
    
    files=ftp.nlst()
    files.remove('.')
    files.remove('..')
    file_list.append(files)    
    ftp.close()

file_list=list(itertools.chain(*file_list))
print(file_list)
