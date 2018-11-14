#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 12:14:52 2018

@author: pineapple
"""

'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

'''
我的：时间复杂度O(n) 空间复杂度O(1)
思路：按照帕斯卡定义来，每生成一层列表是先设置[1]然后append()上一层数字和
    最后还要append(1)
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        i = 2
        while i < numRows:
            tmp = [1]
            for j in range(len(res[i-1])-1):
                tmp.append(res[i-1][j] + res[i-1][j+1])
            tmp.append(1)
            i += 1
            res.append(tmp)
        return res

