#! /usr/bin/env python3

x = 0
trees = 0

with open('3.input', 'r') as file:
  for line in file:
    line = [c for c in line.strip()]
    if line[x] == '#':
      trees += 1
    x = (x + 3) % len(line)

print(trees)
