#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:28:35 2018

@author: pineapple
"""

'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''

'''
别人的：　时间复杂度O(n^2) 空间复杂度O(n)
思路：　动态规划
    opt[i] 表示nums数组中第i个元素前面比它小的元素个数
    初始化opt[i] = 1
    然后两层遍历，如果看到i之前的j位置出的元素小于i的值，
    更新opt[i] = max(opt[i], opt[j]+1)
    最后返回opt中的最大值
'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        opt = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    opt[i] = max(opt[i], opt[j]+1)
        return max(opt)
    
'''
别人的：　时间复杂度O(nlogn) 空间复杂度O(n)
思路：　二分法，
        建立一个数组ans来维护上升的子序列
        然后遍历nums
        将nums[i] 插入到ans中，并且保持递增状态，
        通过对ans进行二分查找(target=nums[i])
        然后查出nums[i]在ans中对应的位置：即ans中第一个比nums[i]大的数(用left表示位置)
        然后将ans[left]替换为nums[i]
        如果left超过了len(ans)-1，就说明nums[i]比ans里面所有数都大
        这时可以直接添加到ans的末尾
        最后返回ans的长度
''' 
    
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        ans = []
        for i in range(len(nums)):
            left = 0
            right = len(ans)-1
            mid = (left+right)//2
            while left <= right:
                if ans[mid] >= nums[i]:
                    right = mid - 1
                elif ans[mid] < nums[i]:
                    left = mid + 1
                mid = (left+right)//2

            if left >= len(ans):
                ans.append(nums[i])
            else:
                ans[left] = nums[i]
        return len(ans)
    

nums = [10,9,2,5,3,7,101,18]
nums = [2,2]
s=Solution()
s.lengthOfLIS(nums)

