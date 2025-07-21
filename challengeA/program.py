#!/usr/bin/env python3

'''
Challenge A: Views of Sunrise
'''

import sys

def viewable(buildings: list[int]) -> int:
    count = 1
    for i in range(len(buildings) - 1):
        if buildings[i] > max(buildings[i+1:]):
            count += 1
    
    return count
        
def main():
    for line in sys.stdin:
        buildings = list(map(int, line.split()))
        count = viewable(buildings)
        print(count)

if __name__ == '__main__':
    main()

# vim set sts=4 sw=4 ts=8 expandtab ft=python: 
