"""
A simple script that demonstrates how we classify textual data with sklearn.

"""
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from nltk.corpus import stopwords
import os
import re

stopLex = set(stopwords.words('english'))  # build a set of english stopwrods
"""
#read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname)
    for line in f:
        review,rating=line.strip().split('\t')  
        reviews.append(review.lower())    
        labels.append(int(rating))
    f.close()
    return reviews,labels

rev_train,labels_train=loadData('reviews_train.txt')
rev_test,labels_test=loadData('reviews_test.txt')


#Build a counter based on the training dataset
counter = CountVectorizer()
counter.fit(rev_train)
"""


def train_comp(path):
    dirlist = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
    for docName in dirlist:
        f = open(path + docName)
        train = open("train_comp.txt")

        sentences = f.split('.')  # split the text into sentences
        for sentence in sentences:  # for each sentence
            sentence = sentence.lower().strip()  # loewr case and strip
            sentence = re.sub('[^a-z]', ' ', sentence)  # replace all non-letter characters  with a space

            words = sentence.split(' ')  # split to get the words in the sentence

            for word in words:  # for each word in the sentence
                if word == '' or word in stopLex:
                    continue  # ignore empty words and stopwords
                else:
                    train.write(word)  # update the frequency of the word


def train_politics(path):
    dirlist = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
    for docName in dirlist:
        f = open(path + docName)
        train = open("train_politics.txt")

        sentences = f.split('.')  # split the text into sentences
        for sentence in sentences:  # for each sentence
            sentence = sentence.lower().strip()  # loewr case and strip
            sentence = re.sub('[^a-z]', ' ', sentence)  # replace all non-letter characters  with a space

            words = sentence.split(' ')  # split to get the words in the sentence

            for word in words:  # for each word in the sentence
                if word == '' or word in stopLex:
                    continue  # ignore empty words and stopwords
                else:
                    train.write(word)  # update the frequency of the word


def train_sport(path):
    dirlist = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
    for docName in dirlist:
        f = open(path + docName)
        train = open("train_sports.txt")

        sentences = f.split('.')  # split the text into sentences
        for sentence in sentences:  # for each sentence
            sentence = sentence.lower().strip()  # loewr case and strip
            sentence = re.sub('[^a-z]', ' ', sentence)  # replace all non-letter characters  with a space

            words = sentence.split(' ')  # split to get the words in the sentence

            for word in words:  # for each word in the sentence
                if word == '' or word in stopLex:
                    continue  # ignore empty words and stopwords
                else:
                    train.write(word)  # update the frequency of the word


def train_autos(path):
    dirlist = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
    for docName in dirlist:
        f = open(path + docName)
        train = open("train_autos.txt")

        sentences = f.split('.')  # split the text into sentences
        for sentence in sentences:  # for each sentence
            sentence = sentence.lower().strip()  # loewr case and strip
            sentence = re.sub('[^a-z]', ' ', sentence)  # replace all non-letter characters  with a space

            words = sentence.split(' ')  # split to get the words in the sentence

            for word in words:  # for each word in the sentence
                if word == '' or word in stopLex:
                    continue  # ignore empty words and stopwords
                else:
                    train.write(word)  # update the frequency of the word


# List all current directories name
root = os.getcwd()
dirlist = [item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item))]
print(dirlist)

# Go in specific tag fdoler
for dirName in dirlist:
    # Split the filename with '.'
    parts = dirName.split('.')
    # Iterate through splited filename list
    if (parts[0] == "comp"):
        print("comp")
        train_comp(root + dirName)
    elif (parts[0] == "talk"):
        print("politics")
        train_politics(root + dirName)
    elif (parts[0] == "rec"):
        if (parts[1] == "sport"):
            print("rec->sports")
            train_sport(root + dirName)
        elif (parts[1] == "autos"):
            print("rec->autos")
            train_autos(root + dirName)

# Read the document
# def readFile()
# print [name for name in os.listdir(".") if os.path.isdir(name)]


"""
# write message to file, m is message to be written, c is the catalog that message belong to
def writeFile(m, c):
    if (c == "comp"):
        f = open("train_comp.txt", "a")
    elif (c == "sports"):
        f = open("train_sports.txt", "a")
    elif (c == "politics"):
        f = open("train_politics.txt", "a")
    elif (c == "rec"):
        f = open("train_rec.txt", "a")    
    else:
        print("Some data can't be classified, see train_unknown.txt")
        f = open("train_unknown.txt", "a")
    
    f.write(m)
    f.close()

"""
"""
#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

#train classifier
clf = RandomForestClassifier(n_estimators=102)

#train all classifier on the same datasets
clf.fit(counts_train,labels_train)

#use hard voting to predict (majority voting)
pred=clf.predict(counts_test)

#print accuracy
print (accuracy_score(pred,labels_test))
"""
