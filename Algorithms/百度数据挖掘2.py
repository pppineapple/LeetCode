#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:35:10 2018

@author: pineapple
"""

a = 'abab'.split()[0]
alist = list(a)
i = 0
n = len(a)
seen = set()
count = 0
while i < n:
    p = alist.pop(0)
    alist.append(p)
    if ''.join(alist) not in seen:
        seen.add(''.join(alist))
        count += 1
    i+=1
 
    
print count


'ooo'.count('oo')
