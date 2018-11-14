#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:57:55 2018

@author: pineapple
"""


'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

'''
我的　实践复杂度O(n) 空间复杂度O(n)
思路：查表法，把nums中的元素和索引建立成一张hash表，
        { key：元素　value：索引 }
    然后看　target - nums[i] 在不在这个表中
    因为表是根据数组遍历一步一步添加键值对的
    所以如果找到了nums[i] + nums[j] == target
    那一定是找到的是值大的，在hash表中查到的是值小的
    所以返回的是　[hash[res], i]
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in hash:
                return [hash[res], i]
            hash[nums[i]] = i
        return []