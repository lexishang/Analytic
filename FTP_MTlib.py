#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:23:33 2020

@author: lexishang
"""

from ftplib import FTP
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import current_thread
import time
import configparser

config=configparser.ConfigParser()
config.read('/home/lexishang/pythoncourse/Insurance-loss/Analytics/AllStatePrediction/POC/configuration/ftp_connections/loss_records_config.properties')

ftp_config_list=[]

for office in config.sections():
    ftp_config={}
    ftp_config['host']=config[office]['host'] # connect to host
    ftp_config['user']=config[office]['user']
    ftp_config['pass']=config[office]['pass']
    ftp_config['remote_dir']=config[office]['remote_dir']
    ftp_config['local_dir']=config[office]['local_dir']
    ftp_config_list.append(ftp_config)
    
#print(ftp_config_list)
#path_to_loss_records='/home/lexishang/pythoncourse/AllState/loss_records_from_regional_office'
#site_list=['allstate_1','allstate_2','allstate_3']
file_list=[]

def download_data(file):
    print(f'thread {current_thread().name} is running')
    file=file[0]
    file_config=file[0]
    file=file[1]
    ftp=FTP(file_config['host']) # connect to host
    ftp.login(file_config['user'],file_config['pass'])
    ftp.cwd(file_config['remote_dir'])
    
    with open(ftp_config['local_dir'] + '/'+file,'wb') as fp:
        ftp.retrbinary('RETR'+file,fp.write)
    ftp.quit()
    return(f'thread {current_thread().name} is complete')

start=time.time()

for file_config in ftp_config_list:
    ftp=FTP(file_config['host']) # connect to host
    ftp.login(ftp_config['user'],ftp_config['pass'])
    ftp.cwd(ftp_config['remote_dir'])
    
    files=ftp.nlst()
    files.remove('.')
    files.remove('..')
    
    for file in files:
        file_list.append([file_config,file])    
    ftp.close()


with ThreadPoolExecutor(max_workers=2) as exe:
    results=[exe.submit(download_data, (file,)) for file in file_list]
    for r in as_completed(results):
        print(r.result())

print('The total download time taken is {}'.format(time.time()-start))
