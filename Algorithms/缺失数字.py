# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 09:47:53 2018

@author: xiaohong
"""

'''
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
'''


'''
我的 时间复杂度 O(nlogn) 排序的时间复杂度 空间复杂度O(1) 0.42
思路： 先对数组排序，然后看索引和值是否相等，如果不相等，这个索引就是这个缺失的值
        如果遍历数组之后，索引和值都相等，name缺失值就是n=len(nums)
'''

def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        for index, item in enumerate(nums):
            if index != item:
                return index
        return n
        
'''
更优雅的代码：时间复杂度O(n), 空间复杂度O(1)
思路： 因为问题是要找0-n个数中缺掉的一个数，
    所以我可以先求出0-n个数的和： n*(n+1)//2
    然后用这个和减去数组nums的和，就是缺失的那个值
'''
def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0
        
        n = len(nums)        
        n_sum = n * (n + 1) // 2
        nums_sum = sum(nums)
        return n_sum - nums_sum
    
    
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return (1+n)*n//2 - sum(nums)