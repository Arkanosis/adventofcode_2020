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
  for v in al:
    if p >= len(s):
      return (False, 0)
    if type(v) == int:
      ok, np = check_rule(s, p, v)
      if not ok:
        return (False, 0)
      else:
        p = np
    else:
      if s[p] != v:
        return (False, 0)
      else:
        p += 1
  return (True, p)

def check_rule(s, p, r):
  for al in rules[r]:
    ok, np = check_al(s, p, al)
    if ok:
      return (True, np)
  return (False, 0)

count = 0
with open('19.1.input', 'r') as file:
  for line in file:
    line = line.strip()
    if ':' in line:
      parse_rule(line)
    else:
      ok, np = check_rule(line, 0, 0)
      if ok and np == len(line):
        count += 1
print(count)
