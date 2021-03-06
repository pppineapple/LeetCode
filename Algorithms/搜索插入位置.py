# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:00:02 2018

@author: xiaohong
"""

'''
搜索插入位置
'''

'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
'''

'''
我的 24ms
'''
def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1 and nums[0] >= target:
            return 0
        elif len(nums) == 1 and nums[0] < target:
            return 1
        else:
            pass

        
        if nums[0] < nums[1]:
            for i in range(len(nums)):
                if nums[i] >= target:
                    return i
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i-1] >= target:
                    return len(nums)-i
            return 0
