#!/usr/bin/python

import sys
import os
import argparse
import random
from components import *

def generateUniqueOofs(code):
    def gen(c):
        l = list(range(len(code)))
        random.shuffle(l)
        nums = [bin(i)[2:] for i in l]
        for bits in nums:
            r = ''
            for bit in bits:
                r += c.upper() if bit == '1' else c
            if r != 'oof':
                yield r
    ret = ['oof']
    ret += list([i + j for i, j in zip(gen('o'), gen('f'))])
    
    for i, item in enumerate(ret):
        nu = list(item)
        l = len(item)
        h = float(l / 2)
        for c in range(int(h) + 2):
            r = (c / h) + random.random() > 1 + (0.1 * random.random())
            if r:
                nu[c], nu[-(c + 1)] = nu[-(c + 1)], nu[c]
        ret[i] = ''.join(nu)

    return {C : O for C, O in zip(code, ret)}


def main():
    parser = argparse.ArgumentParser(description='Obfuscates C/C++ code')
    parser.add_argument('-o', '--output', help='Directs the output to a name of your choice')
    parser.add_argument('-q', '--quiet', help='Do not output anything', action='store_true')
    parser.add_argument('-d', '--dry', help='Dumps results to standard out', action='store_true')
    parser.add_argument('-p', '--nopretest', help='Do not run pretest to make sure obfuscated code will compile', action='store_true')
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

        if not args.nopretest:
            if not testCompile(newFile):
                print('''
This obfuscation will not compile. Please go back to %s
and ensure that the code can be run if it was written on one line.

Please check that every code block is surrounded by curly braces (ie:)

// WRONG, this will not compile 
int a = 1;
if (a == 1)
    cout << "Success";
else
    cout << "Failure;

// RIGHT
int a = 1;
if (a == 1) {
    cout << "Success";
}
else {
    cout << "Failure;
}
                ''' % filename)
                continue

        if args.dry:
            if len(args.file) > 1:
                quietablePrint('\n--- %s ---' % filename)
            print(newFile)
            print('\n')
        else:
            if TOFOLDER:
                openname = args.output + '/' + os.path.basename(openname)
            
            filename, file_extension = os.path.splitext(openname)
            with open(filename + '.oof' + file_extension, 'w+') as out:
                out.write(newFile)

        
        quietablePrint("Converted %d tokens in %s to oofs" % (len(uniqTokens), filename))


if __name__ == "__main__":
    main()
