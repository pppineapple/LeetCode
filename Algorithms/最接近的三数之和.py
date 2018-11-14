#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 17:28:33 2018

@author: pineapple
"""

'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''

'''
别人的：时间复杂度O(n^2) 空间复杂度O(1)
思路：利用和三数之和的思路相同，但是要注意，先对数组排序
    然后要判断target和当前三数和的距离
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        result = sum(nums[:3])
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                left = i+1
                right = len(nums) - 1
                while left < right:
                    tmp = nums[i] + nums[left] + nums[right]
                    if abs(target - tmp) < abs(target - result):
                        result = tmp
                    elif target < tmp:
                        right -= 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    else:
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
        return result
    
    

    
nums = [1,1,1,0]
target = -100

nums = [0,2,1,-3]
target = 1

nums = [1,1,-1,-1,3]
target = -1

nums = [1,2,4,8,16,32,64,128]
target = 82
s = Solution()
s.threeSumClosest(nums, target)

