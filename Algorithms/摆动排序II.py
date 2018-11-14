#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 18:09:06 2018

@author: pineapple
"""


'''
给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

示例 1:

输入: nums = [1, 5, 1, 1, 6, 4]
输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6]
示例 2:

输入: nums = [1, 3, 2, 2, 3, 1]
输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]
说明:
你可以假设所有输入都会得到有效的结果。

进阶:
你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？
'''

'''
别人的：　时间复杂度O(n) 空间复杂度O(n)
思路：先对原数组排序，然后复制出来得到排序后的数组
    然后将排序后的数组右部分倒序从原数组索引为１处开始，
    每隔1个元素修改为右部分的元素。
    然后将排序后的数组剩下左部分倒序从原数组索引为０处开始，
    每隔1个元素修改为做部分的元素。
'''

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return
        nums_sort = sorted(nums)
        right = 1
        if len(nums)%2 == 0:
            for i in range(len(nums)-1, len(nums)//2 - 1, -1):
                nums[right] = nums_sort[i]
                right += 2
            left = 0
            for j in range(len(nums)//2 - 1, -1, -1):
                nums[left] = nums_sort[j]
                left += 2
        else:
            for i in range(len(nums)-1, len(nums)//2, -1):
                nums[right] = nums_sort[i]
                right += 2
            left = 0
            for j in range(len(nums)//2, -1, -1):
                nums[left] = nums_sort[j]
                left += 2   
                      
        
nums = [1,1,2,1,2,2,1]
nums = [1, 5, 1, 1, 6, 4]
s = Solution()
s.wiggleSort(nums)
