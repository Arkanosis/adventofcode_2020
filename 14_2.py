#! /usr/bin/env python3

m = {}
with open('14.input', 'r') as file:
  for line in file:
    line = line.strip()
    if line.startswith('mask = '):
      x = line[7:]
    else:
      line = line.split(']')
      a = bin(int(line[0][4:]))[2:]
      v = int(line[1][3:])
      a = '0' * (36 - len(a)) + a
      al = ''
      for ac, xc in zip(a, x):
        if xc == '0':
          al += ac
        elif xc == '1':
          al += '1'
        else:
          al += 'X'
      al = al.split('X')
      for ct in range(pow(2, len(al) - 1)):
        a = bin(ct)[2:]
        a = '0' * (len(al) - len(a) - 1) + a
        ar = ''
        for i in range(len(a)):
          ar += al[i] + a[i]
        ar += al[-1]
        m[ar] = v

p = 0
for v in m.values():
  p += v
print(p)
