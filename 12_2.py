#! /usr/bin/env python3

x, y = 0, 0
wx, wy = 10, 1
with open('12.input', 'r') as file:
  for line in file:
    line = line.strip()
    i, v = line[0], int(line[1:])
    if i == 'F':
      x += v * wx
      y += v * wy
    elif i == 'N':
      wy += v
    elif i == 'S':
      wy -= v
    elif i == 'E':
      wx += v
    elif i == 'W':
      wx -= v
    elif i == 'L':
      for k in range(v // 90):
        wx, wy = -wy, wx
    elif i == 'R':
      for k in range(v // 90):
        wx, wy = wy, -wx

print(abs(x) + abs(y))
