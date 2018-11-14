#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 15:20:30 2018

@author: pineapple
"""

l1 = [6, 3]
q = [1, 3, 5, 2, 5, 4]
p = [1, 1, 0, 1, 0, 0]

def fun(l1, q, p):
    max_interest = []
    for i in range(len(p)-2):
        fix_interest = sum([q[i] for i in range(len(q)) if p[i] == 1])
        max_i = sum(q[i:i+3])
      
        for j in range(i, i+3):
            if p[i] == 1:
                fix_interest -= q[i]
        max_interest.append(max_i+fix_interest)
    
    fix_interest = sum([q[i] for i in range(len(q)) if p[i] == 1])
    for k in [len(q)-2, len(q)-1]:
        if p[k] == 1:
            fix_interest -= q[k]
    last2 = q[len(q)-2] + q[len(q)-1] + fix_interest 
    max_interest.append(last2)
    
    fix_interest = sum([q[i] for i in range(len(q)) if p[i] == 1])
    if p[len(q)-1] == 1:
        fix_interest -= p[len(q)-1]
    last1 = q[len(q)-1] + fix_interest
    max_interest.append(last1)
    
    return max(max_interest)
        
        
        
sum(q[0:0+3])
