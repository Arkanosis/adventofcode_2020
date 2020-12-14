#! /usr/bin/env python3

m = {}
with open('14.input', 'r') as file:
  for line in file:
    line = line.strip()
    if line.startswith('mask = '):
      x = line[7:]
    else:
      line = line.split(']')
      a = line[0][4:]
      v = bin(int(line[1][3:]))[2:]
      v = '0' * (36 - len(v)) + v
      m[a] = []
      for vc, xc in zip(v, x):
        if xc == 'X':
          m[a].append(vc)
        else:
          m[a].append(xc)

p = 0
for v in m.values():
  p += int(''.join(v), 2)
print(p)
