#!/usr/bin/env python3

'''
Challenge G: Isolated Circuits
'''

import sys
from collections import deque, defaultdict

Graph = list[list[int]]

def circuits(graph: Graph, start: int=0) -> int:
    frontier = deque([start])
    visited  = set()
    count = 0
    
    for i in range(len(graph)):
        if i in visited:
            continue
        
        count += 1
        
        frontier.append(i)
        
        while frontier:
            vertex = frontier.pop()
            
            if vertex in visited:
                continue
            
            visited.add(vertex)
            
            for neighbor, distance in enumerate(graph[vertex]):
                if distance == 0:
                    continue
                
                frontier.append(neighbor)
        
    return count
     
def main():
    system = 1
    while True:
        
        line = sys.stdin.readline()
        if not line:
            break
        vertices = int(line)
    
        graph = []
        for i in range(vertices):
            row = list(map(int, sys.stdin.readline().split()))
            graph.append(row)
    
        count = circuits(graph)
        print(f"System {system} isolated circuits: {count}")
        
        system += 1 

if __name__ == '__main__':
    main()

# vim set sts=4 sw=4 ts=8 expandtab ft=python:
