#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 21:05:44 2018

@author: pineapple
"""

'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3
'''

'''
别人的：　时间复杂度O(n^3) 空间复杂度O(1)
思路：利用递归的DFS，并且将走过的'1'置为'0'
    在判断岛的计数时用变量res来维护
    只要看到grid[i][j] == '1'，res就加1
    然后用DFS函数将周围相连的'1'都置为'0'
    然后继续循环


'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.DFS(grid, i, j)
        return res        
        
    def DFS(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == '1':
            grid[i][j] = '0'
            self.DFS(grid, i+1, j)
            self.DFS(grid, i-1, j)
            self.DFS(grid, i, j+1)           
            self.DFS(grid, i, j-1)
            
grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]

s = Solution()
s.numIslands(grid)
