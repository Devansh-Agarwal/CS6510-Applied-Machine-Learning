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
    #counter = 0
    def learn(self, training_set):
        # implement this function
        nodeGiniIndex = self.getGiniIndex(training_set) # getting giniIndex of current Node
        infoGain = 0.0
        position = 0.0
        maxGain = 0.0 
        splitValue = 0.0
        # split value is equal to the mean of the attribuite which reduces the giniIndex most
        for i in range(11):
            sum = 0.0
            mean = 0.0
            temp1 = []
            for row in training_set :
                temp1.append(row[i])    
            mean = statistics.mean(temp1)
        # calculating the infogain for each attribuite mean splitting
            infoGain =nodeGiniIndex- self.getGiniIndex(training_set, False, mean, i)
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
            self.tree[key] = (self.learn(leftPartition),self.learn(rightPartion),position,splitValue,False,None)    
           # self.counter = self.counter + 1
            return key
        # if info gain is zero 
        else:
            key = random.randint(0, 1000000)
            while key in self.tree:
                key = random.randint(0, 1000000)
            #left,right,attribuitePosition,splitvalue,isleaf, class
            self.tree[key] = (None, None,None,None,True, training_set[0][11])
            #self.counter = self.counter + 1
            return key    
            

    
    # implement this function
    # iterating the tree in a fashion similar to binary search tree
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

    # spliting the date based on the split value     
    def getPartitions(self,partition,splitValue, position):
          leftPartition, rightPartion = [] ,[]
          for row in partition:
              if row[position] < splitValue:
                  leftPartition.append(row)
              else:
                  rightPartion.append(row)
          return leftPartition,rightPartion            

    # function to calculate giniIndex of the current node or the child nodes
    # flag is true if giniIndex for single node is calculated
    def getGiniIndex(self,partition,f1 = True, splitValue = 0.0, attr = 0) :
        count1 = 0.0
        count0 = 0.0
        count2 = 0.0
        count3 = 0.0
        giniIndex = 0.0
        giniIndex2 = 0.0
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
                giniIndex  = 1 - (p0 ** 2) - (p1 ** 2 ) 
            return giniIndex
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
                giniIndex  = 1 - (p0 ** 2) - (p1 ** 2 ) 
            if(count2!=0 and count3 != 0):
                p0 = count2 / total2
                p1 = count3 / total2    
                giniIndex2  = 1 - (p0 ** 2) - (p1 ** 2 ) 
            totalginiIndex = (total/(total+total2))* giniIndex + (total2/(total+total2))* giniIndex2  
            return totalginiIndex                
def createSplit(partition):
    pass

def run_decision_tree():

    # Load data set
    with open("wine-dataset.csv") as f:
        next(f, None)
        data = [tuple(line) for line in csv.reader(f, delimiter=",",quoting=csv.QUOTE_NONNUMERIC)]
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
        # print tree.tree
        # Classify the test set using the tree we just constructed
        results = []
        for instance in test_set:
            result = tree.classify( instance[:-1] )
            results.append( result == instance[-1])
        iterAccuraccy= float(results.count(True))/float(len(results))
            #print iterAccuraccy
        accuracy = accuracy + iterAccuraccy  /10  
    # Accuracy
    
    print "accuracy: %.4f" % accuracy       
    

    # Writing results to a file (DO NOT CHANGE)
    f = open(myname+"result.txt", "w")
    f.write("accuracy: %.4f" % accuracy)
    f.close()


if __name__ == "__main__":
    run_decision_tree()
