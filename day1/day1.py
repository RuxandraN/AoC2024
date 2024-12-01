#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:44:10 2024

@author: ruxandran

"""

first, second = [], []

with open('input.txt') as file:
    for line in file:
        numbers = line.split()
        first.append(int(numbers[0]))
        second.append(int(numbers[1]))

def part1(first: [int], second: [int]) -> int:
    first, second = sorted(first), sorted(second)
    
    return sum(abs(f - s) for f, s in zip(first, second))


def part2(first: [int], second: [int]) -> int:
    first = set(first)
    count_second = {}
    
    for num in second:
        count_second[num] = count_second.get(num, 0) + 1

    return sum(num * count_second.get(num, 0) for num in first)
   
print(part1(first, second))

print(part2(first, second))