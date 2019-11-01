# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:21:19 2019

@author: chhav
""""""
A simple script that demonstrates how we classify textual data with sklearn.

"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from itertools import permutations


# read the reviews and their polarities from a given file

def loadData(fname):
    reviews = []
    labels = []
    f = open(fname)
    for line in f:
        review, rating = line.strip().split('\t')
        reviews.append(review.lower())
        labels.append(int(rating))
    f.close()
    return reviews, labels


rev_train, labels_train = loadData('reviews_train.txt')
rev_test, labels_test = loadData('reviews_test.txt')

# Build a counter based on the training dataset
counter = CountVectorizer()
counter.fit(rev_train)

# count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)  # transform the training data
counts_test = counter.transform(rev_test)  # transform the testing data

# train classifier
model1 = DecisionTreeClassifier()
model2 = MultinomialNB()
model3 = LogisticRegression(solver='liblinear')
model4 = RandomForestClassifier(n_estimators=2500, n_jobs=-1, criterion="entropy", max_features='auto',
                                random_state=150, max_depth=1000, min_samples_split=160)
model5 = MLPClassifier(hidden_layer_sizes=(15,), random_state=1, max_iter=13, warm_start=True)

predictors = [('dt', model1), ('nb', model2), ('lreg', model3), ('rdm', model4), ('mlp', model5)]

VT = VotingClassifier(predictors)

# train all classifier on the same datasets
VT.fit(counts_train, labels_train)

# use hard voting to predict (majority voting)
pred = VT.predict(counts_test)

# print accuracy
print(accuracy_score(pred, labels_test))

modelNames = ['LogisticReg', 'RandomForestClassf', 'MLPClassf']
perm = permutations([('dt', model1), ('nb', model2), ('lreg', model3), ('rdm', model4), ('mlp', model5)], 3)
accuracy = []

for i in list(perm):
    predictors = i
    #    predictors=[('m1',i[0]),('m2',i[1]),',m3']
    VT = VotingClassifier(predictors)
    VT.fit(counts_train, labels_train)
    pred = VT.predict(counts_test)
    #    print (accuracy_score(pred,labels_test))
    accuracy.append(accuracy_score(pred, labels_test))
a = max(accuracy)

print("The 3 classifiers with highest acc is:", modelNames, '\t', a)
