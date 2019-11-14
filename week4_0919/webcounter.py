"""

A scrip that reads a file from the web and returns a set of all the words in the web page
that have a higher frequency than w1 but a lower frequency than w2.

"""

import re
from nltk.corpus import stopwords
import requests


def run(url, w1, w2):
    freq = {}  # keep the freq of each word in the file

    stopLex = set(stopwords.words('english'))  # build a set of english stopwords

    success = False  # become True when we get the file

    for i in range(5):  # try 5 times
        try:
            # use the browser to access the url
            response = requests.get(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
            success = True  # success
            break  # we got the file, break the loop
        except:  # browser.open() threw an exception, the attempt to get the response failed
            print('failed attempt', i)

    # all five attempts failed, return  None
    if not success:
        return None

    text = response.text  # read in the text from the file

    sentences = text.split('.')  # split the text into sentences

    for sentence in sentences:  # for each sentence

        sentence = sentence.lower().strip()  # lower case and strip
        sentence = re.sub('[^a-z]', ' ', sentence)  # replace all non-letter characters  with a space

        words = sentence.split(' ')  # split to get the words in the sentence

        for word in words:  # for each word in the sentence
            if word == '' or word in stopLex:
                continue  # ignore empty words and stopwords
            else:
                freq[word] = freq.get(word, 0) + 1  # update the frequency of the word

    #  w1 and w2 are also ignore stopwords, since comparing them in freq, which is already ignore stopwords
    if w2 not in freq:
        return {}

    if w1 not in freq:
        return set(freq.keys())

    answer = set()

    for key in freq:
        if freq[w1] < freq[key] < freq[w2]:
            answer.add(key)

    if answer == set():  # if answer is empty, return {}
        return {}
    else:
        return answer


# the url below is my own gist text web page for test
if __name__ == '__main__':
    print(run(
        'https://gist.githubusercontent.com/hanfanw/877490eebc980bff82fde039ddc1b90c/raw/938e4904ead19a541a3c8cfcea98eed305eb982a/webcounter_0919_2',
        'follow',
        'pass'
    ))
