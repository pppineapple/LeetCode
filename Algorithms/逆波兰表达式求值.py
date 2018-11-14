#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:54:10 2018

@author: pineapple
"""


'''
根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，
也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。
换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9
示例 2：

输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6
示例 3：

输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''


'''
我的：时间复杂度O(n) 空间复杂度O(n)
思路：以为逆波兰表达式是后缀表达式，所以只需要用栈来记录数字，
    遇到符号，依次弹出顶部的两个元素做计算
    注意：先弹出来的是num2 后弹出来的是num1
    还要注意的是：这里说的除法是整数除法
    虽然可以用//，但是涉及到正数//负数会出问题，
    所以就改成了　直接除小数然后取整
'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operation = '+-*/'
        stack = []
        for i in tokens:
            if i not in operation:
                stack.append(int(i))
            else:               
                num2 = stack.pop()
                num1 = stack.pop()
                if i == '+':
                    res = num1 + num2
                elif i == '-':
                    res = num1 - num2
                elif i == '*':
                    res = num1 * num2
                elif i == '/':
                    res = int(num1 / float(num2))
                stack.append(res)
        return stack[0]