#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 13:58:29 2018

@author: pineapple
"""

'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        a = len(nums)
        while a > 1:
            pop_num = nums.pop()
            a = a-1
            if pop_num in nums:
                nums.remove(pop_num)
                a = a-1
            else:
                return pop_num
        return nums[0]

'''
别人 45ms
'''                
def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        for i in range(0,len(nums),2):
            if i == len(nums)-1:
                return nums[i]
            if nums[i] != nums[i+1]:
                return nums[i]
            
singleNumber([1,1,2,3,2])    


'''
我的：　第二次做 时间复杂度O(n) 空间复杂度O(n)
思路：hash表记录元素出现的次数，然后找出出现次数为１的元素返回
'''        
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0) + 1
        for j in hash:
            if hash[j] == 1:
                return j
            
'''
别人的：数学方法　时间复杂度O(n) 空间复杂度O(n)
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums))*2 - sum(nums)
    
'''
别人的　时间复杂度O(n) 空间复杂度O(１)
思路：
If we take XOR of zero and some bit, it will return that bit　　a ⊕ 0 = a
If we take XOR of two same bits, it will return 0               a ⊕ a = 0
and other:                         a ⊕ b ⊕ a = ( a ⊕ a ) ⊕ b = 0 ⊕ b = b
So we can XOR all bits together to find the unique number.
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a