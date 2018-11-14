#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 19:47:30 2018

@author: pineapple
"""

S = 'ababcb'
T = 'xyx'

def solve(S, T):
    if S is None or T is None:
        return 0
    if len(T) == 1:
        return len(S)
    start = 0
    count = 0
    while start <= len(S)-len(T):   
        if len(set(S[start:start+len(T)])) == len(set(T)):        
            iscount = True
            shash = {}
            for i in range(len(T)):
                if T[i] not in shash:
                    shash[T[i]] = S[i]
                else:
                    if shash[T[i]] != S[i]:
                        iscount = False
                        break
            if iscount:
                count += 1
        start += 1
    return count
solve(S, T)
