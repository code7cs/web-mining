from collections import Counter


# function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex = set()
    lex_conn = open(fname)
    # add every word in the file to the set
    for line in lex_conn:
        # remember to strip to remove the lin-change character
        newLex.add(line.strip())
    lex_conn.close()
    return newLex


def run(path):
    answer = {}
    negLex = loadLexicon('negative-words.txt')
    fin = open(path)
    for line in fin:
        line = line.lower().strip()
        words = line.split(' ')
        res = {}
        for index in [i for i, v in enumerate(words) if v == 'phone']:
            prev_word = words[index - 1]
            if prev_word in negLex:
                res.update({prev_word: 1})
                answer = dict(Counter(res) + Counter(answer))

    fin.close()
    return dict(answer)


if __name__ == "__main__":
    print(run('textfile'))
    #
    # if x == 0 or y == 0:
    #     print("input error")
    # elif x > y:
    #     r1 = x / y
    #     r2 = x % y
    # else:
    #     r1 = y / x
    #     r2 = y % x
    # print("商= ", r1, " 余数= ", r2)
