#! /usr/bin/env python3

def is_sum(number, numbers):
  for a in numbers:
    for b in numbers:
      if a != b and a + b == number:
        return True
  return False

numbers = []
with open('9.input', 'r') as file:
  for line in file:
    number = int(line.strip())
    if len(numbers) == 25:
      if not is_sum(number, numbers):
        invalid = number
        break
      numbers.append(number)
      numbers.pop(0)
    else:
      numbers.append(number)

sums = []
with open('9.input', 'r') as file:
  for line in file:
    number = int(line.strip())
    for i, values in enumerate(sums):
      sums[i] = values + [number]
      if sum(sums[i]) == invalid:
        sums[i].sort()
        print(sums[i][0] + sums[i][-1])
    sums.append([number])
