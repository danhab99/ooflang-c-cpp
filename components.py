import re

_INCLUDE_REGEX = re.compile(r'#include ["<][a-zA-z]+[>"]')
_TOKEN_REGEX = re.compile(r"(\s|\n|;|'|\"|\+|=|-|\[|\]|\{|\}|\(|\)|!|@|#|\$|%|\^|&|<<|>>|\*\*|\*|<|>|,|\.|\/|\?|;|:|\||)")
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
