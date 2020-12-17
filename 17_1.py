#! /usr/bin/env python3

import collections

def count(s):
  result = 0
  for zv in s.values():
    for yv in zv.values():
      for xv in yv.values():
        if xv == '#':
          result += 1
  return result

def display(s, cycle):
  print(f'\n\nAfter {cycle} cycles:\n\n')
  for z in range(-cycle, 1 + cycle):
    print(f'z={z}')
    for y in range(-cycle, 1 + my + cycle):
      for x in range(-cycle, + 1 + mx + cycle):
        print(s[z][y][x], end='')
      print()

def xf():
  return '.'

def yf():
  return collections.defaultdict(xf)

def zf():
  return collections.defaultdict(yf)

mx, my, mz = 0, 0, 0
s = collections.defaultdict(zf)
with open('17.input', 'r') as file:
  for y, line in enumerate(file):
    my += 1
    line = line.strip()
    for x, c in enumerate(line):
      mx = max(mx, len(line))
      s[0][y][x] = c

def neighbors(s, x, y, z):
  count = 0
  for nz in range(z - 1, z + 2):
    for ny in range(y - 1, y + 2):
      for nx in range(x - 1, x + 2):
        if (nx, ny, nz) != (x, y, z):
          if s[nz][ny][nx] == '#':
            count += 1
  return count

#display(s, 0)

for cycle in range(1, 7):
  n = collections.defaultdict(zf)
  for z in range(-cycle, 1 + cycle):
    for y in range(-cycle, 1 + my + cycle):
      for x in range(-cycle, + 1 + mx + cycle):
        if s[z][y][x] == '#':
          if neighbors(s, x, y, z) in [2, 3]:
            n[z][y][x] = '#'
        else:
          if neighbors(s, x, y, z) in [3]:
            n[z][y][x] = '#'
  s = n
  #display(s, cycle)

print(count(s))
