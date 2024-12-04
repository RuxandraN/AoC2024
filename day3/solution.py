"""Day 3 Puzzle"""
import re
from itertools import chain

data = "input.txt"
test = "test.txt"

MUL_INSTRUCTION_RE = 'mul\(\d+\,\d+?\)'
DO_NOT_INSTRUCTION_RE = 'don\'t\(\)'
DO_INSTRUCTION_RE = 'do\(\)'

DO_NOT_INSTRUCTION = "don't()"
DO_INSTRUCTION = "do()"

ALLOWED_INSTRUCTIONS_RE  = [MUL_INSTRUCTION_RE, DO_INSTRUCTION_RE, DO_NOT_INSTRUCTION_RE]

def get_input(file="test.txt"):
    with open(file) as f:
        return f.read().splitlines()
            
    
def part1():
    total = 0
    program = get_input(data)
    instructions = chain.from_iterable(re.findall(MUL_INSTRUCTION_RE, line) for line in program)
    
    for i in instructions:
        total += execute_mul_instruction(i)
        
    return total

def part2():
    total = 0
    program = get_input(data)
    
    lookup = str.join("|", ALLOWED_INSTRUCTIONS_RE)
    instructions = chain.from_iterable(re.findall(lookup, line) for line in program)
    
    execute = True
    for i in instructions:
        if i == DO_NOT_INSTRUCTION:
            execute = False
        elif i == DO_INSTRUCTION:
            execute = True
        else:
            if execute:
                total += execute_mul_instruction(i)
        
    return total

def execute_mul_instruction(instruction):
    numbers = list(map(int, re.findall(r'\d+', instruction)))
    return numbers[0] * numbers[1]

    
print(part1())
print(part2())
