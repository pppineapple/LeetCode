#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:34:57 2018

@author: pineapple
"""

'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''

'''
我的：　时间复杂度O(n) 空间复杂度O(1)
思路：因为输入的区间是乱序的，所以耀先利用sorted函数进行排序，
    排序标准是interval.start
    然后用两个指针遍历数组intervals，将相交区间合并
'''


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x:x.start, reverse = False)
        ans = []
        left = 0
        right = 0
        while right < len(intervals): 
            if intervals[left].end >= intervals[right].start:
                start = min(intervals[left].start, intervals[right].start)
                end = max(intervals[left].end, intervals[right].end)
                tmp = Interval(start, end)
                intervals[left] = tmp
                right += 1
            else:
                left = right
                ans.append(tmp)
        ans.append(tmp)
        return ans
    
'''
更简洁的代码
'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x:x.start, reverse = False)
        ans = []
        point = 0
        while point < len(intervals):
            if ans != [] and ans[-1].end >= intervals[point].start:
                ans[-1].end = max(ans[-1].end, intervals[point].end)
            else:
                ans.append(intervals[point])
            point += 1
        return ans    