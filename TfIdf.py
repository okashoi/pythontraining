# !/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# for python 2.x

from collections import defaultdict

tf = defaultdict(int)
df = defaultdict(int)
filenum = 0


def updateTfAndDf(fin):
    global tf, df, filenum

    word2freq = defaultdict(int)
    for line in fin:
        word2freq[line.strip()] += 1
    for word, freq in word2freq.items():
        tf[word] += freq
        df[word] += 1
    filenum += 1


def calculateTfIdf(word):
    from math import log
    global tf, idf, filenum

    return tf[word] * log(float(filenum) / df[word])


def _main(args):
    import sys

    for filename in args[1:]:
        try:
            fin = open(filename)
            updateTfAndDf(fin)
            fin.close()
        except IOError:
            sys.stderr.write("Error: The file \"" + filename +
                             "\" doesn't exist\n")
            return -1

    for word in tf:
        print "\t".join([word, str(calculateTfIdf(word)),
                         str(tf[word]), str(df[word])])

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(_main(sys.argv))
