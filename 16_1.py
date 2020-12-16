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
      next(file)
      next(file)
      block += 1
    elif block == 2:
      o.append([int(x) for x in line.split(',')])

rate = 0
for t in o:
  for f in t:
    valid = False
    for r in rules:
      if r.r1m <= f <= r.r1M or r.r2m <= f <= r.r2M:
        valid = True
    if not valid:
      rate += f
print(rate)
