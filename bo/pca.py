'''
Created on Dec 1, 2015

@author: yu1
'''
import numpy as np
from sklearn.decomposition import PCA
import time

class PCAHelper:

    pcaTimeUsed = 0.0
    def doPca(self, inputArr, dim, **options):
        outputTxtPath = options.get("outputTxtPath")
        
        pca = PCA(n_components=dim)
        
        start = time.time()
        pca.fit(inputArr)
        end = time.time()
        self.pcaTimeUsed = end - start    
        
        if outputTxtPath and not str(outputTxtPath).isspace():
            np.savetxt(outputTxtPath, pca.transform(inputArr), delimiter=',') 
        return pca.transform(inputArr)


if __name__ == '__main__':
    testArr = [[1, 2, 3], [2, 2, 5], [3, 0, -3], [2, -10, -4]]
    dim = 2
    aPCAHelper = PCAHelper()
    aPCAHelper.doPca(testArr, dim, outputTxtPath="F:\\test.txt")
    print aPCAHelper.pcaTimeUsed
