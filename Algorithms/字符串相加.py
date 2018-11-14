# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 14:36:44 2018

@author: xiaohong
"""


'''
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
'''

'''
我的 0.64
思路 小学学的加法，从个位往前相加，这里会先进行字符串翻转工作
'''
def addStrings(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]        
        output = ''
        nextone = 0
        for i in range(max(len(num1),len(num2))):
            if i <= len(num1)-1 and i <= len(num2)-1:
                s = int(num1[i]) + int(num2[i]) + nextone
                if s >= 10:
                    output = str(s-10) + output
                    nextone = 1
                else:
                    output = str(s) + output
                    nextone = 0
            else:
                if i > len(num1)-1 and i <= len(num2)-1:
                    s = int(num2[i]) + nextone
                elif i <= len(num1)-1 and i> len(num2)-1:
                    s = int(num1[i]) + nextone
                if s >= 10:
                    output = str(s-10) + output
                    nextone = 1
                else:
                    output = str(s) + output
                    nextone = 0
        if nextone == 1:
            return '1'+output
        else:
            return output
        
num1 = '408'
num2 = '5'    
addStrings(num1, num2)    

'''
更简洁的代码
'''

def addStrings(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        result = ''
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
            result += chr(carry % 10 + ord('0'))
            carry //= 10
            i -= 1
            j -= 1
        if carry == 1:
            result += '1'
        return result[::-1]


