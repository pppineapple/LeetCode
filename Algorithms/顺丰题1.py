#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 11:19:34 2018

@author: pineapple
"""

data = [8.0, 10.0, 8.0, 10.0, 8.0, 10.0, 8.0, 10.0, 12.0, 14.5]
#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************
def  schedule(data):
    infolist = []
    for i in range(0, len(data),2):
        infolist.append((data[i],data[i+1]))
    infolist.sort()
    opt = [0] * len(infolist)
    opt[0] = 0
    if infolist[1][0] >= infolist[0][1]:
        opt[1] = 0
    else:
        opt[1] = 1
    for j in range(2,len(infolist)):
        A = opt[j-1] + 1
        u = j-1
        while u > 0:
            if infolist[u][1] <= infolist[j][0]:
                B = opt[u]
                break
            else:
                u -= 1
        if u == 0:
            B = j
        opt[j] = min(A,B)
    return opt[-1]
#******************************结束写代码******************************


_data_cnt = 0
_data_cnt = int(raw_input())
_data_i=0
_data = []
while _data_i < _data_cnt:
    _data_item = float(raw_input())
    _data.append(_data_item)
    _data_i+=1

  
res = schedule(_data)

print str(res) + "\n"
