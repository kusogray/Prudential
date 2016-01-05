'''
Created on Dec 6, 2015

@author: yu1
'''
import logging
import os
import time

from sklearn import svm, grid_search
from sklearn.externals import joblib

from bo.pca import PCAHelper as PCAHelper
from util.DataReader  import DataReader as DataReader
import numpy as np


# 1. load data
workingPath  = "D:\\Kaggle\\\Prudential\\"

productInfo2Hash = {'A7': 10, 'D1': 18, 'D2': 16, 'D3': 17, 'A1': 5, 'A8': 13, 'A3': 6, 'A2': 7, 'A5': 8, 'A4': 3, 'B2': 1, 'A6': 11, 'C3': 12, 'C2': 0, 'C1': 9, 'C4': 15, 'E1': 2, 'D4': 14, 'B1': 4}

dataReader = DataReader(workingPath +"train\\train_refine_sub2.csv")
dataReader.loadData()



# 
# aPCAHelper = PCAHelper()
# arrWith10 = aPCAHelper.doPca(dataReader.trainData, 10, outputTxtPath="F:\\test_10.csv")
# print 'pca to 10 dim spend time: ' , aPCAHelper.pcaTimeUsed
# aPCAHelper.doPca(dataReader.trainData, 2, outputTxtPath="F:\\test_2.csv")
# print 'pca to 2 dim spend time:' , aPCAHelper.pcaTimeUsed


#parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
# param_grid = [
#   {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
#   {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
# {'C': [1, 10, 100, 1000], 'degree': [1,2,3,4], 'kernel': ['poly']},
#  ]
# svr = svm.SVC()
# clf = grid_search.GridSearchCV(svr, param_grid)
# clf.fit(arrWith10, dataReader.trainGt)
# print "clf.best_estimator_: " , clf.best_estimator_
# print "clf.best_score_: " ,clf.best_score_



# print dataReader.trainGt
# print dataReader.trainData
# 

# # 2. run svm train
t0 = time.time()


C_range = 10.0 ** np.arange(-4, 4)
gamma_range = 10.0 ** np.arange(-4, 4)
param_grid = dict(gamma=gamma_range.tolist(), C=C_range.tolist())

svr = svm.SVC()
clf = grid_search.GridSearchCV(svr, param_grid)
clf.fit(dataReader.trainData, dataReader.trainGt)

# svcC = 1.0
# svcGamma = 9.9999999999999995e-07
# clf = svm.SVC(C=1.0, gamma=svcGamma, shrinking=True, verbose=False, tol=0.001)
# clf.fit(dataReader.trainData, dataReader.trainGt) 
# modelPath = workingPath + 'myModel_' +str(svcC)+'_' + str(svcGamma)+'.pkl'
# print "train data runtime: " , time.time() - t0, "seconds process time"
print "svm grid search runtime: " , time.time() - t0, "seconds process time"
# joblib.dump(clf, modelPath)
# clf = joblib.load( modelPath )



# 3. load test data
# test = np.loadtxt("D:\\Kaggle\\DigitRecognizer\\test.txt", delimiter=',', dtype = "int")
# print clf.predict(test)

# f = open('test','a+')
# outputResultTxtPath = "D:\\Kaggle\\DigitRecognizer\\test_output.txt"
# os.remove(outputResultTxtPath)
# hs = open(outputResultTxtPath,"a")


# dataReader.loadTestData("D:\\Kaggle\\DigitRecognizer\\test.csv")
# for i in range(0,len(dataReader.testData)):
#     #PngCvter.cvtToPng(dataReader.testData[i], "D:\\Kaggle\\DigitRecognizer\\test_png\\", i)
#     tmpResult = str(clf.predict(dataReader.testData[i]))
#     print tmpResult
#     tmpResult = tmpResult.replace("[","")
#     tmpResult = tmpResult.replace("]","")
#     hs.write(str(tmpResult) + "\n")
#     
# hs.close() 
#     
# print dataReader.testData
# print len(dataReader.testData)

# text_file = open("D:\\Kaggle\\DigitRecognizer\\Output.txt", "w")


# for i in range(0,len(dataReader.testData)):
# #    print clf.predict(dataReader.testData[i])
#    text_file.write(str(clf.predict(dataReader.testData[i]))+"\n")
#    
# text_file.close()
# print test
# X = [[0, 0], [1, 1]]
# y = [0, 1]
# clf = svm.SVC()
# clf.fit(X, y)  
# print clf.predict([[2., 2.]])
# np.loadtxt(test, delimiter=',', skiprows=1, dtype = "int")
# print test
