#!/usr/bin/env python3

'''
Challenge D: Football Scores
'''

import sys
from collections import defaultdict

SCORES = (2, 3, 7)

def ways(score: int) -> dict[int, list[int]]:
    # 1. Build the table
    table = defaultdict(set)
    
    # 2. Determine the base case
    table[0].add(())
        
    # 3. Recurrence relations
    for points in range(1, score + 1):
        for base in SCORES:
            if points - base in table:
                for permutation in table[points - base]:
                    path = tuple(sorted(permutation + (base,)))
                    table[points].add(path)

    return sorted([list(c) for c in table[score]])
    
def main():
    for line in sys.stdin:
        score = int(line)
        
        table = ways(score)
        
        if len(table) == 1:
            print(f"There is 1 way to achieve a score of {score}:")
        else:
            print(f"There are {len(table)} ways to achieve a score of {score}:")
        
        for path in table:
            path = list(map(str, path))
            print(f"{' '.join(path)}")
    
if __name__ == '__main__':
    main()

# vim set sts=4 sw=4 ts=8 expandtab ft=python:
