import os
import numpy as np
import pandas as pd

def fileToDF(fPath):
    df = pd.read_csv(fPath,header=None)
    #drop name column , just need the ratings...
    df.drop([0], inplace=True, axis=1)
    #replace - with 0 (wont have conflict with existing ratings since 1 is the lowest rating so 0 means no rating is given...)
    df.replace("-","0",inplace=True)
    df = df.apply(pd.to_numeric)
    return df

directory = r'..\RPA\Ratings'
dfMatrixY = None
for filename in os.listdir(directory):
    filePath = os.path.join(directory, filename)
    #print(filePath)
    
    dfTmp = fileToDF(filePath)
    dfMatrixY = pd.concat([dfMatrixY,dfTmp], axis=1)
dfMatrixY.head()

Y = dfMatrixY.values
def tmp(x):
    if x == 0:
        return 0
    else:
        return 1
dfMatrixR = dfMatrixY.applymap(tmp)
dfMatrixR.head()
R = dfMatrixR.values

dfTmp = fileToDF("MyRatings.txt")
dfTmp.shape
myRatingsArray = dfTmp.values
myRatingsArray.shape
myRArray = myRatingsArray > 0
Y2 = np.hstack((Y,myRatingsArray))
R2 = np.hstack((R,myRArray))