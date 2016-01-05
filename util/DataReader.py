import pandas as pd


class DataReader:
    __trainDataPath =""
    __testDataPath =""
    trainGt =[] ## ground truth = labels
    trainData =[]
    testData =[]
    
    def __init__(self, dataPath):
        self.__trainDataPath = dataPath


    def processData(self, outputCSVPath, **options):
        
        isTest = options.get("isTest")
        dataPath = self.__trainDataPath
        if isTest == True:
            dataPath = self.__testDataPath
        else:
            isTest = False
        
        ## 1. read csv data in
        df = pd.read_csv(dataPath, header =0, sep=',')
        if isTest == True:
            self.trainGt = df[df.columns[0]]
        
        ## 2. data pre-processing
        ## 2.1 convert string feature to numeric feature
        col3 = df[df.columns[3]]
        di = dict( zip(set(col3)), range(0, len(set(col3))))
        df[df.columns[3]] = df.replace({df.columns[3]:di})
        
        ## 2.2 fill NaN by categorical or numeric
        for i in range(0, len(df.columns)):
            #print 'fill NaN: ', i, '/',  len(df.columns)
         
            tmpReplaceVal = 0
            if len(set(df[df.columns[i]])) < len(df[df.columns[i]])* 0.8:
                tmpReplaceVal = df[df.columns[i]].mode().iloc()[0]
            else:
                tmpReplaceVal = df[df.columns[i]].mean()
                
            df[df.columns[i]].fillna(tmpReplaceVal,inplace = True)
            
        ## 3. first col is the ground truth, so we drop it
        df = df.drop(df.columns[0],axis=1)
        self.trainData = df
        
        
    def processTestData(self, outputCSVPath, inputDataPath):
        self.__testDataPath = inputDataPath
        self.testData = self.processData(outputCSVPath, isTest=True)
        

