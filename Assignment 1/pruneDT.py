# CS6510 HW 1 Code Skeleton
# Please use this outline to implement your decision tree. You can add any code around this.

import csv
import numpy as np
import random
import statistics
# Enter You Name Here
myname = "Devansh-Agarwal-" # or "Doe-Jane-"

# Implement your decision tree below
# In this pruning is implemented by decreasing the threshsold value
# a node is made a leaf node whenever the entropy of the node is <= 0.18 which removes some of the leaf nodes
# which removes some of the over fitted nodes
class DecisionTree():
    tree = {}
    root = 0
    #counter = 0
    def learn(self, training_set):
        # implement this function
        nodeEntropy = self.getEntropy(training_set)
        infoGain = 0.0
        position = 0.0
        maxGain = 0.0 
        splitValue = 0.0
        for i in range(11):
            sum = 0.0
            mean = 0.0
            temp1 = []
            for row in training_set :
                temp1.append(row[i])    
            mean =statistics.mean(temp1)
            infoGain =nodeEntropy- self.getEntropy(training_set, False, mean, i)
            #print infoGain
            if maxGain < infoGain:
                maxGain = infoGain
                position = i
                splitValue = mean
        #print maxGain, position        
        if nodeEntropy > 0.18 :
            leftPartition, rightPartion = self.getPartitions(training_set,splitValue,position)
            key = random.randint(0, 1000000)
            while key in self.tree:
                key = random.randint(0, 1000000)
            #left,right,attribuitePosition,splitvalue,isleaf, class
            self.tree[key] = (self.learn(leftPartition),self.learn(rightPartion),position,splitValue,False,None)    
           # self.counter = self.counter + 1
            return key
        else:
            key = random.randint(0, 1000000)
            tempCount = 0
            tempClass = 0
            for row in training_set:
                if row[11] == 0:
                    tempCount = tempCount + 1
            if(tempCount > (len(training_set) -tempCount)):
                tempClass = 0
            else : 
                tempClass = 1    
            while key in self.tree:
                key = random.randint(0, 1000000)
            self.tree[key] = (None, None,None,None,True, tempClass)
           # self.counter = self.counter + 1
            return key    
            

    
    # implement this function

    def classify(self, test_instance):
        result = 0 # baseline: always classifies as 0
        currentNode = self.root
        while ((self.tree.get(currentNode))[4] == False):
            temp = (self.tree.get(currentNode))
            if(test_instance[temp[2]] < temp[3]):
                currentNode = temp[0]
            #    print temp[0]
            else:
                currentNode = (self.tree.get(currentNode))[1]    
        return self.tree.get(currentNode)[5]
    def getPartitions(self,partition,splitValue, position):
          leftPartition, rightPartion = [] ,[]
          for row in partition:
              if row[position] < splitValue:
                  leftPartition.append(row)
              else:
                  rightPartion.append(row)
          return leftPartition,rightPartion            

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
    with open("wine-dataset.csv") as f:
        next(f, None)
        data = [tuple(line) for line in csv.reader(f, delimiter=",",quoting=csv.QUOTE_NONNUMERIC)]
    # random.shuffle(data)
    # with open("wine-dataset.csv") as f:
    #     next(f, None)
    #     mutableData = [list((line)) for line in csv.reader(f, delimiter=",",quoting=csv.QUOTE_NONNUMERIC)]
    print "Number of records: %d" % len(data)
    mutableData = np.array(data)
    # Split training/test sets
    # You need to modify the following code for cross validation.
    
    accuracy = 0.0
    for z in range(10):

        K = 10
        training_set = [x for i, x in enumerate(data) if i % K != z]
        test_set = [x for i, x in enumerate(data) if i % K == z]
        tree = DecisionTree()
        # Construct a tree using training set
        tree.root = tree.learn( training_set )
        #print tree.counter
        # Classify the test set using the tree we just constructed
        results = []
        for instance in test_set:
            result = tree.classify( instance[:-1] )
            results.append( result == instance[-1])
        iterAccuraccy= float(results.count(True))/float(len(results))
            #print iterAccuraccy
      #  print iterAccuraccy
        accuracy = accuracy + iterAccuraccy  /10  
    # Accuracy
    
    print "accuracy: %.4f" % accuracy       
    

    # Writing results to a file (DO NOT CHANGE)
    f = open(myname+"result.txt", "w")
    f.write("accuracy: %.4f" % accuracy)
    f.close()


if __name__ == "__main__":
    run_decision_tree()
