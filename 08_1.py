#! /usr/bin/env python3

code = []
with open('8.input', 'r') as file:
  for line in file:
    line = line.strip()
    ins, off = line.split()
    code.append((ins, int(off)))

acc = 0
pc = 0
known = set()
while pc not in known:
  known.add(pc)
  ins, arg = code[pc]
  if ins == 'acc':
    acc += arg
    pc += 1
  elif ins == 'jmp':
    pc += arg
  else:
    pc += 1
print(acc)
