#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:02:45 2018

@author: pineapple
"""

'''
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，
使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''

'''
我的：　时间复杂度O(n^2)　空间复杂度O(n)
思路：因为ＡＢＣＤ一样长度，所以两层嵌套便利Ａ和Ｂ，
　　　建立hash表，健为元素和，值为个数
　　　然后两层嵌套便利Ｃ和Ｄ，如果ＣＤ对应元素的和在hash表中
   　就加上它出现的次数
'''
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
     
        abhash = {}
        for a in A:
            for b in B:
                abhash[a+b] = abhash.get(a+b, 0) + 1
        result = 0
        for c in C:
            for d in D:
                print -(c+d)
                if -(c+d) in abhash:
                    result += abhash[-(c+d)]
                    
        return result
#  
A=[-1,-1]
B=[-1,1]
C=[-1,1]
D=[1,-1]

s = Solution()
s.fourSumCount(A,B,C,D)
c = -1
c = 1
d = 1
d = -1

'''
第二次做
注意：如果是建立两个hash表来做，那一定要注意
    在累加res时，要是两个hash表对于元素的乘积
    因为这里是考虑组合搭配
'''
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hashab = {}
        for a in A:
            for b in B:
                hashab[a+b] = hashab.get(a+b, 0)+1
        hashcd = {}
        for c in C:
            for d in D:
                hashcd[c+d] = hashcd.get(c+d, 0)+1
                
        res = 0
        for i in hashcd:
            if -i in hashab:
                res += hashab[-i]*hashcd[i]
        
        return res