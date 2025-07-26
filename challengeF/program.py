#!/usr/bin/env python3

'''
Challenge F: Matrix
'''

import sys
from typing import Tuple

def compute_table(grid: list[list[int]], rows: int, cols: int) -> list[list[int]]:
    # 1. Initialize table
    table = []
    table = [[float('inf') for _ in range(cols)] for _ in range(rows)] 
    
    # 2. Build table
    for row in range(rows):
        table[row][0] = grid[row][0]
    
    for col in range(1, cols):
        for row in range(rows):
            if row - 1 < 0:
                table[rows - 1][col] = min(
                    table[rows - 1][col],
                    grid[rows - 1][col] + table[0][col - 1])
            else:
                table[row - 1][col] = min(
                    table[row - 1][col],
                    grid[row - 1][col] + table[row][col - 1])
            
            # Left to right
            table[row][col] = min(
                table[row][col],
                grid[row][col] + table[row][col - 1])
            
            # Diagonal movements
            if row + 1 >= rows:
                table[0][col] = min(
                    table[0][col],
                    grid[0][col] + table[rows - 1][col - 1])
            else:
                table[row + 1][col] = min(
                    table[row + 1][col],
                    grid[row + 1][col] + table[row][col - 1])
            
                
    # 3. Use table result
    return table 

def shortest_path(grid: list[list[int]], table: list[list[int]], rows: int, cols: int) -> Tuple[int, list[int]]:
    # 1. Reconstruct the path by going from the end to the beginning.
    path = []
    row, col = rows - 1, cols - 1
    
    weight = float('inf')
    for r in range(rows):
        if table[r][cols - 1] < weight:
            weight = table[r][cols - 1]
            row = r
              
    # 2. Backtrack
    while col > 0:
        path.append(row + 1)
         
        candidates = [] 
        # Diagonal movements
        if row - 1 < 0:
            if table[row][col] - grid[row][col] == table[rows - 1][col - 1]:
                candidates.append(rows - 1)
                
        else: 
            if table[row][col] - grid[row][col] == table[row - 1][col - 1]:
                candidates.append(row - 1)
        
        # Left to right
        if table[row][col] - grid[row][col] == table[row][col - 1]:
            candidates.append(row)

        
        if row + 1 >= rows:
            if table[row][col] - grid[row][col] == table[0][col - 1]:
                candidates.append(0)
        
        else:
            if table[row][col] - grid[row][col] == table[row + 1][col - 1]:
                candidates.append(row + 1)

        candidates.sort(reverse=True)
        row = candidates.pop()
        col -= 1 
    
    path.append(row + 1)
    
    # 3. Return path
    path.reverse()
    return weight, path
    
def main():
    for line in sys.stdin:
        rows, cols = map(int, line.split())
        
        grid = []
        for i in range(rows):
            row = list(map(int, sys.stdin.readline().split()))
            grid.append(row)
        
        table = compute_table(grid, rows, cols)
        
        weight, path = shortest_path(grid, table, rows, cols)
        
        print(f"{weight}")
        print(f"{' '.join(map(str, path))}")

if __name__ == '__main__':
    main()

# vim set sts=4 sw=4 ts=8 expandtab ft=python:
