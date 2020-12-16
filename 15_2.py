#! /usr/bin/env python3

t = 1
m = {}
l = None
with open('15.input', 'r') as file:
  for line in file:
    line = line.strip()
    for n in line.split(','):
      m[l] = t - 1
      l = int(n)
      t += 1

while t <= 30000000:
  c = m.get(l, 0)
  m[l] = t - 1
  if c != 0:
    l = t - 1 - c
  else:
    l = 0
  t += 1

print(l)
