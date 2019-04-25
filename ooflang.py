import sys
import os
import argparse
import re


def getIncludes(text):
    return re.search('#include "[a-zA-z]+"', text)


def getCode(text):
    m = re.finditer('#include ["<][a-zA-z]+[>"]', text)
    m = [i for i in m][-1]
    _, l = m.span()
    return text[l:]


def splitCodeTokens(code):
    with open('./token.regex', 'r') as f:
        r = re.compile(f.read())
        return r.search(code)


def stripComments(code):
    with open('./comment.regex', 'r') as f:
        return re.sub(f.read(), '', code)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Replaces the tokens in your C/C++ project with oofs that decrease readibility')
    parser.add_argument('-f --file', nargs='+',
                        help='File(s) to process', required=True)
    parser.add_argument('-p --process-dependencies',
                        help='Process dependencies listed in each C/C++ file', action='store_true')
    # parser.add_argument('')
    args = parser.parse_args()

    with open(args.file, 'r') as main:
        c = main.read()
        includes = getIncludes(c)
        code = getCode(c)
        code = stripComments(code)
        tokens = splitCodeTokens(code)
        uniqTokens = list(set(tokens))
