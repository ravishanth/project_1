import pandas as pd
import numpy as np
import json, tempfile
import datetime, time
import os,sys,csv, xlrd, re
from bs4 import BeautifulSoup
import requests
import warnings
from datetime import timedelta
import wget
from zipfile import ZipFile
from titlecase import titlecase
import glob
import shutil, sys
import bs4
warnings.filterwarnings('ignore')

SPath = r"D:\\coding\\knoema\\knoema_datasets\\ECOTRM2021"

import Py_Space
PY = Py_Space.MTC()

PY_Space = os.path.join(tempfile.gettempdir(), 'ECOTRM2021_PY_Space')
print('PY_Space: ' + PY_Space)

PY.Create_PySpace(PY_Space)
Source_Export_Path = os.path.join(PY_Space, 'Source')
PY.Create_PySpace(Source_Export_Path)
#------------------------------------------------------------------------------------------------
#EXTRACTING THE LINKS FROM THE SOURCE
result = requests.get("https://github.com/OpportunityInsights/EconomicTracker/tree/main/data")
#result.text
soup = bs4.BeautifulSoup(result.text,"lxml")
#soup

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

download_link = []
for i in links:
    print(i)
    try:
        if i.find('.csv') != -1 :
            print('https://github.com/'+i)
            download_link.append('https://github.com/'+i)
                 
    except (AttributeError) as e:
        pass
#DOWNLOADING THE REQUIRED FILES
count = 0
for link in download_link:
    link = link.replace("https://github.com//","https://raw.githubusercontent.com/").replace("/blob","")
    print(link.split('/')[-1].split("%")[0] +"_"+ link.split('/')[-1].split("%")[-1].split("20")[-1])
    file_name = (link.split('/')[-1].split("%")[0] + "_" + str(count) + "_" + link.split('/')[-1].split("%")[-1].split("20")[-1])
    local_filename = os.path.join(Source_Export_Path,file_name )
    r = requests.get(link, stream=True)
    if r.status_code == 200:
        with open(local_filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    count = count + 1

#------------------------------------------------------------------------------------------------
