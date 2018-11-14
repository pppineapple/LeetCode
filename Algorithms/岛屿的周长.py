# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 08:08:50 2018

@author: xiaohong
"""

'''
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
网格中的格子水平和垂直方向相连（对角线方向不相连）。
整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。
格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
'''

'''
别人的 时间复杂度O(mn) 空间复杂度O(1) 0.47
思路： 因为但其中恰好有一个岛屿 暴力遍历
'''

def islandPerimeter(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        steps = ((1,0),(-1,0), (0, 1), (0,-1))
        row = len(grid)
        col = len(grid[0])
        
        perimeter = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    perimeter += 4
                    for i,j in steps:
                        if x+i >= 0 and x+i < row and y+j >= 0 and y+j < col and grid[x+i][y+j] == 1:
                            perimeter -= 1
                    
        return perimeter

'''
别人的 时间复杂度O(mn) 空间复杂度O(1)
思路： 但其中恰好有一个岛屿 周长公式等于：值为1的方块乘4 然后减去相邻个数*2(注意不要重复)
'''


def islandPerimeter(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        row = len(grid)
        col = len(grid[0])
        
        count = 0
        neig = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    count += 1
                    if x + 1 < row and grid[x+1][y] == 1:
                        neig += 1
                    if y + 1 < col and grid[x][y+1] == 1:
                        neig += 1
        return count*4 - neig * 2
                        


grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]


islandPerimeter(grid)

