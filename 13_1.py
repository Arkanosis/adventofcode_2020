#! /usr/bin/env python3

with open('13.input', 'r') as file:
  time = int(next(file).strip())
  ids = [int(x) for x in next(file).strip().split(',') if x != 'x']

mi, mt = -1, -1
for id in ids:
  t = id
  while t < time:
    t += id
  if mt == -1 or t < mt:
    mi = id
    mt = t

print(mi * (mt - time))
