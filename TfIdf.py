# !/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# for python 2.x


def calculate(fins):
    import math
    from collections import defaultdict

    tf = defaultdict(int)
    df = defaultdict(int)
    for fin in fins:
        word2freq = defaultdict(int)
        for line in fin:
            word2freq[unicode(line.strip(), "utf-8")] += 1
        for word, freq in word2freq.items():
            tf[word] += freq
            df[word] += 1

    N = len(fins)
    for word in word2freq:
        yield word, tf[word] * math.log(float(N) / df[word]), tf[word], df[word]


def _main(args):
    import sys
    fins = []
    for filename in args[1:]:
        try:
            fins.append(open(filename))
        except IOError:
            sys.stderr.write("Error: The file \"" + filename +
                             "\" doesn't exist\n")
            return -1
    for w, tfidf, tf, df in calculate(fins):
        print w + "\t" + str(tfidf) + "\t" + str(tf) + "\t" + str(df)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(_main(sys.argv))
