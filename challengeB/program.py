#!/usr/bin/env python3

'''
Challenge B: Isomorphic Mapping
'''

import sys

def isomorphic(s: str, t: str) -> bool:
    replacement = {}
    for i in range(len(s)):
        if s[i] not in replacement:
            replacement[s[i]] = t[i]
        elif s[i] in replacement and replacement[s[i]] != t[i]:
            return False
    
    return True 
    
def main():
    for line in sys.stdin:
        s, t = line.strip().split()
        
        if (isomorphic(s, t)):
            print("Isomorphic")
        else:
            print("Not Isomorphic")
    
if __name__ == '__main__':
    main()

# vim set sts=4 sw=4 ts=8 expandtab ft=python:
