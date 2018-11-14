#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 20:47:49 2018

@author: pineapple
"""


'''
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，
使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，
并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:
输入: nums = [1,2,3,1], k = 3, t = 0
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1, t = 2
输出: true

示例 3:
输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false
'''

'''
别人的：时间复杂度O(n^2) 空间复杂度O(k)
思路：还是采用小滑块，注意小滑块的长度实际是k-1，因为每一次都会将第k个位置
    的数字与小滑块里面的值作比较，看是不是差的绝对值小于ｔ,这样正好保持
    索引差不会超过k
'''
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if nums == []:
            return False
        record = set()
        for i in range(len(nums)):
            if t == 0:
                if nums[i] in record:
                    return True
            else:
                for r in record:
                    if abs(r-nums[i]) <= t:
                        return True
            
            record.add(nums[i])
            if len(record) == k + 1:
                record.remove(nums[i-k])
        return False
    
nums = [1,2,3,2,1]
k = 2
t = 0
s = Solution()
s.containsNearbyAlmostDuplicate(nums,k,t)
