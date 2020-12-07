#! /usr/bin/env python3

fields = {
  'byr',
  'iyr',
  'eyr',
  'hgt',
  'hcl',
  'ecl',
  'pid',
#  'cid',
}

valid = 0
present = set()
with open('4.input', 'r') as file:
  for line in file:
    line = [kv.split(':')[0] for kv in line.strip().split()]
    if line:
      present.update(line)
    else:
      if fields <= present:
        valid += 1
        print(present, 'valid')
      else:
        print(present, 'invalid')
      present = set()
  else:
    if fields <= present:
      valid += 1
print(valid)
