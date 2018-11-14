#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 12:09:51 2018

@author: pineapple
"""

'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？



例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
'''

'''
我的：　时间复杂度O(n^2) 空间复杂度O(n^2)
思路：动态规划：状态转移表达式：opt[r][c] = opt[r-1][c] + opt[r][c-1]
    第r行第c列位置的路径总数等于 
    第r-1行第c列位置的路径总数 加上　第r行第c-1列位置的路径总数
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==0 or n==0:
            return 0
        opt = [[0]*m for i in range(n)]
        for i in range(m):
            opt[0][i] = 1
        for j in range(n):
            opt[j][0] = 1        
        for c in range(1, m):
            for r in range(1, n):
                opt[r][c] = opt[r-1][c] + opt[r][c-1]                
        return opt[-1][-1]
s = Solution()
s.uniquePaths(1,0) 
    
'''
第二次做
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==0 or n==0:
            return 0
        opt = [[0]*m for i in range(n)]
        opt[0] = [1] * m
        for i in range(n):
            opt[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                opt[i][j] = opt[i-1][j] + opt[i][j-1]
        return opt[-1][-1]