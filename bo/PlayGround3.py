'''
Created on Dec 21, 2015

@author: yu1
'''
from test._mock_backport import inplace
import time

start = time.time()


# import numpy as np
# from collections import Counter
# 
workingPath = "D:\\Kaggle\\\Prudential\\"
 
trainDataPath = workingPath + "train\\train.csv"


import pandas as pd

## 1. read csv data in
df = pd.read_csv(trainDataPath, header =0, sep=',')
trainGt = df[df.columns[0]]

## 2. data pre-processing
## 2.1 convert string feature to numeric feature
col3 = df[df.columns[3]]
# print df[df.columns[3]]
di = {'A7': 10, 'D1': 18, 'D2': 16, 'D3': '17', 'A1': 5, 'A8': 13, 'A3': 6, 'A2': 7, 'A5': 8, 'A4': 3, 'B2': 1, 'A6': 11, 'C3': 12, 'C2': 0, 'C1': 9, 'C4': 15, 'E1': 2, 'D4': 14, 'B1': 4}
df.replace({df.columns[3]:di}, inplace=True)
# print df[df.columns[3]]

## 2.2 Missing Data: fill NaN by categorical or numeric
categoricalIdx =[]
for i in range(1, len(df.columns)):
    print 'fill NaN: ', i, '/',  len(df.columns)
  
    tmpReplaceVal = 0
    if len(set(df[df.columns[i]])) < len(df[df.columns[i]])* 0.8:
        tmpReplaceVal = df[df.columns[i]].mode().iloc()[0]
        print df.columns[i], "is categorical data"
        categoricalIdx.append(df.columns[i])
    else:
        tmpReplaceVal = df[df.columns[i]].mean()
        print df.columns[i], "is numerical data"
         
    df[df.columns[i]].fillna(tmpReplaceVal,inplace = True)

## 2.3 convert categorical features to Nx1 columns

for i in range(0, len(categoricalIdx)):
    tmp = pd.get_dummies(sorted(df[categoricalIdx[i]]))
    
    df = pd.concat([df, tmp], axis=1).astype('float32')
    for j in range(0, len(tmp.columns)):
        newName = categoricalIdx[i] + "_" + str(j)
        df.rename(columns={tmp.columns[j]: newName}, inplace=True)
    print "drop",categoricalIdx[i]
    df.drop(categoricalIdx[i],axis=1,inplace = True)

#print df[df.columns[3]]
#print pd.get_dummies(df[df.columns[3]])

## 3. first col is the ground truth, so we drop it
df = df.drop(df.columns[0],axis=1)
trainData = df
 
print trainData
outputPathName = trainDataPath.replace(".csv","_refine.csv")
trainData.to_csv(outputPathName, sep=',', encoding='utf-8')

end = time.time()
elapsed = end - start
print "elapsed:", elapsed ,"sec"


# modelPath = 'D:\\Kaggle\\DigitRecognizer\\' + 'myModel_' +str(svcC)+'_' + str(svcGamma)+'.pkl'
# # print "train data runtime: " , time.time() - t0, "seconds process time"
# joblib.dump(clf, modelPath)