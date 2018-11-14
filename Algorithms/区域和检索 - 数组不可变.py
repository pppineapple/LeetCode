# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:56:06 2018

@author: xiaohong
"""

'''
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

说明:
你可以假设数组不可变。
会多次调用 sumRange 方法。
'''

'''
我的 0.48
思路 数组切片
'''

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.items = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.items[i:j+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
        

'''
best 0.97
思路，在属性中就储存好[0:i]处的和，最后求和sumRange方法中只要做一个减法就可以了
'''    
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.items = nums
        for i in range(1,len(nums)):
            self.items[i] = nums[i-1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.items[j]
        else:
            return self.items[j] - self.items[i-1]
            #return self.items
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)