#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:16:59 2018

@author: pineapple
"""

'''
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 
整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
'''


'''
我的：　时间复杂度O(n) 空间复杂度O(n)
    思路：所有数字和符号全部入栈，然后先计算乘法和除法
    最后再计算加法和除法
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            elif s[i] in '0123456789':
                num = ''
                while i<len(s) and s[i] in '0123456789 ':
                    if s[i] == ' ':
                        i += 1
                        continue
                    num += s[i]
                    i += 1  
                stack.append(num)
            elif s[i] in '*/':
                op = s[i]
                num1 = stack.pop()
                num2 = ''
                i += 1
                while i < len(s) and s[i] in '0123456789 ':
                    if s[i] == ' ':
                        i += 1
                        continue
                    num2 += s[i]
                    i += 1
                if op == '*':
                    ans = int(num1) * int(num2)
                    stack.append(str(ans))
                elif op == '/':
                    ans = int(num1) // int(num2)
                    stack.append(str(ans))
            else:
                stack.append(s[i])
                i += 1

        while len(stack)>1:
            num2 = int(stack.pop())
            if stack.pop() == '-':
                num2 = num2*(-1)
            num1 = int(stack.pop())
            if stack != []:
                if stack.pop() == '-':
                    num1 = num1*(-1)
            ans = int(num1) + int(num2)
            if stack != []:
                stack.append('+')
            stack.append(str(ans))
        return int(stack[0])

'''
更精简的代码：　时间复杂度O(n) 空间复杂度O(n)
    直接将符号保存到每个数上入栈，最后直接对栈求和
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        op = '+'
        cur_num = 0
        s += '+'
        for i in s:
            if i == ' ':
                continue
            if i.isdigit():
                cur_num = cur_num * 10 + int(i)
                continue
            if op == '+':
                stack.append(cur_num)
            elif op == '-':
                stack.append(-1*cur_num)
            elif op == '*':
                num = stack.pop()
                ans = num * cur_num
                stack.append(ans)
            elif op == '/':
                num = stack.pop()
                ans = num*1.0 /cur_num
                stack.append(int(ans))
            op = i
            cur_num = 0
        return sum(stack)


s = "3+2*2"
s = " 3+5 / 2 "
s = "1-1+1"
s = "1+1+1"
s = '1-1-1'
s = "14-3/2"
S = Solution()
S.calculate(s)


