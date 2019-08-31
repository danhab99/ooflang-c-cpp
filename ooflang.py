#!/usr/bin/python

import sys
import os
import argparse
import random
from components import *

def generateUniqueOofs(code):
    ret = ['oof']

    def pickLetter(p):
        def pick(f, l):
            return f if (p + random.random()) / 2 > 0.5 else l
        l = pick('f', 'o')
        c = pick(True, False)
        l = l.upper() if c else l
        return l

    lastlen = len(ret[-1])

    while len(ret) is not len(code):
        g = ''.join([pickLetter(float(i) / lastlen)
                     for i in range(lastlen)])

        if g not in ret:
            ret.append(g)
        else:
            lastlen += 1

    return {C : O for C, O in zip(code, ret)}


def main():
    c = ''

    with open('test.cpp', 'r') as main:
        c = main.read()

    c = stripComments(c)
    includes = getIncludes(c)
    code = getCode(c)
    tokens = list(splitCodeTokens(code))
    uniqTokens = list(set(tokens))
    oofs = generateUniqueOofs(uniqTokens)

    macros = '\n'.join(["#define %s %s" % (O, C) for C, O in oofs.items()])
    newCode = ' '.join([oofs[word] for word in tokens])

    with open('test.oof.cpp', 'w+') as out:
        out.write("\n".join(includes) + "\n\n" + macros + "\n\n" + newCode)

    print("Converted %d tokens to oofs" % len(uniqTokens))


if __name__ == "__main__":
    main()
