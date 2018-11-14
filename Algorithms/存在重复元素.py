#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 14:21:43 2018

@author: pineapple
"""

'''
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。
如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
'''

'''
我的：　时间复杂度O(n) 空间复杂度O(n)
思路：　遍历数组，建立hash表，如果在hash表中出现过,就返回True
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                return True
        return False
        