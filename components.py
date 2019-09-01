import re
import subprocess
import tempfile
import os

_INCLUDE_REGEX = re.compile(r'#include ["<][a-zA-z]+[>"]')
_TOKEN_REGEX = re.compile(r"(\d*\.\d*|\"|\'|[+-/*%<>!=&|^;?:$][<>+-=&|]?[=*]?|\w+|[(){}[\]])")
_COMMENT_REGEX = re.compile(r'(\/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+\/)|(\/\/.*)')

def getIncludes(text):
  return re.findall(_INCLUDE_REGEX, text)

def getCode(text):
  m = re.finditer(_INCLUDE_REGEX, text)
  m = [i for i in m][-1]
  _, l = m.regs[-1]
  return text[l:]

def splitCodeTokens(code):
  toks = re.split(_TOKEN_REGEX, code)
  toks = [i for i in toks if i != '']
  iter_toks = iter(toks)
  doYield = True
  ret = ''

  while True:
    try:
      r = next(iter_toks)

      if re.match(r'\"', r):
        doYield = not doYield
      
      if re.match('\s', r) and doYield:
        continue

      ret += r
    except StopIteration:
      break
    else:
      if doYield:
        yield ret
        ret = ''

def stripComments(code):
  return re.sub(_COMMENT_REGEX, '', code)

def testCompile(code):
  OUT = tempfile.gettempdir() + '/out.oof.cpp'
  IN = tempfile.gettempdir() + '/in.oof.cpp'
  FNULL = open(os.devnull, 'w')

  with open(IN, 'w+') as f:
    f.write(code)

  if subprocess.call("g++ -o %s %s" % (OUT, IN), shell=True, stdout=FNULL, stderr=FNULL) == 0:
    os.remove(OUT)
    return True
  else:
    return False