#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 12:09:08 2018

@author: pineapple
"""


'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。
找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''

'''
我的：时间复杂度O(logn) 空间复杂度O(1)
思路：二分查找到target的位置
    然后向前向后移动指针找到第一个位置和最后一个位置
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        mid = (left + right)//2
        found = False
        while left <= right and not found:
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                found = True
                break
            mid = (left + right)//2
        
        if not found:
            return [-1,-1]
        
        start = mid-1
        end = mid+1
        while  start >= 0 and nums[start] == target:
            start-=1
        while end < len(nums) and nums[end] == target:
            end += 1
        return [start+1, end-1]
    
'''
更简洁的代码
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        mid = (left + right)//2
        while left <= right:
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                start = mid-1
                end = mid+1
                while start >= 0 and nums[start] == target:
                    start -= 1
                while end < len(nums) and nums[end] == target:
                    end += 1
                return [start+1, end-1]                
            mid = (left + right)//2        
        return [-1,-1]