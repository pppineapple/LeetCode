#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 18:56:55 2018

@author: pineapple
"""

'''
给出 n 代表生成括号的对数，请你写出一个函数，
使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

'''
别人的：　时间复杂度O(n) 空间复杂度O(n)
思路：以n=3举例，合法的括弧字符串：'((()))'　
    这个长度为2n的字符串中每一个位置上的，左括弧数量要大于右括弧数量
    所以采用DFS思想递归时，先判断left剩余数量是否大于０，
    如果left有剩余，就对str插入一个"(",
    然后递归调用函数generatepattern(str+'(', left-1, right, res)
    如果right有剩余，就对str插入一个")",
    然后递归调用函数generatepattern(str+')', left, right-1, res)
    递归出口是　left == 0 and right == 0
    此时就在最后的res数组中插入str
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        str = ''
        self.generatepattern(str, n, n, res)
        return res
        
        
    def generatepattern(self, str, left, right, res):
        if left == 0 and right == 0:
            res.append(str)
        if left > 0:
            self.generatepattern(str+'(', left-1, right, res)
        if right > left:
            self.generatepattern(str+')', left, right-1, res)
                
                
'''
第二次做
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        tmp = ''
        self.generate(n, n, tmp, ans)
        return ans
        
    def generate(self, left, right, tmp, ans):
        if left == 0 and right == 0:
            ans.append(tmp)
            return
        if left > 0:
            self.generate(left-1, right, tmp+'(', ans)
        if left < right :
            self.generate(left, right-1, tmp+')', ans)