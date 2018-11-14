#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:13:54 2018

@author: pineapple
"""

'''
在未排序的数组中找到第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
'''

'''
别人的：　时间复杂度O(nlogn) 空间复杂度O(1)
思路：quick　select思路，类似与快排，每一次迭代都是选择一个枢纽值
    然后枢纽值左边的都小于这个枢纽值，右边都大于枢纽值
    这个时候就看右边这些比枢纽值大的值的长度是不是等于k:if len(nums)-split == k
    如果等于k-1,即说明枢纽值就是第k个大的数字
    如果比枢纽值大的数字的长度小于k，就说明要到枢纽值左边那一部分数字里面去找
    第　k-split 大的数字，就让　nums = nums[:split]，　k = k - (len(nums) - split)
    然后继续找切分点(枢纽值)
    如果比枢纽值大的数字的长度小于k,就说明要到枢纽值右边那一部分数字里面去找
    第　k 大的数字，就让　nums = nums[split+1:]
    然后继续找切分点(枢纽值)
    
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        while True:
            split = self.partition(nums, 0, len(nums))
            if len(nums)-split == k:
                return nums[split]
            elif split > len(nums)-k:
                k = k - (len(nums) - split)
                nums = nums[:split]
            elif split < len(nums)-k:
                nums = nums[split+1:]

    def partition(self,  nums, first, end):
        pivotvalue = nums[first]
        left = first+1
        right = end - 1
        done = False
        while not done:
            while left <= right and nums[left] <= pivotvalue:
                left += 1
            while nums[right] >= pivotvalue and left<=right:
                right -= 1
            if left > right:
                done = True
            else:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
        tmp = nums[right]
        nums[right] = pivotvalue
        nums[first] = tmp                
        return right
    
nums = [4,5,6,7,0,1,2]
k = 2

s = Solution()
s.findKthLargest(nums, k)

'''
第二次做
'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        while True:
            split = self.quicksorthelper(nums, 0, len(nums)-1)
            if split == len(nums) - k:
                return nums[split]
            elif split > len(nums)-k:
                k = k - (len(nums)-split)
                nums = nums[:split]                
            elif split < len(nums)-k:
                nums = nums[split+1:]
              


    
    def quicksorthelper(self, nums, first, last):
        pivotvalue = nums[first]
        left = first + 1
        right = last
        stop = False
        while not stop:
            while left <= right and nums[left] <= pivotvalue:
                left += 1
            while nums[right] >= pivotvalue and left <= right:
                right -= 1
            if left > right:
                stop = True
            else:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
        tmp = nums[first]
        nums[first] = nums[right]
        nums[right] = tmp
        return right
