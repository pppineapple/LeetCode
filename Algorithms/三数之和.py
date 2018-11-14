#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 21:28:21 2018

@author: pineapple
"""

'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

'''
我的：时间复杂度O(n^2) 空间复杂度O(1)
思路：先对nums排序
    然后遍历nums
    然后在每一次遍历过程中，因为排序了，所以可以nums[i]后面的元素做
    双指针对撞，记录nums[i] + nums[left] + nums[right] == 0的三个值
    同时要注意，在遍历nums时，会遇到nums[i] == nums[i-1]，这个时候
    一定要注意跳过nums[i], 否则会在result中出现重复结果
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if nums[i] + nums[left] + nums[right] == 0:
                        result.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif  nums[i] + nums[left] + nums[right] > 0:
                        right -= 1
                    else:
                        left += 1

                
        return result
                
nums = [-1, 0, 1, 2, -1, -4]
s = Solution()
s.threeSum(nums)
n = 0
