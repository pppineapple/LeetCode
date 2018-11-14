# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:14:25 2018

@author: xiaohong
"""

'''
最大子序和
'''

'''
给定一个整数数组 nums ，
找到一个具有最大和的连续子数组（子数组最少包含一个元素），
返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6

解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''



'''
别人的 40ms
'''
def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        current = 0
        m = current
        for i in range(1, len(nums)):
            if current < 0:
                current = 0
            current += nums[i]
            m = max(m, current)
        return m
    
maxSubArray([1,2,-1,2,3,-7])
