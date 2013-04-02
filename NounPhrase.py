# !/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# for python 2.x


def extractor(fin):
    nounphrase = u""
    for line in fin:
        uline = unicode(line.strip(), "utf-8")
        if uline.startswith(u"* ") or uline.startswith(u"EOF"):
            if nounphrase:
                yield nounphrase
                nounphrase = u""
            continue

        try:
            surface, attribute = uline.split(u"\t")[:2]
            pos = attribute.split(u",")[0]
        except ValueError:
            if nounphrase:
                yield nounphrase
                nounphrase = u""
            continue

        if pos != u"名詞":
            if nounphrase:
                yield nounphrase
                nounphrase = u""
            continue

        nounphrase += surface


def _main(args):
    import sys

    try:
        fin = open(args[1])
    except IndexError:
        sys.stderr.write("Error: Missing filename\n")
        sys.stderr.write("Usage: python NounPhrase.py filename\n")
        return -1
    except IOError:
        sys.stderr.write("Error: The file doesn't exist")
        return -1

    for np in extractor(fin):
        print np

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(_main(sys.argv))
