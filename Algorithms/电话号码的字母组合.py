#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 21:35:29 2018

@author: pineapple
"""

'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
'''

'''
别人的：时间复杂度O(logn) 空间复杂度O(n)
思路：递归,分割输入的digits
        递归出口是：
        1.当digits长度为０，返回[]
        2.当digits长度为１，返回hash表中对应的值的列表
    递归表达式就是从前面往后面切割digits
'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        hash = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno',
                7:'pqrs', 8:'tuv', 9:'wxyz'}
        ans = []
        
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(hash[int(digits[0])])
        
        result = self.letterCombinations(digits[1:])
        for i in result:
            for j in hash[int(digits[0])]:
                ans.append(j+i)
        return ans        
        
