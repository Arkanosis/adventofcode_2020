#! /usr/bin/env python3

import collections

def count(s):
  result = 0
  for wv in s.values():
    for zv in wv.values():
      for yv in zv.values():
        for xv in yv.values():
          if xv == '#':
            result += 1
  return result

def display(s, cycle):
  print(f'\n\nAfter {cycle} cycles:\n\n')
  for w in range(-cycle, 1 + cycle):
    for z in range(-cycle, 1 + cycle):
      print(f'z={z}, w={w}')
      for y in range(-cycle, 1 + my + cycle):
        for x in range(-cycle, + 1 + mx + cycle):
          print(s[w][z][y][x], end='')
        print()

def xf():
  return '.'

def yf():
  return collections.defaultdict(xf)

def zf():
  return collections.defaultdict(yf)

def wf():
  return collections.defaultdict(zf)

mx, my = 0, 0
s = collections.defaultdict(wf)
with open('17.input', 'r') as file:
  for y, line in enumerate(file):
    my += 1
    line = line.strip()
    for x, c in enumerate(line):
      mx = max(mx, len(line))
      s[0][0][y][x] = c

def neighbors(s, x, y, z, w):
  count = 0
  for nw in range(w - 1, w + 2):
    for nz in range(z - 1, z + 2):
      for ny in range(y - 1, y + 2):
        for nx in range(x - 1, x + 2):
          if (nx, ny, nz, nw) != (x, y, z, w):
            if s[nw][nz][ny][nx] == '#':
              count += 1
  return count

#display(s, 0)

for cycle in range(1, 7):
  n = collections.defaultdict(wf)
  for w in range(-cycle, 1 + cycle):
    for z in range(-cycle, 1 + cycle):
      for y in range(-cycle, 1 + my + cycle):
        for x in range(-cycle, + 1 + mx + cycle):
          if s[w][z][y][x] == '#':
            if neighbors(s, x, y, z, w) in [2, 3]:
              n[w][z][y][x] = '#'
          else:
            if neighbors(s, x, y, z, w) in [3]:
              n[w][z][y][x] = '#'
  s = n
  #display(s, cycle)

print(count(s))
