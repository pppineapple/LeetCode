#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:40:27 2018

@author: pineapple
"""

'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 
所以你永远不可能到达最后一个位置
'''

'''
别人的：　时间复杂度O(n) 空间复杂度O(1)
思路：　用一个变量max_index来表示最远能到达的索引处
    然后遍历数组nums
    如果max_index>=i：表示最远能到达索引为i的位置
    所以　最大索引就等于 max(max_index, i+nums[i])
    如果max_index<i：表示最远不能到达索引为i的位置
    所以就返回False
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return True
        max_index = nums[0]
        for i in range(1,len(nums)):
            if max_index >= i:
                max_index = max(max_index, i+nums[i])
            else:
                return False
        return True