from sklearn import svm
from sklearn.metrics import accuracy_score
trainingData = []
testingData = []

f = open("features.train", "r")
for line in f:
    tempArray = []
    for word in line.split():
        tempArray.append(float(word))
    trainingData.append(tempArray)
f = open("features.test", "r") 
for line in f:
    tempArray = []
    for word in line.split():
        tempArray.append(float(word))
    testingData.append(tempArray)

trainLables = []
trainFeatures = []
testLables = []
testFeatures = []
for row in trainingData:
    if(row[0] == 5.0 or row[0] == 1.0):
        tempArray = []
        tempArray.append(row[1])
        tempArray.append(row[2])
        trainFeatures.append(tempArray)
        if(row[0] == 1.0):
            trainLables.append(1)
        else:
            trainLables.append(-1)
for row in testingData:
    if(row[0] == 5.0 or row[0] == 1.0):
        tempArray = []
        tempArray.append(row[1])
        tempArray.append(row[2])
        testFeatures.append(tempArray)
        if(row[0] == 1):
            testLables.append(1)
        else:
            testLables.append(-1)
cvalues = [0.01, 1, 100, 10 **4, 10 ** 6]
for c in cvalues:
    svmRbfClf = svm.SVC(C = c,kernel= "rbf", gamma = 1)
    svmRbfClf.fit(trainFeatures,trainLables)
    prediction = svmRbfClf.predict(trainFeatures)
    print("C= ",c, ", train error = ", 1- accuracy_score(trainLables,prediction ))

print("\n\n")
for c in cvalues:
    svmRbfClf = svm.SVC(C = c,kernel= "rbf", gamma = 1)
    svmRbfClf.fit(trainFeatures,trainLables)
    prediction = svmRbfClf.predict(testFeatures)
    print("C= ",c, ", test error", 1- accuracy_score(testLables,prediction ))