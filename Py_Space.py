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
import shutil


class MTC:
    def __init__(self):
        self.ClassName = type(self).__name__ + '.'
        warnings.simplefilter("ignore")

    def Create_PySpace(self, PySpace, Remove_if_Exists=True):
        if Remove_if_Exists is True:
            if os.path.exists(PySpace):
                shutil.rmtree(PySpace, ignore_errors=True)
        if not os.path.exists(PySpace):
            os.makedirs(PySpace)
        return PySpace

if __name__ == '__main__':
    PY = MTC()
