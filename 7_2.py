#! /usr/bin/env python3

import sys

content = {}
with open('7.input', 'r') as file:
  for line in file:
    line = line.strip()
    outside, insides = line.split(' contain ')
    outside = outside.replace(' bags', '')
    inside = []
    if insides != 'no other bags.':
      for x in insides.replace('.', '').split(', '):
        count, color = x.split(' ', 1)
        inside.append((int(count), color.replace(' bags', '').replace(' bag', '')))
    content[outside] = inside

counts = {}
def count(color):
  if color in counts:
    return counts[color]
  else:
    res = 1
    for inside_count, inside_color in content[color]:
      res += inside_count * count(inside_color)
    counts[color] = res
    return res

print(count('shiny gold') - 1)
