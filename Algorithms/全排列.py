#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:40:26 2018

@author: pineapple
"""

'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

'''
我的：时间复杂度O(n)　空间复杂度O(1)
思路：递归思想，
    递归的时候是看，新加入的元素必须是不在res数组中出现的
    递归出口是res的长度和nums长度一样
    就把res加入到ans数组中去
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        ans = []
        self.generate(res, ans, nums)
        return ans
        
        
    def generate(self, res, ans, nums):
        if len(res) == len(nums):
            ans.append(res[:])
        else:            
            for i in range(len(nums)):
                if nums[i] not in res:
                    res.append(nums[i])
                    self.generate(res, ans, nums)
                    res.pop()


nums = [1,2,3]
s = Solution()
s.permute(nums)
