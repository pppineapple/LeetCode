#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 11:46:15 2018

@author: pineapple
"""

'''
颠倒给定的 32 位无符号整数的二进制位。

示例:

输入: 43261596
输出: 964176192
解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
     返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。
进阶:
如果多次调用这个函数，你将如何优化你的算法？
'''

'''
我的：时间复杂度O(n) 空间复杂度O(n)
思路：先将n转化为２进制，用列表储存起来，　[尾    首]
    然后对于长度小于32的列表进行后尾补0操作
    直接从后面开始将列表表示的二进制转化为10进制
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        nlist = []
        while n > 0:
            res = n%2
            n = n//2
            nlist.append(res)
        
        while len(nlist) < 32:
            nlist.append(0)
        ans = 0
        i = 0
        while nlist != []:
            num = nlist.pop()
            ans += num*2**i
            i += 1
        return ans