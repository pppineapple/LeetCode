#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 11:47:08 2018

@author: pineapple
"""
'''
长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，
找出该数组中满足其和 ≥ s 的长度最小的连续子数组。
如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
'''

'''
别人的　时间复杂度O(n) 空间复杂度O(1)
思路：　双指针滑块法：
        因为是找连续的子集，利用快指针i和慢指针j来维护一个滑块效果
        直到慢指针移动到数组末尾，就结束循环
        利用一个变量sumlen来表示滑块内布置的和，初始值为０
        minlen来表示滑块长度，初始值为len(nums)
        循环时，如果滑块内部值的和小于s，就让快指针向前移动，sumlen+=nums[j]
        如果滑块内部值的和大于s，就让慢指针向前移动 sumlen-=nums[i]
        并且这个时候要记录当前滑块的长度,就是和历史滑块长度取小　min(minlen, j-i)
        注意判断一些边界值。
'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums == [] or sum(nums) < s:
            return 0
        l = 0
        r = 0
        sumlen = 0
        minlen = len(nums)
        while l < len(nums):
            if r < len(nums) and sumlen < s:
                sumlen += nums[r]
                r += 1
            else:
                sumlen -= nums[l]
                l += 1
                
            if sumlen >= s:
                minlen = min(minlen, r-l)
        return minlen
    
s = 7
nums = [2,3,1,2,4,3]
S = Solution()
S.minSubArrayLen(s,nums)