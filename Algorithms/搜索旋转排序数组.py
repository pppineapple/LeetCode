#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 16:15:26 2018

@author: pineapple
"""

'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
'''

'''
别人的: 时间复杂度O(logn) 空间复杂度O(1)
思路; 这是搜索题，因为题目要求logn，所以自然想到二分查找
    这里首先要找到旋转之后的两个排序数组，分别用二分查找
    要找出旋转之后的两个排序数组，即找到第二个排序数组的第一个位置索引
    可以采用二分的思想，将mid位置和end位置的元素比较大小
    如果nums[mid] > nums[end]， 就让start = mid + 1
    否则就让end = mid，循环出口条件是不满足start < end
    然后再写一个二分查找的方法即可
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        mid = (start+end)//2
        while start < end:
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
            mid = (start+end)//2
        nums1 = nums[:mid]
        nums2 = nums[mid:]
        if self.binarySearch(nums1, target) == -1:
            if self.binarySearch(nums2, target) == -1:
                return -1
            else:
                return self.binarySearch(nums2, target)+mid
        else:
            return self.binarySearch(nums1, target)        
    def binarySearch(self, nums, target):
        start = 0
        end = len(nums)-1
        found = False
        while start <= end and not found:
            mid = (start+end)//2
            if nums[mid] == target:
                found = True
            elif nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
        if found:
            return mid
        else:
            return -1
            
nums = [4,5,6,7,0,1,2]
target = 0
s = Solution()
s.search(nums, target)

'''
第二次
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        '''
        这里不用这种方法的原因是：题目要求时间复杂度O(logn)
        这种方法时间复杂度O(n)
        point = 1
        while point < len(nums):
            if nums[point] > nums[point-1]:
                point += 1
            else:
                break
        '''
        start = 0
        end = len(nums) - 1
        mid = (start - end) // 2
        while start < end:
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
            mid = (start - end)//2
        point = mid
        
        if point == len(nums):
            return self.binarySearch(nums, target)
        else:
            left = self.binarySearch(nums[:point], target)
            right = self.binarySearch(nums[point:], target)
            if left == -1 and right == -1:
                return -1
            elif left != -1:
                return left
            elif right != -1:
                return right + point
            
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right :
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1
    
'''
第三次
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        while left < right:
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                right = mid
            mid = (left+right)//2
        print left,right
        startindex = left
        if self.midsearch(nums[:startindex], target) != -1:
            return self.midsearch(nums[:startindex], target)
        if self.midsearch(nums[startindex:], target) != -1:
            return self.midsearch(nums[startindex:], target)+startindex
        return -1
               
    def midsearch(self, nums, target):
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            mid = (left+right)//2
        return -1