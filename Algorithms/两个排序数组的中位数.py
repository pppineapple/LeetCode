#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 11:10:14 2018

@author: pineapple
"""

'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

你可以假设 nums1 和 nums2 不同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5
'''

'''
我的：时间复杂度O(n+m)　空间复杂度O(n+m)
思路：　因为两个数组都是是有序的，所以考虑将两个数组合并成一个新的有序数组newlist
    即用两个指针分别从两个数组前面往后面遍历即可
    然后看新数组长度是奇数还是偶数，是奇数就去最中间的值
    是偶数就去中间两个值取平均
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        newlist = []
        i = 0
        j = 0
        while i < n1 or j < n2:
            if i < n1 and j < n2:
                if nums1[i] <= nums2[j]:
                    newlist.append(nums1[i])
                    i += 1
                else:
                    newlist.append(nums2[j])
                    j += 1
            elif i < n1 and j >= n2:
                newlist.append(nums1[i])
                i += 1
            elif i >= n1 and j < n2:
                newlist.append(nums2[j])
                j += 1
        if (n1+n2) % 2 == 0:
            return (newlist[(n1+n2)//2]+newlist[(n1+n2)//2-1])/2.0
        else:
            return newlist[(n1+n2)//2]