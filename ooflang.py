#!/usr/bin/python

import sys
import os
import argparse
import re
import random


def getIncludes(text):
    return re.findall('#include ["<][a-zA-z]+[>"]', text)


def getCode(text):
    m = re.finditer('#include ["<][a-zA-z]+[>"]', text)
    m = [i for i in m][-1]
    _, l = m.regs[-1]
    return text[l:]


def splitCodeTokens(code):
    with open('./token.regex', 'r') as f:
        r = re.compile(f.read())
        return [a for a, b, c, d in r.findall(code)]


def stripComments(code):
    with open('./comment.regex', 'r') as f:
        return re.sub(f.read(), '', code)


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

    return [(C, O) for C, O in zip(code, ret)]


def main():
    parser = argparse.ArgumentParser(
        description='Replaces the tokens in your C/C++ project with oofs that decrease readability')
    parser.add_argument('--file',
                        help='File to process', required=True)
    # parser.add_argument('-p --process-dependencies',
    #                     help='Process dependencies listed in each C/C++ file', action='store_true')
    parser.add_argument(
        '--out', help='Where to store results', required=True)
    args = parser.parse_args()

    c = ''

    with open(args.file, 'r') as main:
        c = main.read()

    c = stripComments(c)
    includes = getIncludes(c)
    code = getCode(c)
    tokens = splitCodeTokens(code)
    uniqTokens = list(set(tokens))
    oofsL = generateUniqueOofs(uniqTokens)
    oofsD = {K: V for K, V in oofsL}

    macros = '\n'.join(["#define %s %s" % (O, C) for C, O in oofsL])
    newCode = ' '.join([oofsD[word] for word in tokens])

    with open(args.out, 'w+') as out:
        out.write("\n".join(includes) + "\n\n" + macros + "\n\n" + newCode)

    print("Done")


if __name__ == "__main__":
    main()
