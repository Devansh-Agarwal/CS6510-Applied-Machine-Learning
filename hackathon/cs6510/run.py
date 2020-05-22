import pandas as pd
import numpy as np
import csv
from sklearn.compose import ColumnTransformer
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
# import seaborn as sns
# import matplotlib.pyplot as plt
from scipy import stats
import sys
import random


def read_train():
    train = pd.read_csv("train.csv")

    train = train[~(train['num_of_cancelled_trips'] >= 6)]
    train = train[~(train['anon_var_1'] >=115)]
    train = train[~(train['anon_var_2'] >= 70)]
    train = train[~(train['anon_var_3'] >= 110 )]
    train = train[~(2>train['customer_score'])]
    train = train[~(train['customer_score']>=3.7 )]

    return train


def hotenc(train):
    mf1 = pd.get_dummies(train['taxi_type'])
    train = train.drop('taxi_type',axis = 1)
    train = train.join(mf1,rsuffix='_Taxitype')

    mf2 = pd.get_dummies(train['customer_score_confidence'])
    train = train.drop('customer_score_confidence',axis = 1)
    train = train.join(mf2,rsuffix='_Customerscore_confidence')

    mf = pd.get_dummies(train['drop_location_type'])
    train = train.drop('drop_location_type',axis = 1)
    train = train.join(mf,rsuffix='_drop_location_type')

    mf = pd.get_dummies(train['sex'])
    train = train.drop('sex',axis = 1)
    train = train.join(mf,rsuffix='sex')

    return train

train = read_train()
train = hotenc(train)
test = pd.read_csv("test.csv")
test = hotenc(test)


data_train,data_test = train_test_split(train, test_size=0, shuffle = True)

data_test = test
price_train = np.array(data_train["pricing_category"])
# price_test = np.array(data_test["pricing_category"])

data_train = data_train.drop('id',axis = 1)
data_train = data_train.drop("pricing_category",axis = 1)


tag = test['id']
tag = np.array(tag)
data_test = data_test.drop('id',axis = 1)
# data_test = data_test.drop("pricing_category",axis = 1)



data_train1 = data_train.copy()
y1_label = [ int(i==1) for i in price_train]


data_train2 = data_train.copy()
y2_label = [ int(i==2) for i in price_train]

data_train3 = data_train.copy()
y3_label = [ int(i==3) for i in price_train]


clf1 = XGBClassifier(nthread=-1,max_depth = 6, learning_rate=0.077,n_estimators=1000,subsample=0.77,colsample_bynode=0.75,verbosity = 0)
clf2 = XGBClassifier(nthread=-1,max_depth = 6, learning_rate=0.077,n_estimators=1000,subsample=0.77,colsample_bynode=0.75,verbosity = 0)
clf3 = XGBClassifier(nthread=-1,max_depth = 6, learning_rate=0.077,n_estimators=1000,subsample=0.77,colsample_bynode=0.75,verbosity = 0)

clf1.fit(data_train1,y1_label)
print(1)
clf2.fit(data_train2,y2_label)
print(1)
clf3.fit(data_train3,y3_label)
print(1)

y1_pred = clf1.predict(data_test)
prob1 = clf1.predict_proba(data_test)

y2_pred = clf2.predict(data_test)
prob2 = clf2.predict_proba(data_test)


y3_pred = clf3.predict(data_test)
prob3 = clf3.predict_proba(data_test)


final = []
cnt = 0
# print(len(price_test))


for i in range(len(data_test)):
    p1 = prob1[i]
    p2 = prob2[i]
    p3 = prob3[i]


    sum1 = p1[1] + p2[0] + p3[0]
    sum2 = p1[0] + p2[1] + p3[0]
    sum3 = p1[0] + p2[0] + p3[1]
    a = [sum1,sum2,sum3]

    if sum2 == max(a):
        final.append([2.0])
    elif sum3==max(a):
        final.append([3.0])
    elif sum1==max(a):
        final.append([1.0])
tag = np.resize(tag,(len(tag),1))
final = np.hstack((tag,final))



with open('Xgboost1vAll.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(final)

csvFile.close()

        # print("Hello")
# print(cnt)
# accuracy = accuracy_score(price_test,final )
# print("Accuracy: %.8f%%" % (accuracy * 100.0))
# id,pricing_category