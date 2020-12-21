#! /usr/bin/env python3

ali = {}
cts = {}
with open('21.input', 'r') as file:
  for line in file:
    line = line.strip()
    ins, als = line[:-1].split(' (contains ')
    ins = ins.split(' ')
    als = als.split(', ')
    for i in ins:
      if i in ali:
        ali[i] += 1
      else:
        ali[i] = 1
    for al in als:
      if al in cts:
        cts[al] &= set(ins)
      else:
        cts[al] = set(ins)
unsafe = set()
for als in cts.values():
  unsafe.update(als)
ct = 0
for i, ict in ali.items():
  if i not in unsafe:
    ct += ict
print(ct)
