#! /usr/bin/env python3

cts = {}
with open('21.input', 'r') as file:
  for line in file:
    line = line.strip()
    ins, als = line[:-1].split(' (contains ')
    ins = ins.split(' ')
    als = als.split(', ')
    for al in als:
      if al in cts:
        cts[al] &= set(ins)
      else:
        cts[al] = set(ins)

while [1 for als in cts.values() if len(als) > 1]:
  for al, ins in cts.items():
    if len(ins) == 1:
      i = next(iter(ins))
      for al, ins in cts.items():
        if len(ins) > 1 and i in ins:
          ins.remove(i)

print(','.join([i for _, i in sorted([(al, next(iter(ins))) for al, ins in cts.items()])]))
