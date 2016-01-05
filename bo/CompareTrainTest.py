'''
Created on Dec 21, 2015

@author: yu1
'''
from test._mock_backport import inplace
import time
import pandas as pd

start = time.time()

# import numpy as np
# from collections import Counter
# 
workingPath = "D:\\Kaggle\\\Prudential\\"
 
trainDataPath = workingPath + "train\\train_sub.csv"
testDataPath = workingPath + "test\\test.csv"
 

## 1. read csv data in
df = pd.read_csv(trainDataPath, header =0, sep=',')
trainGt = df[df.columns[0]]

## 2. data pre-processing
## 2.1 convert string feature to numeric feature
col3 = df[df.columns[3]]
di = {'A7': 10, 'D1': 18, 'D2': 16, 'D3': 17, 'A1': 5, 'A8': 13, 'A3': 6, 'A2': 7, 'A5': 8, 'A4': 3, 'B2': 1, 'A6': 11, 'C3': 12, 'C2': 0, 'C1': 9, 'C4': 15, 'E1': 2, 'D4': 14, 'B1': 4}
df[df.columns[3]] = df.replace({df.columns[3]:di})

df = pd.concat([df, pd.get_dummies(df.columns[3])], axis=1)

print df
