#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:36:46 2018

@author: pineapple
"""

'''
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。
如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。
所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，
表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。
你必须输出所有学生中的已知的朋友圈总数。

示例 1:

输入: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2 
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。
示例 2:

输入: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出: 1
说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
注意：

N 在[1,200]的范围内。
对于所有学生，有M[i][i] = 1。
如果有M[i][j] = 1，则有M[j][i] = 1。
'''

'''
我的：时间复杂度O(n^2) 空间复杂度O(n)
思路：利用DFS，将行和列中为1的，然后改写为0
    遍历M的行和列，利用count计数
    返回count
'''

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if M == []:
            return 0
        count=0
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    self.DFS(M, i, j)
                    count += 1
        return count
        
    def DFS(self, M, x, y):
        if M[x][y] == 1:
            M[x][y] = 0
            for i in range(len(M)):
                if M[i][y]==1:
                    self.DFS(M, i, y)
            for j in range(len(M[0])):
                if M[x][j]==1:
                    self.DFS(M, x, j)
M = [[1,1,0],
     [1,1,0],
     [0,0,1]]

M = [[1,0,0],
     [0,1,0],
     [0,0,1]]

M = [[1,0,0,1],
     [0,1,1,0],
     [0,1,1,1],
     [1,0,1,1]]
s = Solution()
s.findCircleNum(M)
