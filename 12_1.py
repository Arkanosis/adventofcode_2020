#! /usr/bin/env python3

o, x, y = 0, 0, 0
with open('12.input', 'r') as file:
  for line in file:
    line = line.strip()
    i, v = line[0], int(line[1:])
    if i == 'F':
      i = 'ENWS'[o]
    if i == 'N':
      y += v
    elif i == 'S':
      y -= v
    elif i == 'E':
      x += v
    elif i == 'W':
      x -= v
    elif i == 'L':
      o = int((o + v / 90) % 4)
    elif i == 'R':
      o = int((o - v / 90) % 4)

print(abs(x) + abs(y))
