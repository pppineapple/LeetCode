#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:19:50 2018

@author: pineapple
"""

def compute(k, b, n, t):
    z1 = 1
    for i in range(n):
        z1 = k * z1 + b
    s = 0
    z2 = t
    while z2 < z1:
        z2 = k * z2 + b
        s += 1
    return s

while True:
    try:
        line = map(int, raw_input().split(' '))
        k, b, n, t = line[0], line[1], line[2], line[3]
        print compute(k, b, n, t)
    except:
        break


