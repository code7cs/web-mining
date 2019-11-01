"""
A simple script that demonstrates how we classify textual data with sklearn.

"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import ComplementNB
# from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.neural_network import MLPClassifier

from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import SpectralClustering

from sklearn.multiclass import OutputCodeClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier
from mlxtend.classifier import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors.nearest_centroid import NearestCentroid


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
# clf = MultinomialNB()

# clf = AdaBoostClassifier(n_estimators=500)

# clf = RandomForestClassifier(n_estimators=10)
# boosting = AdaBoostClassifier(base_estimator=clf, n_estimators=1)

clf = GradientBoostingClassifier(n_estimators=200, learning_rate=1.0, max_depth=1, random_state=0)
# train all classifier on the same datasets
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
# clf = BaggingClassifier(KNeighborsClassifier(), max_samples=0.8, max_features=0.1)
# for i in range(10, 200):
# clf = RandomForestClassifier(n_estimators=i)
# clf = AdaBoostClassifier(n_estimators=12)
# clf = RandomForestClassifier(n_estimators=123)
clf3 = MultinomialNB()
lr = LogisticRegression()
# sclf = StackingClassifier(classifiers=[clf1, clf3], meta_classifier=lr)
# clf = DecisionTreeClassifier(criterion='entropy', max_depth=1)

# for i in range(20, 100):
# clf = KNeighborsClassifier(n_neighbors=10)
clf.fit(counts_train, labels_train)

# use hard voting to predict (majority voting)
pred = clf.predict(counts_test)

# print accuracy
print(accuracy_score(pred, labels_test))
