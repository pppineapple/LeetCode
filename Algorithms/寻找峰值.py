#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 11:50:03 2018

@author: pineapple
"""
'''
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5 
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
说明:

你的解法应该是 O(logN) 时间复杂度的。
'''


'''
我的：　时间复杂度O(logn) 空间复杂度O(1)
既然题目中提到是O(logN) 时间复杂度，那自然就想到了二分查找
题目中已经说明　nums[i] ≠ nums[i+1]
所以跳跃条件就是，如果　nums[mid] < nums[mid + 1]，就把区间往右缩
如果nums[mid] > nums[mid + 1]，　就把区间往左缩
知道 left > right

只是这里要注意的是：有时候你的mid指针可能会到数组的尾端，
那么条件语句nums[mid] < nums[mid + 1]就不能用了
所以需要在循环时加上额外条件mid < len(nums)-1
并且最后还要判断一次 if mid < len(nums)-1:
'''


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        mid = (left + right)//2
        while mid < len(nums)-1 and left <= right:
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] > nums[mid + 1]:
                right = mid - 1
            mid = (left + right)//2
            
        if mid < len(nums)-1:
            return left
        else:
            return len(nums)-1
        
nums = [1]
