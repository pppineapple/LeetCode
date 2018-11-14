#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:43:11 2018

@author: pineapple
"""

'''
给定一个排序数组，你需要在原地删除重复出现的元素，
使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组
并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定 nums = [1,1,1,2,2,3],

函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,1,2,3,3],

函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。

你不需要考虑数组中超出新长度后面的元素。
'''


'''
别人的：　 时间复杂度O(n) 空间复杂度O(1)
三个指针　i,k,j　维护整个数组
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        i = 1
        k = i-1
        j = i+1
        while j < len(nums):
            if nums[j] != nums[i] or (nums[j] == nums[i] and nums[k] != nums[i]):
                k = i
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i+1
    

'''
别人的：　 时间复杂度O(n) 空间复杂度O(1)
单指针i，另一种角度，从ｉ=2开始，如果nums[i] == nums[i-2]
就del删除　nums[i-2]　同时记录nums长度的变量n = n-1
否则指针i向前移动
'''    
class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        i = 2
        n = len(nums)
        while i < len(nums):
            if nums[i] == nums[i-2]:
                del nums[i]
                n -= 1
            else:
               i += 1
        return n