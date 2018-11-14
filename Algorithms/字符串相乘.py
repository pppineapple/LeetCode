#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 09:55:49 2018

@author: pineapple
"""

'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，
它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
'''

'''
我的：时间复杂度O(n^2) 空间复杂度O(n)
思路：倒着遍历两个数组，然后采用小学学过的两数乘法来计算

'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        list1 = map(int, list(num1))
        list2 = map(int, list(num2))
        s = 0
        poweri = 0
        for i in range(len(list1)-1, -1, -1):
            powerj = 0
            for j in range(len(list2)-1, -1, -1):
                s += list2[j] * 10 ** powerj * list1[i] * 10 ** poweri
                powerj += 1
            poweri += 1
        return str(s)
    
 
'''
更详细的代码，速度更快
思路：用一个新的数组来储存每一次数组相乘的结果，并且保持进位处理
'''    

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        list1 = map(int, list(num1))
        list2 = map(int, list(num2))
        product = [0] * (len(list1) + len(list2))
        postion = len(product) - 1
        for i in range(len(list1)-1,-1,-1):
            pos = postion
            for j in range(len(list2)-1, -1, -1):
                product[pos] += list1[i] * list2[j]
                product[pos-1] += product[pos] // 10
                product[pos] = product[pos] % 10
                pos -= 1
            postion -= 1
        
        begin = 0
        stop = False
        while begin < len(product) and not stop:
            if product[begin] == 0:
                begin += 1
            else:
                stop = True
        if stop:
            return ''.join(map(str,product[begin:]))
        else:
            return '0'
        
        
        
        
num1 = '123'
num2 = '234'
num1 = '123'
num2 = '456'
num1 = '3'
num2 = '4'
s = Solution()
s.multiply(num1, num2)