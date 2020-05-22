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


svmClf = svm.SVC(kernel='linear')
svmClf.fit(trainFeatures,trainLables)

prediction = svmClf.predict(testFeatures)
print("accuracy", accuracy_score(testLables,prediction ))

print("Number of support vectors", len(svmClf.support_vectors_))