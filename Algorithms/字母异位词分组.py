#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:23:19 2018

@author: pineapple
"""
'''
给定一个字符串数组，将字母异位词组合在一起。
字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
'''

'''
我的：时间复杂度：O(n) 空间复杂度O(n)
思路：利用hash表来储存异位词，然后hash表的key用排序过后的字符串表示
    因为异位词排序之后都是一样
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """                
        shash = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in shash:
                shash[ss] = [s]
            else:
                shash[ss].append(s)
        result = []    
        for i in shash:
            result.append(shash[i])
        return result          
        
        
    
strs =  ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
s.groupAnagrams(strs)
s = strs[1]

sorted('abc')
{['a','b']:1}
