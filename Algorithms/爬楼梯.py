# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 18:04:10 2018

@author: xiaohong
"""

'''
爬楼梯
'''

'''
假设你正在爬楼梯。需要 n 步你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 步 + 1 步
2.  2 步

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 步 + 1 步 + 1 步
2.  1 步 + 2 步
3.  2 步 + 1 步
'''

'''
我的： 24ms
动态规划
'''
def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return 1
        if n == 2:
            return 2

        opt = [0] * n
        opt[0] = 1
        opt[1] = 2       
        for i in range(2,n):
            opt[i] = opt[i-1] + opt[i-2]
        return opt[-1]


'''
best 20ms
'''
def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        pre, cur = 1, 1
        for i in range(1,n):
            pre,cur = cur,pre+cur
        return cur


'''
第二次做：动态规划：时间复杂度O(n) 空间复杂度O(n)
思路：第n次爬楼梯的方案等于n-1次的方案加上n-2次的方案
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        opt = [0] * n
        opt[0] = 1
        opt[1] = 2
        for i in range(2, n):
            opt[i] = opt[i-1] + opt[i-2]
            
        return opt[-1]
        
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        opt = [0] * n
        opt[0] = 1
        opt[1] = 2
        for i in range(2, n):
            opt[i] = opt[i-1] + opt[i-2]
        return opt[-1]








