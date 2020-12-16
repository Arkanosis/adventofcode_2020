#! /usr/bin/env python3

class Rule:
  pass

block = 0
rules = []
o = []

with open('16.input', 'r') as file:
  for line in file:
    line = line.strip()
    if not line:
      next(file)
      block += 1
      continue
    if block == 0:
      rule = Rule()
      rule.field, values = line.split(': ')
      r1, r2 = values.split(' or ')
      r1m, r1M = r1.split('-')
      r2m, r2M = r2.split('-')
      rule.r1m = int(r1m)
      rule.r1M = int(r1M)
      rule.r2m = int(r2m)
      rule.r2M = int(r2M)
      rules.append(rule)
    elif block == 1:
      my = [int(x) for x in line.split(',')]
      next(file)
      next(file)
      block += 1
    elif block == 2:
      o.append([int(x) for x in line.split(',')])

v = []
for t in o:
  allvalid = True
  for f in t:
    valid = False
    for r in rules:
      if r.r1m <= f <= r.r1M or r.r2m <= f <= r.r2M:
        valid = True
    if not valid:
      allvalid = False
  if allvalid:
    v.append(t)

p = []
for r1 in rules:
  p.append([])
  for r2 in rules:
    p[-1].append(r2.field)

for t in v + [my]:
  for i, f in enumerate(t):
    for r in rules:
      if not (r.r1m <= f <= r.r1M or r.r2m <= f <= r.r2M):
        p[i].remove(r.field)

found = set()
while sum([len(pos) for pos in p]) != 20:
  for pos in p:
    if len(pos) == 1 and pos[0] not in found:
      known = pos[0]
  for pos in p:
    if len(pos) != 1 and known in pos:
      pos.remove(known)
  found.add(known)

prod = 1
for i, f in enumerate(my):
  if p[i][0].startswith('departure'):
    prod *= f
print(prod)
