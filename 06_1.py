#! /usr/bin/env python3

ans = set()
sum = 0
with open('6.input', 'r') as file:
  for line in file:
    line = line.strip()
    if line:
      ans.update(line)
    else:
      sum += len(ans)
      ans = set()
  else:
    sum += len(ans)
print(sum)
