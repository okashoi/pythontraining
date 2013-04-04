# !/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# for python 2.x


def getSentences(fin):
    for line in fin:
        uline = unicode(line.strip(), "utf-8")
        if not uline:
            continue
        for sentence in uline.split((u"。")):
            if not sentence:
                continue
            yield sentence


def _main(args):
    import sys
    try:
        fin = open(args[1])
    except IndexError:
        sys.stderr.write("Error: Missing filename\n")
        sys.stderr.write("Usage: python SenteceSegmentator.py filename")
        return -1
    except IOError:
        sys.stderr.write("Error: The file doesn't exist")
        return -1

    for sentence in getSentences(fin):
        print sentence
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(_main(sys.argv))
