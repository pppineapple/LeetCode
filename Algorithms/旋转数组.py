#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 10:18:48 2018

@author: pineapple
"""

'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
'''

'''
别人的：　时间复杂度O(n) 空间复杂度O(1)
思路：　旋转　[1,2,3,4,5,6,7]　k = 3
可以先将数组反转，[7,6,5,4,3,2,1]
然后将前ｋ个元素反转　[5,6,7,4,3,2,1]
再将后ｋ个元素反转　[5,6,7,1,2,3,4]
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        ''' method 1
        k = k%len(nums)
        i = 0
        while i < k:
            node = nums.pop()
            nums.insert(0, node)
            i += 1
        ''' 
        
        ''' method 2 '''
        k = k%len(nums)        
        nums.reverse()
        left = 0
        right = k-1
        while left < right:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1        
        left = k
        right = len(nums)-1
        while left < right:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1
                
nums = [1,2,3,4,5,6,7]
k = 3
