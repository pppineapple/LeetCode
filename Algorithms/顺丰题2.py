#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 11:02:34 2018

@author: pineapple
"""

nums = [1,1,1,2,2,3]

#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************
def  topk(nums):
    if len(nums) == 0:
        return 0
    if len(nums) < 3:
        return sum(nums)
    hash = {}
    for i in nums:
        hash[i] = hash.get(i, 0) + 1
    hashcount = {}
    for j in hash:
        if hash[j] not in hashcount:
            hashcount[hash[j]] = [j]
        else:
            hashcount[hash[j]].append(j)
    index = hashcount.keys()
    index.sort()
    findex = hashcount[index[-1]]
    sindex = hashcount[index[-2]]
    if len(findex) > 1:
        minf = len(nums)
        for f in findex:
            minf = min(minf, nums.index(f))
        fvalue = nums[minf]
        findex.remove(nums[minf])
        minf = len(nums)
        for f in findex:
            minf = min(minf, nums.index(f))        
        svalue = nums[minf]
    else:
        fvalue = findex[0]
        if len(sindex) > 1:
            mins = len(nums)
            for s in sindex:
                mins = min(mins, nums.index(s))
            svalue = nums[mins]
        else:
            svalue = sindex[0]
    return svalue+fvalue

#******************************结束写代码******************************


_nums_cnt = 0
_nums_cnt = int(raw_input())
_nums_i=0
_nums = []
while _nums_i < _nums_cnt:
    _nums_item = int(raw_input())
    _nums.append(_nums_item)
    _nums_i+=1

  
res = topk(_nums)

print str(res) + "\n"