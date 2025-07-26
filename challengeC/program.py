#!/usr/bin/env python3

'''
Challenge C: Missing Operations
'''

import sys

EQUATION = "(((9 {} 8) {} 7) {} 6) {} (5 {} (4 {} (3 {} (2 {} 1))))"

def generate_operations(operations: list[str], count: int, target: int) -> None:
    if count == 0:
        equation = EQUATION.format(*operations)
        if eval(equation) == target:
            print(f"{equation} = {target}")
        return 
    
    generate_operations(operations + ['+'], count - 1, target)
    generate_operations(operations + ['-'], count - 1, target)
    generate_operations(operations + ['*'], count - 1, target)   

def main():
    for line in sys.stdin:
        target = int(line)
        
        generate_operations([], 8, target)
        
if __name__ == '__main__':
    main()

# vim set sts=4 sw=4 ts=8 expandtab ft=python:
