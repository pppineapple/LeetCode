#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 20:41:07 2018

@author: pineapple
"""

def query(line2, first, last):
    left = min(first, last)
    right = max(first, last)
    return max(line2[left-1:right])

def update(line2, first, last):
    line2[first-1] = last
    
while True:
    try:
        line1 = map(int, raw_input().split(' '))
        N, M = line1[0], line1[1]
        line2 = map(int, raw_input().split(' '))
        for i in range(M):
            line =  raw_input().split(' ')
            first = int(line[1])
            last = int(line[2])
            if line[0] == "Q":
                print query(line2, first, last)
            else:
                update(line2, first, last)
    except:
        break