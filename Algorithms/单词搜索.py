#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:59:43 2018

@author: pineapple
"""

'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
'''

'''
别人的：　时间复杂度O(n^2logn) 空间复杂度O(n)
思路：DFS然后加上回溯法递归
    但是要注意，在每一次DFS搜索时：
    走过的路径需要置为'done'，但是在这次DFS搜索完成后，
    'done'需要还原为原来的值
    还要注意的是，这是找单词匹配，所以单词的首字母可以在board的任何位置开始
    所以需要两层循环i,j
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.DFS(board, word, i, j, 0):
                    return True
        return False
        
    def DFS(self, board, word, i, j, cur):
        if len(word) == cur:
            return True
        if i >= len(board) or j >= len(board[0]) or i<0 or j<0:
            return False
        if board[i][j] != word[cur]:
            return False
        else:
            board[i][j] = 'done'
            result =  self.DFS(board, word, i+1, j, cur+1) or \
                      self.DFS(board, word, i-1, j, cur+1) or \
                      self.DFS(board, word, i, j+1, cur+1) or \
                      self.DFS(board, word, i, j-1, cur+1) 
            board[i][j] = word[cur]
            return result
