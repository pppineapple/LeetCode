#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:23:31 2018

@author: pineapple
"""
'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，
同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''

'''
我的：时间复杂度O(n) 空间复杂度O(1)
思路：单指针遍历，如果nums[i]==0，就pop掉它，然后数组尾部加 0
    这时指针不动，知道当前位置nums[i]不等于0，指针向前移动
    最终指针只移动到 len(nums) 减去数组含0个数处为止。
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = nums.count(0)
        i = 0
        while i < (len(nums)-zero):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1
                
'''
更好的思路： 时间复杂度O(n) 空间复杂度O(1)
只要把数组中所有的非零元素，按顺序给数组的前段元素位赋值，
剩下的全部直接赋值 0
双指针，慢指针维护数组前段被赋值的元素，快指针维护赋值的元素
    如果快指针的元素不为０，就将该元素赋值到慢指针处，
    快慢指针同时前进１
    如果快指针的元素为０，快指针前进１，慢指针不动
    直到快指针到达数组末端
    最后从慢指针的停留位置开始一直到数组末端的元素全部赋值０
'''                
class Solution1(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        for k in range(i, len(nums)):
            nums[k] = 0
            