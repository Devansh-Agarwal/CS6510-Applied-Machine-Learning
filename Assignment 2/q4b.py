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


trainFeatures50 = []
trainLables50 = []
for x in range(50):
    trainFeatures50.append(trainFeatures[x])
    trainLables50.append(trainLables[x])
svmClf50 = svm.SVC(kernel='linear')
svmClf50.fit(trainFeatures50,trainLables50)
prediction50 = svmClf50.predict(testFeatures)

print("for 50 points:")
print("accuracy",accuracy_score(testLables,prediction50 ))
print("number of support vectors",len(svmClf50.support_vectors_))

trainFeatures100 = []
trainLables100 = []
for x in range(100):
    trainFeatures100.append(trainFeatures[x])
    trainLables100.append(trainLables[x])
svmClf100 = svm.SVC(kernel='linear')
svmClf100.fit(trainFeatures100,trainLables100)
prediction100 = svmClf100.predict(testFeatures)


print("for 100 points:")
print("accuracy",accuracy_score(testLables,prediction100 ))
print("number of support vectors",len(svmClf100.support_vectors_))


trainFeatures200 = []
trainLables200 = []
for x in range(200):
    trainFeatures200.append(trainFeatures[x])
    trainLables200.append(trainLables[x])
svmClf200 = svm.SVC(kernel='linear')
svmClf200.fit(trainFeatures200,trainLables200)
prediction200 = svmClf200.predict(testFeatures)

print("for 200 points:")
print("accuracy",accuracy_score(testLables,prediction200 ))
print("number of support vectors",len(svmClf200.support_vectors_))


trainFeatures800 = []
trainLables800 = []
for x in range(800):
    trainFeatures800.append(trainFeatures[x])
    trainLables800.append(trainLables[x])
svmClf800 = svm.SVC(kernel='linear')
svmClf800.fit(trainFeatures800,trainLables800)
prediction800 = svmClf800.predict(testFeatures)

print("for 800 points:")
print("accuracy",accuracy_score(testLables,prediction800 ))
print("number of support vectors",len(svmClf800.support_vectors_))

