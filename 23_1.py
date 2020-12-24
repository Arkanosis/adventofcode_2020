#! /usr/bin/env python3

with open('23.input', 'r') as file:
  for line in file:
    line = line.strip()
    c = [x for x in line]

ic = [int(x) for x in c]
mn, Mx = min(ic), max(ic)

for m in range(0, 100):
  #print(f'-- move {m + 1} --')
  s = m % len(c)
  b, i, a = c[:s], c[s], c[s + 1:]
  #print(f'cups: {" ".join(b)} ({i}) {" ".join(a)}')
  p = a[:3]
  t = len(p)
  if t < 3:
    p += b[:3 - t]
  for k in p:
    c.remove(k)
  #print(f'pick up: {" ".join(p)}')
  d = int(i) - 1
  while str(d) not in c:
    #print(d, 'not in', c, m)
    d -= 1
    if d < mn:
      d = Mx
  d = str(d)
  #print(f'destination: {d}\n')
  i = c.index(d)
  c = c[:i + 1] + p + c[i + 1:]
  if i < s:
    c = c[t:] + c[:t]
#print(f'-- final --')
s = (m + 1) % len(c)
b, i, a = c[:s], c[s], c[s + 1:]
#print(f'cups: {" ".join(b)} ({i}) {" ".join(a)}')
b, a = ''.join(c).split('1')
print(a + b)
