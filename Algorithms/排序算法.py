#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 22:42:08 2018

@author: pineapple
"""

'''
快排
'''

def helpquckersort(alist, first, last):
    pivotvalue = alist[first]
    left = first + 1
    right = last
    
    stop = False
    while not stop:
        while left <= right and alist[left] <= pivotvalue:
            left += 1
        while alist[right] >= pivotvalue and left <= right:
            right -= 1
        if left > right:
            stop = True
        else:
            tmp = alist[left]
            alist[left] = alist[right]
            alist[right] = tmp
    tmp = alist[first]
    alist[first] = alist[right]
    alist[right] = tmp
    return right



def quickersort(alist, first, last):
    if first < last:
        split = helpquckersort(alist, first, last)
        quickersort(alist, first, split-1)
        quickersort(alist, split+1, last)

        
alist = [54,26,93,17,77,31,44,55,20]
quickersort(alist, 0, len(alist)-1)


'''
归并排序
'''
def merge(left, right):
    result = []
    l = 0
    r = 0
    while l < len(left) and  r < len(right):
        if left[l] > right[r]:
            result.append(right[r])
            r += 1
        else:
            result.append(left[l])
            l += 1
    if l < len(left):
        result += left[l:]
    if r < len(right):
        result += right[r:]
    return result
            
def mergesort(alist):
    if len(alist) <= 1:
        return alist
    else:
        mid = len(alist)//2
        left = mergesort(alist[:mid])
        right =  mergesort(alist[mid:])
        return merge(left, right)
    
alist	=	[54,26,93,17,77,31,44,55,20]
mergesort(alist)
    