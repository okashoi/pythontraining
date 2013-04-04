# !/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# for python 2.x


def group(fin):
    nounphrase = u""
    for line in fin:
        uline = unicode(line.strip(), "utf-8")
        if uline.startswith(u"* ") or uline.startswith(u"EOF"):
            if nounphrase:
                yield nounphrase + u"/t名詞句,*,*,*,*,*,*,*,*\t0"
                nounphrase = u""
            yield uline
            continue

        try:
            surface, attribute = uline.split(u"\t")[:2]
            pos = attribute.split(u",")[0]
        except ValueError:
            continue

        if pos != u"名詞":
            if nounphrase:
                yield nounphrase + u"\t名詞句,*,*,*,*,*,*,*,*\t0"
                nounphrase = u""
            yield uline
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

    for uline in group(fin):
        print uline.encode("utf-8")

    fin.close()

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(_main(sys.argv))
