'''
Created on Dec 21, 2015

@author: yu1
'''
from test._mock_backport import inplace

# import numpy as np
# from collections import Counter
# 
workingPath = "D:\\Kaggle\\\Prudential\\"
 
trainDataPath = workingPath + "test\\test.csv"
#outPath = workingPath + "train\\train_refine_sub22.csv"
# 
# 
# 
# f = open(trainDataPath, 'rb')
# fo = open(outPath,'wb')
# 
# # go through each line of the file
# x = 0
# y = []
# for line in f:
#     bits = line.split(',')
#     y.append(bits)
#     
#     x += 1
# 
# 
# f.close()
# 
# col_totals = zip(*y) 
# 
# for i in range(0,len(col_totals)):
#     c = Counter(col_totals[i])
#     tmpMaj= c.most_common(1)[0][0].rstrip()
#     if (tmpMaj and not tmpMaj.isspace()):
#         tmp = 1
#     else:
#         tmpMaj= c.most_common(2)[1][0].rstrip()
#     print "tmpMaj:" ,tmpMaj
#     for j in range(0, len(col_totals[i])):
#         if col_totals[i][j] and not col_totals[i][j].isspace():
#             #print x, bits[2]
#             tmp = 1
#         else:
# #             y[i][j] = tmpMaj
# #             tmp = 1
# #             if i ==3:
# #                 tmp = 1
#             
#             if col_totals[i][j] == "\r\n":
#                 #print col_totals[i][j].splitlines()[0]
#                 y[j][i] = tmpMaj + "\r\n"
#             else:
#                 y[j][i] = tmpMaj
#             
# 
# print y
# # c = Counter([1,2,3,4,4,4,4,4])
# # print c.most_common(1)[0][0]
# fo.close()

import pandas as pd

## 1. read csv data in
df = pd.read_csv(trainDataPath, header =0, sep=',')
trainGt = df[df.columns[0]]

## 2. data pre-processing
## 2.1 convert string feature to numeric feature
col3 = df[df.columns[3]]
di = dict( zip(set(col3), range(0, len(set(col3)))))
df[df.columns[3]] = df.replace({df.columns[3]:di})


 ## 2.2 fill NaN by categorical or numeric
for i in range(0, len(df.columns)):
    print 'fill NaN: ', i, '/',  len(df.columns)
 
    tmpReplaceVal = 0
    if len(set(df[df.columns[i]])) < len(df[df.columns[i]])* 0.8:
        tmpReplaceVal = df[df.columns[i]].mode().iloc()[0]
    else:
        tmpReplaceVal = df[df.columns[i]].mean()
        
    df[df.columns[i]].fillna(tmpReplaceVal,inplace = True)

    
## 3. first col is the ground truth, so we drop it
df = df.drop(df.columns[0],axis=1)
trainData = df

print trainData
outputPathName = trainDataPath.replace(".csv","_refine.csv")
trainData.to_csv(outputPathName, sep=',', encoding='utf-8')