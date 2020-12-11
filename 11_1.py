#! /usr/bin/env python3

import copy

def mutate(seats):
  def g(r, s):
    if 0 <= r < len(seats):
      if 0 <= s < len(seats[0]):
        return seats[r][s]
    return '.'

  def adj(r, s):
    return [
      g(r + 1, s - 1), g(r + 1, s), g(r + 1, s + 1),
      g(r    , s - 1),              g(r    , s + 1),
      g(r - 1, s - 1), g(r - 1, s), g(r - 1, s + 1),
    ]

  news = copy.deepcopy(seats)
  for r in range(len(news)):
    for s in range(len(news[0])):
      if g(r, s) == 'L' and '#' not in adj(r, s):
        news[r][s] = '#'
      if g(r, s) == '#' and adj(r, s).count('#') >= 4:
        news[r][s] = 'L'
  return news

def count(seats):
  return sum([r.count('#') for r in seats])

seats = []
with open('11.input', 'r') as file:
  for line in file:
    line = line.strip()
    seats.append([s for s in line])

while True:
  news = mutate(seats)
  if news == seats:
    break
  seats = news

print(count(seats))
