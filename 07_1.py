#! /usr/bin/env python3

import sys

outsides = {'shiny gold'}
prevlen = 0
while len(outsides) != prevlen:
  prevlen = len(outsides)
  new = []
  with open('7.input', 'r') as file:
    for line in file:
      line = line.strip()
      outside, inside = line.split(' contain ')
      for color in outsides:
        if color in inside:
          new.append(outside.replace(' bags', ''))
    outsides.update(new)

print(len(outsides) - 1)
