#! /usr/bin/env python3

with open('13.input', 'r') as file:
  next(file)
  ids = [int(x) if x != 'x' else -1 for x in next(file).strip().split(',')]

n = 1
o = []
for i, id in enumerate(ids):
  if id != -1:
    n *= id
    o.append((id, i))

# Smart method below
# Based on the Chinese remainder theorem

t = 0
for id, delta in o:
  ni = n // id
  s = ni
  while s % id != 1:
    s += ni
  t += (id - delta) * s
t %= n

print(t)

# Optimized brute force version below
# Use the C++ version instead, it's already slow enough
# (slow: ~45 min on a single core of a i7-8750H)

# o.sort(reverse=True)

# ms = o[0][0]
# md = o[0][1]
# od = []
# for id, delta in o[1:]:
#   od.append((id, delta - md))

# import itertools
# for t in itertools.count(0, ms):
#   ok = True
#   for id, delta in od:
#     if (t + delta) % id:
#       ok = False
#       break
#   if ok:
#     print(t - md)
#     break
