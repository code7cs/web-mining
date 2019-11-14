# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:17:57 2019

@author: howard9900090
"""

import codecs
import os
from nltk.corpus import stopwords
import re


def predict(someset):
    return 'comp'


filesa = os.listdir('20_newsgroups/comp.windows.x')
filesb = os.listdir('20_newsgroups/rec.sport.baseball')
filesc = os.listdir('20_newsgroups/talk.politics.misc')
filesd = os.listdir('20_newsgroups/rec.autos')

fw = codecs.open('result.txt', 'w', encoding='utf8')
stopLex = set(stopwords.words('english'))

for x in range(0, len(filesa)):
    fin = codecs.open('20_newsgroups/comp.windows.x/' + filesa[x], encoding='utf8', errors='ignore')
    print('20_newsgroups/comp.windows.x/' + filesa[x])
    start = False
    wordset = set()
    for line in fin:
        tmp = line.strip().replace('\n', '')
        if len(tmp) == 0:
            start = True
        if start:
            words = re.sub('[^a-z]', ' ', line.lower()).split(' ')
            for word in words:
                if word in stopLex:
                    continue
                wordset.add(word)
    result = predict(wordset)
    fw.write('20_newsgroups/comp.windows.x/' + filesa[x] + '\t' + result + '\t' + 'comp' + '\n')

for x in range(0, len(filesb)):
    fin = codecs.open('20_newsgroups/rec.sport.baseball/' + filesb[x], encoding='utf8', errors='ignore')
    print('20_newsgroups/rec.sport.baseball/' + filesb[x])
    start = False
    wordset = set()
    for line in fin:
        tmp = line.strip().replace('\n', '')
        if len(tmp) == 0: start = True
        if start:
            words = re.sub('[^a-z]', ' ', line.lower()).split(' ')
            for word in words:
                if word in stopLex: continue
                wordset.add(word)
    result = predict(wordset)
    fw.write('20_newsgroups/rec.sport.baseball/' + filesb[x] + '\t' + result + '\t' + 'sports' + '\n')

for x in range(0, len(filesc)):
    fin = codecs.open('20_newsgroups/talk.politics.misc/' + filesc[x], encoding='utf8', errors='ignore')
    print('20_newsgroups/talk.politics.misc/' + filesc[x])
    start = False
    wordset = set()
    for line in fin:
        tmp = line.strip().replace('\n', '')
        if len(tmp) == 0: start = True
        if start:
            words = re.sub('[^a-z]', ' ', line.lower()).split(' ')
            for word in words:
                if word in stopLex: continue
                wordset.add(word)
    result = predict(wordset)
    fw.write('20_newsgroups/talk.politics.misc/' + filesc[x] + '\t' + result + '\t' + 'politics' + '\n')

for x in range(0, len(filesd)):
    fin = codecs.open('20_newsgroups/rec.autos/' + filesd[x], encoding='utf8', errors='ignore')
    print('20_newsgroups/rec.autos/' + filesd[x])
    start = False
    wordset = set()
    for line in fin:
        tmp = line.strip().replace('\n', '')
        if len(tmp) == 0: start = True
        if start:
            words = re.sub('[^a-z]', ' ', line.lower()).split(' ')
            for word in words:
                if word in stopLex: continue
                wordset.add(word)
    result = predict(wordset)
    fw.write('20_newsgroups/rec.autos/' + filesd[x] + '\t' + result + '\t' + 'rec' + '\n')

fin = codecs.open('result.txt', encoding='utf8', errors='ignore')

tot = 0
cor = 0
for line in fin:
    arr = line.split('\t')
    print(arr[1] + '|' + arr[2])
    tot = tot + 1
    if arr[1] == arr[2]:
        cor = cor + 1

print(str(cor))
print(str(tot))

print('Accuracy:' + str((cor / tot) * 100) + '%')
