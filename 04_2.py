#! /usr/bin/env python3

def byr(x):
  return 1920 <= int(x) <= 2002

def iyr(x):
  return 2010 <= int(x) <= 2020

def eyr(x):
  return 2020 <= int(x) <= 2030

def hgt(x):
  if x.endswith('cm'):
    return 150 <= int(x[:-2]) <= 193
  elif x.endswith('in'):
    return 59 <= int(x[:-2]) <= 76
  return False

def hcl(x):
  if len(x) != 7 or x[0] != '#':
    return False
  for c in x[1:]:
    if c not in '0123456789abcdef':
      return False
  return True

def ecl(x):
  return x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def pid(x):
  int(x)
  return len(x) == 9

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
    values = [kv.split(':') for kv in line.strip().split()]
    if values:
      for key, value in values:
        if key in fields:
          try:
            if globals()[key](value):
              present.add(key)
          except:
            pass
    else:
      if fields <= present:
        valid += 1
      present = set()
  else:
    if fields <= present:
      valid += 1
print(valid)
