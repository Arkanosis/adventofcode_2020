#! /usr/bin/env python3

d = ([], [])
p = -1
with open('22.input', 'r') as file:
  for line in file:
    line = line.strip()
    if ':' in line:
      p += 1
    elif line:
      d[p].append(int(line))

while len(d[0]) and len(d[1]):
  c0, c1 = d[0].pop(0), d[1].pop(0)
  if c0 > c1:
    d[0].extend([c0, c1])
  elif c1 > c0:
    d[1].extend([c1, c0])
  else:
    pass

p = 1
s = 0
for c in (d[0] + d[1])[::-1]:
  s += c * p
  p += 1

print(s)
