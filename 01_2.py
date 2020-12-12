#! /usr/bin/env python3

with open('1.input') as file:
    numbers = [int(line.strip()) for line in file.readlines()]

for a in numbers:
    for b in numbers:
        for c in numbers:
            if a + b + c == 2020:
                print(a, b, c, a * b * c)
