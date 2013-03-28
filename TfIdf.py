# !/usr/bin/python
# -*- coding: utf-8 -*-

# for python 2.x


def calculate(fins):
    import math
    from collections import defaultdict

    freq = defaultdict(int)
    df = defaultdict(int)
    for fin in fins:
        count = defaultdict(int)
        for line in fin:
            count[unicode(line.strip(), "utf-8")] += 1
        for nounphrase, c in count.items():
            freq[nounphrase] += c
            df[nounphrase] += 1

    N = len(fins)
    for w in freq.keys():
        yield w, freq[w] * math.log(float(N) / df[w]), freq[w], df[w]


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
