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
    parser = argparse.ArgumentParser(description='Obfuscates C/C++ code')
    parser.add_argument('-o', '--output', help='Directs the output to a name of your choice')
    parser.add_argument('-q', '--quiet', help='Do not output anything', action='store_true')
    parser.add_argument('-d', '--dry', help='Dumps results to standard out', action='store_true')
    parser.add_argument('file', metavar='Input File', type=str, nargs='+')

    args = parser.parse_args()
    TOFOLDER = args.output and len(args.file) > 1
    
    if TOFOLDER:
        os.mkdir(args.output)

    def quietablePrint(msg):
        if not args.quiet:
            print(msg)
    
    for filename in args.file:
        c = ''
        with open(filename, 'r') as main:
            c = main.read()

        c = stripComments(c)
        includes = getIncludes(c)
        code = getCode(c)
        tokens = list(splitCodeTokens(code))
        uniqTokens = list(set(tokens))
        oofs = generateUniqueOofs(uniqTokens)

        macros = '\n'.join(["#define %s %s" % (O, C) for C, O in oofs.items()])
        newCode = ' '.join([oofs[word] for word in tokens])
        newFile = "\n".join(includes) + "\n\n" + macros + "\n\n" + newCode
        openname = filename

        if args.dry:
            if len(args.file) > 1:
                quietablePrint('\n--- %s ---' % filename)
            print(newFile)
            print('\n')
        else:
            if TOFOLDER:
                openname = args.output + '/' + os.path.basename(openname)

            with open(openname + '.oof', 'w+') as out:
                out.write(newFile)

        
        quietablePrint("Converted %d tokens in %s to oofs" % (len(uniqTokens), filename))


if __name__ == "__main__":
    main()
