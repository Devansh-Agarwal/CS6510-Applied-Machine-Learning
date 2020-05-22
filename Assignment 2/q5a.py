from sklearn import svm
from sklearn.metrics import accuracy_score
trainFeatures = []
trainLables = []
f = open("gisette_train.data", "r")
for line in f:
    tempArray = []
    for word in line.split():
        tempArray.append(float(word))
    trainFeatures.append(tempArray)
f = open("gisette_train.labels", "r") 
for line in f:
    tempArray = []
    for word in line.split():
        tempArray.append(float(word))
    trainLables.append(tempArray)
# print(len(trainLables),len(trainFeatures))

testFeatures = []
testLables = []
f = open("gisette_valid.data", "r")
for line in f:
    tempArray = []
    for word in line.split():
        tempArray.append(float(word))
    testFeatures.append(tempArray)
f = open("gisette_valid.labels", "r") 
for line in f:
    tempArray = []
    for word in line.split():
        tempArray.append(float(word))
    testLables.append(tempArray)
# print(len(testLables),len(testFeatures))

# print(len(trainFeatures))
svmClf = svm.SVC(kernel='linear')
svmClf.fit(trainFeatures,trainLables)

prediction = svmClf.predict(testFeatures)
print("Test error",1- accuracy_score(testLables,prediction ))
prediction = svmClf.predict(trainFeatures)
print("Train error", 1-accuracy_score(trainLables,prediction ))
print("number of support vectors ", len(svmClf.support_vectors_))