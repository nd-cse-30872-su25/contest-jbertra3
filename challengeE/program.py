#!/usr/bin/env python3

'''
Challenge E: Tree Paths
'''

import sys

def construct_path(target: int, tree: list[int], index: int, path: list[int], paths: list[list[int]]) -> None:    
    if index >= len(tree):
        return
    
    if tree[index] == 0:
        return  
    
    path.append(tree[index])
    if (2 * index + 1 >= len(tree) or tree[2 * index + 1] == 0) and (2 * index + 2 >= len(tree) or tree[2 * index + 2] == 0):
        if sum(path) == target:
            paths.append(path.copy())
            
    construct_path(target, tree, 2 * index + 1, path, paths)
    construct_path(target, tree, 2 * index + 2, path, paths)
    
    path.pop() 
    
def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        target = int(line)
        
        tree = list(map(int, sys.stdin.readline().split()))
    
        paths = []
        construct_path(target, tree, 0, [], paths)
        paths.sort()
  
        for path in paths:
            print(f"{target}: {', '.join(list(map(str, path)))}") 

if __name__ == '__main__':
    main()

# vim set sts=4 sw=4 ts=8 expandtab ft=python:
