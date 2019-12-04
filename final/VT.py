"""
A simple script that demonstrates how we classify textual data with sklearn.

"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import RidgeClassifierCV

from itertools import combinations


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
model4 = RandomForestClassifier(n_estimators=123)
model5 = RidgeClassifierCV(alphas=[1e-4, 1e-3, 1e-2, 1e-1])

result = []
for i in list(combinations([('dt', model1), ('nb', model2), ('lreg', model3), ('rf', model4), ('gb', model5)], 3)):
    predictors = i
    VT = VotingClassifier(predictors)

    # train all classifier on the same datasets
    VT.fit(counts_train, labels_train)

    # use hard voting to predict (majority voting)
    pred = VT.predict(counts_test)
    result.append({accuracy_score(pred, labels_test), predictors})
    # print(result)

alist = []
for i, val in result:
    alist.append(i)

# print max accuracy
print(max(alist))
# index = result.index(max(alist))
