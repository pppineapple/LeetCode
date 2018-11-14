#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 19:33:23 2018

@author: pineapple
"""

char = '123456789'
n = 5
def fun(char, n):
    if n < 0:
        return ''
    if n > len(char):
        return -1
    left = 0
    right = left + n
    result = []
    while right < len(char)+1:
        result.append(char[left:right])
        right += 1
        left += 1
    return ' '.join(map(str, result))

fun('abc', 0)
