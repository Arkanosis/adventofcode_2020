#! /usr/bin/env python3

from operator import add, mul

def tokenize(string):
  for token in string.split(' '):
    while token[0] == '(':
      yield '('
      token = token[1:]
    e = []
    while token[-1] == ')':
      e.append(')')
      token = token[:-1]
    yield token
    for p in e:
      yield(p)

def eval(exp):
  value = 0
  op = add
  for token in exp:
    if token == '+':
      op = add
    elif token == '*':
      return mul(value, eval(exp))
    elif token == '(':
      value = op(value, eval(exp))
    elif token == ')':
      return value
    else:
      value = op(value, int(token))
  return value

sum = 0
with open('18.input', 'r') as file:
  for line in file:
    line = line.strip()
    sum += eval(tokenize(line))
print(sum)
