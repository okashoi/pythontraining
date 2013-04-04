# !/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# for python 2.*


def isNumberExpression(word):
    for char in word:
        if char in u"0123456789０１２３４５６７８９":
            return True
    return False

if __name__ == '__main__':
    import sys

    try:
        fin = open(sys.argv[1])
    except IndexError:
        sys.stderr.write("Error: Missing filename\n")
        sys.stderr.write("Usage: python NounPhrase.py filename\n")
        sys.exit(-1)
    except IOError:
        sys.stderr.write("Error: The file doesn't exist")
        sys.exit(-1)

    for line in fin:
        uline = unicode(line.strip(), "utf-8")
        word = uline.split()[0]
        if isNumberExpression(word):
            continue
        print uline.encode("utf-8")

    fin.close()
    sys.exit(0)