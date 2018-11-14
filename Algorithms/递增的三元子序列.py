#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 21:19:05 2018

@author: pineapple
"""


'''
给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:

输入: [1,2,3,4,5]
输出: true
示例 2:

输入: [5,4,3,2,1]
输出: false
'''

'''
别人的：　时间复杂度O(n) 空间复杂度O(1)
思路：利用两个变量one和two来表示数组中i和位置靠后并且比i大的j，
    然后来找大于j同时位置靠后的k
    首先初始one和two无限大
    然后遍历nums，一旦num比one小就令 one = num
    一旦 num小于等于two，并且num大于one，就令 two = num
    这时　tow就比one大，并且在数组中two的位置比one靠后
    一旦 num大于two，就说明找到了递增的长度为３的子集：one<two<num
'''

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3 or nums == []:
            return False
        one = float('inf')
        two = float('inf')
        for num in nums:
            if num <= one:
                one = num
            elif num <= two and num > one:
                two = num
            else:
                return True
        return False
    
nums = [2,1,5,0,4,6]
nums = [1,2,3,4,5,6]
nums = [5,4,3,2,1,0]
nums = [2,4,-2,-3]
nums = [5,1,5,5,2,5,4]
s = Solution()
s.increasingTriplet(nums)
