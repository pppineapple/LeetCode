#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 14:34:04 2018

@author: pineapple
"""

'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2

示例 2:
输入: [3,1,3,4,2]
输出: 3

说明：
1.不能更改原数组（假设数组是只读的）。
2.只能使用额外的 O(1) 的空间。
3.时间复杂度小于 O(n2) 。
4.数组中只有一个重复的数字，但它可能不止重复出现一次。
'''

'''
别人的：　时间复杂度O(nlogn) 空间复杂度O(1)
    根据要求不能修改原数组，即不能排序
    不能使用额外空间，即不能用hash表
    时间复杂度小于O(n^2)，即不能暴力搜索
    数组中不止重复出现一次，即不能使用数学方法 sum(nums) - sum([1,...n])来求解
    
    所以就考虑遍历数组，同时使用二分搜索O(logn)
    这里二分搜索是指搜索[1, ... , n]中进行二分搜索，得到mid
    然后遍历数组nums，使用count统计数组中不大于mid的元素
    如果count  > mid就说明重复的数组在[mid+1, ... , n]中
    然后left = mid + 1, right = right继续二分搜索
    终止条件是　left > right, 返回left
'''


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 1
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count > mid:
                right = mid-1
            else:
                left = mid+1
        return left
            
'''
别人的：时间复杂度O(n) 空间复杂度O(1)
思路：想象一下对于不重复数组[1,3,2],考虑下标和数组元素对应有：
    0->1, 1->3, 2->2
    那从下标0开始，然后找到该下标对应的元素，
    将该元素作为下标，继续找该小标对于的元素，知道下标达到或者超过数组长度
    就得到　0->1->3
    那对于重复的数组，比如 [1,3,3,2],就有
    0->1, 1->3, 2->3, 3->2
    就有　0->1->3->2->3->... 就出现了2->3循环
    所以就可以参照查找环形链表环起点的方法的方法查找重复的值
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow

nums = [1,3,4,2,2]
nums = [1,1,2,3,4]
nums = [1,4,4,2,4]
nums = [3,1,3,4,2]
s = Solution()
s.findDuplicate(nums)
