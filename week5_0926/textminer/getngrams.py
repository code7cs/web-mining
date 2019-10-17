"""
POS tags list: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
"""

import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk import load


def loadLexicon(fname):
    newLex = set()
    lex_conn = open(fname)
    # add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())  # remember to strip to remove the lin-change character
    lex_conn.close()
    return newLex


def processSentence(sentence, posLex, negLex, tagger):
    # split sentences
    sentences = sent_tokenize(sentence)
    print('NUMBER OF SENTENCES: ', len(sentences))

    four_grams = []  # holds the pairs found in the text

    # for each sentence
    for each_sentence in sentences:
        terms = nltk.word_tokenize(each_sentence)  # tokenize the sentence
        tagged_terms = tagger.tag(terms)  # do POS tagging on the tokenized sentence

        for i in range(len(tagged_terms) - 3):  # for every tagged term
            term0 = tagged_terms[i]
            term1 = tagged_terms[i + 1]  # any word
            term2 = tagged_terms[i + 2]
            term3 = tagged_terms[i + 3]
            if term0[0] == 'not':
                if (term2[0] in posLex) or (term2[0] in negLex):
                    if re.match('NN', term3[1]):
                        four_grams.append(
                            term0[0] + " " + term1[0] + " " + term2[0] + " " + term3[0])
    return four_grams


if __name__ == '__main__':
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    test_tagger = load(_POS_TAGGER)

    # read the input
    f = open('input.txt')
    test_sentence = f.read().strip()
    # load the positive and negative lexicons
    posLex = loadLexicon('positive-words.txt')
    negLex = loadLexicon('negative-words.txt')

    print(processSentence(test_sentence, posLex, negLex, test_tagger))
    f.close()
