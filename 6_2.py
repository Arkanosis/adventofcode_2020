#! /usr/bin/env python3

rank = 0
ans = set()
sum = 0
with open('6.input', 'r') as file:
  for line in file:
    line = line.strip()
    if line:
      if not rank:
        ans.update(line)
      else:
        ans &= set(line)
      rank += 1
    else:
      sum += len(ans)
      ans = set()
      rank = 0
  else:
    sum += len(ans)
print(sum)
