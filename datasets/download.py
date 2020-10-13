import os
import time
from zipfile import ZipFile
from kaggle.api.kaggle_api_extended import KaggleApi


def dnld_kaggle_data(dataset, filename, delete_zip=True):
    #MVP function to download data from kaggle
    
    t1  = time.time() 
    
    #connect
    api = KaggleApi()
    api.authenticate()

    #download
    print('Downloadnig...')
    api.dataset_download_file(dataset, filename)
   
    #extract
    if os.path.isfile(filename+'.zip'): 
        print('Extracting...')
        zf = ZipFile(filename+'.zip')
        zf.extractall() 
        zf.close()

        #delete
        if delete_zip:
            os.remove(filename+'.zip')
            
    os.replace(filename, 'data/'+filename)
    t2 = time.time()
    
    print(f'File ready! It took {round(t2-t1, 1)} seconds.')