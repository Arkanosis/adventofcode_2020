#! /usr/bin/env python3

ins = []
with open('10.input', 'r') as file:
  for line in file:
    line = line.strip()
    ins.append(int(line))
ins.sort()
ins.append(ins[-1] + 3)

prev = 0
ct1, ct3 = 0, 0
for ad in ins:
  if ad - prev == 1:
    ct1 += 1
  elif ad - prev == 3:
    ct3 += 1
  prev = ad
print(ct1 * ct3)
