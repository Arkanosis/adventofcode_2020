#! /usr/bin/env python3

with open('1.input') as file:
    numbers = [int(line.strip()) for line in file.readlines()]

for a in numbers:
    for b in numbers:
        if a + b == 2020:
            print(a, b, a * b)
