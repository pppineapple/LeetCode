#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 19:37:11 2018

@author: pineapple
"""



def  miHomeGiftBag(p, M):
    p.sort()
    subset = [[None] * (M+1) for i in range(len(p))]
    for i in range(len(p)):
        subset[i][0] = True
    for j in range(len(subset[0])):
        subset[0][j] = False        
    subset[0][p[0]] = True
    for i in range(1, len(p)):
        for s in range(1, M+1):
            if p[i] > M:
                subset[i][s] = subset[i-1][s]
            else:
                A = subset[i-1][s-p[i]]
                B = subset[i-1][s]
                subset[i][s] = A or B
    if subset[-1][-1]:
        return 1
    else:
        return 0

subset[-1][-1] = None


p = [99, 199, 1999, 10000, 39, 1499]
M = 10238
p = [3,34,4,12,5,1]
M = 34
miHomeGiftBag(p, M)
