# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 20:09:57 2018

@author: xiaohong
"""

'''
给定一个包含了一些 0 和 1的非空二维数组 grid , 
一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。
你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。
'''

'''
别人的 时间复杂度O(mn) 空间复杂度O(1)
思路 DFS深度优先搜索，递归
    遍历数组，一旦发现1，就开始DFS，并计算岛屿面积，最后不断max比较现有最大岛屿面积和当前岛屿面积
'''

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """        
        
        steps = ((-1,0),(1,0),(0,-1),(0,1))
        
        def dfs(x, y, r,c, grid):
            if x <0 or x >=r or y<0 or y>=c or grid[x][y]==0:
                return 0
            size = 1
            grid[x][y] = 0           
            for i,j in steps:
                size += dfs(x+i,y+j, r, c, grid)
            return size
        
        r = len(grid)
        c = len(grid[0])
        island_size = 0
        for m in range(r):
            for n in range(c):
                if grid[m][n] == 1:
                    island_size = max(island_size, dfs(m,n,r,c,grid))
        return island_size