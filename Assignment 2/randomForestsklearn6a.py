from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import csv
import numpy as np
import random


with open("spam.data") as f:
    #    next(f, None)
        data = [tuple(line) for line in csv.reader(f, delimiter=" ",quoting=csv.QUOTE_NONNUMERIC)]
    
    # with open("wine-dataset.csv") as f:
    #     next(f, None)
    #     mutableData = [list((line)) for line in csv.reader(f, delimiter=",",quoting=csv.QUOTE_NONNUMERIC)]
  #  print "Number of records: %d" % (len(data))
  
random.shuffle(data)    
trainData = []
testData = []
for x in range(3221):
    trainData.append(data[x])
for x in range(3221, 4601):
    testData.append(data[x])
#print(len(testData), len(trainData))        
numberOfTrees = 25
m = 8
trainLables = []
trainFeatures = []
for x in trainData:
	trainLables.append(x[-1])
	trainFeatures.append(list(x[:-2]))
testLables = []
testFeatures = []
for x in testData:
	testLables.append(x[-1])
	testFeatures.append(list(x[:-2]))

rfClf = RandomForestClassifier(n_estimators= numberOfTrees,max_features  = 8 )
rfClf.fit(trainFeatures,trainLables)

prediction = rfClf.predict(testFeatures)
print("m = ",m,"accuracy = ",accuracy_score(testLables,prediction ))

