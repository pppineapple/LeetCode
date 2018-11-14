#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 22:05:56 2018

@author: pineapple
"""

'''
根据百度百科，生命游戏，简称为生命，
是英国数学家约翰·何顿·康威在1970年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。
每个细胞具有一个初始状态 live（1）即为活细胞， 
或 dead（0）即为死细胞。
每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上细胞的下一个（一次更新后的）状态。
下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，
其中细胞的出生和死亡是同时发生的。

示例:

输入: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
进阶:

你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？
'''

'''
参考了别人的思路：时间复杂度O(n^2) 空间复杂度O(n^2)
思路：利用copy进行深拷贝board得到tmp数组
    然后遍历tmp，利用辅助函数LifeCount统计周围八个位置的活细胞数量
    更新board数组中的细胞状态
'''

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        import copy
        tmp = copy.deepcopy(board)
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                board[i][j] = self.LifeCount(tmp, i, j)
        
        
    def LifeCount(self, board, x, y):
        neig = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
        
        count = 0
        for i, j in neig:
            
            if x+i >= len(board) or x+i < 0 or y+j >= len(board[0]) or y+j < 0:
                continue
            if board[x+i][y+j] == 1:
                count += 1
        
        if board[x][y] == 1:
            if count < 2 or count > 3:
                return 0
            else:
                return 1
        if board[x][y] == 0 and count == 3:
            return 1
        return 0
    
    
'''
别人的：　时间复杂度O(n^2) 空间复杂度O(1)
思路：根据题意细胞状态转换有四中：
        status0: 0 -> 0　活细胞周围八个位置的活细胞数少于两个
        status1: 1 -> 1　活细胞周围八个位置有两个或三个活细胞
        status2: 1 -> 0　活细胞周围八个位置有超过三个活细胞
        status3: 0 -> 1　死细胞周围正好有三个活细胞
        所以考虑两次更新数组：
        第一次遍历时：将细胞死活状态用　status0 - status3这四个状态来表示
        第二次遍历时：将状态标识直接对２取模即可
        注意：
        在编写辅助函数LifeCount中　新增一个或条件：board[x+i][y+j] == 2
'''
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        '''
        status0: 0 -> 0
        status1: 1 -> 1
        status2: 1 -> 0
        status3: 0 -> 1
        '''     
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                count = self.LifeCount(board, i, j)
                if board[i][j] == 1:
                    if count == 2 or count == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 2
                else:
                    if count == 3:
                        board[i][j] = 3
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                board[i][j] = board[i][j] % 2
        
        
    def LifeCount(self, board, x, y):
        neig = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
        count = 0
        for i, j in neig:
            if x+i >= len(board) or x+i < 0 or y+j >= len(board[0]) or y+j < 0:
                continue
            if board[x+i][y+j] == 1 or board[x+i][y+j] == 2:
                count += 1
        return count