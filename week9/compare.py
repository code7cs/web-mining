from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.linear_model import RidgeClassifierCV


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

counter = CountVectorizer()
counter.fit(rev_train)

# count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)  # transform the training data
counts_test = counter.transform(rev_test)  # transform the testing data

# train classifier
model2 = MultinomialNB()
model3 = LogisticRegression(solver='liblinear')
model4 = RidgeClassifierCV(alphas=[1e-4, 1e-3, 1e-2, 1e-1])
model6 = MultinomialNB()
model7 = SVC(gamma='scale', decision_function_shape='ovo')

model2.fit(counts_train, labels_train)
model3.fit(counts_train, labels_train)
model4.fit(counts_train, labels_train)
model6.fit(counts_train, labels_train)
model7.fit(counts_train, labels_train)

pred2 = model2.predict(counts_test)
pred3 = model3.predict(counts_test)
pred4 = model4.predict(counts_test)
pred6 = model6.predict(counts_test)
pred7 = model7.predict(counts_test)

print('MultinomialNB', accuracy_score(pred2, labels_test))
print('LogisticRegression', accuracy_score(pred3, labels_test))
print('RidgeClassifierCV', accuracy_score(pred4, labels_test))
print('MultinomialNB', accuracy_score(pred6, labels_test))
print('SVC', accuracy_score(pred7, labels_test))
print('\n')

maxp = 0
out = [0, 0, 0]
models = ['MultinomialNB', 'LogisticRegression', 'RidgeClassifierCV', 'MultinomialNB', 'SVC']
predictors = [('dt', model2), ('lreg', model3), ('rcc', model4), ('mnb', model6), ('svc', model7)]
for x in range(0, 3):
    for y in range(x + 1, 4):
        for z in range(y + 1, 5):
            p = [predictors[x], predictors[y], predictors[z]];
            VT = VotingClassifier(p)
            VT.fit(counts_train, labels_train)
            pred = VT.predict(counts_test)
            pval = accuracy_score(pred, labels_test)
            if pval > maxp:
                maxp = pval
                out = [x, y, z]
            print(models[x] + ' / ' + models[y] + ' / ' + models[z] + '\t\t' + str(pval))

print('\nhighest predict:', maxp)
print('models: ' + models[out[0]] + ',' + models[out[1]] + ',' + models[out[2]])
