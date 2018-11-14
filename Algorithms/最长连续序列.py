#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 10:00:03 2018

@author: pineapple
"""

'''
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''

'''
我的：时间复杂度O(nlogn) 空间复杂度O(n)
思路：利用优先队列一遍扫描数组nums
    然后依次弹出优先队列的值
        用变量max_sub_len来记录最长的子串长度
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        if nums == []:
            return 0
        new = []
        for i in set(nums):
            heapq.heappush(new, i)
    
        count = 1
        max_sub_len = 1
        tmp = heapq.heappop(new)
        while new != []:
            node = heapq.heappop(new)
            if node == tmp + 1:
                count += 1                
            else:                
                max_sub_len = max(max_sub_len, count)
                count = 1
            tmp = node
        return max(max_sub_len, count)
    
'''
别人的代码：时间复杂度O(n) 空间复杂度O(n)
思路：既然要求时间复杂度O(n)，考虑利用hash表
    首先建立一个hash表，key为nums中的元素，
    然后value设为True，表示这个值value还没有被取过
    然后遍历数组nums,如果这个num还没有被取过，就设置它为False
    然后向后扩展 cur = num + 1,看cur在不在hash中
    如果在：就将记录子串长度的sub_len+=1
    然后向前扩展 cur = num - 1,看cur在不在hash中
    如果在：就将记录子串长度的sub_len+=1
    最后对子串长度和最大子串长度取max
    返回最大子串长度
'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]看cur在不在hash中
    如果在：就将记录子串长度的sub_len+=1
        :rtype: int
        """
        hash = {}
        for i in nums:
            hash[i] = True            
        max_sub_len = 0
        for num in nums:
            if not hash.get(num):
                continue
            hash[num] = False
            sub_len = 1
            
            cur = num + 1
            while cur in hash:
                hash[cur] = False
                cur += 1
                sub_len += 1
            cur = num - 1
            while cur in hash:
                hash[cur] = False
                cur -= 1
                sub_len += 1
            max_sub_len = max(max_sub_len, sub_len)
        return max_sub_len

    
nums = [0,0,-1]
nums = [100, 4, 200, 1, 3, 2]
nums = [9,1,4,7,3,-1,0,5,8,-1,6]
nums = [1,2,0,1]
s = Solution()
s.longestConsecutive(nums)
