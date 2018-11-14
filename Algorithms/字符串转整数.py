#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 08:52:57 2018

@author: pineapple
"""

'''
实现 atoi，将字符串转为整数。

该函数首先根据需要丢弃任意多的空格字符，直到找到第一个非空格字符为止。如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。

当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。

若函数不能执行有效的转换，返回 0。

说明：

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。如果数值超过可表示的范围，则返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

示例 1:

输入: "42"
输出: 42
示例 2:

输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:

输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
     因此返回 INT_MIN (−231) 。
'''

'''
别人的：时间复杂度O(n) 空间复杂度O(1)
思路：
通过试错可以总结出要注意的四个点：

１输入字符串为空、或其他不合法情况，返回0；
２字符串开头的空格要在预处理中删掉；
３处理可能出现的正负号“+”，“-”，正负号只能出现一次；
４超出整数范围的值取整数范围的边界值。
'''


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        str = str.strip()
        if str == '':
            return 0
        number, flag = 0, 1
        if str[0] == '-':
            str = str[1:]
            flag = -1
        elif str[0] == '+':
            str = str[1:]
        
        for c in str:
            if c >= '0' and c <= '9':
                number = number * 10 + ord(c) - ord('0')
            else:
                break
        number = flag * number
        if number >= 2147483648:
            return 2147483647
        elif number <= -2147483648:
            return -2147483648
        else:
            return number
            
str = '42'
str = '   -42'
str = "4193 with words"
str = "words and 987"
str = "-91283472332"
s = Solution()
s.myAtoi(str)

'''
第二次做
'''
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        if len(str) == 0:
            return 0
        if str[0] == '-':
            flag = -1
            str = str[1:]
        elif str[0] == '+':
            flag = 1
            str = str[1:]
        elif str[0] in '0123456789':
            flag = 1
        else:
            return 0
        
        i = 0
        while i < len(str):
            if str[i] not in '0123456789':
                break
            else:
                i += 1
        num = 0
        for j in range(len(str[:i])):
            num += int(str[:i][len(str[:i])-j-1]) * 10 ** j
        num = num * flag
        
        if num < -2**31:
            return -2**31
        elif num > 2**31-1:
            return 2**31-1
        else:
            return num