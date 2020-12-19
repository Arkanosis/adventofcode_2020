#! /usr/bin/env python3

rules = {}

def parse_rule(s):
  r, ts = s.split(':')
  als = []
  for al in ts.split('|'):
    vs = []
    for v in al.split(' '):
      if v:
        if v[0] == '"':
          vs.append(v[1:-1])
        else:
          vs.append(int(v))
    als.append(vs)
  rules[int(r)] = als

def check_al(s, p, al):
  if p >= len(s):
    return
  if type(al[0]) == str:
    if s[p] == al[0]:
      yield p + 1
  else:
    for np in check_rule(s, p, al[0]):
      if len(al) == 1:
        yield np
      else:
        yield from check_al(s, np, al[1:])

def check_rule(s, p, r):
  for al in rules[r]:
    yield from check_al(s, p, al)

count = 0
with open('19.2.input', 'r') as file:
  for line in file:
    line = line.strip()
    if ':' in line:
      parse_rule(line)
    else:
      for np in check_rule(line, 0, 0):
        if np == len(line):
          count += 1
print(count)
