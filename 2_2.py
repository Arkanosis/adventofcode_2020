#! /usr/bin/env python3

valid = 0

with open('2.input') as file:
    for line in file:
        line = line.strip().split(': ')
        boundaries, char = line[0].split(' ')
        min, max = boundaries.split('-')
        min, max = int(min), int(max)
        if (line[1][min - 1] + line[1][max - 1]).count(char) == 1:
            valid += 1

print(valid)
