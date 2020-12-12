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

present = set()
with open('5.input', 'r') as file:
  for line in file:
    line = line.strip()
    present.add(getid(line))

for i in range(128 * 8):
  if i not in present and i - 1 in present and i + 1 in present:
    print(i)
