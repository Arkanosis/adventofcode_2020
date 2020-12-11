#! /usr/bin/env python3

ins = []
with open('10.input', 'r') as file:
  for line in file:
    line = line.strip()
    ins.append(int(line))
ins.sort()
ins.append(ins[-1] + 3)

ct = [1] + ([0] * ins[-1])
for i in ins:
  ct[i] = ct[i - 1] + ct[i - 2] + ct[i - 3]
print(ct[-1])
