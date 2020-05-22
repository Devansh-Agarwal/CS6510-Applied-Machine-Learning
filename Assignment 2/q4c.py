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

#false
print("part i")
svmPoly2Clf = svm.SVC(C = 0.0001,kernel= "poly",degree = 2, coef0 = 1, gamma = 1)
svmPoly2Clf.fit(trainFeatures,trainLables)
prediction = svmPoly2Clf.predict(trainFeatures)
print("for q = 2 c = 0.0001")
print("Training error",1- accuracy_score(trainLables,prediction ))
print("number of support_vectors",len(svmPoly2Clf.support_vectors_))

svmPoly5Clf = svm.SVC(C = 0.0001,kernel= "poly",degree = 5, coef0 = 1, gamma = 1)
svmPoly5Clf.fit(trainFeatures,trainLables)
prediction = svmPoly5Clf.predict(trainFeatures)

print("for q = 5 c = 0.0001")
print("Training error ",1- accuracy_score(trainLables,prediction ))
print("number of support_vectors",len(svmPoly5Clf.support_vectors_))


#true
print("\n\npart ii")
svmPoly2Clf = svm.SVC(C = 0.001,kernel= "poly",degree = 2, coef0 = 1, gamma = 1)
svmPoly2Clf.fit(trainFeatures,trainLables)
prediction = svmPoly2Clf.predict(testFeatures)
print("for q = 2 c = 0.001")
print("number of support_vectors",len(svmPoly2Clf.support_vectors_))
svmPoly5Clf = svm.SVC(C = 0.001,kernel= "poly",degree = 5, coef0 = 1, gamma = 1)
svmPoly5Clf.fit(trainFeatures,trainLables)
prediction = svmPoly5Clf.predict(testFeatures)
print("for q = 5 c = 0.001")
print("number of support_vectors",len(svmPoly5Clf.support_vectors_))


#false
print("\n\npart iii")
svmPoly2Clf = svm.SVC(C = 0.01,kernel= "poly",degree = 2, coef0 = 1, gamma = 1)
svmPoly2Clf.fit(trainFeatures,trainLables)
prediction = svmPoly2Clf.predict(trainFeatures)
print("for  q = 2 c = 0.01")
print("Training error",1- accuracy_score(trainLables,prediction ))
print("number of support_vectors",len(svmPoly2Clf.support_vectors_))
svmPoly5Clf = svm.SVC(C = 0.01,kernel= "poly",degree = 5, coef0 = 1, gamma = 1)
svmPoly5Clf.fit(trainFeatures,trainLables)
prediction = svmPoly5Clf.predict(trainFeatures)
print("for q = 5 c = 0.001")
print("Training error",1- accuracy_score(trainLables,prediction ))
print("number of support_vectors",len(svmPoly5Clf.support_vectors_))


#false
print("\n\npart iv")
svmPoly2Clf = svm.SVC(C = 1,kernel= "poly",degree = 2, coef0 = 1, gamma = 1)
svmPoly2Clf.fit(trainFeatures,trainLables)
prediction = svmPoly2Clf.predict(testFeatures)
print("for  q = 2 c = 1")
print("Test error",1- accuracy_score(testLables,prediction ))
print("number of support_vectors",len(svmPoly2Clf.support_vectors_))
svmPoly5Clf = svm.SVC(C = 1,kernel= "poly",degree = 5, coef0 = 1, gamma = 1)
svmPoly5Clf.fit(trainFeatures,trainLables)
prediction = svmPoly5Clf.predict(testFeatures)
print("for q = 5 c = 1")
print("Test error",1- accuracy_score(testLables,prediction ))
print("number of support_vectors",len(svmPoly5Clf.support_vectors_))