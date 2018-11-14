# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 20:11:17 2018

@author: xiaohong
"""

'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
'''




'''
我的代码：36ms
思路，利用栈的特点
'''
def isValid(s):
        """
        :type s: str
        :rtype: bool
        """ 
        
        def match(top, symbol):
            left, right = '([{' , ')]}'
            return left.index(top) == right.index(symbol)
            
        symbolLeft = '([{'
        if len(s)  % 2 == 1:
            return False
        
        stack = []

        index = 0
        balance = True
        while index < len(s) and balance:
            symbol = s[index]
            if symbol in symbolLeft:
                stack.append(symbol)
            else:
                if stack == []:
                    return False
                else:
                    top = stack.pop()
                    if not match(top, symbol):
                        balance = False
            index += 1
        if len(stack) == 0 and balance:
            return True
        else:
            return False

'''
best: 20ms
'''

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """ 
        
        try:
            stack = []
            for key in s :
                if(key == '(' or key == '[' or key == '{'):
                    stack.append(key)
                else:
                    if((key == ')' and stack.pop() == '(') or
                            (key == ']' and stack.pop() == '[') or
                            (key == '}' and stack.pop() == '{')):
                        pass
                    else:
                        return False
            if(len(stack) == 0):
                return True
        except IndexError:
            return False
        return False

'''
我的　时间复杂度O(n) 空间复杂度O(1)
思路：利用数据结构栈，遍历字符串s,入栈的都是坐括弧号，
    一但遇到不是左括弧号的情况，先看栈是不是为空，为空就返回False
    不为空就把这个括弧号和栈的顶端做比较：
    如果不能匹配，返回False
    如果匹配,就继续遍历
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        symbolhash = {')':'(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if i in symbolhash.values():
                stack.append(i)
            else:
                if stack == []:
                    return False
                else:
                    symbol = stack.pop()
                    if symbol != symbolhash[i]:
                        return False
        if stack == []:
            return True
        else:
            return False
        
s = ''
S = Solution()
S.isValid(s)


'''
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hash = {'(':')','[':']','{':'}'}

        stack = []
        for i in range(len(s)):
            if s[i] in hash.keys():
                stack.append(s[i])
            else:
                if stack != []:
                    left = stack.pop()
                    if hash[left] != s[i]:
                        return False
                else:
                    return False
        if stack != []:
            return False
        return True
                
