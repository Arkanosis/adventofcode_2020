#! /usr/bin/env python3

grid = set()
with open('24.input', 'r') as file:
  for line in file:
    line = line.strip()
    pos = 0
    x, y, z = 0, 0, 0
    while pos < len(line):
      if line[pos] == 'e':
        x += 1
        y -= 1
        pos += 1
      elif line[pos] == 'w':
        x -= 1
        y += 1
        pos += 1
      elif line[pos] == 's':
        if line[pos + 1] == 'e':
          y -= 1
          z += 1
        else:
          x -= 1
          z += 1
        pos += 2
      elif line[pos] == 'n':
        if line[pos + 1] == 'e':
          x += 1
          z -= 1
        else:
          y += 1
          z -= 1
        pos += 2
    if (x, y, z) in grid:
      grid.remove((x, y, z))
    else:
      grid.add((x, y, z))
print(len(grid))
