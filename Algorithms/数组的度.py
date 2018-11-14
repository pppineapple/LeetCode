# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:41:56 2018

@author: xiaohong
"""

'''
给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:
输入: [1, 2, 2, 3, 1]
输出: 2
解释: 
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.

示例 2:
输入: [1,2,2,3,1,4,2]
输出: 6
注意:

nums.length 在1到50,000区间范围内。
nums[i] 是一个在0到49,999范围内的整数。
'''

'''
别人的 0.83
思路： 首先遍历数组，创建3个哈希表记录数组每个元素出现的次数，出现的初始位置，
        出现的末位置，同时用一个变量记录元素出现的最多次数
        然后遍历一遍元素次数哈希表，与元素出现的最多次数相比较，如果有多个元素出现
        最多数，然就比较他们的起始位置和结束位置，去最短的。
'''


def findShortestSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numcount = {}
        numfirst = {}
        numend = {}
        maxcount = 0
        for i in range(len(nums)):
            if nums[i] not in numcount:
                numcount[nums[i]] = 1
                numfirst[nums[i]] = i
                numend[nums[i]] = i
            else:
                numcount[nums[i]] += 1
                numend[nums[i]] = i
            maxcount = max(maxcount, numcount[nums[i]])
        
        shortmin = len(nums)
        for num in numcount:
            if numcount[num] == maxcount:
                shortmin = min(shortmin, numend[num]-numfirst[num]+1)
        return shortmin
        
nums =  [1, 2, 2, 3, 1]
nums = [1,2,2,3,1,4,2]       
findShortestSubArray(nums)

