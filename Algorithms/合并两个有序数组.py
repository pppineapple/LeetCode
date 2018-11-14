#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 08:56:18 2018

@author: pineapple
"""

'''
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
'''

        
'''
我的　时间复杂度O(n),空间复杂度O(1)
思路：从nums1的尾巴遍历，比较nums1的m位置和nums2的n位置元素大小关系
    将大的元素放入nums1遍历位置
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m==0 and n==0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        elif n == 0:
            return        
        p = m + n -1
        p1 = m-1
        p2 = n-1
        while p >= 0:
            if  (p1 >= 0 and nums1[p1] > nums2[p2]) or (p2 < 0 and p>=0):
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
            if (p2 >= 0 and nums1[p1] <= nums2[p2]) or (p1 < 0 and p>=0) :
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1

                
            
            
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        if n == 0:
            return
        elif m == 0:
            nums1[:n] = nums2[:n]            
        end = m + n - 1              
        while end >= 0:
            if (nums1[m-1] > nums2[n-1] and m-1 >= 0) or (n-1 < 0 and m-1 >= 0):
                nums1[end] = nums1[m-1]
                m -= 1
                end -= 1
            if (nums2[n-1] >= nums1[m-1] and n-1 >= 0) or (m-1 < 0 and n-1 >= 0):
                nums1[end] = nums2[n-1]
                n -= 1
                end -= 1  
                
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

nums1 = [1,2,4,5,6,0]
m = 5
nums2 = [3]
n = 1

nums1 = [2,0]
m = 1
nums2 = [1]
n = 1

s = Solution()
s.merge(nums1,m,nums2,n)

'''
第三次
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
        if n == 0:
            return
        point = len(nums1)-1
        while point >= 0:
            if m > 0 and n> 0:
                if nums1[m-1] > nums2[n-1]:
                    tmp = nums1[m]
                    nums1[point] = nums1[m-1]
                    nums1[m-1] = tmp
                    m -= 1
                else:
                    nums1[point] = nums2[n-1]
                    n -= 1
                
            elif n > 0:
                nums1[point] = nums2[n-1]
                n -= 1
            elif m > 0:
                nums1[point] = nums1[m-1]
                m -= 1
            point -= 1