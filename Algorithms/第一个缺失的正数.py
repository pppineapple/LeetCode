#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 22:30:24 2018

@author: pineapple
"""

'''
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
'''


'''
别人：时间复杂度O(n) 空间复杂度O(1)
思路：因为要求是时间复杂度是O(n) 空间复杂度O(1)
    所以就是要求一次只能做一层循环，并且只能原地修改数组
        然后就是以i遍历数组：
        看该i位置的元素nums[i] 是否大于０，并且小于nums的长度，
        如果nums[i]的值不是等于数组索引值加１
        即：nums[i] != nums[nums[i]-1]
        就将　i位置的值和　nums[i]-1　位置的值对调
比如：[3,4,-1,1] 就会变成　[1, -1, 3, 4]
        然后再遍历一遍数组：如果位置i的元素值不等于索引加１就返回索引加１
        如果所有元素的值都等于索引加１，就返回　len(nums) + 1

'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1        
        for i in range(len(nums)):
                while nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[nums[i]-1]:
                    tmp = nums[nums[i]-1]
                    nums[nums[i]-1] = nums[i]
                    nums[i] = tmp                  
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
    
nums = [1,1]
s = Solution()
s.firstMissingPositive(nums)