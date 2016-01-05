'''
Created on Dec 21, 2015

@author: yu1
'''

import numpy as np


workingPath  = "D:\\Kaggle\\\Prudential\\"

trainDataPath = workingPath +"train\\train_refine.csv"
outPath = workingPath +"train\\train_refine2.csv"
# trainDataPath = workingPath +"train\\train.csv"
# 
# trainData = np.genfromtxt(trainDataPath, delimiter=',', skiprows=1, dtype='str')
# trainGt= set(trainData[:,3])
# #trainData = numpyDelete(trainData, 0, axis=1)
d = {}
i=0
for member in trainGt:
    d[member] = i
    i = i+1
 
print d 


f = open(trainDataPath,'rb')
fo = open(outPath,'wb')

# go through each line of the file
for line in f:
    bits = line.split(',')
    # change second column
    if not bits[3] == "Product_Info_2":
        bits[3] = str(d[bits[3]])
    # join it back together and write it out
    fo.write( ','.join(bits) )

f.close()
fo.close()


