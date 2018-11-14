#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 12:26:15 2018

@author: pineapple
"""

'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 

注意事项：您可以假定该字符串只包含小写字母。
'''

'''
我的：　时间复杂度O(n) 空间复杂度O(n)
思路：通过哈希表建立元素与index的对应关系，然后遍历哈希表
    找寻索引最小的符合索引只有一个的字符
'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {}
        for i in range(len(s)):
            if s[i] not in hash:
                hash[s[i]] = [i]
            else:
                hash[s[i]].append(i)
        minindex = len(s)
        for j in hash:
            if len(hash[j]) == 1:
                minindex = min(minindex, hash[j][0])
        if minindex == len(s):
            return -1
        else:
            return minindex
s = 'leetcode'
S = Solution()
S.reverse(x)
