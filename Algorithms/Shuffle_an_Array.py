#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 09:54:20 2018

@author: pineapple
"""


'''
打乱一个没有重复元素的数组。

示例:

// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();
'''

'''
别人的：
思路：　随机打乱可以才用随机抽取前i-1个中的一个
    然后和第i个元素交换的方式达到
'''

import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums
        self.items = self.origin[:]
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.origin)):
            j = random.randint(0, i)
            tmp = self.items[j]
            self.items[j] = self.items[i]
            self.items[i] = tmp

        return self.items
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

items = [1,2,3]
shuffle(items)
