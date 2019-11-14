from sklearn.feature_extraction.text import CountVectorizer  # lib for ML
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier

import os

# Get the list of all files and directories
# in the root directory
path = "20_newsgroups/sci.space"
for fileName in os.listdir(path):
    newName = fileName + ".txt"
    os.rename(fileName, newName)


# print the list
# print(dir_list)


# read the reviews and their polarities from a given file
def loadData(fname):
    reviews = []
    labels = []
    f = open(fname)  # open file
    for line in f:
        review, rating = line.strip().split('\t')
        reviews.append(review.lower())  # reviews
        labels.append(rating)  # label=rating; using 0&1 for the label hence int is used
    f.close()
    return reviews, labels


rev_train, labels_train = loadData('20_newsgroups/sci.space')  # 1 doc in every line of the text file
rev_test, labels_test = loadData('20_newsgroups/sci.med')

# Build a counter based on the training dataset

counter = CountVectorizer()  # count number of times the unique word occurs, word-its freq
counter.fit(rev_train)  # just take train words

# count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)  # transform the training data
counts_test = counter.transform(rev_test)  # transform the testing data

# train classifier
# print(counts_train)
# train classifier

clf = MLPClassifier(hidden_layer_sizes=(15,), random_state=1, max_iter=13, warm_start=True)

# train all classifier on the same datasets
clf.fit(counts_train, labels_train)  # build model, doc,its lable

# use hard voting to predict (majority voting)
pred = clf.predict(counts_test)

# print accuracy
print(accuracy_score(pred, labels_test))
