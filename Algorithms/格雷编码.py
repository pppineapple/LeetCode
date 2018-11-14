#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 20:51:38 2018

@author: pineapple
"""


'''
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。
格雷编码序列必须以 0 开头。

示例 1:

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。

00 - 0
10 - 2
11 - 3
01 - 1
示例 2:

输入: 0
输出: [0]
解释: 我们定义格雷编码序列必须以 0 开头。
     给定编码总位数为 n 的格雷编码序列，其长度为 2n。
     当 n = 0 时，长度为 20 = 1。
     因此，当 n = 0 时，其格雷编码序列为 [0]。
'''

'''
别人的：时间复杂度O(n) 空间复杂度O(n)
思路：
０的格雷编码是[0]
1的格雷编码是[0,1]
2的格雷编码是[00,10,11,01]
相当于是１的格雷编码[0,1]
按顺序后补'0'得到[00,10]
按逆序前补'1'得到[11,01]
然后将这两部分合起来得到[00, 10, 11, 01]就是格雷编码

就是递归处理
写出递归出口条件：n==0和n==1
递归操作　[j+'0' for j in pre] + [i+'1' for i in pre[::-1]] 
'''

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = self.generate(n)  
        print ans
        output = map(self.two2ten, ans)
        return output
               
    def generate(self, n):
        ans = None
        if n == 0:
            return ['0']
        elif n == 1:
            return ['0', '1']
        else:
            pre = self.generate(n-1)
            ans =  [j+'0' for j in pre] + [i+'1' for i in pre[::-1]] 
        return ans
                
            
    def two2ten(self, slist):
        res = 0
        for i in range(len(slist)-1,-1,-1):
            res += int(slist[i]) * 2 ** i
        return res