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

print("rbf kernel")
svmRbfClf = svm.SVC(kernel= "rbf", gamma = 0.001)
svmRbfClf.fit(trainFeatures,trainLables)
prediction = svmRbfClf.predict(testFeatures)
prediction = svmRbfClf.predict(testFeatures)
print("Test error",1-  accuracy_score(testLables,prediction ))
prediction = svmRbfClf.predict(trainFeatures)
print("Train error", 1- accuracy_score(trainLables,prediction ))
print("number of support vectors", len(svmRbfClf.support_vectors_))

svmPolyClf = svm.SVC(kernel= "poly",degree = 2, coef0 = 1, gamma = 1)
svmPolyClf.fit(trainFeatures,trainLables)
prediction = svmPolyClf.predict(testFeatures)
prediction = svmPolyClf.predict(testFeatures)
print("Poly kernel")
print("Test error",1- accuracy_score(testLables,prediction ))
prediction = svmPolyClf.predict(trainFeatures)
print("Train error", 1- accuracy_score(trainLables,prediction ))
print("number of support vectors ", len(svmPolyClf.support_vectors_))
