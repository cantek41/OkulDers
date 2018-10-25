#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 08:48:27 2018

@author: can
"""

import pandas as pd

f=pd.read_excel("ornek1.xlsx")

for i in f.index:
    ad=f["DosyaAd"][i]
    print(ad)
    open(ad, "x")
    

import os


for i in f.index:
    ad=f["DosyaAd"][i]
    kad=ad[9:11]
    if not os.path.exists(kad):
        os.mkdir(kad)
    open(kad+"/"+ad,"x")

for i in f.index:
    ad=f["DosyaAd"][i]
    os.remove(ad)
#    open(ad, "x")
