#! /usr/bin/env python3

def getid(p):
  rmin, rmax = 0, 128
  for c in p[:7]:
    if c == 'F':
      rmax -= (rmax - rmin) // 2
    else:
      rmin += (rmax - rmin) // 2
  cmin, cmax = 0, 8
  for c in p[7:]:
    if c == 'L':
      cmax -= (cmax - cmin) // 2
    else:
      cmin += (cmax - cmin) // 2
  return 8 * rmin + cmin

highest = 0
with open('5.input', 'r') as file:
  for line in file:
    line = line.strip()
    i = getid(line)
    if i > highest:
      highest = i
print(highest)
