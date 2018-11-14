#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 10:19:09 2018

@author: pineapple
"""

'''
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小
'''

'''
我的：时间复杂度O(n) 空间复杂度O(n)
思路：将数组的元素频率用hash记录下来
    然后将hash的键值对调用hash_count记录下来，
    然后在按照hash_count的keys()排序输出对于的元素
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash = {}
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
        hash_count = {}
        for key,value in hash.items():
            if value not in hash_count:
                hash_count[value] = [key]
            else:
                hash_count[value].append(key)
        keys = hash_count.keys()[:]
        ans = []
        i = 0
        while i < k:
            n = hash_count[keys.pop()]
            for j in n:
                ans.append(j)
            i+=len(n)
        return ans

nums = [6,0,1,4,9,7,-3,1,-4,-8,4,-7,-3,3,2,-3,9,5,-4,0]
k = 6

'''
别人的：时间复杂度O(nlogk) 空间复杂度O(n)
思路：用优先队列来维护一个长度为k的队列，优先值为元素的个数计数
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash = {}
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
        import heapq
        heap = []
        for key,value in hash.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                if heap[0][0] < value:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (value, key))
        return [i[1] for i in heap]

