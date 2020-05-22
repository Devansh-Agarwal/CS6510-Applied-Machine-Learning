# CS6510 HW 1 Code Skeleton
# Please use this outline to implement your decision tree. You can add any code around this.

import csv
import numpy as np
import random
import statistics # used for mean 
# Enter You Name Here
myname = "Devansh-Agarwal-" # or "Doe-Jane-"

# Code takes about 10 secs on an i7
# Implement your decision tree below
# tree is implemented using dictionery 
class DecisionTree():
    tree = {}
    root = 0
    m = 8
    counter = 0
    def learn(self, training_set, numAtt):
        # implement this function
        self.m = numAtt
        nodeEntropy = self.getEntropy(training_set) # getting entropy of current Node
        infoGain = 0.0
        position = 0.0
        maxGain = 0.0 
        splitValue = 0.0
        attribuites = set()
        while len (attribuites) < self.m:
            attribuites.add(random.randint(0,56)) 
        #print(attribuites)    
        # split value is equal to the mean of the attribuite which reduces the entropy most
        for i in attribuites:
            sum = 0.0
            mean = 0.0
            temp1 = []
            for row in training_set :
                temp1.append(row[i])    
            mean = statistics.mean(temp1)
        # calculating the infogain for each attribuite mean splitting
            infoGain =nodeEntropy- self.getEntropy(training_set, False, mean, i)
            #print infoGain
            if maxGain < infoGain:
                maxGain = infoGain
                position = i
                splitValue = mean
        #if maxGain is greater than 0 then do not make it a leaf node and continue splitting        
        if maxGain > 0 :
            leftPartition, rightPartion = self.getPartitions(training_set,splitValue,position)
            #getting the key for the current node
            key = random.randint(0, 1000000)
            while key in self.tree:
                key = random.randint(0, 1000000)
            #left,right,attribuitePosition,splitvalue,isleaf, class
            self.tree[key] = (self.learn(leftPartition, self.m),self.learn(rightPartion,self.m),position,splitValue,False,None)    
            self.counter = self.counter + 1
            return key
        # if info gain is zero 
        else:
            key = random.randint(0, 1000000)
            while key in self.tree:
                key = random.randint(0, 1000000)
            #left,right,attribuitePosition,splitvalue,isleaf, class
            self.tree[key] = (None, None,None,None,True, training_set[0][len(training_set[0])-1])
            self.counter = self.counter + 1
            return key    
            

    
    # implement this function
    # iterating the tree in a fashion similar to binary search tree
    def classify(self, test_instance):
        result = 0 # baseline: always classifies as 0
        currentNode = self.root
        while ((self.tree.get(currentNode))[4] == False):
            temp = (self.tree.get(currentNode))
          #  print(temp[2])
            if(test_instance[temp[2]] < temp[3]):
                currentNode = temp[0]
            #    print temp[0]
            else:
                currentNode = (self.tree.get(currentNode))[1]    
        return self.tree.get(currentNode)[5]

    # spliting the date based on the split value     
    def getPartitions(self,partition,splitValue, position):
          leftPartition, rightPartion = [] ,[]
          for row in partition:
              if row[position] < splitValue:
                  leftPartition.append(row)
              else:
                  rightPartion.append(row)
          return leftPartition,rightPartion            

    # function to calculate entropy of the current node or the child nodes
    # flag is true if entropy for single node is calculated
    def getEntropy(self,partition,f1 = True, splitValue = 0.0, attr = 0) :
        count1 = 0.0
        count0 = 0.0
        count2 = 0.0
        count3 = 0.0
        entropy = 0.0
        entropy2 = 0.0
        total = 0.0
        total2 = 0.0

        if f1 :
            for row in partition :
                if(row[len(row) -1 ] == 0):
                    count0 = count0 + 1
                else:
                    count1 = count1 + 1
            total = count1 + count0
            if(count1 != 0 and count0 != 0) :
                p0 = count0 / total
                p1 = count1 / total     
                entropy  = - ((p0 * np.log2(p0)) + (p1 * np.log2(p1)))
            return entropy
        else:
            for row in partition :
                if row[attr] <= splitValue:
                    if(row[len(row) -1 ] == 0):
                        count0 = count0 + 1
                    else:
                        count1 = count1 + 1
                else :
                    if(row[len(row) -1 ] == 0):
                        count2 = count2 + 1
                    else:
                        count3 = count3 + 1        
            total = count1 + count0
            total2 = count2 + count3
            if(count1 != 0 and count0 != 0) :
                p0 = count0 / total
                p1 = count1 / total     
                entropy  = - ((p0 * np.log2(p0)) + (p1 * np.log2(p1)))
            if(count2!=0 and count3 != 0):
                p0 = count2 / total2
                p1 = count3 / total2    
                entropy2  = - ((p0 * np.log2(p0)) + (p1 * np.log2(p1)))
            totalEntropy = (total/(total+total2))* entropy + (total2/(total+total2))* entropy2  
            return totalEntropy                
def createSplit(partition):
    pass

def run_decision_tree():

    # Load data set
    with open("spam.data") as f:
    #    next(f, None)
        data = [tuple(line) for line in csv.reader(f, delimiter=" ",quoting=csv.QUOTE_NONNUMERIC)]
    
   
    random.shuffle(data)
    trainData = []
    testData = []
    #partitioning data
    for x in range(3221):
        trainData.append(data[x])
    for x in range(3221, 4601):
        testData.append(data[x])        

    numberOfTrees = 21
    a = 8
    forest = []
    forestData = []
    
    #creating data set
    for t in range(numberOfTrees):
        tempData = []
        for x in range(3221):
            tempData.append(trainData[random.randint(0,3220)])
        forestData.append(tempData)
    #learning
    for t in range(numberOfTrees):
        tree = DecisionTree()
        tree.root = tree.learn(forestData[t],a)
        forest.append(tree)    
    results = []
    #testing    
    for instance in testData:
        numZeros = 0
        numOnes = 0
        for treee in forest:
            result = treee.classify(instance[:-1])    
            if(int(result) == 0):
                numZeros +=1
            else:
                numOnes += 1
        if(numOnes > numZeros):
            results.append(1 == int(instance[-1]))
        else:
            results.append(0 == int(instance[-1]))             
    iterAccuraccy= float(results.count(True))/float(len(results))
    print("m = ",a,", Test accuracy = ", 	iterAccuraccy)
    

if __name__ == "__main__":
    run_decision_tree()
