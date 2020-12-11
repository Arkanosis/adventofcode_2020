#! /usr/bin/env python3

import copy

def mutate(seats):
  def see(r, s):
    res = []
    for ri, si in [
        (+1, -1), (+1, +0), (+1, +1),
        (+0, -1),           (+0, +1),
        (-1, -1), (-1, +0), (-1, +1),
    ]:
      rs, ss = r + ri, s + si
      while 0 <= rs < len(seats) and 0 <= ss < len(seats[0]):
        if seats[rs][ss] != '.':
          res.append(seats[rs][ss])
          break
        rs, ss = rs + ri, ss + si
    return res

  news = copy.deepcopy(seats)
  for r in range(len(news)):
    for s in range(len(news[0])):
      if seats[r][s] == 'L' and '#' not in see(r, s):
        news[r][s] = '#'
      if seats[r][s] == '#' and see(r, s).count('#') >= 5:
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
