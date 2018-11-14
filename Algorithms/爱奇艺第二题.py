#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 19:33:27 2018

@author: pineapple
"""

def midsearch(a, target):
    a.sort()
    left = 0
    right = len(a)-1
    mid = (left + right)//2
    while left < right:
        splitlen = sum(a[mid:])-a[mid]*(len(a)-mid)
        if splitlen == target:
            print a[mid]
        elif splitlen < target:
            right = mid - 1
        elif splitlen > target:
            left = mid + 1
        mid = (left + right)//2
    
    v1 = a[left]
    v2 = a[left+1]
    vmid = (v1+v2)//2
    while v1 < v2:
        splitlength = sum(a[left+1:])-vmid*(len(a)-left-1)
        if splitlength == target:
            print vmid
        elif splitlength > target:
            v1 = vmid + 1
        elif splitlength < target:
            v2 = vmid - 1
        vmid = (v1+v2)//2
    return vmid

while True:
    try:
        line1 = map(int, raw_input().split(' '))
        n = line1[0]
        target = line1[1]
        a = map(int, raw_input().split(' '))
        print midsearch(a, target)
    except:
        break
    
