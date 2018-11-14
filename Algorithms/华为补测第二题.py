#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:27:43 2018

@author: pineapple
"""
def transform(line):
    hash = {}
    left = 0
    right = 1
    stop = False
    while not stop: 
        if right < len(line):
            if line[right] in '-+':
                unit = line[left:right]
                unit_key = unit.split('X^')[1]
                unit_value = unit.split('X^')[0]
                if unit_key in hash:
                    hash[unit_key] = hash[unit_key] + int(unit_value)
                else:
                    hash[unit_key] = int(unit_value)
                left = right
                right += 1
                
            else:
                right += 1
        else:
            stop = True
            unit = line[left:right]
            unit_key = unit.split('X^')[1]
            unit_value = unit.split('X^')[0]
            if unit_key in hash:
                hash[unit_key] = hash[unit_key] + int(unit_value)
            else:
                hash[unit_key] = int(unit_value)
            
    output = sorted(hash.items(), key = lambda x:x[0], reverse = True)
    ans = ''
    for i in output:
        u = str(i[1]) + 'X^' + str(i[0])
        if i[1] != 0:
            if i[1] > 0:           
                ans += '+'+u
            else:
                ans += u
                
    if len(ans) > 0:
        if ans[0] == '+':
            print ans[1:]
        else:
            print ans
    else:
        print ''

line = '-7X^4+7X^4-3X^3+3X^3'
line = '-7X^4+5X^6-3X^3+3X^3+1X^0'
transform(line)







