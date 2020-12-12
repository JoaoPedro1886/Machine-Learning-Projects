# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 00:48:16 2020

@author: Joao Pedro
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import pandas as pd
import random
filename = "DADOS\MICRODADOS_ENEM_2018.csv"
n = sum(1 for line in open(filename)) - 1 #number of records in file (excludes header)
s = 500000 #desired sample size
skip = sorted(random.sample(range(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
data = pd.read_csv(r"DADOS\MICRODADOS_ENEM_2018.csv",encoding="Latin1",sep=";",skiprows=skip)
data= data.sample(500000,axis=0)
data = data[["TP_SEXO","NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT","TP_STATUS_REDACAO","NU_NOTA_REDACAO","Q027"]]
data = data.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
data['MEDIATOTAL'] = (data['NU_NOTA_MT'] + data['NU_NOTA_LC'] + data['NU_NOTA_CN'] + data['NU_NOTA_CH'])/4
data.MEDIATOTAL.describe
data1 = data[data['TP_SEXO'] == 'M']
data1 = data1[data1['Q027'] == 'D']
data2 = data[data['TP_SEXO'] == 'F']
data2 = data2[data2['Q027'] == 'D']
y1=data1.MEDIATOTAL.quantile(np.arange(0.01,1,0.01),'linear')
y2=data2.MEDIATOTAL.quantile(np.arange(0.01,1,0.01),'linear')
x=np.arange(1,100,1)
fig, ax = plt.subplots()
ax.plot(x, y1)
ax.plot(x, y2,'r')
plt.show()