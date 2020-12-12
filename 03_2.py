#! /usr/bin/env python3

prod = 1

for slope in [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]:
  x = 0
  y = 0
  trees = 0
  with open('3.input', 'r') as file:
    for line in file:
      line = line.strip()
      if y % slope[1] == 0:
        if line[x] == '#':
          trees += 1
        x = (x + slope[0]) % len(line)
      y += 1
    prod *= trees

print(prod)
