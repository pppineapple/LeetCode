#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:37:38 2018

@author: pineapple
"""

'''
别人的思路：　时间复杂度O(n^2logn) 空间复杂度O(1)
我的代码：利用DFS编写一个辅助函数DFS来将满足条件的board[x][y]修改为想要的sign
    首先遍历board的边界，利用DFS将边界上为'O'以及它们的延伸改写为'*'
    然后遍历board的行和列，
    将剩下的'O'改写为'X'，将剩下的'*'改写为'*'
'''

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == []:
            return 
        for j in range(len(board[0])):
            self.DFS(board, 0, j, '*')
            self.DFS(board, len(board)-1, j, '*')
        for i in range(len(board)):
            self.DFS(board, i, 0, '*')
            self.DFS(board, i, len(board[0])-1, '*')
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
            
    def DFS(self, board, x, y, sign):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return
        steps = [[0,-1], [0,1], [1, 0], [-1, 0]]
        if board[x][y] == 'O':
            board[x][y] = sign
            for i, j in steps:
                self.DFS(board, x+i, y+j, sign)
        else:
            return
        
board = [["O","X","O","O","X","X"],
         ["O","X","X","X","O","X"],
         ["X","O","O","X","O","O"],
         ["X","O","X","X","X","X"],
         ["O","O","X","O","X","X"],
         ["X","X","O","O","O","O"]]
s = Solution()
s.solve(board)

