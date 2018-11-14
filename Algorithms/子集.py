#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 12:21:22 2018

@author: pineapple
"""

'''
别人的 时间复杂度O(n) 空间复杂度O(1)
思路：DFS递归：
用result来表示这些子集，用到了栈的数据结构
[1]-->[1,2]-->[1,2,3]
[2]-->[2,3]
[3]
然后每次递归时候都将result装进ans里面
最后返回ans
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        ans = []
        self.DFS(0, len(nums), nums, result, ans)
        return ans
    def DFS(self,cur,n,nums,res,ans):           
        ans.append(res[:])
        for i in range(cur,n):
            res.append(nums[i])
            self.DFS(i+1, len(nums), nums, res, ans)
            res.pop()
            
            
            
nums = [1,2,3]
s = Solution()
s.subsets(nums)

a = [1,2,3]
b = []
a1 = []
b.append(a1[:])

a[:].append(10)
b = a[:]
b.append(10)

a = {1:[1,2,3]}
b = a.copy()
a[1].append(4)

import copy
c = copy.deepcopy(a)
a[1].append(4)
a1 = [1,2,3,4,[5]]
a2 = a1[:]
a1[4].append(-5)
a2.append(5)

'''
第二次做，看了答案
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        tmp = []
        cur = 0
        self.generate(cur, nums, tmp, ans)
        return ans
    
    def generate(self,cur, nums, tmp, ans):
        if tmp not in ans:
            ans.append(tmp[:])
        for i in range(cur, len(nums)):
            if nums[i] not in tmp:
                tmp.append(nums[i])
                self.generate(i+1, nums, tmp, ans)
                tmp.pop()